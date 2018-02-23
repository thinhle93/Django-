from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	response = "Why wont this work"
	return HttpResponse(response)

def new(request):
	response = "this is the new"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, num):
	response = "place holder for number " + num
	return HttpResponse(response)

def edit(request, number):
	response = "place holder for edit blog" + number 
	return HttpResponse(response)
def delete(request, numb):
	return redirect('/')


# from django.shortcuts import render, HttpResponse, redirect 
# def index(request):
# 	reponse = "This is the index"
# 	return HttpResponse(response)
# Create your views here.
