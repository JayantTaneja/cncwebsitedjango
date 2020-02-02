from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from .certificates import render_to_pdf
from django.contrib.auth.models import User
import datetime
from django.contrib import messages


# Create your views here.


def EventsList(request):
    events = Event.objects.filter(status='False').order_by('-date')
    user = request.user
    if user.is_authenticated:
        registrations = Registration.objects.filter(user=user)
    else:
        registrations = []
    context = {
        'events': events,
        'registrations': registrations,
    }
    return render(request, 'events/event_list.html', context)


def EventDetail(request, eventid):
    event = get_object_or_404(Event, id=eventid)
    user = request.user
    if Registration.objects.filter(event=event):
        registration = Registration.objects.filter(user=user, event=event)
        context = {'event': event, 'registration': registration}
    else:
        context = {'event': event}
    return render(request, 'events/event_detail1.html', context)


def Getpdf(request, username, eventid, *args, **kwargs):
    user = User.objects.get(username=username)
    event = Event.objects.get(id=eventid)
    if username == user.username:
        data = {
            'user': user
        }
        pdf = render_to_pdf('events/certi1.html', )
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return HttpResponse('404')


@login_required
def RegisterForEvent(request, eventid):
    user = request.user
    event = Event.objects.get(id=eventid)
    date = datetime.datetime.now()
    registration = Registration(user=user, event=event, date=date)
    registration.save()
    messages.success(request, 'Thanks for registering for Event - {}'.format(event.event_name))
    if event.status == 'True':
        return redirect('events:events_list')
    else:
        return redirect('events:events_detail', eventid=event.id)


@login_required
def UnregisterForEvent(request, eventid):
    user = request.user
    event = Event.objects.get(id=eventid)
    registration = Registration.objects.get(user=user, event=event)
    registration.delete()
    messages.error(request, 'You\'ve Unregistered for Event - {}'.format(event.event_name))
    if event.status == 'True':
        return redirect('events:events_list')
    else:
        return redirect('events:events_detail', eventid=event.id)
