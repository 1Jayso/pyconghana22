#home views 
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 


# Create your views here.
def ticket(request):
    context = {}
    template = 'ticket/ticket.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = 'ticket/register.html'
    return render(request, template, context)