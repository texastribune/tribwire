from django.db import models
from django.contrib import admin

class Link(models.Model):
	headline = models.CharField(max_length=128, unique=True)
	blurb = models.CharField(max_length=128, unique=True)
	dateSuggested = models.DateField() 
	#user = models.OnetoOneField(User)
	#source = models.OnetoOneField(Source)
	#wire = models.ForeignKey(Wire)

class Source(models.Model):
	source = models.CharField(max_length=128, unique=False)
	link = models.URLField()
	#favicon = models.OnetoOneField(Favicon)

class Wire(models.Model):
	name = models.CharField(max_length=128, unique=True)