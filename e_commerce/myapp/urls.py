from django.conf.urls import patterns, url
from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^endpoint/$', views.ipn_endpoint, name='ipn_endpoint'),
)