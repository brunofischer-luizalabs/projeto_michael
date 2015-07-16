from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.main', name='home'),
    url(r'^about.html', 'main.views.about', name='about'),
    url(r'^contact.html', 'main.views.contact', name='contact'),
    url(r'^index.html', 'main.views.main', name='home_principal'),
    # url(r'^projeto_michael/', include('projeto_michael.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
