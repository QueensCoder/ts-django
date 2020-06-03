from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
from .form import NameForm
from .models import Todos


def test(req):
    return HttpResponse('<h1>Hello world</h1>')


def index(req):
    todos = Todos.objects.all()
    return render(req, 'new/index.html', {'todos': todos})


def form(req):
    form = NameForm()
    if req.POST:
        name = req.POST['name']
        email = req.POST['email']
        data = {
            'name': name,
            'email': email
        }

        new_todo = Todos(name=name, email=email, description='new description')
        new_todo.save()
        return render(req, 'new/index.html', {'form': form, 'data': data})

    else:
        return render(req, 'new/index.html', {'form': form})
