from unicodedata import name
from django.urls import path 
from webApp.views import contact, index, about ,contact
urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    
]
