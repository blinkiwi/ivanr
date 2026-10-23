from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class HomeBlock(models.Model):
    SECTION_CHOICES = (
        ("header", "Header / Navbar"),
        ("hero", "Hero"),
        ("about", "Nosotros"),
        ("features", "Características"),
        ("choose_us", "Por qué elegirnos"),
        ("portfolio", "Portafolio / Proyectos"),
        ("cta", "Llamado a la acción"),
        ("pricing", "Precios"),
        ("reviews", "Reseñas / Testimonios"),
        ("blog", "Blog"),
        ("contact", "Contacto"),
        ("footer", "Pie de página"),
        ("custom", "Sección personalizada"),
    )

    section = models.CharField(
        max_length=30,
        choices=SECTION_CHOICES,
        db_index=True,
        verbose_name="Sección",
        help_text="En qué parte del home aparece este bloque",
    )
    key = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Clave interna",
        help_text="Identificador único del bloque (ej. hero, features-1)",
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Título",
        help_text="Título principal del bloque",
    )
    subtitle = models.TextField(
        blank=True,
        verbose_name="Subtítulo",
        help_text="Texto secundario o descripción corta",
    )
    content = CKEditor5Field(
        blank=True,
        config_name='extends',
        verbose_name="Contenido (HTML)",
        help_text="Editor visual. Puedes pegar HTML o escribir con formato.",
    )
    data = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="Datos estructurados (JSON)",
        help_text="Lista de ítems, tarjetas, productos, etc. (opcional)",
    )
    image = models.ImageField(
        upload_to="home/blocks/",
        blank=True,
        null=True,
        verbose_name="Imagen principal",
        help_text="Imagen destacada del bloque",
    )
    image_alt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Texto alternativo (imagen)",
        help_text="Descripción para accesibilidad y SEO",
    )
    bg_image = models.ImageField(
        upload_to="home/blocks/bg/",
        blank=True,
        null=True,
        verbose_name="Imagen de fondo",
        help_text="Fondo de la sección (si aplica)",
    )
    button_text = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Texto botón 1",
        help_text="Etiqueta del primer botón CTA",
    )
    button_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL botón 1",
        help_text="Enlace del primer botón (ej. /contacto)",
    )
    button_text_2 = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Texto botón 2",
        help_text="Etiqueta del segundo botón CTA",
    )
    button_url_2 = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL botón 2",
        help_text="Enlace del segundo botón",
    )
    css_classes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Clases CSS extra",
        help_text="Clases de Tailwind adicionales (opcional)",
    )
    is_active = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name="Visible en el sitio",
        help_text="Desmarcar para ocultar este bloque del home",
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name="Orden",
        help_text="Orden de aparición (menor = primero)",
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    class Meta:
        ordering = ("order", "id")
        verbose_name = "Bloque del Home"
        verbose_name_plural = "Bloques del Home"

    def __str__(self):
        return f"{self.get_section_display()} · {self.key}"


# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # Add a slug field
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='portfolio_images/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # Add a slug field
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BrandSettings(models.Model):
    """Configuración global de marca: título, favicon y colores de texto."""
    site_title = models.CharField(
        max_length=200,
        default="Pixind",
        verbose_name="Título del sitio",
        help_text="Título que aparece en la pestaña del navegador",
    )
    favicon = models.ImageField(
        upload_to="branding/",
        blank=True,
        null=True,
        verbose_name="Favicon",
        help_text="Icono de la pestaña del navegador (PNG, ICO, SVG)",
    )
    primary_color = models.CharField(
        max_length=7,
        default="#3b82f6",
        verbose_name="Color primario",
        help_text="Color usado en botones, enlaces y elementos destacados",
    )
    text_color = models.CharField(
        max_length=7,
        default="#0f172a",
        verbose_name="Color de texto principal",
        help_text="Color del texto principal del sitio",
    )
    secondary_text_color = models.CharField(
        max_length=7,
        default="#64748b",
        verbose_name="Color de texto secundario",
        help_text="Color de subtítulos y texto menos importante",
    )
    link_hover_color = models.CharField(
        max_length=7,
        default="#2563eb",
        verbose_name="Color hover de enlaces",
        help_text="Color que adquieren los enlaces al pasar el mouse por encima",
    )

    class Meta:
        verbose_name = "Configuración de Marca"
        verbose_name_plural = "Configuración de Marca"

    def save(self, *args, **kwargs):
        # Patrón singleton: solo una instancia permitida (pk=1)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={
            "site_title": "Pixind",
            "primary_color": "#3b82f6",
            "text_color": "#0f172a",
            "secondary_text_color": "#64748b",
            "link_hover_color": "#2563eb",
        })
        return obj

    def __str__(self):
        return "Configuración de Marca"