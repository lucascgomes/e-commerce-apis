from django.conf.urls import patterns, url
from myapp import views 
from e_commerce.paypal_checkout.paypal_ipn import Endpoint

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^endpoint/$', EndPoint()),
)