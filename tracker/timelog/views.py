# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from timelog.models import TimeEntry, Tag
from django.utils import timezone

import re


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

    output = "Entry with id %s titled \"%s\" created." % (new_time_entry.id, title)

    tag_ids_in_title = [match[1:].lower() for match in re.findall("#[\w.]+", title)]
    for tag_id in tag_ids_in_title:
        (tag, created) = Tag.objects.get_or_create(name=tag_id)
        if created:
            output += "\nTag id \"%s\" created." % tag_id
        new_time_entry.tags.add(tag)
    new_time_entry.save()
    return HttpResponse(output, content_type='text')

def tagOutputsRecursively(tag, prefix = ""):
    """
    Returns string with tag outputs
    """
    entries = tag.timeentry_set.all()
    output = prefix + "Entries with tag \"%s\":\n" % tag.name
    for entry in entries:
        output += prefix + "  [%s: %s]\n" % (entry.id, entry.title)
    for child_tag in tag.tag_set.all():
        output += tagOutputsRecursively(child_tag, prefix + "  ")
    return output

def tagIndex(request):
    output = ""
    for tag in Tag.objects.all():
        output += tag.name + '\n'
    return HttpResponse(output, content_type='text')

def tagDetail(request, tag_id):
    output = ""
    try:
        tag = Tag.objects.get(name=tag_id)
        output += tagOutputsRecursively(tag)
    except Tag.DoesNotExist:
        output += "(Tag \"%s\" does not exist)" % tag_id
    return HttpResponse(output, content_type='text')
