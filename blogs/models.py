from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

