import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from tasks.models import CreateTask

# Create your views here.
logger = logging.getLogger("django")

@login_required(login_url='/login/')
def home(request):
    try:
        all_task = CreateTask.objects.filter(is_delete = False)
        tasks = CreateTask.objects.filter(is_delete= False)
        five_task = tasks[:5]
        current_user = request.user
        # user = User.objects.get()

        total_tasks = all_task.count()
        task_complete = all_task.filter(status = "Completed").count()
        task_open = all_task.filter(status = "Open").count()
        task_progress = all_task.filter(status = "In Progress").count()

        contex ={  'total_tasks':total_tasks, "task_open": task_open,  "task_progress":task_progress,
                 'task_complete': task_complete, 'tasks':five_task, 'current_user': current_user}
        return render(request, 'tasks/home.html', contex)
    
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/home.html')