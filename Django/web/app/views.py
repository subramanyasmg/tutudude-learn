from django.shortcuts import render, redirect

from app.forms import ContactForm


# Create your views here.

def index(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # print(f"{form.values['name']}: {form.values['email']}")
            contact = form.cleaned_data
            print(contact)
            return render(request, "index.html", {"form": form})
    else:
        form = ContactForm()
        return render(request, "index.html", {"form": form})
