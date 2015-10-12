from django.shortcuts import render
from django.views import generic

# Create your views here.
def Index(request, guestbook_id):
    template_name = 'guestbook/index.html'
