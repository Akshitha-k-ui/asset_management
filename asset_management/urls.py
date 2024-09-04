"""asset_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from assets import views as asset_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),
    #   path('accounts/', include('django.contrib.auth.urls')),
     path('login/', asset_views.custom_login, name='login'),
    path('admin_dashboard/', asset_views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', asset_views.user_dashboard, name='user_dashboard'),
    path('logout/', asset_views.logout_view, name='logout'),
    path('assets/', asset_views.asset_list, name='asset_list'),  # Ensure this line exists
    path('add_asset/', asset_views.add_asset, name='add_asset'),

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)