from django.db import models

# Create your models here.
class NotesManager(models.Model):
    notesId= models.AutoField(primary_key=True)
    bookingId= models.CharField(blank=False,max_length=250)
    userId= models.CharField(blank=False,max_length=250)
    notes= models.CharField(blank=False,max_length=500)
    image= models.TextField(blank=True,max_length=10000)
    audio= models.TextField(blank=True,max_length=10000)
    video= models.TextField(blank=True,max_length=10000)