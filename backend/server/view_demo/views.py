from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos


def test(req):
    return HttpResponse('<h1>Hello world</h1>')


def index(req):
    todos = Todos.objects.all()
    return render(req, 'new/index.html', {})
