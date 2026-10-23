from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.urls import reverse
from unfold.admin import ModelAdmin
from unfold.decorators import display

from .models import HomeBlock, BrandSettings


@admin.register(HomeBlock)
class HomeBlockAdmin(ModelAdmin):
    # ---------- LIST VIEW ----------
    list_display = (
        "section_badge",
        "block_info",
        "image_preview_small",
        "is_active_badge",
        "order_field",
        "updated_at_short",
        "action_buttons",
    )
    list_display_links = ("block_info",)
    list_filter = ("section", "is_active")
    search_fields = ("key", "title", "subtitle")
    prepopulated_fields = {"key": ("title",)}
    save_on_top = True
    ordering = ("order", "id")
    readonly_fields = ("created_at", "updated_at", "image_preview_big", "bg_preview_big")
    list_per_page = 30
    compressed_fields = True
    change_list_template = "admin/app/homeblock/change_list.html"

    # ---------- FORM VIEW ----------
    fieldsets = (
        (
            "1 · Identificación",
            {
                "description": "Define dónde y cómo se llama este bloque en el home.",
                "fields": (
                    ("section", "key"),
                    ("title", "subtitle"),
                    ("is_active", "order"),
                    "css_classes",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "2 · Contenido (Editor visual)",
            {
                "description": "Edita el texto y HTML del bloque con el editor WYSIWYG.",
                "fields": ("content",),
                "classes": ("wide",),
            },
        ),
        (
            "3 · Imágenes",
            {
                "description": "Sube imágenes. Se mostrará una vista previa automáticamente.",
                "fields": (
                    ("image", "image_preview_big"),
                    ("image_alt",),
                    ("bg_image", "bg_preview_big"),
                ),
                "classes": ("wide",),
            },
        ),
        (
            "4 · Botones / CTA",
            {
                "description": "Configura hasta dos botones de llamada a la acción.",
                "fields": (
                    ("button_text", "button_url"),
                    ("button_text_2", "button_url_2"),
                ),
                "classes": ("wide",),
            },
        ),
        (
            "5 · Datos estructurados (JSON)",
            {
                "description": "Lista de ítems, tarjetas, productos o testimonios (avanzado).",
                "fields": ("data",),
                "classes": ("collapse", "wide",),
            },
        ),
        (
            "6 · Metadatos",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    # ---------- CUSTOM DISPLAY METHODS ----------
    @display(description="Sección", ordering="section")
    def section_badge(self, obj):
        colors = {
            "header": "#6366f1",
            "hero": "#22c55e",
            "about": "#06b6d4",
            "features": "#f59e0b",
            "choose_us": "#a855f7",
            "portfolio": "#ec4899",
            "cta": "#ef4444",
            "pricing": "#14b8a6",
            "reviews": "#f97316",
            "blog": "#8b5cf6",
            "contact": "#0ea5e9",
            "footer": "#475569",
            "custom": "#64748b",
        }
        c = colors.get(obj.section, "#64748b")
        return format_html(
            '<span style="background:{}15;color:{};border:1px solid {}33;padding:3px 10px;border-radius:9999px;font-size:10px;font-weight:700;letter-spacing:0.3px;text-transform:uppercase;">{}</span>',
            c, c, c, obj.get_section_display(),
        )

    @display(description="Bloque")
    def block_info(self, obj):
        title = obj.title or obj.key
        subtitle = obj.subtitle
        subtitle_html = f'<br><span style="color:#94a3b8;font-size:11px;">{subtitle[:60]}{"…" if subtitle and len(subtitle) > 60 else ""}</span>' if subtitle else ''
        return format_html(
            '<div style="line-height:1.35;"><strong style="color:#0f172a;">{}</strong>{}</div>',
            title, subtitle_html,
        )

    @display(description="Imagen")
    def image_preview_small(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:44px;height:44px;border-radius:8px;object-fit:cover;border:1px solid #e2e8f0;box-shadow:0 1px 2px rgba(0,0,0,0.06);"/>',
                obj.image.url,
            )
        if obj.bg_image:
            return format_html(
                '<img src="{}" style="width:44px;height:44px;border-radius:8px;object-fit:cover;border:1px solid #e2e8f0;opacity:0.85;box-shadow:0 1px 2px rgba(0,0,0,0.06);"/>',
                obj.bg_image.url,
            )
        return mark_safe('<span style="color:#cbd5e1;">—</span>')

    @display(description="Vista previa (imagen)")
    def image_preview_big(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:320px;border-radius:10px;border:1px solid #e2e8f0;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);"/>',
                obj.image.url,
            )
        if obj.bg_image:
            return format_html(
                '<img src="{}" style="max-width:320px;border-radius:10px;border:1px solid #e2e8f0;opacity:0.85;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);"/>',
                obj.bg_image.url,
            )
        return mark_safe('<div style="color:#94a3b8;font-style:italic;">Sin imagen cargada</div>')

    @display(description="Vista previa (fondo)")
    def bg_preview_big(self, obj):
        if obj.bg_image:
            return format_html(
                '<img src="{}" style="max-width:320px;border-radius:10px;border:1px solid #e2e8f0;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);"/>',
                obj.bg_image.url,
            )
        return mark_safe('<div style="color:#94a3b8;font-style:italic;">Sin imagen de fondo</div>')

    @display(description="Visible", ordering="is_active", boolean=True)
    def is_active_badge(self, obj):
        return obj.is_active

    @display(description="Orden", ordering="order")
    def order_field(self, obj):
        return format_html(
            '<span style="background:#f1f5f9;padding:2px 8px;border-radius:6px;font-size:11px;color:#475569;font-weight:600;">#{}</span>',
            obj.order,
        )

    @display(description="Actualizado")
    def updated_at_short(self, obj):
        return obj.updated_at.strftime("%d/%m %H:%M") if obj.updated_at else "—"

    @display(description="Acciones")
    def action_buttons(self, obj):
        change_url = reverse("admin:App_homeblock_change", args=[obj.pk])
        return format_html(
            '<a href="{}" class="button" style="background:#3b82f6;color:#fff;padding:4px 10px;border-radius:6px;font-size:11px;font-weight:600;text-decoration:none;">Editar</a>',
            change_url,
        )

    # ---------- HELPERS ----------
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Make key field readonly when editing existing object
        if obj:
            form.base_fields["key"].widget.attrs["readonly"] = True
            form.base_fields["key"].help_text = "La clave no se puede cambiar tras guardar."
        return form


# ============================================================================
# CONFIGURACIÓN DE MARCA (singleton)
# ============================================================================
from django import forms


class ColorInput(forms.TextInput):
    input_type = "color"


class BrandSettingsForm(forms.ModelForm):
    class Meta:
        model = BrandSettings
        fields = "__all__"
        widgets = {
            "primary_color": ColorInput(attrs={"class": "color-picker"}),
            "text_color": ColorInput(attrs={"class": "color-picker"}),
            "secondary_text_color": ColorInput(attrs={"class": "color-picker"}),
            "link_hover_color": ColorInput(attrs={"class": "color-picker"}),
            "site_title": forms.TextInput(attrs={"class": "vTextField", "style": "width: 100%;"}),
        }


@admin.register(BrandSettings)
class BrandSettingsAdmin(ModelAdmin):
    form = BrandSettingsForm
    list_display = ("site_title", "favicon_preview", "primary_color_swatch", "text_color_swatch", "secondary_text_color_swatch", "link_hover_color_swatch")
    list_display_links = ("site_title",)
    readonly_fields = ("favicon_preview_big", "color_swatches")
    save_on_top = True
    ordering = ("pk",)
    fieldsets = (
        (
            "1 · Identidad",
            {
                "description": "Configura el título y el favicon que se mostrarán en el navegador.",
                "fields": (
                    ("site_title",),
                    ("favicon", "favicon_preview_big"),
                ),
                "classes": ("wide",),
            },
        ),
        (
            "2 · Colores de Texto",
            {
                "description": "Elige los colores principales del sitio usando el selector de color.",
                "fields": (
                    ("primary_color", "text_color", "secondary_text_color", "link_hover_color"),
                    "color_swatches",
                ),
                "classes": ("wide",),
            },
        ),
    )

    def has_add_permission(self, request):
        # Evitar crear más de una instancia
        return not BrandSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    # ---------- CUSTOM DISPLAY ----------
    @display(description="Favicon")
    def favicon_preview(self, obj):
        if obj.favicon:
            return format_html(
                '<img src="{}" style="width:28px;height:28px;border-radius:6px;border:1px solid #e2e8f0;object-fit:cover;"/>',
                obj.favicon.url,
            )
        return mark_safe('<span style="color:#cbd5e1;">—</span>')

    @display(description="Favicon")
    def favicon_preview_big(self, obj):
        if obj.favicon:
            return format_html(
                '<img src="{}" style="max-width:160px;border-radius:10px;border:1px solid #e2e8f0;box-shadow:0 4px 6px -1px rgba(0,0,0,0.1);"/>',
                obj.favicon.url,
            )
        return mark_safe('<div style="color:#94a3b8;font-style:italic;">Sin favicon cargado</div>')

    @display(description="Color primario")
    def primary_color_swatch(self, obj):
        return mark_safe(
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:4px;border:1px solid #e2e8f0;background:{obj.primary_color};"></span> {obj.primary_color}'
        )

    @display(description="Color texto")
    def text_color_swatch(self, obj):
        return mark_safe(
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:4px;border:1px solid #e2e8f0;background:{obj.text_color};"></span> {obj.text_color}'
        )

    @display(description="Color secundario")
    def secondary_text_color_swatch(self, obj):
        return mark_safe(
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:4px;border:1px solid #e2e8f0;background:{obj.secondary_text_color};"></span> {obj.secondary_text_color}'
        )

    @display(description="Color hover enlaces")
    def link_hover_color_swatch(self, obj):
        return mark_safe(
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:4px;border:1px solid #e2e8f0;background:{obj.link_hover_color};"></span> {obj.link_hover_color}'
        )

    @display(description="Vista previa de colores")
    def color_swatches(self, obj):
        return mark_safe(
            f'''
            <div style="display:flex;gap:12px;margin-top:8px;">
                <div style="flex:1;padding:12px;border-radius:10px;border:1px solid #e2e8f0;background:{obj.primary_color};color:#fff;">
                    <strong>Primario</strong><br><small>{obj.primary_color}</small>
                </div>
                <div style="flex:1;padding:12px;border-radius:10px;border:1px solid #e2e8f0;background:#fff;color:{obj.text_color};">
                    <strong>Texto</strong><br><small>{obj.text_color}</small>
                </div>
                <div style="flex:1;padding:12px;border-radius:10px;border:1px solid #e2e8f0;background:#fff;color:{obj.secondary_text_color};">
                    <strong>Secundario</strong><br><small>{obj.secondary_text_color}</small>
                </div>
                <div style="flex:1;padding:12px;border-radius:10px;border:1px solid #e2e8f0;background:{obj.link_hover_color};color:#fff;">
                    <strong>Hover enlaces</strong><br><small>{obj.link_hover_color}</small>
                </div>
            </div>
            '''
        )
