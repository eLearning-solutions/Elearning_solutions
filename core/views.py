from django.http import HttpResponse
import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib import messages

from blog.models import Post


def index(request):
    return render(request, 'core/index.html', {})



@csrf_exempt
def offload_email(request):
    if request.method == 'POST':
        req_ = request.body.decode()
        req = json.loads(req_)
        try:
            name = req.get('name')
            email = req.get('email')
            phone_number = req.get('phone_number')
            message = req.get('message')
            mail = EmailMultiAlternatives(subject='ELS Contact Form',
                                          body=f"Phone Number: {phone_number}\nEmail: {email}\n{message}",
                                          from_email=f'{name} <{email}>', reply_to=[email],
                                          to=[ 'fiona@elearningsolutions.co.ke'])
            mail.send()
            return HttpResponse(status=200, content=f'Success')
        except Exception as e:
            return HttpResponse(status=400, content=e)
    return HttpResponse('Send post data instead')
