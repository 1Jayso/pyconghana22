from django.urls import path
from . import views

app_name = 'sponsors'
urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('prospectus', views.Prospectus, name='Prospectus')
]
