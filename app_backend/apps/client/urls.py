from django.contrib import admin
from django.urls import path, include

from .viewsets import PhoneBookViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('phones', PhoneBookViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls)),
  path('admin/', admin.site.urls),
]