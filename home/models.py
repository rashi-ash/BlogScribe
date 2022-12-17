from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class BlogModel (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
    image=models.ImageField(upload_to='images', null=True, blank=True)
    title = models.CharField(max_length=255)
    desc = RichTextField()
    addedtime=models.DateTimeField(auto_now_add=True, blank=True)
    updatedtime=models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.width > 300 or img.height > 200 :
            output_size = (300, 200,)
            img.thumbnail(output_size)
            img.save(self.image.path)
       


