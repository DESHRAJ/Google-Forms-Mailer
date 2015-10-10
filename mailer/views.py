from django.shortcuts import render
import csv

# Create your views here.
def home(request):
	'''
	Home page view 
	'''
	template = "index.html"
	return render(request, template, {})

def mailer(request, template = "mailer.html"):
	if request.method == "POST":
		
	return render(request, template, {})

