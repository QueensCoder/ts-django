### django cheat sheet

## how tostart project

pipenv shell

pipenv install django

django-admin startproject <project name>

cd project_folder

python manage.py run server - runs server

### make new app

python manage.py startapp <app name> - to make new app

    - include new app under installed applications in settings

### make migrations and create new tables

    - inside of a created app write a model inside of the models.py file

    - then createdb name of db

    - include db name and configuration in settings.py

    - postgres requires psycopg

    python manage.py makemigrations
    python manage.py migrate

### setting up views

    - if using template engine instead of rest frame work

    - create templates folder in root dir of project, same level as all apps

    - inside of main app settings make sure app is inside of installed apps

    - under templates section inside of the DIRs list add : os.path.join(BASE_DIR, 'templates')
    - this will join the file path required to find the templates

    -in settings.py add a new path
        path('demo/', include('view_demo.urls'))
        now when demo is hit in browser view_demo.urls will handle what is returned to the browser

    - inside of view_demo dir make a urls.py file

    from django.urls import path
    from . import views

    urlpatterns = [
        path('index', views.index, name='index'),
        path('test', views.test, name='test')
    ]

    - first path uses index function in views and route is demo/index
    -second math uses test function in views route is demo/test

    inside template folder create a new folder and add index.html in new folder
    should look like template/new/index.html

    then inside of views_demo/views.py
    add test to first and hit that route
    should return hello world in browser

    then try index which will return html

    from django.shortcuts import render
    from django.http import HttpResponse
    from .models import Todos


    def test(req):
        return HttpResponse('<h1>Hello world</h1>')


    def index(req):
        todos = Todos.objects.all()
        return render(req, 'new/index.html', {'todos': todos})

    to use data in template engine
    use if statement to check if todos exist
    if they do then iterate over all todos and display

    conditonal statement syntax
    {% if todos %}
        for loop and/or html displayed
    {% else %}
        show something else
    {% endif %}
        determines end of if

    loop syntax
    {% for todo in todos}
        <h1>{{todo.name}}</h1>
    {% endfor %}

### super user

    python manage.py createsuperuser

    insert details

    creates a super user that has controll of backend of website

    register model with super user
    in app go into admin.py
    import model and then

    admin.site.register(ModelNameHere)

    this allows for table info to be displayed in admin area so admin can manipulate data

### forms

    create form.py file

    from django import forms and then create a form class and pass in forms.Form

    now each variable you add such as name or email can use form.<some field name>

    similar to how the db is designed
