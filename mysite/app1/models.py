from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name="library")

    def __unicode__(self):
        return unicode(self.name)


class Book(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(blank=False)
    about = models.CharField(max_length=500)
    library = models.ForeignKey(Library, null=False)

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Notification(models.Model):
    book_name = models.CharField(max_length=50)
    library = models.ForeignKey(Library, null=False)
    status = models.BooleanField(default=0)
    notified_user = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return unicode(self.book_name)
