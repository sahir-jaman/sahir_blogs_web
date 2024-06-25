from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title

