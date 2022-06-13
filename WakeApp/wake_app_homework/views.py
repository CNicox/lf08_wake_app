from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import *
# Create your views here.


#def home(request):
#    numbers =[1,2,3,4,5]
#    args = {'numbers': numbers}
#    return render(request, 'WakeApp/home.html', args)


class IndexView(ListView):
    template_name = 'WakeApp/home.html'
    model = Route
    context_object_name = 'posts'
    extra_context = {
        'route_form': RouteForm(),
    }

#['destination', 'home_address', 'route_length', 'morning_routine', 'classes_start', 'wake_up_time']
def add_route(request):
    f = RouteForm(request.POST)
    if f.is_valid():
        new_route= Route(
            destination = f.cleaned_data['destination'],
            home_address = f.cleaned_data['home_address'],
            route_length=f.cleaned_data['route_length'],
            morning_routine=f.cleaned_data['morning_routine'],
            classes_start=f.cleaned_data['classes_start'],
            wake_up_time=f.cleaned_data['wake_up_time'],
        )
    new_route.save()
    return render(request, "WakeApp/home.html")
    #return HttpResponseRedirect(reverse('imdb:movie-detail', kwargs={'pk':pk}))