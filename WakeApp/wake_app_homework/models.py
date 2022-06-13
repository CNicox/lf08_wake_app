from django.db import models

# Create your models here.
# admin admin

class Route(models.Model):
    destination = models.CharField(max_length=512)
    home_address = models.CharField(max_length=512)
    route_length = models.DateTimeField()
    morning_routine = models.DateTimeField()
    classes_start = models.DateTimeField()
    wake_up_time = models.DateTimeField()




