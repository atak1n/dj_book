from django.urls import path
from .views import HomePageView, AboutPageView, ContactsPageView, PricePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contacts/', ContactsPageView.as_view, name='contacts'),
    path('price/', PricePageView.as_view, name='price'),
]
