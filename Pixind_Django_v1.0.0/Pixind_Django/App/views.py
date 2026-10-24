from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.conf import settings
import os
import re
from .models import Blog
from .models import Portfolio

# cache de la hoja de estilos con la paleta: {color: css}
_PALETTE_CACHE = {}
_DEFAULT_PRIMARY = '#4ec163'
_HEX_RE = re.compile(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})')


def rz_palette_css(request):
    """tailwind.css con el color primario de la paleta reescrito (SiteConfig.color_primary)."""
    from .models import SiteConfig
    site = SiteConfig.objects.first()
    color = ((site.color_primary if site else '') or '').strip()
    if not _HEX_RE.fullmatch(color):
        color = _DEFAULT_PRIMARY
    key = color.lower()
    css = _PALETTE_CACHE.get(key)
    if css is None:
        ruta = os.path.join(settings.BASE_DIR, 'static', 'app', 'css', 'tailwind.css')
        try:
            with open(ruta, encoding='utf-8') as f:
                css = f.read()
        except OSError:
            return HttpResponse('', content_type='text/css')
        css = css.replace(_DEFAULT_PRIMARY, color).replace(_DEFAULT_PRIMARY.upper(), color.upper())
        _PALETTE_CACHE.clear()
        _PALETTE_CACHE[key] = css
    return HttpResponse(css, content_type='text/css')

# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'

class IndexTwoView(TemplateView):
    template_name = 'pages/index-two.html'

class IndexThreeView(TemplateView):
    template_name = 'pages/index-three.html'

class IndexFourView(TemplateView):
    template_name = 'pages/index-four.html'

class IndexFiveView(TemplateView):
    template_name = 'pages/index-five.html'

class IndexMultiView(TemplateView):
    template_name = 'pages/index-multi.html'

class AboutusView(TemplateView):
    template_name = 'pages/aboutus.html'

class FeaturesView(TemplateView):
    template_name = 'pages/features.html'

class BlogView(TemplateView):
    template_name = 'pages/blog.html'
    
class SingleBlogView(TemplateView):
    template_name = 'pages/single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('title')  # may be None
        if slug:
            # Detail mode
            context['blog'] = get_object_or_404(Blog, slug=slug)
            context['blogs'] = None
        else:
            # List mode
            context['blogs'] = Blog.objects.all()
            context['blog'] = None
        return context

class PortfolioView(TemplateView):
    template_name = 'pages/portfolio.html'

class SinglePortfolioView(TemplateView):
    template_name = 'pages/single-portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('title')  # may be None
        if slug:
            # Detail mode
            context['portfolio'] = get_object_or_404(Portfolio, slug=slug)
            context['portfolios'] = None
        else:
            # List mode
            context['portfolios'] = Portfolio.objects.all()
            context['portfolio'] = None
        return context

class PricingView(TemplateView):
    template_name = 'pages/pricing.html'

class TeamView(TemplateView):
    template_name = 'pages/team.html'

class ContactusView(TemplateView):
    template_name = 'pages/contactus.html'