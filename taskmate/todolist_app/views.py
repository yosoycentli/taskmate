from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    return render(request, 'todolist.html', {})
