from django.conf.urls import include, url
from views import Init
urlpatterns = [
    url(r'^init', Init, name='/map-init'),
]