from django.conf.urls.defaults import *
from filematcher.matcher.models import *

info_dict = {
    'queryset': FileInstance.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
