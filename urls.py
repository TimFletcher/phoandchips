from django.conf.urls.defaults import *
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^guests/', include('guests.urls')),
    (r'^guestbook/', include('guestbook.urls')),
    (r'^admin/', include(admin.site.urls))
)

# Serve static files for local dev only
try:
    import local_settings as settings
    if settings.DEBUG:
        urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        )
except Exception, e:
    print 'No local settings'