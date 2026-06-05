from django.shortcuts import render
from contact import views

# Create your views here.

def view(request):
    return render(request, 'contact/index.html')