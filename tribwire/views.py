from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .forms import PostModelForm

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('tribwire/index.html', context_dict, context)

def new_wire(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
    	save_it=form.save(commit=False)
    	save_it.save()
    return render_to_response('tribwire/new_wire.html', locals(), context_instance=RequestContext(request))