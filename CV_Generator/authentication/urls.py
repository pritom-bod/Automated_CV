from django.urls import path
from . import views

urlpatterns = [
    path('', views.userCreate, name='register'),
    path('login/', views.login_from, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('changewithold/', views.change_with_old, name='changewithold'),
    path('withoutold/',views.without_old, name='withoutold'),
    path('success/', views.success, name='success'),
]
