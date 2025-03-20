"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from rest_framework.authtoken.views import obtain_auth_token # type: ignore
from django.conf import settings # type: ignore

# Debug print to verify URL patterns
print("Token endpoint URL:", path('api/token/', obtain_auth_token, name='api_token_auth'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentors/', include('mentor.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
