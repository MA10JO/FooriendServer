from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Post, Category,  Comment
from .serializers import AdvSerializer, CommentSerializer

# Create your views here.
@csrf_exempt
def PostList(request):
    if request.method == 'GET':
        query_set = Post.objects.all()
        serializer = AdvSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdvSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def CommentList(request):
    if request.method == 'GET':
        query_set = Comment.objects.all()
        serializer = CommentSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


"""
# Create your views here.
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'head_image', 'file_upload', 'star_point']
    #모델면_form.html

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            return response
        else:
            return redirect('/review/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    # 템플릿은 모델명_list.html : post_list.html
    # 매개변수 모델명_list : post_list

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html : post_detail.html
    # 매개변수 모델명 : post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

def category_page(request, slug):
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
        return render(request, 'review/post_list.html', {
            'category' : category,
            'post_list' : post_list,
            'categories' : Category.objects.all()
        })
"""