from django.shortcuts import render

from contact.models import Contact


def view(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')[:10]
    return render(request, 'contact/index.html', {'contacts': contacts})


def contact(request, contact_id):
    single_contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact/contact.html', {'contact': single_contact})