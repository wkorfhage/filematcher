from django.conf.urls.defaults import *

urlpatterns = patterns('filematcher.matcher.views',
    (r'^files/', include('filematcher.matcher.urls')),

    (r'^admin/', include('django.contrib.admin.urls')),
)
