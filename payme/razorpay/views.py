from django.shortcuts import render
from .models import *

import razorpay
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    if request.method == "POST":
        name= request.POST.get('name')
        amount  = int(request.POST.get('amount'))*100
        print(name, amount)

        client = razorpay.Client(auth=("rzp_test_9nmrK825fjo0Ym", "1f1icPZDRCKvac3lzpOmLSl1"))
        #client = razorpay.Client(auth=("rzp_test_fIQJWiEsCEUyzS", "UiKtan5P5LpnMFLNkKvCEw7x"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        coffee = Payment(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()



        return render(request, 'index.html', {'payment': payment})



    return render(request, 'index.html')


@csrf_exempt
def success(request):
    if request.method  =="POST":
        a = request.POST
        order_id = ""
        for  key,val  in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = Payment.objects.filter(order_id=order_id).first()
        user.paid = True
        user.save()


    return render(request, 'success.html')




