# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = {'posts':posts}
	return HttpResponse(t.render(c))
