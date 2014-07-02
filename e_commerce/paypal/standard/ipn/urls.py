from django.conf.urls import patterns, url

urlpatterns = patterns('paypal.standard.ipn.views',
                       url(r'^endpoint/$', 'ipn', name="paypal-ipn"),
)
