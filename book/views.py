# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Book


class HomePageView(ListView):
    template_name = 'home.html'
    model = Book
    context_object_name = 'all_books'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class PricePageView(HomePageView):
    template_name = 'price.html'