from django.db import models

# Create your models here.
class Portfolio(models.Model):
    thumnail_image = models.ImageField()
    item_title = models.CharField(max_length=20)
    item_content = models.TextField()
    item_link = models.URLField(max_length=200)

    def __str__(self):
        return self.item_title