from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

admin.site.register(Subscriber)