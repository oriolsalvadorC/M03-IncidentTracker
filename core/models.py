from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SecurityIncident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=20)
    detected_at = models.DateTimeField()
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
