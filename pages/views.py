from django.shortcuts import render #koristi se kad se renderuju template-i
from django.http import HttpResponse


#fja koja uzima zahtev od veb pretrazivaca i vraca odgovor
#ovo je view funkcija, ali je nazvana indeks jer vraca glavnu stranicu, koja se uvek zove index.html
def index(request):
    return HttpResponse("<h1>Moj vebsajt</h1>") 
