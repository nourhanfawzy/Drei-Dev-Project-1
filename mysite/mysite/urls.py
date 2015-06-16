from django.conf.urls import patterns, include, url
from django.contrib import admin
from app1.views import home
from app1.user_account_views import *
from app1.library_book_views import *

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),


    url(r'^messages/', include('postman.urls')),

    url(r'^$', home, name='home'),
    url(r'^sign_up$', user_signup, name='sign_up'),
    url(r'^sign_in$', user_signin, name='sign_in'),
    url(r'^sign_out$', user_signout, name='sign_out'),
    url(r'^my_account/(?P<user_id>\d+)$', user_account, name='my_account'),

    url(r'^edit_account/(?P<user_id>\d+)$',
        user_edit_account, name='edit_account'),

    url(r'^library_list$',
        LibrariesListView.as_view(), name='library_list'),

    url(
        r'^(?P<pk>[-\w]+)/Library_Detail$',
        LibrariesDetailView.as_view(), name='library_detail'),

    url(
        r'^book_list/(?P<library_id>\d+)/$',
        MyBookListView.as_view(), name='book_list'),

    url(r'^book_form/(?P<library_id>\d+)/$',
        BookCreate.as_view(), name='book_form'),

    url(
        r'^(?P<pk>[-\w]+)/Book_Detail$',
        MyBookDetailView.as_view(), name='book_detail'),
    url(
        r'^(?P<pk>[-\w]+)/Book_Update$',
        BookUpdate.as_view(), name='book_update'),
    url(
        r'^(?P<pk>[-\w]+)/Book_Delete$',
        BookDelete.as_view(), name='book_delete'),

    url(
        r'^notification_list/(?P<user_id>\d+)/$',
        NotificationListView.as_view(), name='notification_list'),
)
