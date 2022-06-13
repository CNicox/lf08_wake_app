from django.forms import ModelForm
from .models import *

class RouteForm(ModelForm):
     class Meta:
         model = Route
         fields = ['destination', 'home_address', 'route_length', 'morning_routine', 'classes_start', 'wake_up_time']