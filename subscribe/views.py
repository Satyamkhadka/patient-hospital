from django.shortcuts import render, redirect
from patient_record.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import SubscribeModel


def subscribe(request):
    q = request.POST.get("subscription-email")
    if request.method == 'POST':
        subject = 'Subscribed to newsletter from disease information system'
        message = 'Thank you '+q + \
            ' for subscribing to our newsletter. You will receive latest update on latest disease, symptoms and prevention.'
        recepient = q
        send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
    obj, created = SubscribeModel.objects.get_or_create(
        email=q
    )
    return redirect('/?s=1')
