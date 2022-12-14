
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profilePage, name="profilePage"),
    path("follow/<int:profileUser_id>", views.follow, name="follow"),
    path("following", views.followingPosts, name="followingPosts"),
    path("editPost/<int:post_id>", views.editPost, name="editPost"),
    path("updateLike", views.updateLike, name="updateLike"),
]
