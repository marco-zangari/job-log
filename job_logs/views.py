from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm
# Create your views here.


def index(request):
    """Home page for JobLog."""
    return render(request, 'job_logs/index.html')


def topics(request):
    """Show all the topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'job_logs/topics.html', context)


def topic(request, topic_id):
    """Show one individual topic from topics and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'job_logs/topic.html', context)


def new_topic(request):
    """Add new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('job_logs:topics'))
    context = {'form': form}
    return render(request, 'job_logs/new_topic.html', context)
