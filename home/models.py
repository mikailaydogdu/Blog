from django.db import models

# Create your models here.

class CourseOnline(models.Model):
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    subject = models.CharField(max_length = 50,verbose_name = "Konu")
    content = models.TextField()

    def __str__(self):
        return self.content

class CourseOfline(models.Model):
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    subject = models.CharField(max_length = 50,verbose_name = "Konu")
    content = models.TextField()

    def __str__(self):
        return self.content

class Work(models.Model):
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    url = models.CharField(max_length = 50,verbose_name = "Url")
    image = models.FileField(blank = True, null= True,verbose_name="Fotoğraf")
    content = models.TextField()

    def __str__(self):
        return self.title