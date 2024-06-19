import logging

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages

from tasks.models import CreateTask

logger = logging.getLogger("django")
@login_required(login_url='/login/')
def update_task(request, pk):
    try:
        task = CreateTask.objects.get(id=pk)
        current_user = request.user
        all_user = User.objects.exclude(username = current_user.username)
        if request.method == "POST":
            data = request.POST
            title = data.get('title')
            priority =data.get('priority')
            description = data.get('description')
            status = data.get('status')
            createdBy = data.get('createdBy')
            assignedTo = data.get('assignedTo')
            startdate = data.get('startdate')
            enddate =data.get('enddate')

            CreateTask.objects.filter(id=pk).update(title=title, priority=priority, description= description, status=status, 
                                                    createdBy=createdBy, assignedTo=assignedTo, startdate=startdate, enddate=enddate, updated_at=datetime.now())   
            messages.success(request, "Task updated Sucessfully")
            return redirect('/task-list/')
        return render(request, 'tasks/update_task.html', {'current_user': current_user, 'all_user': all_user, 'tasks':task })
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/update_task.html',)

@login_required(login_url='/login/')
def delete_task(request, pk):
    try:
        task = CreateTask.objects.get(id=pk)
        if request.method == "POST":
           task.is_delete= True
           task.save()
           messages.warning(request, "Task deleted !!" )
           return redirect('/task-list/')

        return render(request, 'tasks/update_task.html')
    except Exception as exe:
        logger.error(str(exe), exc_info=True)
        return render(request, 'tasks/update_task.html')