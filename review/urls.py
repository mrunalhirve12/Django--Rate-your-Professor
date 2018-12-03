from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='review-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_reviews'),
    path('review/new/', PostCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update', PostUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='review-delete'),
    path('review/<int:pk>/', PostDetailView.as_view(), name='review-detail'),
    path('about/', views.about, name='review-about'),
]
