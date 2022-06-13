from django.db import models

# Create your models here.
# datas from database

class Todo(models.Model):
    content=models.TextField()
