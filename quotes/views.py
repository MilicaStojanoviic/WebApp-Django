from django.shortcuts import render
from django.http import HttpResponseRedirect

from . forms import QuoteForm
from pages.models import Page

#slicno kao za kontakt formu samo umesto slanja mejla imamo save, sto cuva pod u bazi
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)  #files je dodat da uploadovane fajlove mozemo da sacuvamo
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'quotes/quote.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})