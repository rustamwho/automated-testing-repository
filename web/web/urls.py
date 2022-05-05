from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('api/', include('topics.urls', namespace='topics')),
    path('api/', include('solutions.urls', namespace='solutions'))
]

# API docs
schema_view = get_schema_view(
   openapi.Info(
      title="Automated testing repository API",
      default_version='v1',
      description='Документация для приложения по автоматизированному '
                  'тестированию репозитория',
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="hello@world.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]