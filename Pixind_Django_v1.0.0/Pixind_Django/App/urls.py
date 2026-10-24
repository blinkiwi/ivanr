from django.urls import path
from .views import (
    IndexView,IndexTwoView,IndexThreeView,IndexFourView,IndexFiveView,IndexMultiView,
    AboutusView,FeaturesView,BlogView,SingleBlogView,PortfolioView,SinglePortfolioView,
    PricingView,TeamView,ContactusView,rz_palette_css
)

app_name = 'App'

urlpatterns = [
    path("", IndexFiveView.as_view(), name="index"),

    # tailwind.css con el primario de la paleta aplicada
    path("rz-palette.css", rz_palette_css, name="rz_palette_css"),

    path("index-two/", IndexTwoView.as_view(), name="index_two"),
    path("index-three/", IndexThreeView.as_view(), name="index_three"),
    path("index-four/", IndexFourView.as_view(), name="index_four"),
    path("index-five/", IndexFiveView.as_view(), name="index_five"),
    path("index-multi/", IndexMultiView.as_view(), name="index_multi"),
    
    path("aboutus/", AboutusView.as_view(), name="aboutus"),
    path("features/", FeaturesView.as_view(), name="features"),
    
    path("blog/", BlogView.as_view(), name="blog"),
    
    path("single-blog/", SingleBlogView.as_view(), name="blog_list_or_default"),
    path("single-blog/<slug:title>/", SingleBlogView.as_view(), name="single_blog"),
    
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    
    path("single-portfolio/", SinglePortfolioView.as_view(), name="portfolio_list_or_default"),
    path("single-portfolio/<slug:title>/", SinglePortfolioView.as_view(), name="single_portfolio"),
    
    path("pricing/", PricingView.as_view(), name="pricing"),
    path("team/", TeamView.as_view(), name="team"),
    
    path("contactus/", ContactusView.as_view(), name="contactus"),
]