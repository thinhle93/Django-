from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^random$', views.random),
    url(r'^reset$', views.reset)

  ]