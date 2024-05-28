
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter_2/gauss_seidel', views.gauss_seidel, name='gauss_seidel'),
    path('chapter_2/jacobi', views.jacobi, name='jacobi'),
    path('chapter_2/SOR', views.sor, name='sor'),
]