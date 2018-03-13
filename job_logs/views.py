from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """Home page for JobLog."""
    return render(request, 'job_logs/index.html')


def topics(request):
    """Show all the topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'job_logs/topics.html', context)
