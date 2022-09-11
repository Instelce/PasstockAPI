from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from api import views as api_views
from users import views as auth_views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),

    path('register/', auth_views.RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginAPIView.as_view(), name="login"),
    path('logout/', auth_views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
