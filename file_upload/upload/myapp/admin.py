from django.contrib import admin

# Register your models here.
from myapp.models import ImageUpload


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(ImageUpload, ImageUploadAdmin)