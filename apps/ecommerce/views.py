from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


# Create your views here.

def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Welcome to Homepage",
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title": "Contact Page",
        "content": "Welcome to The content page",
        "form": contact_form,
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, 'contact_page.html', context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to The about page",
    }
    return render(request, 'home_page.html', context)
