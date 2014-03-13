from django.conf.urls import patterns, url, include
from views.mainViews import index, members, logout, mainpage, top_menu
from views.categoryViews import listCategory, listProduct, item
from views.productViews import detail

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^mainpage', mainpage, name='mainpage'),
                       url(r'^item', item, name='item'),
                       url(r'^top_menu', top_menu, name='top_menu'),
                       url(r'^$', index, name='index'),
                       url(r'^category_list', listCategory, name='listCategory'),
                       url(r'^(?P<category>[\w ]+)/$' , listProduct, name='listProduct' ),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)/$', detail, name='detail'),
)   
