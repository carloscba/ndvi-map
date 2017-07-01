from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import task_ndvi

urlpatterns = [
    url(r'^task_ndvi/$', task_ndvi),
]

urlpatterns = format_suffix_patterns(urlpatterns)