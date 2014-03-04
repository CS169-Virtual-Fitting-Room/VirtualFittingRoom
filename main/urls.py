from django.conf.urls import patterns, url
from views.userViews import index

urlpatterns = patterns('', url(r'^$', index, name='index'),
)   
