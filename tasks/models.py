from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, db_column="created_by", related_name="+", null=True)
    created_at = models.DateTimeField(auto_now=True, null=True, )
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, db_column="updated_by", null=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True


class CreateTask(Base):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=50)
    createdBy = models.CharField(max_length=50)
    assignedTo = models.CharField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()

    class Meta:
        db_table = 'createtask'
