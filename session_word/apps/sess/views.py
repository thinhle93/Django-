from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	
	

	return render(request, 'sess/index_sess.html')

def process(request):
	if request.method == "POST":
		if not "word" in request.POST:
			word = "?"
		else:
			word = request.POST['word']
		if not "color" in request.POST:
			color = "black"
		else:
			color = request.POST['color']
		if not "size" in request.POST:
			size = "lowercase"
		else:
			
			size = "uppercase"

		if not 'words' in request.session:
			request.session['words'] = []



		data = {"word": word, "clr": color, "size": size, "time": strftime("%I:%M:%S %p, %b %d, %Y", gmtime())}
		
		add = request.session['words']
		add.append(data)
		request.session['words'] = add

		
	
	return redirect('/')

def reset(request):
	request.session['words'] = []

	return redirect('/')




		


