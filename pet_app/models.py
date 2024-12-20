from django.db import models

# Create your models here.
class Pet(models.Model):
    petName = models.CharField(max_length=255)
    petAge = models.IntegerField()
    petBread = models.CharField(max_length=255)
    petImage = models.CharField(max_length=500)

    class Meta:
        db_table = "pets"



class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = "blog"