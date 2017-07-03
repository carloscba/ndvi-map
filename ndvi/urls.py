from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import obtain_jwt_token

from django.contrib import admin
from django.conf.urls import url, include

from apps.user.views import UserViewSet
from apps.field.views import FieldViewSet
from apps.task.views import task_ndvi

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'fields', FieldViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('apps.task.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]