from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request --> response
# request handler
# action
def calculate():
    x=1
    y=2
    return x
def say_hello(request):
    #return HttpResponse("Hello World")
    x=calculate()
    #y=2
    return render(request,'hello.html',{'name':'Mosh'})
