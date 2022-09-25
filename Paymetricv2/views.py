from django.shortcuts import render, redirect

from accounts.forms import LoginForm
from .forms import ContactForm

from django.contrib.auth import get_user_model
User = get_user_model()

def startup(request):
    return render(request, "startup.html")

def home_page(request):
    return render(request, "home/home_page.html")

def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form

    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)