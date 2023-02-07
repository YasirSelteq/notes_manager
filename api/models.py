from django.db import models

class Notes(models.Model):
    notesId = models.AutoField(primary_key=True,blank=False)
    bookingId = models.CharField(blank=False, max_length=250)
    userId = models.CharField(blank=False, max_length=250)
    notes = models.CharField(blank=False, max_length=500)
    isEnable = models.BooleanField(blank=False, default=True)
    noteType = models.CharField(blank=False, max_length=500, default='self')

class Audio(models.Model):
    audioId = models.AutoField(primary_key=True)
    note = models.CharField(blank=False, max_length=250)
    audioUrl = models.CharField(blank=True, max_length=500)
    isEnable = models.BooleanField(blank=False, default=True)

class Video(models.Model):
    videoId = models.AutoField(primary_key=True)
    note = models.CharField(blank=False, max_length=250)
    videoUrl=  models.CharField(blank=True, max_length=500)
    isEnable = models.BooleanField(blank=False, default=True)

class Image(models.Model):
    imageId = models.AutoField(primary_key=True)
    note = models.CharField(blank=False, max_length=250)
    imageUrl =  models.CharField(blank=True, max_length=500)
    isEnable = models.BooleanField(blank=False, default=True)