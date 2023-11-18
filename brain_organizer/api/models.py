from django.db import models

class Project(models.Model):
    input = models.TextField()
    mind_map = models.FileField()
    