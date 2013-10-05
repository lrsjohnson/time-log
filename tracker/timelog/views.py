# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from timelog.models import TimeEntry, Tag
from django.utils import timezone


def home(request):
    return HttpResponse("Text of website!")

def timeEntryDetail(request, time_entry_id):
    time_entry = get_object_or_404(TimeEntry, pk=time_entry_id)
    return HttpResponse("Time entry #  %s: \"%s\"" % (time_entry.id, time_entry.title))

def timeEntryForm(request):
    context = {
        'error_message' : '',
        }
    return render(request, 'timelog/entryform.html', context)

def createTimeEntry(request):
    title = request.POST['entryTitle']
    new_time_entry = TimeEntry(
        title = title,
        start_time = timezone.now(),
        end_time = timezone.now(),        
        )
    new_time_entry.save()
    return HttpResponse("Entry with id %s titled \"%s\" created." % (new_time_entry.id, title))

def tagDetail(request, tag_id):
    output = "Entries with tag \"%s\":\n" % tag_id
    try:
        tag = Tag.objects.get(name=tag_id)
        entries = tag.timeentry_set.all()
        for entry in entries:
            output += "[%s: %s]\n" % (entry.id, entry.title)
    except Tag.DoesNotExist:
        output += "(Tag does not exist)"
    return HttpResponse(output, content_type='text')
