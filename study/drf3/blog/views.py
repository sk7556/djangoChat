from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 추가: 검색 기능
    def get_queryset(self):
        queryset = Post.objects.all()
        search_param = self.request.query_params.get('search', None)

        if search_param:
            queryset = queryset.filter(
                Q(title__icontains=search_param) |
                Q(content__icontains=search_param)
            )

        return queryset

    # 추가: 댓글 생성
    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
