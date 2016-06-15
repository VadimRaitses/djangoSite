from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    text2 = models.TextField(default='SOME STRING')
    name = models.CharField(max_length=200,default='SOME STRING')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.name ='Vadik'
        self.text2 = 'Vad'
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
   

    def publish(self):

        self.save()

    def __str__(self):
        return self.title