from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from .models import Blog
from .models import Portfolio

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import HomeBlock

        home_blocks_qs = HomeBlock.objects.filter(is_active=True).order_by("order", "id")
        home_blocks = list(home_blocks_qs)
        home_blocks_by_key = {b.key: b for b in home_blocks}
        home_blocks_by_section = {}
        for b in home_blocks:
            home_blocks_by_section.setdefault(b.section, []).append(b)

        context.update(
            {
                "home_blocks": home_blocks,
                "home_blocks_by_key": home_blocks_by_key,
                "home_blocks_by_section": home_blocks_by_section,
            }
        )
        return context

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