from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tasks.models import CreateTask


@login_required(login_url='/login/')
def summary_report_view(request):
    total_tasks = CreateTask.objects.count()
    completed_tasks = CreateTask.objects.filter(status='Completed').count()
    in_progress_tasks = CreateTask.objects.filter(status='In Progress').count()
    open_tasks = CreateTask.objects.filter(status='Open').count()

    summary = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'open_tasks': open_tasks,
        'percentage_completed': round((completed_tasks / total_tasks) * 100,3) if total_tasks else 0
    }


    return render(request, 'tasks/summary_report.html', {'summary': summary})

    logger.error(str(exe), exc_info=True)