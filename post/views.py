from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import blogpost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('post:home'))

def login_view(request):
    if request.method == "GET":
        msg = request.GET.get("msg")     
        context = {"msg" : msg}
        return render(request, 'post/login.html', context)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return HttpResponseRedirect(reverse('post:login') + "?msg=Username and Password, both are mandatory... 😅")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('post:home'))
        else:
            return HttpResponseRedirect(reverse('post:login') + "?msg=🤬🤬 Username and Password galat hai... 🤬🤬")

def register_view(request):
    if request.method == "GET":
        msg = request.GET.get("msg")     
        context = {"msg" : msg}
        return render(request, 'post/register.html',context)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, username, password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('post:home'))