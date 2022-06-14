from django.db import models

# Create your models here.
# admin admin

class Route(models.Model):
    destination = models.CharField(max_length=512)
    home_address = models.CharField(max_length=512)
    route_length = models.TimeField()
    morning_routine = models.TimeField()
    classes_start = models.TimeField()
    wake_up_time = models.TimeField()

    class Meta:
        unique_together = ('destination', 'home_address',)

    def __str__(self):
        return f'{self.destination} to {self.home_address}'




