from django.conf.urls import patterns, url, include
from views.mainViews import index, members, logout, mainpage
from views.categoryViews import glasses, hats, headphones, item, top_menu

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^mainpage', mainpage, name='mainpage'),
                       url(r'^glasses', glasses, name='glasses'),
                       url(r'^hats', hats, name='hats'),
                       url(r'^headphones', headphones, name='headphones'),
                       url(r'^item', item, name='item'),
                       url(r'^top_menu', top_menu, name='top_menu'),
                       url(r'^$', index, name='index'),
)   
