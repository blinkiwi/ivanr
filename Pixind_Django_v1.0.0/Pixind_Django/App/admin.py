from django.contrib import admin
from .models import (
    SiteConfig, StickyNav, NavItem, HeaderBlock, SectionBlock, FeatureBlock,
    ServiceTab, PricingBlock, FAQItem, ReviewItem, CounterItem, PartnerLogo,
    FooterColumn, FooterLink, SocialLink, FooterBlock, ContactInfo, TeamBlock,
    Blog, Portfolio,
)

admin.site.site_header = "Rizoivan · Panel de contenido"
admin.site.site_title = "Rizoivan CMS"
admin.site.index_title = "Dashboard"


# --------------------------------------------------------------- panel CMS ---
def _cms_home(request):
    from django.template.response import TemplateResponse
    from .cms import cms_context

    context = dict(admin.site.each_context(request))
    context.update(cms_context())
    context["title"] = "Panel de contenido"
    return TemplateResponse(request, "admin/cms_home.html", context)


_orig_get_urls = admin.AdminSite.get_urls


def _get_urls_with_cms(self):
    from django.contrib.admin.views.decorators import staff_member_required
    from django.urls import path as _path

    return [_path("cms/", staff_member_required(_cms_home), name="cms-home")] + _orig_get_urls(self)


admin.AdminSite.get_urls = _get_urls_with_cms


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'meta_title', 'updated_at')

    fieldsets = (
        ('Identidad', {'fields': ('site_name', 'meta_title', 'meta_description', 'logo', 'favicon')}),
        ('Footer', {'fields': ('copyright_text',)}),
        ('Créditos del footer (al lado del copyright)', {
            'fields': ('credits_text', 'credits_by', 'credits_name', 'credits_url'),
            'description': 'Se renderizan como: © año COPYRIGHT · TEXTO ♥ NOMBRE_NOMBRE. Déjalos vacíos para ocultar los créditos.',
        }),
        ('Apariencia del sitio (botones flotantes)', {
            'fields': ('default_theme', 'show_theme_switcher', 'show_rtl_switcher'),
            'description': 'Tema por defecto (oscuro) y activar/desactivar los botones flotantes de tema y LTR/RTL de la web.',
        }),
        ('Tecnicos', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(StickyNav)
class StickyNavAdmin(admin.ModelAdmin):
    list_display = ('cta_label', 'cta_url')

    def has_add_permission(self, request):
        return not StickyNav.objects.exists()  # singleton


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    ordering = ('order',)


@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'order')
    list_editable = ('url', 'order')
    ordering = ('order',)


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_line2', 'button_text', 'order')

    fieldsets = (
        ('Titulos y texto', {'fields': ('title', 'title_line2', 'subtitle', 'order')}),
        ('Boton principal + video', {'fields': ('button_text', 'button_link', 'video_id', 'video_label')}),
        ('Fondo', {'fields': ('image',)}),
        ('Tarjeta del formulario', {
            'fields': ('card_title', 'card_name_label', 'card_email_label',
                       'card_phone_label', 'card_button_text'),
        }),
    )


@admin.register(SectionBlock)
class SectionBlockAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'eyebrow', 'order')
    list_editable = ('title', 'eyebrow', 'order')
    list_display_links = ('key',)
    search_fields = ('title', 'eyebrow')

    fieldsets = (
        ('Seccion', {'fields': ('key', 'order')}),
        ('Cabecera (texto)', {'fields': ('eyebrow', 'title', 'description')}),
        ('Boton', {'fields': ('button_label', 'button_url')}),
        ('Imagenes / fondo', {'fields': ('image', 'background_image', 'extra_image')}),
        ('Solo About', {'fields': ('badge_text', 'person_text', 'checklist')}),
        ('Solo About (stat flotante)', {
            'fields': ('stat_label', 'stat_number', 'stat_target', 'stat_percent'),
            'classes': ('collapse',),
        }),
        ('Solo Mapa', {'fields': ('embed_url',)}),
        ('Solo Contacto (placeholders del formulario)', {
            'fields': ('form_name_label', 'form_email_label', 'form_subject_label',
                       'form_message_label', 'form_button_label'),
        }),
    )


@admin.register(FeatureBlock)
class FeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'order')
    list_editable = ('title', 'order')
    search_fields = ('title',)


@admin.register(ServiceTab)
class ServiceTabAdmin(admin.ModelAdmin):
    list_display = ('label', 'title', 'order')
    list_editable = ('order',)


@admin.register(PricingBlock)
class PricingBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'period', 'billing', 'highlight', 'order')
    list_editable = ('price', 'order', 'highlight')
    list_filter = ('billing',)


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    search_fields = ('question',)


@admin.register(ReviewItem)
class ReviewItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)


@admin.register(CounterItem)
class CounterItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'symbol', 'order')
    list_editable = ('number', 'symbol', 'order')


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ('alt', 'order')
    list_editable = ('order',)


@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    list_display = ('key', 'heading', 'order')
    list_editable = ('heading', 'order')
    inlines = [FooterLinkInline]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon', 'url', 'order')
    list_editable = ('order',)


@admin.register(FooterBlock)
class FooterBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'icon')
    list_editable = ('value', 'icon')


@admin.register(TeamBlock)
class TeamBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('role', 'order')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
