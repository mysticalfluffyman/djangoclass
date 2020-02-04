"""class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.NewsTemplateView.as_view(), name='home'),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    #jwt
    path("apis/tokens/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("apis/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #urls for api
    path("api-auth/", include("rest_framework.urls")),
    path("apis/accounts/", include("accounts.apis.api_urls")),
    path("apis/news/", include("news.apis.api_urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)