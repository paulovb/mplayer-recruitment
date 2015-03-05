from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'mplayerrecruitment.app.views.home', name='home'),
    url(r'^recruitment/', 'mplayerrecruitment.app.views.recruitment', name='recruitment'),
    url(r'^thanks/', 'mplayerrecruitment.app.views.thanks', name='thanks'),

    # url(r'^mplayerrecruitment/', include('mplayerrecruitment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)

urlpatterns += staticfiles_urlpatterns()
