from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^link_form.html$', views.CreateLink.as_view(), name='link_form'),
        url(r'^receive$', views.receive_links, name='receive_links')
		)
