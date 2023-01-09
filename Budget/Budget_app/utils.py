from datetime import date

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse

from Budget_app.models import CountsList


def set_remainder(request):
    count = CountsList.objects.get(id=request.POST['count_list_id'])
    if request.POST['transaction_type'] == 'True':
        count.balance += float(request.POST['transaction_value'])
    else:
        count.balance -= float(request.POST['transaction_value'])
    count.save()
    return count.balance


def set_transfer_utils(request):
    count_from = CountsList.objects.get(id=request.POST['from_count'])
    count_to = CountsList.objects.get(id=request.POST['to_count'])
    count_from.balance -= float(request.POST['transaction_value'])
    count_to.balance += float(request.POST['transaction_value'])
    count_from.save()
    count_to.save()
    return count_from.balance, count_to.balance


def get_currency_values():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'
    response = requests.get(url)
    data = response.json()
    returned_cur = [x for x in data if x['cc'] in ['USD', 'EUR']]
    return returned_cur


def email_sender(request):
    pk = User.objects.get(email=request.POST['email']).pk
    send_mail(
        subject='Password reset',
        message=f'http://127.0.0.1:8000/password-reset/done/{pk}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(request.POST['email'].lower(),)
    )


