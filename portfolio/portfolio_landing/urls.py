
from .views import index, cv_page

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('', index, name='index'),
    path('cv/', cv_page, name='cv_page'),


]




