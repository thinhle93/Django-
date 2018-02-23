# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	courses = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	date_added = models.DateTimeField(auto_now_add=True)
# Create your models here.
