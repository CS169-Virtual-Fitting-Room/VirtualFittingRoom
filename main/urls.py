from django.conf.urls import patterns, url, include
from views.userViews import index, members, logout

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^$', index, name='index'),
)   
