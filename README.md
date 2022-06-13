# Django-Projects
# Chatting Web App
## How to build 
Prerequisite : django , pyhton , postgresql , pgadmin installed
Project structure - > D:\Django Projects\Chatting Web app
### 1. Creating Virtual Environment 
**Step 1 :**
```
pip install virtualenv venv
```
**Step 2 :**
```
python -m venv env
```
### 1. Create Django root App
```
env\SCripts\activate
```
root one builds with django admin

```
django-admin startproject django-chat
```
Run and see
```
cd django-chat
python manage.py runserver
```
### 2. Create Django chat App
sub one build with python manage.py 
``` 
python manage.py startapp chat
```
### 3. Templates
create "templates" folder in root directory. then got to settings.py and add 'chats' in 'Installed Apps"
``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',
]
```
then go to "TEMPLATES" and add in "DIRS" following thing in settings.py :

``` 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 
```
**Note: Instead of templates you can use other nams also**
### 3. url , view 
root urls.py
 ```  
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')), #for main url path
]
```
create urls.py in chat app folder
chat>urls.py

 ```
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
]

 ```
chat>views.py

 ```
 from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'home.html')
 ```
 
 Now run 
 
  ```
  (env) D:\..... djangochat:  python manage.py runserver
  ```
  
  Results :  displays home.html
