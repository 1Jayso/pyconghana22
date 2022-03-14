#home views 
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 


# Create your views here.
def privacypolicy(request):
    context = {}
    template = 'privacypolicy.html'
    return render(request, template, context)