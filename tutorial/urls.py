"""tutorial URL Configuration

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
from django.urls import path, re_path
from .views import  hello_params_url, hello_template, home_page

urlpatterns = [
    path('home/', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('homeTemplate/', hello_template, name='hellotemplate'),
    path('home_params/<str:name>/<int:eta>/', hello_params_url, name='helloParamUrl'),
]
