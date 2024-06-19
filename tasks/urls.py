from django.urls import path 
from . import views

urlpatterns =[
    path('home/', views.home, name='home'),
    path('create-task/',views.createtask, name='create-task'),
    path('task-list/', views.taskList, name='task-list'),
    path('task/update/<pk>', views.update_task, name='task-update'),
    path('task/delete/<pk>', views.delete_task, name='task-delete'),
    path('report', views.report, name='report'),
    path('report/complete', views.detail_report_completed, name='report-completed'),
    path('report/open', views.detail_report_Open, name='report-open'),
    path('report/progress', views.detail_report_inprogress, name='report-progress'),
    path('report/summary', views.summary_report_view, name='report-summary'),
]