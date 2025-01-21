from django.urls import path
from . import views  #importuj sve view-ove iz ovog paketa

urlpatterns= [
    path('contact', views.contact, name='contact'),  #mora da se doda na pocetku
    #url(r'^$', views.index, name='index'), #r'^$' ovo predstavlja osnovnu pocetnu stranicu bez ikakvih dodataka, about...
    path('', views.index, {'pagename': ''}, name='index'),
    path('<str:pagename>', views.index, name='index'),
    #url(r'([^/]*)', views.index, name='index')
]