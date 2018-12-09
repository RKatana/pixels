from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^$", views.index, name = "index"),
    url(r"^search/",views.search, name = "search"),
    url(r"^locations/",views.locations_page, name = "location"),
    url(r"^location/(\w+)",views.locations, name = "locations")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)