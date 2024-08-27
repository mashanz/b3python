from django.shortcuts import render
from django.http import JsonResponse
from django.template.context_processors import csrf
from django.db import connection
from django.views.decorators.http import require_http_methods

# INSERT DATA
@require_http_methods(["POST"])
def posts_create(request):
    title = "Judul Lain"
    content = "Kontent Lain"
    
    with connection.cursor() as c:
        c.execute("INSERT INTO posts (title, content) VALUES (%s, %s) returning *", [title, content])
        row = c.fetchone()
    
    print(row)
    
    return JsonResponse({
        "method": "POST",
        "description": "CREATE"
    })

@require_http_methods(["GET"])
def posts_read_all(request):
    csrf_generate = csrf(request)
    csrf_value = csrf_generate['csrf_token']  
    print(csrf_value)

    with connection.cursor() as c:
        c.execute("SELECT * FROM posts")
        row = c.fetchall()
    
    print(row)

    return JsonResponse({
        "method": "GET",
        "description": "READ ALL",
        "token": f"{csrf_value}"
    })

@require_http_methods(["GET"])
def posts_read_one(request, posts_id):
    # tambahkan validasi posts_id adalah uuid bukan integer atau str
    # ...

    with connection.cursor() as c:
        c.execute("SELECT * FROM posts WHERE id = %s", [posts_id])
        row = c.fetchone()

    print(row)
    title = ""
    content = ""
    
    if row:
        title = row[1]
        content = row[2]

    return JsonResponse({
        "method": "GET",
        "description": "READ ONE",
        "data": posts_id,
        "title": title,
        "content": content
    })

@require_http_methods(["PATCH"])
def posts_update(request, posts_id):
    return JsonResponse({
        "method": "PATCH",
        "description": "UPDATE DATA",
        "data": posts_id
    })

@require_http_methods(["DELETE"])
def posts_delete(request, posts_id):
    return JsonResponse({
        "method": "DELETE",
        "description": "DELETE DATA",
        "data": posts_id
    })