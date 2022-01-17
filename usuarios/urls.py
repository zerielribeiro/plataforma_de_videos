from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('sair/', views.sair, name = 'sair'),
]