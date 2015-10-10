from django.shortcuts import render
from mailer.models import Person, MailTemplate
from django.core.mail import send_mail
import csv
import settings
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
		message = MailTemplate.objects.get(id = 1)
		import csv
		f = request.FILES['file']
		with open('google_form_data.csv', 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
		with open('google_form_data.csv', 'rb') as f:
			# row[0] = name 
			# row[1] = email
			reader = csv.reader(f)
			for row in reader:
				print row
				p = Person.objects.create(name = row[0])
				message = "Hello "+p.name+", \n \n"+"Thanks for registering for the XYZ Competition \n" + "Your registration Number is " + p.id + "\n \n" + message
				send_mail("XYZ Competition", message, settings.EMAIL_HOST_USER, row[1])
		return HttpResponse("<h2>Email sent to all new participants successfully</h2>")
	return render(request, template, {})
