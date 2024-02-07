from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('contact', views.contact, name='contact'),
    path('about-us', views.about, name='about'),
]
