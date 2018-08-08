from django.db import models

# Create your models here.
class Portfolio(models.Model):
    thumnail_image = models.ImageField()
    item_title = models.CharField(max_length=20)
    item_content = models.TextField()
    github_link = models.URLField(max_length=200)