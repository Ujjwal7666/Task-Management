
import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from tasks.models import CreateTask
logger = logging.getLogger("django")
@login_required(login_url='/login/')
def report(request):
    try:
        return render(request, 'tasks/report.html')
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/report.html')

@login_required(login_url='/login/')
def detail_report_completed(request):
    try:
        complete = CreateTask.objects.filter(status='Completed')
        return render(request, 'tasks/report_complete.html',{'complete': complete})
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/report_complete.html')
    
@login_required(login_url='/login/')
def detail_report_Open(request):
    try:
        open = CreateTask.objects.filter(status='Open')
        return render(request, 'tasks/report_open.html',{'open': open})
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/report_complete.html')


@login_required(login_url='/login/')
def detail_report_inprogress(request):
    try:
        progress = CreateTask.objects.filter(status='In Progress')
        return render(request, 'tasks/report_progress.html',{'progress': progress})

    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/report_progress.html')
