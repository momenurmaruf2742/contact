from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/view_contacts.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added successfully')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully')
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully')
        return redirect('home')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

def search_contacts(request):
    query = request.GET.get('q')
    contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(last_name__icontains=query) | Contact.objects.filter(email__icontains=query) if query else Contact.objects.all()
    
    return render(request, 'contacts/view_contacts.html', {'contacts': contacts})