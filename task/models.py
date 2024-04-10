from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class list(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    taskname = models.CharField(max_length=50)
    due = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.taskname
    
