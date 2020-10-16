from django.shortcuts import render, redirect

from myapp.models import setdir

from myapp.forms import UploadForm

import os

def index(request):

    position = os.getcwd()

    os.chdir("..")

    if not os.path.exists("data"):
        os.makedirs("data")

    os.chdir(position)

    return render(request, 'index.html', {})


def image_list(request):
    return render(request, 'list.html', {})


def upload_image(request):
    if request.method == 'POST':
        setdir("personal/test")
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {
        'form':form
    })