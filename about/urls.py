from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'about'
urlpatterns = [
    path('', view=views.about, name='about'),
    path('accommodation', view=views.accommodation, name='accommodation'),
    path('financialaid', view=views.financialaid, name='financialaid'),
]
