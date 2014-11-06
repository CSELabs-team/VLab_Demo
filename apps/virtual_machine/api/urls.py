from django.conf.urls import patterns, include, url
from apps.virtual_machine.api.handlers import *

urlpatterns = patterns('',
    url(r'^wakeup[/]?$', WakeUpVMHandler.as_view()),
    url(r'^status[/]?$', VMStatusHandler.as_view()), # Status API is used for admin user
)