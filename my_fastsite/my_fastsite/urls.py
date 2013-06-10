from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_fastsite.views.home', name='home'),
    # url(r'^my_fastsite/', include('my_fastsite.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'', TemplateView.as_view(template_name="base.html")),
)
