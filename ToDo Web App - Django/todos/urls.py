from os import name
from django.urls import path
from . import views
#creating my viws here

urlpatterns=[
    path('list/',views.list_todo_items),
    path('insert_todo/',views.insert_todo_items , name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_items , name='delete_todo_item'),
    path('update_todo/<int:todo_id>',views.update_items , name='update_todo_item'),
    path('update_done/<int:todo_id>',views.update_data_done , name='updating_done'),

    ]