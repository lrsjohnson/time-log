from django.db import models

# Create your models here.

class TimeEntry(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField('start')
    end_time = models.DateTimeField('end')

    def __unicode__(self):
        return self.title
