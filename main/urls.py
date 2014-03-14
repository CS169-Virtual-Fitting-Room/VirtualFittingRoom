from django.conf.urls import patterns, url, include
from views.mainViews import index, members, logout, mainpage, top_menu
from views.categoryViews import listProduct, category_list
from views.productViews import detail, detailpage

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^mainpage', mainpage, name='mainpage'),
                       url(r'^top_menu', top_menu, name='top_menu'),
                       url(r'^$', index, name='index'),
                       url(r'^(?P<category>[\w ]+)/$', category_list, name='category_list'),
                       url(r'^(?P<category>[\w ]+)/list/$' , listProduct, name='listProduct' ),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)/$', detailpage, name='detailpage'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)/info/$', detail, name='detail'),
)   
