from __future__ import unicode_literals

from django.db import models

class dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	

class ninja(models.Model):
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	dojo = models.ForeignKey(dojo, related_name="ninjas")

# Create your models here.
