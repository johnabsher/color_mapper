"""colors URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hex_form, name='home'),

    path('test/', views.test),
    path('test/<colormap>/', views.test_p, name='test'),
    path('test/<colormap>/<int:n>/', views.test_p, name='test'),
    path('test/<colormap>/reverse/', views.test_p, {'flip': True}, name='test'),
    path('test/<colormap>/<int:n>/reverse/', views.test_p, {'flip': True}, name='test'),

    path('api/<colormap>/', views.color_json, name='api'),
    path('api/<colormap>/<int:n>', views.color_json, name='api'),
    path('api/<colormap>/reverse/', views.color_json, {'flip': True}, name='api'),
    path('api/<colormap>/<int:n>/reverse/', views.color_json, {'flip': True}, name='api'),
]
