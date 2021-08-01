from django.http.response import JsonResponse
from django.shortcuts import render
from .models import blogpost
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    posts =  blogpost.objects.all().order_by('-id')[:10]
    context = { "posts" : posts}
    return render(request, 'post/home.html',context)


def post_detail(request, id):
    post = blogpost.objects.get(id=id)
    context = {"post" : post}
    return render(request, 'post/single_post.html', context)

def search(request):
    term = request.GET.get("q", "")
    posts =  blogpost.objects.filter(title__contains=term).order_by('-id')[:10]
    context = { "posts" : posts}
    return render(request, 'post/home.html', context)

@login_required(login_url='http://127.0.0.1:8000/admin/login/')
def secret_view(request):
    return JsonResponse(dict(a="sddffdfs", b="sjdbfksdjbfk"))