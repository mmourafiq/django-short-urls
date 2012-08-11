# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('short_urls.views',        
    url(r'^$', 'listing',
        {'template_name':'short_urls/list.html'},
        name='shorturls_list'),
    url(r'^create/?$', 'create',
        {'template_name':'short_urls/form.html', 'next': 'shorturls_list'},
        name='shorturls_create'),    
    url(r'^([\w\d]*)/?$', 'view', name='shorturls_view'),
)