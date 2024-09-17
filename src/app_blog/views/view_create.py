from django.shortcuts import render
from django.db import connection

def view(request):
    # parsing form data
    title = request.POST.get('title', None)
    content = request.POST.get('content', None)

    # Safe to DB
    with connection.cursor() as c:
        c.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s) returning *",
            [title, content],
        )
        row = c.fetchone()

    return render(request, "app_blog/create.html", {"row": row})
