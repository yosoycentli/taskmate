from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    context = {
        'welcome_text':"Welcome To Todo List App"
        }
    return render(request, 'todolist.html', context)
