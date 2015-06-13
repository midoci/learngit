#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns
#
urlpatterns = patterns('',
    url(r'^hello$', 'userManagement.views.hello',name='hello'),
    )
