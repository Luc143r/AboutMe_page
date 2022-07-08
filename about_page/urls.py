from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('about/', views.aboutme_page, name='about_page'),
    path('portfolio/', views.portfolio_page, name='portfolio_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('future/', views.future_page, name='future_page'),
]