from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import PostModelForm

def index(request):

    return render_to_response('tribwire/index.html', locals(), context_instance=RequestContext(request))

def new_wire(request):

    form = PostModelForm(request.POST or None)
    if form.is_valid():
    	save_it=form.save(commit=False)
    	save_it.save()
    	
    return render_to_response('tribwire/new_wire.html', locals(), context_instance=RequestContext(request))