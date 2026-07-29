# Django Notes

## Resources
- https://docs.djangoproject.com/en/6.0/intro/tutorial01/
- https://www.markdownguide.org/cheat-sheet/#extended-syntax
- https://docs.djangoproject.com/en/6.0/topics/install/#database-installation

## Initial Setup
1. Create a virtual environment for dependencies: `python -m venv name`
2. From there activate the virtual environment : `name\Scripts\activate`
3. Install Django : `pip install django`
To view dependencies : `pip list`
4. Create a new Django project: `django-admin startproject mysite djangotutorial`

## Part 1 - First View, Projects vs Apps, URLs
After we have created our django project going to go over some of the files that were created

manage.py - command line utility lets interact django project in many ways

mysite/ - directory actual py package for project 

mysite/__init__.py - empty file tells python this directory should be python package

mysite/settings.py - settings/configuration for project

mysite/urls.py - URL declarations for project; a "table of contents" of your Django-powered site

mysite/wsgi.py - entry point for WSGI-compatible web servers to serve your project

mysite/asgi.py - entry point for ASGI-compatible web servers to serve your project

Lets run it locally : `python manage.py runserver`

Only for dev use only 

Each application write in django consists of python package. Django has util to auto generate dir so can focus on build app

### Projects vs apps

app is web application that does something. Project is collecion of configuration and apps for website.

A project can contain multiple apps an app can be multiple projects

To create app : `python manage.py startapp polls`

We are writing first view at 
polls/views.py

After we have created a view 

In order to view our first view we need to map it to url 
found in urls.py - need to make it in polls folder 

go to polls/urls.py

after the url is made now need config root url in mysite project 
use include() and path()
include() should be used when include other url patterns 
admin.site.urls is pre built withing django 

## Part 2 - Database Setup

django and python defaults to sqlite 
for our project will use postgresql

in root settings.py edit timezone

in settings.py there are installed apps - these are ones that come default by django 
admin - admin site 
auth - authentication 
content types - framework content type
sessions - session framework
messages - message framework
static files - manage static file

some of these apps make use of least 1 db table
we need create table in db before can use 

Need run this command : `python manage.py migrate`

### What does migrate do?

Looks at INSTALLED_APPS setting and creates any necessary db tables according to db settings in mysite/settings.py and the db migrations shipped with app 

### Creating models

Django follow DRY - Do not repeat yourself

For Poll app we are going to create 2 models : Question and Choice 

A Question has a question and publication date 
A Choice as 2 fields : 
    - Text of Choice 
    - Vote tally
Each Choice is associated with a Question.

important to know for our app thinking about models

To note each model represented by subclasses django.db.models.Model. Each model has # of class var each represent db field in model

all classes for model derive from field class 
to note first arguement for field class can rename col 

relationship defined with foreignkey choice is related to single question

### Activating models 

That code for model code tells Django some cool info and is able to 

make a table like SQL 
create py db access api for accessing question and choice objects

first we need to tell project where poll app installed 
to do so add reference in INSTALLED_APPS setting polls config class in polls/app.py

so its path goes as follow  polls.apps.PollsConfig then edit mysite/settings.py and add dotted path to installed apps 

after add that run command `python manage.py makemigrations polls`
when run command tell django made changes to model we did made 2 new ones and like changes be store in migration

migrations how django stores changes to models and thus db schema - they are files on disk you can read migration for new model its in migrations folder 

There is command will run migrations for you and manage db schemas  automatic thats called migrate will be cover later

take look sql that migration would run 

`python manage.py sqlmigrate polls 0001`

To check problems with project 

`python manage.py check`

Now we run migrate to create model tables in our db 

`python manage.py migrate`

migrations benefit let change models over time with no need delete tables or db 

### 3 step guide to change models
1. Change your models (in models.py).

2. Run python manage.py makemigrations to create migrations for those changes

3. Run python manage.py migrate to apply those changes to the database.

to note suppose commit migrations its good 

### Playing with API

hop in python shell
`python manage.py shell`

we have no question in system
`Question.objects.all()`

After following exmaples and messing with api our output to line above
QuerySet Question object (1)

Not helpful need to go to model and add __str__ make it easier for naming 

tiimezone docs https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/

The queries and api is all new but got good practice link to documenation 
https://docs.djangoproject.com/en/6.0/topics/db/queries/

Stop here for today : admin

Creating admin sites to manage project is tedious as fk 
So django does that need run command get started good to note - need look into config it tho

lets create a admin user 
`python manage.py createsuperuser`

After create user run server

we will stop here went to admin site and logged in 
after logged in able to edit some things comes from library django.contrib.auth - aut framework ship with django

Thats begs to ask where is polls app? - not in admin app

what need to do is tell admin that question objects have an admin interface. we do this by opening polls/admin.py 

and edit code - look at file

after doing so django knows now in admin site     
You can edit and mess with it in site once registered

meant for admins but need to consider differetn views for different people for lumora

ON TO PART 3 but the models API not comfortable so will practice that b4 part 3 it is reccomended 