from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# rest_framework 추가 후 추가된 코드
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# FBV 사용하는 방식
@api_view(['GET']) # ['GET', 'POST']하면 둘 다 처리 가능
def postlist(request):
    posts = [
        {'title':'1', 'content':'111'},
        {'title':'2', 'content':'222'},
        {'title':'3', 'content':'333'},
    ]
    serializer = posts # 직렬화 하는 단계
    return Response(serializer) # Response로 반환 되었을 때 데이터를 읽을 수도 있고, POST를 보낼 수도 있습니다.