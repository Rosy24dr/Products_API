from django.db import models

# Create your models here.

class Review(models.Model):
    review = models.CharField(max_length=400)
    year_of_review = models.IntegerField()