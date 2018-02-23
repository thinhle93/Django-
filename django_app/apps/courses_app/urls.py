from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
   url(r'^$', views.index),
   url(r'^/add$', views.add),
   url(r'^/delete/(?P<ide>\d+)$', views.checkdel),
   url(r'^/confirmdel/(?P<ide>\d+)$', views.confirmdel),
]
