from django.urls import path, include

from .views import ActivateUser

app_name = 'users'

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('activate-account/<str:uid>/<str:token>', ActivateUser.as_view()),
]