from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'^search/?$', 'frontend.views.search'),
    (r'^browse/(?P<field>(artist|title|album|any))/(?P<value>.*)$', 'frontend.views.browse'),

    # control and info
    (r'^control/setvolume/(?P<level>\d{1,3})$', 'frontend.views.setvolume'),
    (r'^control/playpause$', 'frontend.views.playpause'),
    (r'^control/updatedb$', 'frontend.views.updatedb'),
    (r'^control/next$', 'frontend.views.next'),
    (r'^unfuckdb$', 'frontend.views.unfuckdb'),
    (r'^ajax/mpd_status$', 'frontend.views.ajax_mpd_status'),
    (r'^ajax/search$', 'frontend.views.ajax_search'),
    (r'^ajax/random$', 'frontend.views.ajax_random'),
    (r'^ajax/createblock$', 'frontend.views.ajax_createblock'),
    (r'^ajax/playlist$', 'frontend.views.ajax_playlist'),
    (r'^ajax/vote/(?P<blockid>.*)$', 'frontend.views.ajax_vote'),
    (r'^ajax/unvote/(?P<blockid>.*)$', 'frontend.views.ajax_unvote'),

    # login stuff
    (r'^accounts/login$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}),

    # path for static content
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # default
    (r'^$', 'frontend.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
