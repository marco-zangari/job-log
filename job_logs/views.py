from django.shortcuts import render

# Create your views here.


def index(request):
    """Home page for JobLog."""
    return render(request, 'job_logs/index.html')
