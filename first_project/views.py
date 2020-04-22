# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("Hello World!!")
	my_dict = {'insert_me':'I am a index'}
	return render(request, 'index.html', context=my_dict)