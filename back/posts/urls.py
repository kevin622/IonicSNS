from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts, name='get_posts'),
    path('<post_id>/', views.get_single_post, name='get_single_post'),
    path('<post_id>/change/', views.change_post, name='change_post'),
    path('<post_id>/like/', views.like_post, name='like_post'),
    path('<comment_id>/change/', views.change_comment, name='change_comment'),
    path('<comment_id>/like/', views.like_comment, name='like_comment'),
]
