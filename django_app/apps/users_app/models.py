# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_check = re.compile(r'^[a-zA-Z_\s-]+$')

class UserManager(models.Manager):
	def validator(self, postData):
		errors ={}
		if not name_check.match(postData['name']):
			errors['name'] = "Name can only contain letters"
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Invalid email"
		return errors


class User(models.Model):
	fullname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = UserManager()


# Create your models here.
