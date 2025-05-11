from django.urls import path
from . import views

urlpatterns = [
    path('', views.userCreate, name='register'),
    path('login/', views.login_from, name='login')
]
