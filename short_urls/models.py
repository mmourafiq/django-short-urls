# -*- coding: utf-8 -*-
from django.utils.translation import ugettext, ugettext_lazy as _
from django.db import models

class ShortURL(models.Model):
    url = models.URLField(verbose_name="URL", unique=True)
    code = models.CharField(max_length=7, unique=True)    
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)    
    acces_counter = models.IntegerField(default=0, verbose_name="Access Counts")

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ["-acces_counter"]
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"
        unique_together = (('url', 'code'),)
    
    @models.permalink
    def get_absolute_url(self):
        url = 'shorturl_view'
        return (url, [self.code])
    
