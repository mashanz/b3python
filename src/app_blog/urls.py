from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_read_all),
    path("<str:posts_id>", views.posts_read_one),
    path("create", views.posts_create),
    path("<str:posts_id>/update", views.posts_update),
    path("<str:posts_id>/delete", views.posts_delete)
]