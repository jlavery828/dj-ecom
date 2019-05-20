from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def home_page(request):
    context = {
        "title": "Hello World!"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About"
    }
    return render(request, "home_page.html", context)

