from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

router = DefaultRouter(trailing_slash=True)
router.register('', UserViewSet, base_name='users')


urlpatterns = [
    path('', include(router.urls)),
]

