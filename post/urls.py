from django.contrib import admin
from django.urls import path
from . import views

app_name= "post"

urlpatterns = [
    path("", views.home , name="home"),
    path("post/<id>", views.post_detail , name="post_detail"),
    path("search", views.search , name="search"),
    path("secret", views.secret_view , name="secret"),
    path("logout", views.logout_view , name="logout"),
    path("login", views.login_view , name="login"),
    path("register", views.register_view , name="register"),
    path("long", views.very_long_view , name="long"),
    path("aaaa", views.aaaa , name="aaaa"),
    path("mail", views.mail_sender , name="mail_sender"),
]