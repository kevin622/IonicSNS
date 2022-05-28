from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name='profle'),
    path('follow/<username>/', views.follow, name='follow'),
]
