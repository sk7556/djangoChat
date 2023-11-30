# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('django.contrib.auth.urls')),  # 추가: 로그인 및 로그아웃 기능
    path('', include('main.urls')),  # 추가: 프론트엔드 URL
]
