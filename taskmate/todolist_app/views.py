from django.shortcuts import render
from django.http import HttpResponse

def todolist(request):
    context = {
        'welcome_text':"Welcome To Todo List Page"
        }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'contact_text':"Welcome To Contact Page"
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome To About Page"
        }
    return render(request, 'about.html', context)