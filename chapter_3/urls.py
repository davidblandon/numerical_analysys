
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter_2/Lagrange', views.lagrange, name='lagrange'),
    path('chapter_2/newton_interpolante', views.newton_interpolante, name='newton_interpolante'),
    path('chapter_2/vandermonde', views.vandermonde, name='vandermonde'),
    path('chapter_2/spline_lineal', views.spline_lineal, name='spline_lineal'),
    path('chapter_2/spline_cubico', views.spline_cubico, name='spline_cubico'),
]