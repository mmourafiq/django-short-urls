# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import ShortURL
from forms import ShortURLForm
from url_generator import URLEncoder 

encoder = URLEncoder()

def listing(request, template_name=None):
    """redirections listing"""
    short_urls = ShortURL.objects.all()
    c = RequestContext(request, {
                                 'short_urls': short_urls,
                                 })

    return render_to_response(template_name, c)    

def create(request, template_name=None, next=None):
    """create new redirection"""
    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            mini = form.save()
            mini.code = encoder.encode_url(mini.id)    
            mini.save()
            return HttpResponseRedirect(reverse(next))
    else:
        form = ShortURLForm()
        
    c = RequestContext(request, {
                                 'form': form,
                                 })
    return render_to_response(template_name, c)    

def view(request, code):
    """Redirects url with code to the original url"""
    short = get_object_or_404(ShortURL, code=code)
    short.acces_counter += 1
    short.save()
    return redirect(short.url, permanent=True)
