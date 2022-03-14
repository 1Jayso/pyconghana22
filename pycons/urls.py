from django.urls import path
from . import views

app_name = 'pycons'
urlpatterns = [ 
    path('', view=views.past, name='past'),
]