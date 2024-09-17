from django.urls import path
from .views import home, add_contact, edit_contact, delete_contact, search_contacts

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('search/', search_contacts, name='search_contacts'),
]