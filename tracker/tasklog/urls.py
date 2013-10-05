from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tasklog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
)
