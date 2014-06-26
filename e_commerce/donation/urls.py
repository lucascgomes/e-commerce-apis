from django.conf.urls import patterns, url
from donation import views 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)