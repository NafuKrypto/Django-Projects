from email.policy import default
from http.client import HTTPResponse
from multiprocessing import context
from unittest import loader
from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest
from django.template import loader 
from django.urls import reverse

# Create your views here.
from .models import Todo
def list_todo_items(request):
    context={'todo_list':Todo.objects.all()}
    return render(request,'todos/todolist.html',context) #folder path/html file

def insert_todo_items(request:HttpRequest):
    
    todo= Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/') #folder path/html file

def delete_items(request,todo_id):
    todo_delete_item_delete=Todo.objects.get(id=todo_id)
    todo_delete_item_delete.delete()

    return redirect('/todos/list/')

def update_items(request,todo_id):
    todo_update_item=Todo.objects.filter(id=todo_id)
    #template=loader.get_template('todos/update.html')
    context={
        'updated_items':todo_update_item,
        }
    return render(request,'todos/update.html',context) #HttpResponse(template.render(context,request))

def update_data_done(request:HttpRequest, todo_id):
    if 'content1' in request.POST:
         todo_updating=Todo(id=todo_id , content=request.POST.get('content1',False))
         todo_updating.save()
    #changed_content= request.POST['content1']
     
    #todo_updating.content = changed_content #request.POST.get(temp,False)#
   
    context={
       'todo_list':Todo.objects.all()
        }
    return redirect('/todos/list/')