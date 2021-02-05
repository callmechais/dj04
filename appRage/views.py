from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def homeRage(requests):
    return HttpResponseRedirect('static/index.html')