from django.urls import path
from . import views  #importuj sve view-ove iz ovog paketa

urlpatterns= [
    #url(r'^$', views.index, name='index'), #r'^$' ovo predstavlja osnovnu pocetnu stranicu bez ikakvih dodataka, about...
    path('', views.index, name='index'),
]