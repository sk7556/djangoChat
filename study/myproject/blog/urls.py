# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostCreateView, PostEditView, PostDeleteView, PostDetailView,CommentCreateView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='postcreate'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='postedit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='postdelete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('comment/create/', CommentCreateView.as_view(), name='commentcreate'),
]
