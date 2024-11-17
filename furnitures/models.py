from django.db import models

class Furniture(models.Model):
  prodName = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  availability = models.CharField(max_length=255)
  slug = models.SlugField(default="", null=False)

def __str__(self):
    return f"{self.prodName}"