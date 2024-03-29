from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
import datetime
from .models import *
from .forms import *
# Create your views here.





class IndexView(ListView):
    template_name = 'WakeApp/home.html'
    model = Route
    context_object_name = 'routes'
    extra_context = {
        'route_form': RouteForm(),
    }

def add_route(request):
    f = RouteForm(request.POST)
    if f.is_valid():
        print(type(f.cleaned_data['classes_start']))

        route_time = datetime.timedelta(hours=f.cleaned_data['route_length'].hour, minutes=f.cleaned_data['route_length'].minute)
        morning_routine_time = datetime.timedelta(hours=f.cleaned_data['morning_routine'].hour, minutes=f.cleaned_data['morning_routine'].minute)
        route_time_total = route_time + morning_routine_time
        time_to_wake_up = datetime.timedelta(hours=f.cleaned_data['classes_start'].hour, minutes=f.cleaned_data['classes_start'].minute) - route_time_total
        if route_time_total > time_to_wake_up:
            #show error here
            return HttpResponseRedirect(reverse('wake_app_homework:index'))
        print(type(time_to_wake_up))
        new_route = Route(
            destination = f.cleaned_data['destination'],
            home_address = f.cleaned_data['home_address'],
            route_length=f.cleaned_data['route_length'],
            morning_routine=f.cleaned_data['morning_routine'],
            classes_start=f.cleaned_data['classes_start'],
            wake_up_time=datetime.datetime.strptime(str(time_to_wake_up), "%H:%M:%S"),
        )
        #print(new_route)
    else:
        print(f.errors)
    new_route.save()
    #return render(request, "WakeApp/home.html")
    return HttpResponseRedirect(reverse('wake_app_homework:index'))