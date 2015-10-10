from django.shortcuts import render
from mailer.models import Person, MailTemplate
from django.http import HttpResponse
from django.core.mail import send_mail
import csv
from google_forms_mailer import settings
# Create your views here.
def home(request):
	'''
	Home page view 
	'''
	template = "index.html"
	return render(request, template, {})

def mailer(request, template = "mailer.html"):
	'''
	View for sending the mail to all the participants after 
	reading the csv file
	'''
	if request.method == "POST":
		import csv
		f = request.FILES['file']
		with open('google_form_data.csv', 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
		with open('google_form_data.csv', 'rb') as f:
			# row[1] = name 
			# row[15] = email
			reader = csv.reader(f)
			for row in reader:
				message = MailTemplate.objects.get(id = 1).message
				p = Person.objects.create(name = row[1])
				p.save()
				message = "Hello "+str(p.name)+", \n \n"+"Thanks for registering for the TechnoGrail-2015 \n" + "Your registration Number is " + str(p.id) + "\n \n" + str(message)
				send_mail("Welcome to TechnoGrail-2015", str(message), 'desh.py@gmail.com', [str(row[15])], fail_silently=False)
				print message
		return HttpResponse("<h2>Email sent to all new participants successfully</h2>")
	return render(request, template, {})
