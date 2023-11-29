from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

# def postlist(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/postlist.html', {'posts':posts})


# def postlist(request):
#     posts = [
#         {'title':'1', 'content':'111'},
#         {'title':'2', 'content':'222'},
#         {'title':'3', 'content':'333'},
#     ]
#     return render(request, 'blog/postlist.html', {'posts':posts})

# def postlist(request):
#     posts = [
#         {'title':'1', 'content':'111'},
#         {'title':'2', 'content':'222'},
#         {'title':'3', 'content':'333'},
#     ]
#     return JsonResponse(posts, safe=False) # dictionary이외를 받을 경우, safe=False로 설정

# 호기심에 의한 테스트
# def postlist(request):
#     posts = list(Post.objects.all()) # post는 serializable하지 않습니다.
#     return JsonResponse(posts, safe=False) # dictionary이외를 받을 경우, safe=False로 설정

def postlist(request):
    posts = []
    for i in Post.objects.all():
        posts.append({'title':i.title, 'content':i.content})
    return JsonResponse(posts, safe=False) # dictionary이외를 받을 경우, safe=False로 설정