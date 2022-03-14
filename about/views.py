#home views 
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 


# Create your views here.
def about(request):
    context = {}
    template = '2022/about.html'
    return render(request, template, context)

def accommodation(request):
    context = {}
    template = 'accommodation/accommodation.html'
    return render(request, template, context)


def financialaid(request):
    context = {}
    template = 'financialaid/financialaid.html'
    return render(request, template, context)
