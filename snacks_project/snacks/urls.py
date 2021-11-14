from django.urls import path
from .views import Home, About, Snacks

urlpatterns = [
    path('', Snacks.as_view(), name='snack'),
    path('home', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about')
]
