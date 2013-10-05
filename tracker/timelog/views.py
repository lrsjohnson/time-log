# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from timelog.models import TimeEntry


def home(request):
    return HttpResponse("Text of website!")

def timeEntryDetail(request, time_entry_id):
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id)
    return HttpResponse("Time entry #  %s: %s" % (time_entry_id, time_entry.title))
    
    
