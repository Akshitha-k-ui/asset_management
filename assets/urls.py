# assets/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
  
    path('assets/', views.asset_list, name='asset_list'),
    #  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
     path('add/', views.add_asset, name='add_asset'),
    path('edit/<int:pk>/', views.edit_asset, name='edit_asset'),
    path('delete/<int:pk>/', views.delete_asset, name='delete_asset'),
    path('login/', views.custom_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('/user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('list/', views.asset_list, name='asset_list'),
    
]
from django.contrib import admin

admin.site.site_header = "Assets Management Dashboard"
admin.site.site_title = "Assets Management Dashboard"
admin.site.index_title = "Welcome to Assets Management Dashboard"





