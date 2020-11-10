from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})