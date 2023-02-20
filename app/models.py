from django.db import models

# Create your models here.

class Webpage(models.Model):
    topic_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.topic_name