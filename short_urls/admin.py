# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django.contrib import admin
from models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
    list_display   = ('url', 'code', 'created_at', 'acces_counter')    
    date_hierarchy = 'created_at'
    ordering       = ('created_at', )
    search_fields  = ('url',)

admin.site.register(ShortURL, ShortURLAdmin)