# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django import forms
from models import ShortURL

class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ('url',)