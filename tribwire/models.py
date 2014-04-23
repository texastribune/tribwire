from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from datetime import date
from django.utils.translation import gettext as _

from django.forms import ModelForm

class Link(models.Model):
    url = models.URLField(unique=True)
    headline = models.CharField(max_length=120)
    blurb = models.TextField(max_length=300)
    date_suggested = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model())
    source = models.ForeignKey('Source')
    wires = models.ManyToManyField('Wire')

    def __unicode__(self):
        return self.url

class Source(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    favicon = models.TextField()

    def __unicode__(self):
        return self.name


class Wire(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class LinkForm(ModelForm):
    """Auto generated form to create Server models."""
    class Meta:
        model = Link        