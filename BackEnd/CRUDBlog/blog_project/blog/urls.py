# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.shortcuts import render

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

def index(request):
    return render(request, 'blog/index.html')

urlpatterns = [
    path('index/', index, name='index'),
    path('', include(router.urls)),  # /api/posts/ 형태로 변경
]
