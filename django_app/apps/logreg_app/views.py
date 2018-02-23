from django.shortcuts import render, redirect
from .models import Login 
import bcrypt
from django.contrib import messages
def index(request):

	return render(request, 'logreg_app/index_logreg.html')

def register(request):

	if request.method == "POST":
		errors = Login.objects.validate(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
				return redirect('/login')
		else:
			cryptpass = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
			Login.objects.create(fname=request.POST["fname"], lname=request.POST["lname"], email=request.POST["email"], password=cryptpass)
			data = {
				"user": Login.objects.get(email=request.POST['email'])
			}
			info = Login.objects.get(email=request.POST['email'])
			request.session['user'] = info.id
			return redirect('/login/success')



def logcheck(request):
	if request.method == "POST":
	#pass in the email and use it to look in the database for a matching one and compare password
	#user filter which will return a list, if its empty then the person is not registered
	#if its not empty then that email is registered but also need to check the bcrypt password
		checklog = Login.objects.filter(email=request.POST['useremail'])
		#logpass = checklog[0]
		
		if len(checklog) > 0:
			logpass = checklog[0]
			if bcrypt.checkpw(request.POST['passcheck'].encode(), logpass.password.encode()) == True:
				request.session['user'] = logpass.id 

				return redirect('/login/success')
			else:
				messages.error(request, "Invalid Log In")
				return redirect('/login')
		else:
			messages.error(request, "Invalid Log In")
			return redirect('/login')

def success(request):
	info = Login.objects.get(id=request.session['user'])
	context = {
		"user": info
	}
	return render(request, "logreg_app/userpage.html", context)
	
def logout(request):
	request.session.clear()
	return redirect('/login')
# Create your views here.
