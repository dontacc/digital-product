"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
# from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework_simplejwt import views as view_jwt

urlpatterns = [
    path('admin/', admin.site.urls),
    path("restframework-auth" , include('rest_framework.urls')),


    # path("api/token/" , view_jwt.TokenObtainPairView.as_view() , name="token_obtain_pair"), #access token
    # path("api/token/refres/" , view_jwt.TokenRefreshView.as_view() , name="token_refresh") # refresh token


]
