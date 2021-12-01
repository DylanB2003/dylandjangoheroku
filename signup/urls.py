from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('api',views.api),
    path('',TemplateView.as_view(template_name="index.html")),
    path('accounts/',include('allauth.urls')),
    path('logout',LogoutView.as_view()),
]