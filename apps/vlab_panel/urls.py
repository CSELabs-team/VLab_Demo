from django.conf.urls import patterns, include, url
from apps.vlab_panel import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', views.panel_index, name='panel_index'),
)
