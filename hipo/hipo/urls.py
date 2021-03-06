"""hipo URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipe import views as recipe_views
from accounts import views as accounts_views



urlpatterns = [
    path('', recipe_views.index, name='index'),
    path('share/', recipe_views.share, name='share'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts_views.signup, name='signup'),
    path('accounts/profile/', accounts_views.dashboard, name='dashboard'),
    path('accounts/profile/<slug:username>/', accounts_views.profile, name='profile'),
    path('detail/<slug:recipe_name>', recipe_views.recipe_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
