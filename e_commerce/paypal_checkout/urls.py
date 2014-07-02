from django.conf.urls import patterns, url
from paypal_checkout import views

urlpatterns = patterns('',
    url(r'^endpoint/$', views.ipn_endpoint, name='ipn_endpoint'),
)