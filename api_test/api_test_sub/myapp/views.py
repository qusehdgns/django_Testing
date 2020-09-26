from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

import os

# POST 500
from django.views.decorators.csrf import csrf_exempt
# pandas 
import pandas as pd
# csv
import csv


# Create your views here.
def receive_file(request):
    return render(request, 'receive_file.html')

@csrf_exempt
def save_file(request):

    position = os.getcwd()

    if not os.path.exists("data"):
        os.makedirs("data")
    
    os.chdir("./data")

    csv_file = request.FILES['csv_file']

    df = pd.read_csv(csv_file)

    df.to_csv("./test.csv", header=True, index=False)

    os.chdir(position)

    print("success")
    
    return HttpResponse("test")
