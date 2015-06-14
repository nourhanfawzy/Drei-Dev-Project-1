from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.name)
