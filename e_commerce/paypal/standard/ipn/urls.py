from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('paypal.standard.ipn.views',
                       url(r'^endpoint/$', 'ipn', {'SSL':settings.ENABLE_SSL},name="paypal-ipn"),
)
