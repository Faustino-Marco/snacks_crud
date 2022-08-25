# LAB - Class 28
## Project: Django CRUD
#### Author: Faustino Marco Simpliciano

### Links and Resources
- Development server: http://127.0.0.1:8000/
- front-end application: "Snacks"

### Feature Tasks & Requirements 08/23
- Create web site in Django with 2 pages
    - home page
    - about page
    - create views/urls/templates as needed for home and about pages
    - use ancestor template to contain navigation elements
    - Should be built the "Django Way"
        - Match the structure of in-class demo

### Typical Steps to Start Django Project
- create project
  - `django-admin startproject name_name_name .`
    - DON'T FORGET THE `.`
  - `mkdir templates`
    - `touch templates/snack_list.html`
  - `python manage.py runserver`
    - if working, now migrate
  - `python manage.py migrate`
- add app to project
  - `python manage.py startapp name_`
- define app
- update settings for app
  - settings
    - installed apps
      - add `#local`
        - add `app_name`
    - templates
      - DIRS
        - add into [] `BASE_DIR / "templates"`
- handle models
  -> models.py
    - make classes
    - `class N_ame(models.Model):`
      - name = models.CharField(max_length=256)
      - etc.
- handle views
  -> views.py
    - handle imports
    - `from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView`
    - `from .models import Thing`
    - make classes
    - `class ThingListView(ListView):`
      - `template_name = "thing_list.html"`
      - `model = Thing`
  - go to admin path to login on dev server
  - see admin.py
    - `from .models import Snack`
    - `admin.site.register(Snack)`
  - `python manage.py showmigrations`
    - `python manage.py makemigrations name_of_app`
    - repeat show migrations cmd
    - runserver
    - use cmd to apply new migration
- add urlpattern
  - create urls.py in app
    - copy over from urls.py in project dir?
    - from django.urls import path
    - from .views import all your views
    - create list of urlpatterns
      - path()
  - `python manage.py createsuperuser`
    - usrnm
    - email
    - pswd
  - populate admin.py
    - register models
      - `from .models import Thing`
      - `admin.site.model(Thing)`
- add tests

### Setup
<!-- .env requirements (where applicable) -->
- requirements.txt
- .gitignore populated using [this](https://www.toptal.com/developers/gitignore/api/python,windows) template.
<!-- 
- PORT - Port Number
- DATABASE_URL - URL to the running Postgres instance/db -->
- How to initialize/run your application (where applicable) e.g. python main.py
  - `python manage.py runserver`
- How to use your library (where applicable)
- Tests
  - How do you run tests?
    - `python manage.py test`
  - Any tests of note?
    - Homepage status code
    - About page status code
    - Homepage use of template
    - About page use of template
  - Describe any tests that you did not complete, skipped, etc
    - N/A
