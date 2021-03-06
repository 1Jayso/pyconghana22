"""PyConGhana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import handler404, handler500
from jet.dashboard.dashboard_modules import google_analytics_views

from django_robohash.views import robohash 
from django.views.static import serve 

from django.conf.urls import handler404, handler500

from home import views

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    path('tickets/', include('tickets.urls', namespace='ticket')),
    path('accounts/', include('registration.backends.default.urls')),
    #path('accounts/', include('registration.backends.simple.urls')),
    path('profile/', include('registration.urls', namespace='profiles')),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path('sponsors/', include('sponsors.urls', namespace='sponsors')),
    path('coc/', include('coc.urls', namespace='coc')),
    # path('contact/', include('contact.urls', namespace='contact')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('support_us/', include('support_us.urls', namespace='support_us')),
    path('prospectus/', include('sponsors.urls', namespace='Prospectus')),
    path('talks/', include('talks.urls', namespace='talks')),
    path('privacypolicy/', include('privacypolicy.urls', namespace='privacypolicy')),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('faq/', include('faq.urls', namespace='faqs')),
    path('pyconorganizers/', admin.site.urls),
    path('pycons/', include('pycons.urls', namespace='pycons')),
    path('robohash/<string>/', robohash, name='robohash'),
    path('avatar/', include('avatar.urls')),


    #Past PyCons 
    path('2018/', include('pycongh2018.urls', namespace='pycongh2018')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.

handler404 = 'home.views.handler404'




# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "PyCon Ghana Admin"
admin.site.site_title = "PyCon Ghana Admin Portal"
admin.site.index_title = "Welcome to PyCon Ghana Portal"