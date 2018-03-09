from django.db import models

# Create your models here.

from django.db import models


class Link(models.Model):
    code = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')