# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from time import gmtime, strftime

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0

	

	return render(request, "game/index_ngold.html")

def process(request):
	if request.method == "POST":

		if not 'feed' in request.session:
			request.session['feed'] = []
		if request.POST['place'] == 'farm':
			result = random.randrange(10,21)
			request.session['feed'].append("Went to the farm and earned " + str(result) + " gold! " + str(strftime("%I:%M:%S %p, %b %d, %Y", gmtime())))
		if request.POST['place'] == 'cave':
			result = random.randrange(5,11)
			request.session['feed'].append("Went to the cave and earned " + str(result) +" gold! " + str(strftime("%I:%M:%S %p, %b %d, %Y", gmtime())))

		if request.POST['place'] == 'house':
			result = random.randrange(2,5)
			request.session['feed'].append("Went to the house and earned " + str(result) +" gold! " + str(strftime("%I:%M:%S %p, %b %d, %Y", gmtime())))

		if request.POST['place'] == 'casino':
			result = random.randrange(-50,50)
			if result < 0:
				request.session['feed'].append("Went to the casino and lost " + str(result) + " gold! " + str(strftime("%I:%M:%S %p, %b %d, %Y", gmtime())))
			else:
				request.session['feed'].append("Went to the cave and earned " + str(result) +" gold !" + str(strftime("%I:%M:%S %p, %b %d, %Y", gmtime())))

		request.session['gold'] += result
		

	return redirect("/")
def reset(request):
	request.session['gold'] = 0
	request.session['feed'] = []


	return redirect("/")
# Create your views here.
