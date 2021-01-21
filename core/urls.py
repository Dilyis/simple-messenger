from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings
from message.views import UserMessagesViewSet
from user.views import LoginView

docs_schema_view = get_schema_view(
    openapi.Info(
        title='Simple-messenger API',
        default_version='v1',
        description=
        'N.B. documentation is auto-generated, so some sections may be wrong. '
        'Ask developers if you have any issues.',
        terms_of_service='',
        license=openapi.License(name='BSD License'),
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)
cache_timeout = settings.SWAGGER_CACHE_TIMEOUT
docs_urls = [
    path('swagger.json', docs_schema_view.without_ui(
        cache_timeout=cache_timeout), name='schema-swagger-json'),
    path('swagger/', docs_schema_view.with_ui(
        'swagger', cache_timeout=cache_timeout), name='schema-swagger-ui'),
    path('redoc/', docs_schema_view.with_ui(
        'redoc', cache_timeout=cache_timeout), name='schema-redoc-ui'),
]

urlpatterns = [
    path('docs/', include(docs_urls)),
    path('admin/', admin.site.urls),
    path('api/v1/login/', LoginView.as_view(), name='users-login'),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/users/<int:pk>/messages/', UserMessagesViewSet.as_view()),
    path('api/v1/messages/', include('message.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
