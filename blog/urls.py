from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostListView, PostDeleteView, UserPostListView, UsersPostsRelation
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 
    path('<int:pk>/like/', UsersPostsRelation.as_view(), name='like'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about-us')
]

