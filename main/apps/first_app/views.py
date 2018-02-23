from django.shortcuts import render, HttpResponse, redirect
def index(request):
	response = "Hello there. This is the first request"
	return HttpResponse(response)

# Create your views here.
