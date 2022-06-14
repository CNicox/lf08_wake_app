from django.forms import ModelForm, DateTimeField, SelectDateWidget, SplitDateTimeWidget, SplitDateTimeField, TimeField, \
    TimeInput


from .models import *

class RouteForm(ModelForm):
    route_length = TimeField(required=True, widget=TimeInput(attrs={'type': 'time'}))
    morning_routine = TimeField(required=True, widget=TimeInput(attrs={'type': 'time'}))
    classes_start = TimeField(required=True, widget=TimeInput(attrs={'type': 'time'}))
    #'time': forms.TimeInput(attrs={'type': 'time'})
    class Meta:
         model = Route
         fields = ['destination', 'home_address', 'route_length',
                   'morning_routine', 'classes_start']