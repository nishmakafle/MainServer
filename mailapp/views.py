from asgiref.sync import sync_to_async
from django.core.mail import send_mail
from django.views.generic import View
from django.shortcuts import render
from .models import *
import asyncio
import time


async def homeview(request):
    context = {
    }
    return render(request, "home.html", context)


async def django_send_mail(email, subject, message):
    print("sending mail")
    # send_mail_async = sync_to_async(send_mail, thread_sensitive=False)
    # await send_mail_async("this is test subject", "Hello world, This is test message.", "noreply.necommerce@gmail.com", ["nishma.kafle225@gmail.com"], fail_silently=True)
    await sync_to_async(send_mail, thread_sensitive=False)(subject, message, "noreply.necommerce@gmail.com", [email], fail_silently=True)
    print("mail sent...")


async def create_randon_subscriber(n):
    print("creating subscribers")
    for i in range(n):
        email = "email_" + str(i) + "@gmail.com"
        await sync_to_async(Subscriber.objects.create, thread_sensitive=True)(email=email)

    print("created succesfully")



async def send_mail_view(request):
    if request.method == "GET":
        return render(request, "sendmail.html")
    else:
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print("welcome to send mail function")
        # python 3.7 +
        # asyncio.create_task(create_randon_subscriber(100))
        # asyncio.create_task(django_send_mail(email, subject, message))
        # asyncio.gather(create_randon_subscriber(500), django_send_mail())

        # python 3.6 
        loop = asyncio.get_event_loop()
        task1 = loop.create_task(django_send_mail(email, subject, message))
        context = {
            "message": f"Mail will be sent to {email} with the subject {subject} immediately. Thanks"
        }
        return render(request, "sendmail.html", context)


async def dj_send_mail(email):
    send_mail_async = sync_to_async(send_mail, thread_sensitive=False)
    await send_mail_async("this is test subject", "Hello world, This is test message.", "noreply.necommerce@gmail.com", [email], fail_silently=True)


async def send_mail_series(request):
    context = {}
    t1 = time.time()
    await dj_send_mail("nishma.kafle225@gmail.com")
    await django_send_mail("nishma.kafle225@gmail.com")
    t2 = time.time()
    context["time"] = t2-t1
    return render(request, "sendmail.html", context)