from django.shortcuts import render

from core.models import *


def index(request):
    return render(request, 'index.html',{})