from django.shortcuts import render, HttpResponse, redirect 
from time import gmtime, strftime, localtime

def index(request):
	

	context = {
	"time": strftime("%H:%M %p", localtime()),
	"date": strftime("%Y-%m-%d", localtime()),
	
	}

	return render(request, 'display_time/page.html', context)




# Create your views here.
