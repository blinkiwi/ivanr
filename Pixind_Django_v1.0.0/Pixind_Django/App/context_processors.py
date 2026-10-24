"""Contexto global: todo el contenido del home viene de la base de datos.

Si una tabla esta vacia se usan los valores por defecto (homepage_defaults),
que son exactamente los textos/imagenes originales de la plantilla.
"""
from django.conf import settings
from django.templatetags.static import static

from .models import (
    SiteConfig, StickyNav, NavItem, HeaderBlock, SectionBlock, FeatureBlock,
    ServiceTab, PricingBlock, FAQItem, ReviewItem, CounterItem, PartnerLogo,
    FooterColumn, SocialLink, FooterBlock, ContactInfo, TeamBlock, Blog, Portfolio,
)
from . import homepage_defaults as D


def media_url(value):
    """Resuelve una imagen: ruta estatica, URL absoluta o archivo subido."""
    if not value:
        return ''
    value = str(value)
    if value.startswith(('http://', 'https://', '//', '/')):
        return value
    return settings.MEDIA_URL + value


def _image(db_value, default=''):
    return media_url(db_value) or default


def _hero_dict(obj):
    data = dict(D.HERO)
    if obj:
        data.update({
            'title': obj.title or data['title'],
            'title_line2': obj.title_line2 or data['title_line2'],
            'subtitle': obj.subtitle or data['subtitle'],
            'button_text': obj.button_text or data['button_text'],
            'button_link': obj.button_link or data['button_link'],
            'video_id': obj.video_id or data['video_id'],
            'video_label': obj.video_label or data['video_label'],
            'card_title': obj.card_title or data['card_title'],
            'card_name_label': obj.card_name_label or data['card_name_label'],
            'card_email_label': obj.card_email_label or data['card_email_label'],
            'card_phone_label': obj.card_phone_label or data['card_phone_label'],
            'card_button_text': obj.card_button_text or data['card_button_text'],
        })
        data['image'] = _image(obj.image.name if obj.image else '', data['image'])
    return data


def _section_dict(key, obj):
    data = dict(D.SECTIONS.get(key, {}))
    if obj:
        for field in ('eyebrow', 'title', 'description', 'button_label', 'button_url',
                      'badge_text', 'person_text', 'checklist', 'embed_url',
                      'stat_label', 'stat_number', 'stat_percent',
                      'form_name_label', 'form_email_label', 'form_subject_label',
                      'form_message_label', 'form_button_label'):
            value = getattr(obj, field, '')
            if value:
                data[field] = value
        if getattr(obj, 'stat_target', None):
            data['stat_target'] = obj.stat_target
        if obj.image:
            data['image'] = media_url(obj.image.name)
        if obj.background_image:
            data['background_image'] = media_url(obj.background_image.name)
        if obj.extra_image:
            data['extra_image'] = media_url(obj.extra_image.name)
    if 'checklist' in data:
        data['checklist'] = [c.strip() for c in data['checklist'].splitlines() if c.strip()]
    if 'title' in data:
        data['title_html'] = data['title'].replace('\n', '<br>')
    return data


def _rows(model, limit=None):
    qs = model.objects.all()
    if limit:
        qs = qs[:limit]
    return list(qs)


def _assets_version():
    """Version de los assets propios: cambia su valor cuando cambia un archivo,
    lo que invalida la caché del navegador (?v=...)."""
    import os
    rutas = [
        os.path.join(settings.BASE_DIR, "static", "admin_custom", "admin.css"),
        os.path.join(settings.BASE_DIR, "static", "admin_custom", "admin-mobile.css"),
        os.path.join(settings.BASE_DIR, "static", "admin_custom", "admin.js"),
        os.path.join(settings.BASE_DIR, "static", "app", "css", "site-custom.css"),
    ]
    try:
        return str(int(max(os.path.getmtime(r) for r in rutas)))
    except Exception:
        return "1"


def global_context(request):
    site = SiteConfig.objects.first()
    nav = StickyNav.objects.first()
    hero_obj = HeaderBlock.objects.filter(order=0).first()

    # --- sitio -------------------------------------------------------------
    site_name = (site.site_name if site else None) or D.SITE['site_name']
    meta_title = (site.meta_title if site else None) or D.SITE['meta_title']
    meta_description = (site.meta_description if site else None) or D.SITE['meta_description']
    copyright_text = (site.copyright_text if site else None) or D.SITE['copyright_text']
    logo = site.logo if site and site.logo else None
    favicon = site.favicon if site and site.favicon else None

    # --- header sticky -----------------------------------------------------
    nav_items = [
        {'label': i.label, 'url': i.url}
        for i in _rows(NavItem)
    ] or list(D.NAV_ITEMS)
    nav_logo = _image(nav.logo.name if nav and nav.logo else '',
                      media_url(logo.name) if logo else static('app/images/logo-dark.png'))
    sticky = {
        'logo': nav_logo,
        'cta_label': (nav.cta_label if nav else None) or D.STICKY_NAV['cta_label'],
        'cta_url': (nav.cta_url if nav else '') or D.STICKY_NAV['cta_url'],
    }

    # --- secciones ---------------------------------------------------------
    section_objs = {s.key: s for s in _rows(SectionBlock)}
    sections = {key: _section_dict(key, section_objs.get(key)) for key in D.SECTIONS}

    # --- listas ------------------------------------------------------------
    feature_objs = _rows(FeatureBlock)
    if feature_objs:
        features = [{
            'title': f.title, 'desc': f.description, 'icon': f.icon,
            'url': f.url, 'class': '', 'data': f'.{2 * (idx + 1)}s',
        } for idx, f in enumerate(feature_objs)]
    else:
        features = [{
            'title': f['title'], 'desc': f['description'], 'icon': f['icon'],
            'url': f['url'], 'class': '', 'data': f'.{2 * (idx + 1)}s',
        } for idx, f in enumerate(D.FEATURES)]

    tab_objs = _rows(ServiceTab)
    if tab_objs:
        service_tabs = [{
            'label': t.label, 'title': t.title, 'text': t.text,
            'image': _image(t.image.name if t.image else '', ''),
            'url': t.url,
        } for t in tab_objs]
    else:
        service_tabs = [dict(t) for t in D.SERVICE_TABS]

    def pricing_list(billing):
        objs = PricingBlock.objects.filter(billing=billing)
        plans = list(objs)
        if not plans:
            plans = [p for p in D.PRICING if p['billing'] == billing]
            return [{
                'title': p['title'], 'price': p['price'], 'period': p['period'],
                'highlight': p['highlight'],
                'features': [x for x in p['features'].splitlines() if x.strip()],
                'button_text': p['button_text'], 'button_url': p['button_link'],
            } for p in plans]
        return [{
            'title': p.title, 'price': p.price, 'period': p.period,
            'highlight': p.highlight,
            'features': [x for x in p.features.splitlines() if x.strip()],
            'button_text': p.button_text, 'button_url': p.button_link,
        } for p in plans]

    faq_objs = _rows(FAQItem)
    faqs = ([{'question': f.question, 'answer': f.answer} for f in faq_objs]
            or [dict(f) for f in D.FAQS])

    review_objs = _rows(ReviewItem)
    reviews = ([{'name': r.name, 'role': r.role, 'desc': r.text,
                 'img': _image(r.avatar.name if r.avatar else '', '')}
                for r in review_objs]
               or [dict(name=r['name'], title=r['role'], desc=r['text'], img=r['avatar'])
                   for r in D.REVIEWS])

    counter_objs = _rows(CounterItem)
    counters = ([{'icon': c.icon, 'number': c.number, 'target': c.target,
                  'symbol': c.symbol, 'title': c.title, 'data': f'.{2 * (i + 1)}s'}
                 for i, c in enumerate(counter_objs)]
                or [dict(c, data=f'.{2 * (i + 1)}s') for i, c in enumerate(D.COUNTERS)])

    partner_objs = _rows(PartnerLogo)
    partners = ([{'img': _image(p.image.name if p.image else '', ''), 'alt': p.alt,
                  'data': f'.{2 * (i + 1)}s'}
                 for i, p in enumerate(partner_objs)]
                or [dict(img=p['image'], alt=p['alt'], data=f'.{2 * (i + 1)}s')
                    for i, p in enumerate(D.PARTNERS)])

    blogs = [{'img': media_url(b.img.name), 'title': b.title, 'desc': b.desc,
              'data': f'.{2 * (i + 1)}s'}
             for i, b in enumerate(Blog.objects.all()[:3])]

    portfolios = [{'img': media_url(p.img.name), 'title': p.title, 'name': p.name,
                   'groups': p.groups, 'data': f'.{2 * (i + 1)}s'}
                  for i, p in enumerate(Portfolio.objects.all()[:6])]

    # --- contacto / footer -------------------------------------------------
    contacts = [{'label': c.label, 'value': c.value, 'icon': c.icon}
                for c in _rows(ContactInfo)] or [dict(c) for c in D.CONTACTS]

    footer_obj = FooterBlock.objects.filter(order=0).first()
    footer_description = (footer_obj.description if footer_obj else '') or D.FOOTER['description']

    socials = [{'icon': s.icon, 'url': s.url} for s in _rows(SocialLink)] or list(D.SOCIALS)

    columns = []
    col_objs = list(FooterColumn.objects.all())
    if col_objs:
        for col in col_objs:
            columns.append({
                'key': col.key, 'heading': col.heading,
                'links': [{'label': l.label, 'url': l.url}
                          for l in col.links.all().order_by('order')],
            })
    else:
        columns = [dict(c, links=list(c['links'])) for c in D.FOOTER_COLUMNS]

    footer_columns = [c for c in columns if c['key'] != 'bottom']
    footer_bottom_links = next((c['links'] for c in columns if c['key'] == 'bottom'), [])

    return {
        # assets propios (anti-caché)
        'admin_assets_version': _assets_version(),
        # créditos del footer (al lado del copyright); vacío = ocultarlos
        'credits_text': (site.credits_text if site else D.SITE['credits_text']),
        'credits_by': (site.credits_by if site else D.SITE['credits_by']),
        'credits_name': ((site.credits_name if site else None) or site_name),
        'credits_url': ((site.credits_url if site else None) or '/'),
        # apariencia: botones flotantes y tema por defecto
        'show_theme_switcher': (site.show_theme_switcher if site else D.SITE['show_theme_switcher']),
        'show_rtl_switcher': (site.show_rtl_switcher if site else D.SITE['show_rtl_switcher']),
        'default_theme': (site.default_theme if site else D.SITE['default_theme']),
        # sitio / head
        'site_name': site_name,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'copyright_year': copyright_text.split()[0] if copyright_text else '2026',
        'copyright_text': copyright_text,
        'logo': logo,
        'favicon': favicon,
        # header sticky
        'sticky': sticky,
        'nav_items': nav_items,
        # hero
        'hero': _hero_dict(hero_obj),
        # secciones
        'sections': sections,
        # listas del home
        'features': features,
        'service_tabs': service_tabs,
        'pricing_monthly': pricing_list(1),
        'pricing_yearly': pricing_list(2),
        'faqs': faqs,
        'reviews': reviews,
        'counters': counters,
        'partners': partners,
        'blogs': blogs,
        'portfolios': portfolios,
        # contacto / footer
        'contact_infos': contacts,
        'contacts': contacts,
        'footer_description': footer_description,
        'footer_socials': socials,
        'footer_columns': footer_columns,
        'footer_bottom_links': footer_bottom_links,
        # claves legacy que usan otras paginas
        'header_block': hero_obj,
        'feature_blocks': FeatureBlock.objects.all()[:8],
        'pricing_blocks': PricingBlock.objects.all()[:3],
        'team_blocks': TeamBlock.objects.all()[:6],
        'footer_block': footer_obj,
    }
