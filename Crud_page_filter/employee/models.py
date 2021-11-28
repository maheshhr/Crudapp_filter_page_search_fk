from django.db import models

from department.models import Department


class Employee(models.Model):
    eid = models.CharField(max_length=25)
    ename = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.dept_name
