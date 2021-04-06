from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests,'home.html')


def contact(requests):
    return render(requests, 'contact.html')