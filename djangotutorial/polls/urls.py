from django.urls import path

# Referencing views.py in this folder
from . import views 

urlpatterns = [
    path("",views.index,name="index")
]
