from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

#from .forms import ContactForm, LoginForm

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/form.html', {'form': form})

def register_page(request):

    return (request, "auth/register.html", {})

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

