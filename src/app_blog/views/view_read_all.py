from django.db import connection
from django.shortcuts import render
from .utility import namedtuplefetchall


def view(request):
    with connection.cursor() as c:
        c.execute("SELECT * FROM posts")
        rows = namedtuplefetchall(c)
    
    return render(
        request=request, 
        template_name="app_blog/read_all.html", 
        context={
            "rows": rows
        }
    )
