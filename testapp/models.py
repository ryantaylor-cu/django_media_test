from django.db import models

# Create your models here.

# List of images requires "many to one" relationship, see:
#   https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/

class ReportTest(models.Model):
    title = models.CharField(max_length = 255)
    # There's an implicit "imagetest_set" field that provides a list of images
    # back to all the images linked to this report

class ImageTest(models.Model):
    # I called the model ImageTest, and the actual image field is called graph.
    # I should have invented better names :-)
    graph = models.ImageField()
    # Each image is linked to a report
    report = models.ForeignKey(ReportTest, on_delete=models.CASCADE)
