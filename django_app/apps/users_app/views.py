# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import User

from django.contrib import messages


def index(request):
	context={
		"users": User.objects.all()
	}
	print context['users']
	return render(request, "users_app/index_users.html", context)


def show(request, ide):
	user = {
		"current": User.objects.get(id=ide)
	}
	return render(request, 'users_app/show_user.html', user)

def new(request):

	return render(request, 'users_app/new_user.html')

def processnew(request):
	errors = User.objects.validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/users/new')
	else:
		User.objects.create(fullname=request.POST['name'], email=request.POST['email'])

		return redirect('/users')

def edit(request, ide):
	
	user = {
		"edit": User.objects.get(id=ide)
	}
	return render(request, 'users_app/edit_user.html', user)


def processedit(request, ide):
	errors = User.objects.validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/users'+str(ide)+"/edit")
	else:
		edit = User.objects.get(id=ide)

		edit.fullname = request.POST['name']
		edit.email = request.POST['email']
		edit.save()
		return redirect('/users'+str(ide))

def delete(request, ide):
	d = User.objects.get(id=ide)
	d.delete()
	
	return redirect('/users')
# Create your views here.
