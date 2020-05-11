from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
from .form import NameForm


def test(req):
    return HttpResponse('<h1>Hello world</h1>')


def index(req):
    todos = Todos.objects.all()
    return render(req, 'new/index.html', {'todos': todos})


def form(req):
    form = NameForm()
    if req.POST:
        data = req.POST['your_name']
        return render(req, 'new/index.html', {'form': form, 'data': data})

    else:
        return render(req, 'new/index.html', {'form': form})
