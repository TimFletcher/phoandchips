from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    url(r'^register/', register, name='guests_register'),
    url(r'^rsvp/', rsvp, name='guests_rsvp'),
    url(r'^thanks/', direct_to_template, {'template': "guest_thanks.html"}, name='guests_thanks')
)