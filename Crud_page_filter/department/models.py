from django.db import models


class Department(models.Model):
    dept_id = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.dept_name
