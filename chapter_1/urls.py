
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter_1/biseccion', views.biseccion, name='biseccion'),
    path('chapter_1/newton', views.newton, name='newton'),
    path('chapter_1/punto_fijo', views.punto_fijo, name='punto_fijo'),
    path('chapter_1/raices_multiples', views.raices_multiples, name='raices_multiples'),
    path('chapter_1/regla_falsa', views.regla_falsa, name='regla_falsa'),
    path('chapter_1/secante', views.secante, name='secante'),
]