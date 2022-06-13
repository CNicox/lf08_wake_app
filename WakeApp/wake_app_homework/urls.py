from django.conf.urls import url
from django.urls import path

from . import views
app_name = "wake_app_homework"

urlpatterns = [
    #path('index/', views.IndexView.as_view(), name="index"),
    #path('index/', views.home, name='home'),
    path('index/', views.IndexView.as_view(), name="index"),
    path('route/add/', views.add_route, name="add-route"),

]