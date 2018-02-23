# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course
def index(request):
	context = {
		"course": Course.objects.all()

	}
	return render(request,'courses_app/index_course.html', context)

def add(request):
	Course.objects.create(courses=request.POST['course'], desc=request.POST['desc'])
	return redirect('/courses')

def checkdel(request, ide):
	check = {
		"delete": Course.objects.get(id=ide)
	}
	return render(request, "courses_app/checkdel.html", check)

def confirmdel(request, ide):
	d = Course.objects.get(id=ide)
	d.delete()
	
	return redirect('/courses')
# Create your views here.
