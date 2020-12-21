from django.shortcuts import render

# Create your views here.

def index(request):
	context_dict = {'text':'hello world', 'number':100}
	return render(request, 'basicapp/index.html', context_dict)

def relative(request):
	return render(request, 'basicapp/relative_url_templates.html')

def other(request):
	return render(request, 'basicapp/other.html')

