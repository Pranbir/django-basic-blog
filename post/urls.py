from django.contrib import admin
from django.urls import path
from . import views

app_name= "post"

urlpatterns = [
    path("", views.home , name="home"),
    path("post/<id>", views.post_detail , name="post_detail"),
    path("search", views.search , name="search"),
    path("secret", views.secret_view , name="secret"),
]