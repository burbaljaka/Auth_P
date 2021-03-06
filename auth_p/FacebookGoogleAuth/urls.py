from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('terms/', views.terms, name='terms'),
    path('policy/', views.policy, name='policy'),
    path('welcome/', views.welcome, name='welcome'),
]