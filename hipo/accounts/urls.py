from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.dashboard, name='profile'),
    path('profile/<slug:username>/', views.profile, name='profile'),
]
