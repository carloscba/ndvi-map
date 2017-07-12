from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.profiles.urls')),
    url(r'^api/', include('apps.product.urls')),
]