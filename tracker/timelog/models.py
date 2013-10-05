from django.db import models

# Create your models here.

class TimeEntry(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField('start')
    end_time = models.DateTimeField('end')
    description = models.TextField(default='', blank=True)
    tags = models.ManyToManyField('Tag')
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)

    def __unicode__(self):
        return self.name
