from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) 
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
