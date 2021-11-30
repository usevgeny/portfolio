
from .views import index, cv_page, index_fr, cv_page_fr

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('', index, name='index'),
    path('cv/', cv_page, name='cv_page'),
    path('lang/fr/', index_fr, name='index_fr'),
    path('lang/fr/cv/', cv_page_fr, name='cv_page_fr'),

]




