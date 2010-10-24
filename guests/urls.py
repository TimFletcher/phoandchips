from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^register/', register, name='guests_register'),
    url(r'^rsvp/', rsvp, name='guests_rsvp'),
    url(r'^thanks/', thanks, name='guests_thanks')
)