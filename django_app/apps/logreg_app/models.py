from __future__ import unicode_literals

from django.db import models


class LogValidate(models.Manager):
	def validate(self,postData):
		errors = {}
		if len(postData['fname']) < 2:
			errors['fname'] = "First name has to be more than 1 letter."
		if len(postData['lname']) < 2:
			errors['lname'] = "Last name has to be more than 1 letter."
		if postData['pass'] != postData['repass']:
			errors['pass'] = "Passwords do not match"

		return errors


class Login(models.Model):
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	objects = LogValidate()
# Create your models here.
