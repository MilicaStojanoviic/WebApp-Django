from django.shortcuts import render, get_object_or_404 #koristi se kad se renderuju template-i
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page
from .forms import ContactForm


#fja koja uzima zahtev od veb pretrazivaca i vraca odgovor
#ovo je view funkcija, ali je nazvana indeks jer vraca glavnu stranicu, koja se uvek zove index.html
#def index(request):
#    return render(request, "pages/page.html")
#    return HttpResponse("<h1>Moj vebsajt</h1>") 

#sada se pravi nova fja 
def index(request, pagename):
    pagename= '/'+pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context={
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    #assert False  #za testiranje pogleda
    return render(request, 'pages/page.html', context)


def contact(request):
    submitted = False  #tako se u sustini kada udjem na stranicu orvo prikazuje forma a ne poruka
    if request.method == 'POST':  #ako je metod post to znaci da je korisnik poslao formu
        form = ContactForm(request.POST)  #kreira se instanca contactForm sa pod koje je korisnik uneo
        if form.is_valid(): #proverava da li su polja validna
            cd = form.cleaned_data  
            con = get_connection('django.core.mail.backends.console.EmailBackend')  #email se za razvojne svrhe salje u konzolu umesto pravog slanja
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
                )
            return HttpResponseRedirect('/contact?submitted=True')  #preusmerava se korisnik na poruku
    else:
        form = ContactForm()  #ovo je kad se prvi put dodje na stranicu defolt, kreira se prazna forma, jer korisnik nije poslao formu
        if 'submitted' in request.GET:   #proverava da li je forma vec poslata, ako je u urlu subn=mitted prisutan prikazuje se poruka
            submitted = True
    #sledeca linija renderuje html sablon, ona prosledjuje formu, listu instanca i submitted i kontrolise sta ce biti prikazano
    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})