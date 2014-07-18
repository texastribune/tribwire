from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from . import models
from .forms import PostModelForm


def index(request):

    return render_to_response('tribwire/index.html', locals(), context_instance=RequestContext(request))

class CreateLink(CreateView):
    model = models.Link
