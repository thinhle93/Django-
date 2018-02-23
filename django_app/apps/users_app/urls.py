from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
	url(r'^(?P<ide>\d+)$', views.show),
	url(r'^/new$', views.new),
	url(r'^/processnew$', views.processnew),
	url(r'^(?P<ide>\d+)/edit$', views.edit),
	url(r'^/processedit(?P<ide>\d+)$', views.processedit),
	url(r'^(?P<ide>\d+)/delete$', views.delete),
	     # This line has changed!
  ]
