from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('donation.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^donation/', include('donation.urls'))
)
