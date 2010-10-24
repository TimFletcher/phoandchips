from django.conf.urls.defaults import *
from views import guestbook
from models import Entry

urlpatterns = patterns('',
    url(r'^$', guestbook, name='guestbook_guestbook'),
    # url(r'^entry/(?P<object_id>\d+)/$', object_detail, all_entries, name='guestbook_object_detail'),
)