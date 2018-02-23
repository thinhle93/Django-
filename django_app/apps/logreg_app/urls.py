from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
   url(r'^$', views.index),
   url(r'^/register$', views.register),
   url(r'^/logcheck$', views.logcheck),
   url(r'^/success$', views.success),
   url(r'^/logout$', views.logout),
   #url(r'^process/(?P<num>\d+)$', views.user),
  
]