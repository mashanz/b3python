from django.shortcuts import render
from django.http import request

# Create your views here.
def index(request):
    # proses sebelum render ada di sini
    return render(request, "app_landing/index.html")