from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from timelog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^entry/(?P<time_entry_id>\d+)/$', views.timeEntryDetail, name='detail'),
    url(r'^entry/form$', views.timeEntryForm, name='detail'),
    url(r'^entry/create$', views.createTimeEntry, name='createEntry'),
    url(r'^tag/(?P<tag_id>[\w.]+)/$', views.tagDetail, name='tagDetail'),
    url(r'^tag/$', views.tagIndex, name='tagIndex'))
