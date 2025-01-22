from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Quote
from . forms import QuoteForm
from pages.models import Page

class QuoteList(LoginRequiredMixin, ListView):  #class generic view
    login_url = reverse_lazy('login')
    #model = Quote bez ovoga kad dodajem mixin
    context_object_name = 'all_quotes'  #moze da radi i bez ovoga ali je bolje da se da ime

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs): #sluzi da mi se normalno prikazuje meni
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context
    
class QuoteView(DetailView):
    model = Quote
    context_object_name = 'quote'
    
    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context
    
class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

#slicno kao za kontakt formu samo umesto slanja mejla imamo save, sto cuva pod u bazi
@login_required(login_url=reverse_lazy('login'))  #sada menjam i samu fju 
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)  #files je dodat da uploadovane fajlove mozemo da sacuvamo
        if form.is_valid():
            quote = form.save(commit=False)
            try:
                 quote.username = request.user
            except Exception:
                 pass
            quote.save()
            #form.save()
            return HttpResponseRedirect(reverse('quote_req') + '?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'quotes/quote.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})