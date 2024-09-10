from django.shortcuts import render

def view(request):
    return render(request, "app_blog/create.html")