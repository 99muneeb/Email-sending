from django.shortcuts import render
from Email_send.settings import EMAIL_HOST_USER
from . import forms 
from django.core.mail import send_mail 

# Create your views here.
#DataFlair #Send Email
def Email_send(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Muneeb'
        message = 'Hope you are successfuly send email:)'
        recepient = str(sub['Email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})
