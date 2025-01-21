from django.urls import path
from . import views 

urlpatterns= [
    #url(r'^$', views.quote_req, name='quote-request'),
    path('quote', views.quote_req, name='quote_req'),
]