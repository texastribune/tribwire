from django.conf.urls import patterns, url
from tribwire import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))