from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def view(request):
    return render(request, "app_blog/read_one.html")
