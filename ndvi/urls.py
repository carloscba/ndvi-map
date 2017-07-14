from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from apps.lotes.views import LotesViewSet
from apps.profiles.views import *

router = DefaultRouter()

router.register('lotes', LotesViewSet)
router.register('profile', ProfileViewSet)
router.register('login', LoginViewSet, base_name='login')

urlpatterns = [
    url(r'', include(router.urls))
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]