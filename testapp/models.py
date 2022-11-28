from django.db import models

# Create your models here.

class ReportTest(models.Model):
    title = models.CharField(max_length = 255)
    graph = models.ImageField()
