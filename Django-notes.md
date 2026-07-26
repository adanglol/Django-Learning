# Django Notes

## Resources
- https://docs.djangoproject.com/en/6.0/intro/tutorial01/
- https://www.markdownguide.org/cheat-sheet/#extended-syntax

## Initial Setup
1. Create a virtual environment for dependencies: `python -m venv name`
2. From there activate the virtual environment : `name\Scripts\activate`
3. Install Django : `pip install django`
To view dependencies : `pip list`
4. Create a new Django project: `django-admin startproject mysite djangotutorial`

## Django Concepts
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

Projects vs apps

app is web application that does something. Project is collecion of configuration and apps for website.

A project can contain multiple apps an app can be multiple projects

To create app : `python manage.py startapp polls`

We are writing first view at 
polls/views.py

After we have created a view 