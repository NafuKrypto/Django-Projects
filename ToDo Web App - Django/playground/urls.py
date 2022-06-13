from django.urls import path
from . import views

#URLConfiguration Module
urlpatterns = [
    #use path to create a url pattern object
    #first param of path is route ->str
    #second param of path is view -> returns Httpresponse object
    #the path function returns a url pattern object
    #views.say_hello -> passing a reference to this function 
    
    ##path('playground/hello',views.say_hello)
     
    path('hello/',views.say_hello)
    
    ]

