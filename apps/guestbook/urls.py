from django.conf.urls.defaults import *
from views import guestbook
from models import Entry

urlpatterns = patterns('',
    url(r'^$', guestbook, name='guestbook_guestbook'),
)