from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  #the path for our index view
    
    # Delete search history
    path('deleteCity/', views.deleteCity, name='deleteCity'),
]