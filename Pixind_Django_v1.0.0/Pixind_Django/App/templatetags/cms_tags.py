from django import template
from django.apps import apps
from django.urls import reverse
import re

register = template.Library()


@register.filter
def rstrip_dot(value):
    """Quita puntos y espacios finales para no duplicar el punto final del footer."""
    return re.sub(r"[\s.]+$", "", str(value or ""))

# (model, etiqueta, glifo) — KPIs del dashboard
SPECS = [
    ("headerblock", "Hero", "◆"),
    ("sectionblock", "Secciones", "▦"),
    ("featureblock", "Features", "✦"),
    ("pricingblock", "Precios", "$"),
    ("faqitem", "FAQs", "?"),
    ("reviewitem", "Testimonios", "❝"),
    ("partnerlogo", "Partners", "⬡"),
    ("blog", "Posts blog", "✎"),
    ("portfolio", "Portfolio", "▣"),
    ("contactinfo", "Contactos", "✉"),
    ("navitem", "Menú header", "☰"),
    ("footerlink", "Footer links", "⌸"),
]


@register.simple_tag
def cms_kpis():
    """Filas + enlace de changangelist por bloque editable del home."""
    out = []
    for model_name, label, icon in SPECS:
        model = apps.get_model("App", model_name)
        try:
            url = reverse(f"admin:{model._meta.app_label}_{model._meta.model_name}_changelist")
        except Exception:
            url = "/admin/App/"
        out.append({"label": label, "icon": icon, "count": model.objects.count(), "url": url})
    return out
