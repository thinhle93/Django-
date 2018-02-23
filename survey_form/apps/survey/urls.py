from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    #url(r'^process$', view.process)
    url(r'^result$', views.result),
    
    

  ]