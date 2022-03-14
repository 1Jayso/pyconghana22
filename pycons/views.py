#home views 
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
 



# 2022.  
def past(request):
    context = {}
    template = '2022/past.html'
    return render(request, template, context)




def handler404(request, exception):
    return render(request, '404.html', locals())