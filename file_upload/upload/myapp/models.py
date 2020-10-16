from django.db import models

# Create your models here.
test_dir = str()

def setdir(request):
    global test_dir
    test_dir = request

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return test_dir + "/" + filename

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    pic = models.FileField(null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return self.title
