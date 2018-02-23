from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<num>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<numb>\d+)/delete$', views.delete)

  ]
