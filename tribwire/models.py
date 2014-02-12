from django.db import models
from django.contrib import admin

class Link(models.Model):
	headline = models.CharField(max_length=128)
	blurb = models.CharField(max_length=128)
	date_suggested = models.DateField() 
	#user = models.OnetoOneField(User)
	source = models.ForeignKey('Source')
	wire = models.ForeignKey('Wire')

class Source(models.Model):
	name = models.CharField(max_length=128, unique=True)
	url = models.URLField()
	#favicon = models.OnetoOneField(Favicon)

class Wire(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField()