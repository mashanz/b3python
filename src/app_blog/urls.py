from django.urls import path
from . import views

# make sure di lock setiap url atleast maksimal 1-2 method saja.
urlpatterns = [
    path("", views.posts_read_all),                        # GET all data           -> /
    path("id/<str:posts_id>", views.posts_read_one),       # GET one data           -> /id/(123)
    path("create", views.posts_create),                    # POST one data          -> /(create)
    path("id/<str:posts_id>/update", views.posts_update),  # PATCH one data         -> /id/(123)/update
    path("id/<str:posts_id>/delete", views.posts_delete)   # DELETE one data        -> /id/(123)/delete
]