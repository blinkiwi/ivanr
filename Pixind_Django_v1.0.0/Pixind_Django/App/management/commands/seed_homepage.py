"""Copia el contenido original de la plantilla al panel (idempotente).

No pisa filas que ya existen: solo crea las que falten.
"""
from django.core.management.base import BaseCommand

from App.models import (
    SiteConfig, StickyNav, NavItem, HeaderBlock, SectionBlock, FeatureBlock,
    ServiceTab, PricingBlock, FAQItem, ReviewItem, CounterItem, PartnerLogo,
    FooterColumn, FooterLink, SocialLink, FooterBlock, ContactInfo,
)
from App import homepage_defaults as D


class Command(BaseCommand):
    help = 'Precarga el panel con el contenido actual del homepage (seed)'

    def handle(self, *args, **options):
        created = 0

        # Sitio
        if not SiteConfig.objects.exists():
            SiteConfig.objects.create(**D.SITE)
            created += 1

        # Header sticky
        if not StickyNav.objects.exists():
            StickyNav.objects.create(**D.STICKY_NAV)
            created += 1

        # Menu
        if not NavItem.objects.exists():
            for i, item in enumerate(D.NAV_ITEMS):
                NavItem.objects.create(order=i, **item)
                created += 1

        # Hero
        hero_fields = {k: v for k, v in D.HERO.items() if k != 'image'}
        if not HeaderBlock.objects.filter(order=0).exists():
            HeaderBlock.objects.create(order=0, **hero_fields)
            created += 1

        # Secciones
        for i, (key, data) in enumerate(D.SECTIONS.items()):
            if not SectionBlock.objects.filter(key=key).exists():
                SectionBlock.objects.create(key=key, order=i, **data)
                created += 1

        # Features
        if not FeatureBlock.objects.exists():
            for i, f in enumerate(D.FEATURES):
                FeatureBlock.objects.create(
                    order=i, title=f['title'], description=f['description'],
                    icon=f['icon'], url=f['url'])
                created += 1

        # Servicios / tabs
        if not ServiceTab.objects.exists():
            for i, t in enumerate(D.SERVICE_TABS):
                row = ServiceTab(order=i, label=t['label'], title=t['title'],
                                 text=t['text'], url=t['url'])
                row.image.name = t['image']
                row.save()
                created += 1

        # Precios
        if not PricingBlock.objects.exists():
            for i, p in enumerate(D.PRICING):
                PricingBlock.objects.create(
                    order=i, billing=p['billing'], title=p['title'], price=p['price'],
                    period=p['period'], features=p['features'],
                    button_text=p['button_text'], button_link=p['button_link'],
                    highlight=p['highlight'])
                created += 1

        # FAQs
        if not FAQItem.objects.exists():
            for i, f in enumerate(D.FAQS):
                FAQItem.objects.create(order=i, **f)
                created += 1

        # Testimonios
        if not ReviewItem.objects.exists():
            for i, r in enumerate(D.REVIEWS):
                row = ReviewItem(order=i, name=r['name'], role=r['role'], text=r['text'])
                row.avatar.name = r['avatar']
                row.save()
                created += 1

        # Contadores
        if not CounterItem.objects.exists():
            for i, c in enumerate(D.COUNTERS):
                CounterItem.objects.create(order=i, **c)
                created += 1

        # Partners
        if not PartnerLogo.objects.exists():
            for i, p in enumerate(D.PARTNERS):
                row = PartnerLogo(order=i, alt=p['alt'])
                row.image.name = p['image']
                row.save()
                created += 1

        # Contactos
        if not ContactInfo.objects.exists():
            for c in D.CONTACTS:
                ContactInfo.objects.create(**c)
                created += 1

        # Footer
        if not FooterBlock.objects.exists():
            FooterBlock.objects.create(order=0, title='Footer', description=D.FOOTER['description'])
            created += 1
        if not SocialLink.objects.exists():
            for i, s in enumerate(D.SOCIALS):
                SocialLink.objects.create(order=i, **s)
                created += 1
        for i, col in enumerate(D.FOOTER_COLUMNS):
            column, was_created = FooterColumn.objects.get_or_create(
                key=col['key'], defaults={'heading': col['heading'], 'order': i})
            created += 1 if was_created else 0
            for j, link in enumerate(col['links']):
                _, link_created = FooterLink.objects.get_or_create(
                    column=column, label=link['label'],
                    defaults={'url': link['url'], 'order': j})
                created += 1 if link_created else 0

        self.stdout.write(self.style.SUCCESS(
            f'Seed completado: {created} filas creadas (las existentes no se tocaron).'))
