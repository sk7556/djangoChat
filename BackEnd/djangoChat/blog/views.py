from rest_framework import viewsets, permissions
from .models import Notice, BlogPost
from .serializers import NoticeSerializer, BlogPostSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny]) # 권한 설정 페이지를 관리하지 못해 임시로 permission 해제
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

@permission_classes([AllowAny])
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)