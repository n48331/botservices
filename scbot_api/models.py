from django.db import models
import uuid
from django.utils import timezone

class Communication(models.Model):
    project = models.ForeignKey('Project', related_name='communications', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=255, default='SCBOT')

    def __str__(self):
        return self.message + ": " + str(self.project)

class File(models.Model):
    project = models.ForeignKey('Project', related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    def __str__(self):
        return self.name + ": " + str(self.project)
class Project(models.Model):
    project_id = models.CharField(max_length=20, unique=True)
    asset_name = models.CharField(max_length=255)
    asset_category = models.CharField(max_length=50)
    campaign_type = models.CharField(max_length=50)
    project_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    csm = models.CharField(max_length=100)  # Customer Success Manager
    pmo = models.CharField(max_length=100)  # Project Management Officer
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.asset_name
