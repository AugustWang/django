from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from one import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oneisall.views.home', name='home'),
    # url(r'^oneisall/', include('oneisall.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^one/$',views.one_article),
    url(r'^one_img/$',views.one_img),
)
