from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    numbers =[1,2,3,4,5]
    args = {'numbers': numbers}
    return render(request, 'WakeApp/home.html', args)