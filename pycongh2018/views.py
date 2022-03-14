#home views 
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 

# Create your views here.


def home18(request):
    context = {}
    template = '2018/home18.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = '2018/about18.html'
    return render(request, template, context)

def schedule(request):
    context = {}
    template = '2018/schedule18.html'
    return render(request, template, context)

def conduct(request):
    context = {}
    template = '2018/coc18.html'
    return render(request, template, context)

def guidelines(request):
    context = {}
    template = '2018/guidelines.html'
    return render(request, template, context)

def eporting(request):
    context = {}
    template = 'conduct/eporting-guidelines/eporting-guidelines.html'
    return render(request, template, context)

def sponsor_us(request):
    context = {}
    template = '2018/sponsor18.html'
    return render(request, template, context)

def sponsors(request):
    context = {}
    template = '2018/sponsors18.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = '2018/egister18.html'
    return render(request, template, context)

def traveladvice(request):
    context = {}
    template = '2018/travel18.html'
    return render(request, template, context)

def fin_aid(request):
    context = {}
    template = '2018/fin-aid18.html'
    return render(request, template, context)

def team(request):
    context = {}
    template = '2018/team18.html'
    return render(request, template, context)

def report(request):
    context = {}
    template = '2018/report18.html'
    return render(request, template, context)
