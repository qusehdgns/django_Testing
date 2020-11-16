from django.shortcuts import render, redirect

from myapp.models import setdir

from myapp.forms import UploadForm

from myapp.models import ImageUpload

from django.http import FileResponse

import os

def index(request):

    position = os.getcwd()

    os.chdir("..")

    if not os.path.exists("data"):
        os.makedirs("data")

    os.chdir(position)

    return render(request, 'index.html', {})


def image_list(request):
    file = ImageUpload.objects.all()

    print(file)

    files = []

    for temp in file:
        print(temp)
        files.append(temp)

    print(files)

    return render(request, 'list.html', {'file' : files})


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

def down(request):
    title = request.GET['filename'];

    file = ImageUpload.objects.get(title=title)
    filename = file.pic.path
    response = FileResponse(open(filename, 'rb'))
    return response