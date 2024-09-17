from django.urls import path
from . import views

# make sure di lock setiap url atleast maksimal 1-2 method saja.
urlpatterns = [
    path("api", views.apis.posts_read_all),  # GET all data           -> /
    path(
        "api/id/<str:posts_id>", views.apis.posts_read_one
    ),  # GET one data           -> /id/(123)
    path("api/create", views.apis.posts_create),  # POST one data          -> /(create)
    path(
        "api/id/<str:posts_id>/update", views.apis.posts_update
    ),  # PATCH one data         -> /id/(123)/update
    path(
        "api/id/<str:posts_id>/delete", views.apis.posts_delete
    ),  # DELETE one data        -> /id/(123)/delete
    # Rendering HTML
    path("view/read_all", views.view_read_all.view),
    path("view/read_one", views.view_read_one.view),
    path("view/create", views.view_create.view),
    path("view/update", views.view_update.view),
    path("view/delete", views.view_delete.view),
]
