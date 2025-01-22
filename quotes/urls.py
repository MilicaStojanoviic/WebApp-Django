from django.urls import path
from . import views 
from .views import QuoteList, QuoteView

urlpatterns= [
    #url(r'^$', views.quote_req, name='quote-request'),
    path('', views.quote_req, name='quote_req'),
    path('show/<int:pk>', QuoteView.as_view(), name='quote-detail'),
    path('show', QuoteList.as_view(), name='show-quotes'),
]