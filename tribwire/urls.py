from django.conf.urls import patterns, url
from tribwire import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new_wire.html$', views.new_wire, name='new_wire'),)

