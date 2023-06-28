from django.urls import path
from .views import *

app_name = "mailapp"

urlpatterns = [
    path("", homeview, name="home"),
    path("send-mail/", send_mail_view, name="sendmail"),

    path("send-mail-series/", send_mail_series, name="sendmailseries"),
]