import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tasks.models import CreateTask

from tasks.models import CreateTask

logger = logging.getLogger("django")
@login_required(login_url='/login/')
def taskList(request):
    try:
        tasks = CreateTask.objects.filter(is_delete= False)
        return render(request, 'tasks/tasks_list.html', {'tasks':tasks})
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/tasks_list.html')