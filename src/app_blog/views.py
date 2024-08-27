from django.shortcuts import render
from django.http import JsonResponse, request
from django.template.context_processors import csrf
from django.db import connection
from django.views.decorators.http import require_http_methods
import json

# INSERT DATA
@require_http_methods(["POST"])
def posts_create(request):

    # cara baca post form-data dan x-www-form-urlencoded
    # title = request.POST.get('title', None)
    # content = request.POST.get('content', None)

    # cara baca raw body dan parsing pake json
    json_parsed = json.loads(request.body)
    title = json_parsed["title"]
    content = json_parsed["content"]

    print("===")
    print(title)
    print(content)
    print("===")
    
    with connection.cursor() as c:
        c.execute(f"INSERT INTO posts (title, content) VALUES ({title}, {content}) returning *", [title, content])
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

    title = request.GET.get('title', '')

    with connection.cursor() as c:
        if not title:
            c.execute("SELECT * FROM posts")
        c.execute("SELECT * FROM posts WHERE title ilike %s", [title])
        row = c.fetchall()
    
    print(row)

    return JsonResponse({
        "method": "GET",
        "description": "READ ALL",
        "token": f"{csrf_value}",
        "count_match": len(row)
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