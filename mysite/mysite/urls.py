from django.conf.urls import patterns, include, url
from django.contrib import admin
from app1.useraccount_views import home, user_signup, user_account, user_signout, user_signin, user_edit_account

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^signup$', user_signup, name='signup'),
    url(r'^signin$', user_signin, name='signin'),
    url(r'^signout$', user_signout, name='signout'),
    url(r'^myaccount/(?P<u_id>\d+)$', user_account, name='myaccount'),
    url(r'^editaccount/(?P<u_id>\d+)$', user_edit_account, name='editaccount'),
)
