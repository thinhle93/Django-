# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
	
	return render(request, "amadon_app/index_amadon.html")

def process(request):
	if request.method == "POST":
		
		if not "totalspent" in request.session:
			request.session['totalspent'] = 0

		if not "totalamount" in request.session:
			request.session['totalamount'] = 0
		if not "totalitem" in request.session:
			request.session['totalitem'] = 0

		if request.POST['product'] == "shirt":
			price = 19.99
		elif request.POST['product'] == "sweater":
			price = 29.99
		elif request.POST['product'] == "cup":
			price = 5.99
		elif request.POST['product'] == "book":
			price = 49.99

		request.session['totalamount'] = price * int(request.POST['quantity'])
		request.session['totalspent'] += request.session['totalamount']
		request.session['totalitem'] += int(request.POST['quantity'])

	return redirect('/checkout')

def checkout(request):
	return render(request, 'amadon_app/checkout.html')

def reset(request):
	request.session['totalspent'] = 0
	request.session['totalitem'] = 0

	return redirect('/')
# Create your views here.
