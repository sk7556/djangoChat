from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.urls import reverse

    
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/변경.html'

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')
    
    def get_success_url(self):
        return reverse('postdetail', args=[str(self.object.pk)])
    

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist') # 삭제되고 처리가 다 완료되지 않았을 수 있으니 지연 필요한 reverse_lazy를 사용함.

class PostTest(CreateView):
    model = Post
    
    def get(self, request):
        return HttpResponse('PostTest get')
    
    def post(self, request):
        return HttpResponse('PostTest post')
    

postlist = PostList.as_view() # as_view는 진입 메소드
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()