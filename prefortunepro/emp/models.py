from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_id=models.CharField(max_length=20)
    emp_salary=models.CharField(max_length=20)
    dept_fid=models.CharField(max_length=20)



    
    


