from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if not 'word' in request.session:
		request.session['word'] = 0
	else:
		request.session['word'] = request.session['word']

	return render(request, 'survey/index_survey.html')




def result(request):
	request.session['word'] += 1
	data = {
	"name": request.POST['name'],
	"location": request.POST['location'],
	"favoritelang": request.POST['favlang'],
	"comment": request.POST['comment']
	}
	return render(request, 'survey/index_result.html', data)
