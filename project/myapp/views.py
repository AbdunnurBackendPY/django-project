from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def about(request):
    return render(request, 'myapp/about.html')


def contacts(request):
    return render(request, 'myapp/contacts.html')
