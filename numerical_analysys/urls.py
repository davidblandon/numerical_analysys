
from django.contrib import admin
from django.urls import include, path
from chapter_1.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('chapter_1/', include('chapter_1.urls')),
    path('chapter_2/', include('chapter_2.urls')),
    path('chapter_2/', include('chapter_3.urls')),

]
