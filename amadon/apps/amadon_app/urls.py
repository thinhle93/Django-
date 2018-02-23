from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^process$', views.process), 
	url(r'^checkout$', views.checkout), # This line has changed!
	url(r'^reset$', views.reset),
	]
