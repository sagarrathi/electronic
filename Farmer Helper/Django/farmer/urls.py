from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('das.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^charter/', 'charter',name="charter"),
    url(r'^timer/', 'timer',name="time"),

    # url(r'^farmer/', include('farmer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
