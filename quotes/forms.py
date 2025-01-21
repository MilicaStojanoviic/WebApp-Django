from django import forms
from django.forms import ModelForm  #ovo radi u sustini sav posao za forme, omogucava automatsko generisanje html formi na osnovu def modela
from .models import Quote  # uvozi klasu quote iz modela

class QuoteForm(ModelForm):  #ova klasa nasledjuje modelform
    required_css_class = 'required'  #ovo je vec postojeci css koji mogu da menjam
    class Meta: #interna klasa u modelform koja sadrzi inf o tome s kojim modelom forma treba da bude povezana
        model = Quote
        fields = ['name', 'position', 'company', 'address','phone', 'email', 'web', 'description','sitestatus', 'priority', 'jobfile']
        #da sam zelela da ukljucim sva polja iz modela koristila bih fields = '__all__'