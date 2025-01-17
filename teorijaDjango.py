#Django implementira MVC dizajn patern, uopsteno model pruza interfejs prema bazi podataka koja sadrzi pod o aplikaciji
#view prikuplja inf od korisnika i odlucuje koje info ce se prikazivati korisniku, a kontroler upravlja poslovnim logikom 
#i sluzi kao posrednik za razmenu info izmedju ova dva
#django malo drugacije implementira ovo: model ima istu funkciju, orm(object-relational mapping) obezbedjuje interfejs prema bazi
#template pruza logiku prikaza pod korisniku, a view upravlja poslovnom logikom, razmenom poruka 
#template salje viewu korisnicki input, a view templateu podatke za prikaz, view salje modelu create, update, delete naredbe, a 
#model viewu dataset-ove

#ORM omogucava da se pod iz relacione baze koriste kao objekti u programskom jeziku, bez potrebe za pisanjem sql koda
#znaci on mapira klase iz koda na tabele u bazi(instanca klase je red u tabeli, a atributi su kolone), kreiranje, citanje i pisanje u bazi 
#se vrsi preko metoda
#Hibernate je popularan ORM ZA Javu

#from django.db import models

#class Book(models.Model):                   #CREATE TABLE
#    title = models.CharField(max_length=200)
#    author = models.CharField(max_length=100)
#    published_date = models.DateField()

#    def __str__(self):
#        return self.title

#book = Book(title="1984", author="George Orwell", published_date="1949-06-08")
#book.save()       # Ovo generiše i izvršava SQL INSERT upit

#books = Book.objects.all()     # SELECT * FROM Book
#for book in books:
#    print(book.title)

#book = Book.objects.get(id=1)      # SELECT * FROM Book WHERE id=1
#book.title = "Animal Farm"
#book.save()       # Generiše SQL UPDATE

#book = Book.objects.get(id=1)
#book.delete()       # Generiše SQL DELETE

#Django automatski instalira i konfigurise SQLite bazu, a podrzava i MySQL, Oracle i PostgradeSQL




#posto su dizajn i programiranje razlicite kategirije template prikazuje podatke poslovne logike preko obicnih tagova
#<h1>Informacije o vašoj porudžbini</h1>
#<p>Dragi/Draga {{ person_name }},</p>
#ovo sto je u okviru taga view salje template-u, ovako dizajner ne mora nista da zna o backendu
#a s druge strane programer sam moze da napravi front tako sto preuzme html sablon sa neta i doda django tagove, Bootstrap

#DRY(Don't repeat yourself) je Djangov glavni princip npr u templateu se primenjuje tako sto cu napraviti parent i child template .html
#parent ce imati one delove koji se cesto ponavljaju npr top navigation, header i footer, a glavni deo i kontent stranica se nalazi u childu

#da bi se obezbedila sigurnost podataka u templateu mogu da imam samo logiku za prikazivanje tj da prikazem neke varijable njihovim pozivom,
#da prodjem kroz neke liste podataka da mogu da ih ubacim u html liste i da koristim neke filtere za formatiranje podataka
#ne mogu da u templ izvrsavam python kod, da dodelim vrednosti varijablama i izvrsavam naprednu logiku

#api je skup pravila, protokola i alata koji se koriste za komunikaviju izmedju softv apl(to je interfejs preko koga se salju zahtevi i odg)
#rest api-najcesce za web str koristi http protokol i vraca pod u json ili xml formatu, soap api- koristi xml format i obezbedjuje visoku sigurnost
#rest je skup pravila i principa(softverska arhitektura), restful je web servis koji su implementirali tu arhitekturu

#broker u it-ju znaci posrednik koji omogucava komunikaciju i razmenu pod, view je u djangu zapravo broker, on skladisti pod iz baze i
#prosledjuje templateu, za web app view prosledjuje template(html), a za restful api ovaj kontent su json fajlovi
#svaka stranica koja koristi http, to je transport pod preko metoda get, post..., restful api je poseban nacin za izlaganje podataka
#klasicne web stranice salju html a restful api vraca json

#view je predstavljen preko funkcije ili klase, postoje built-in view-i u django-u, za funkcije bi bile 404(page not found), 
#500(server error).. a za klase view koji prikazuje listu objekate(npr listu artikala), form view...

#kada user klikne na link na sajtu, zahtev za url-om se salje djangu(lokalno je to zahtev za htmlom), kad on primi taj zahtev, odlucuje
#koji view ce se baviti tim zahtevom to se radi u urls.py fajlu kad u tom fajlu nadje taj url on poziva view koji je povezan sa njim,
#taj view renderuje kontent template-a i poslovnu logiku i vraca sve to brauzeru da prikaze

#instalacija pythona sa stikliranjem path-a, instaliraj django, migriraj bazu, pokreni server
#postoji opcija da se napravi viruelno okruzenje, da ova instalacija ne utice na druge projekte
#python -m pip install -U pip 
#pip install django
#idi u python na cmdu i kucni import django, ctrl++z+enter da izadjem
#django-admin startproject django_projekat
#cd django_projekat
#python manage.py migrate -kreiranje baze
#python manage.py runserver 


#uvek kad pokrenem projekat mora u cmdu cd django_projekat python manage.py runserver

