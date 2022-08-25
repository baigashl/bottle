from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
]