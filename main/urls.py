from django.conf.urls import patterns, url, include
from views.mainViews import index, members, logout, mainpage, top_menu, fittingroom,qunit
from views.categoryViews import listProduct, category_list
from views.productViews import detail, detailpage
from views.commentViews import addComment, getComments
from views.internalViews import setUpDb

urlpatterns = patterns('', url(r'', include('social_auth.urls')),
                       url(r'^internal', setUpDb, name='internal'),
                       url(r'^members', members, name='members'),
                       url(r'^logout', logout, name='logout'),
                       url(r'^mainpage', mainpage, name='mainpage'),
                       url(r'^top_menu', top_menu, name='top_menu'),
					   url(r'^qunit', qunit, name='qunit'),
                       url(r'^fittingroom', fittingroom, name='fittingroom'),
                       url(r'^$', index, name='index'),
                       url(r'^(?P<category>[\w ]+)/$', category_list, name='category_list'),
                       url(r'^(?P<category>[\w ]+)/list/$' , listProduct, name='listProduct' ),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)_(?P<id>[\d]+)/$', detailpage, name='detailpage'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)_(?P<id>[\d]+)/info/$', detail, name='detail'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)_(?P<id>[\d]+)/comments/add/$', addComment, name='addComment'),
                       url(r'^(?P<category>[\w ]+)/(?P<product>[\w ]+)_(?P<id>[\d]+)/comments/get/$', getComments, name='getComments'),
)   
