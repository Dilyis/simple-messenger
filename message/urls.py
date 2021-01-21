from django.urls import path, include
from rest_framework.routers import DefaultRouter

from message.views import MessageViewSet

router = DefaultRouter(trailing_slash=True)
router.register('', MessageViewSet, base_name='messages')


urlpatterns = [
    path('', include(router.urls)),
]

