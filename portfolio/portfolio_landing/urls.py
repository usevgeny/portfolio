from django.urls import path
from .views import index

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *




urlpatterns = [
    path('', index, name='index'),
    path('cv/', cv_page, name='cv_page'),


]





if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
