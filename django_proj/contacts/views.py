from django.urls import include, path
from django.contrib import admin

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the contacts index.")


# Create your views here.
