from django.conf.urls import patterns, url, include
from views.mainViews import index, members, logout, mainpage
from views.categoryViews import category_list

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^mainpage', mainpage, name='mainpage'),
                       url(r'^category_list', category_list, name='category_list'),
                       url(r'^$', index, name='index'),
)   
