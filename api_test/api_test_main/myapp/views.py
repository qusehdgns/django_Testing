from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
def send_file(request) :
    return render(request, 'send_file.html')