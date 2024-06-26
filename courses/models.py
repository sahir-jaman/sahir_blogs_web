from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Section(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    video_link = models.TextField(null=True, blank=True)  # Use this field for video URLs if needed
    extra_files = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
