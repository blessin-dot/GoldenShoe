"""devsearch URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('shoes/', views.shoes, name="shoes"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.register, name="register"),
    path('info/', views.info_page, name="info_page"),
    path('refund/', views.refund, name="refund"),
    path('clear_basket/', views.clear_basket, name="clear_basket"),
    path('checkout/', views.checkout, name="checkout"),
    path('view_basket/', views.view_basket, name="view_basket"),
    path('basket/<str:pk>/', views.add_basket, name="add_basket"),
]
