from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 
def random(request):
	if not 'count' in request.session:
		request.session = 0
	else:
		request.session['count'] += 1

	word = get_random_string(length=5)
	context = {"random": word,
		'counter': request.session['count']
	}

	return render(request, 'random_word/randword.html', context)

def reset(request):
	request.session['count'] = 0
	return redirect('/random')
# Create your views here.
