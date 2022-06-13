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
