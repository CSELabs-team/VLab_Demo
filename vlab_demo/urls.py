from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'apps.thirdauth.views.social_login', name='social_login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^panel/', include('apps.vlab_panel.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
