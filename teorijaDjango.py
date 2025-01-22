#https://083950260099-attachments.s3.us-east-2.amazonaws.com/33211/bbb96849-df88-4cd4-849e-8daafcf58e04/MFDW1E2I-231118.pdf
#http://127.0.0.1:8000/


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


#uvek kad pokrenem projekat mora u cmdu cd django_projekat python manage.py runserver, ctrl+c da izadjem



#paket u pyhtonu je skup modula(moduli su svi fajlovi sa .py ekstenzijom), paket mora da sadrzi i init.py da bi se taj folder tako identifikovao
#poziv neke metode bi bio paket.modul.klasa.metoda
#npr forms.Form je poziv Form klase iz paketa forms

#svaki django projekat ima db.sqlite3, manage.py i u paketu: init.py, settings.py, urls.py, wsgi.py
#db se kreira sa migrate komandom, manage alat za komandnu liniju koja sluzi za izvrsivanje django komandi
#init kaze da je taj direktorijum python paket, wsgi je interfejs kojim omogucava komunikaciju izmedju web servera i aplikacije
#on se koristi uglavnom za produkciju, ali posto mi ne objavljujemo koristimo runserver i to je dovoljno
#settings su neka predefinisana podesavanja, npr za bazu, email...

#u djangou sve funkcionise preko aplikacija, a sam projekat je kolekcija aplikacija i konf podesavanja
#aplikacije ne samo da dodajes funkcionalnosti projektu, bez da ometas druge delove, vec su one i prenosne i mogu da se koriste u vise projekata
#znaci to su funkcionalnosti specificne za 1 oblast sistema(npr korisnicki profil, blog, proizvodi u e prodavnici)
#i tako se razliciti delovi projekta razdvajaju i odrzavaju nezavisno, tako da se mogu cak ti delovi lako preneti iz jednog projekta u drugi
#ako se pravi prodavnica projekat moze da ima sledece aplikacije proizvnodi, narudzbine, korisnici(svaka ap ima svoje modele, viewove, template)

#nova ap se kreira cd django_projekat  python manage.py startapp nazivapp
#bitno je da app bude u istom direktorijumu kao i manage.py da ne bih imala greske

#kada se app napravi mora da se instalira/registruje u settings.py tako sto je dodam u listu INSTALLED_APPS 'pages.apps.PagesConfig'

#modifikacija views.py
#modifikacija urls.py da bi se prikaziovao moj kod, ali da se ne bi to nalazilo na istom mestu, ugl se za svaku app pravi novi url fajl
#menjam i urls u django pr
#koristi path umesto url lakse je

#nakon toga se kreiraju pages modeli
#dodaje se kod u admin.py
#kreiramo migraciju da se model doda u bazu python manage.py makemigrations pages, python manage.py migrate

#posto django vec ima ugadjen interjes za admina, samo treba da se kreira admin user python manage.py createsuperuser (admin, admin@gmail.com, gnjilekruske)
#http://127.0.0.1:8000/admin/, tu se dodaju stranice i kod u admin.py

#u settings.py menjam deo kod templates, dirs je lista puteva do folders koji sadrze templates, app_dirs true, znaci da ce
#django traziti folder pod imenom dirs u svakoj aplikaciji, a posto nisu svi templ vezani za app, dirs je koristan da se povezu ostali templ
#posto smo u django_projektu naoravili templates, povezali smo ih u dirs
#os.path.join samo pomaze da se kreira cela putanja do template direktorijuma
#staticki fajlovi(slike, css i js) su u drugom direktorijumu u odnosu na app, tako django postize brzinu i skalabilnost
#ovaj direktorijum se def u settings.py i zove se STATIC_URL, a mi dodajemo staticfiles_dirs 
#ovo ima istu ulogu kao dirs za templates

#nakon toga apdejtujem views u pages
#{% block <name> %}{% endblock <name> %} u html-u omogucava da imam deo koji je promenljiv kad child nasledi ovaj template
#zatim u pages app pravim templates koje ce naslediti ovaj iz django_projekat, ali dodajem tu jos jedan folder pages
#jer ako imam da mi se 2 html-a zovu index, za razlicite app, onda ce django kad pretrazuje templ po app, uzeti orvu koju nadje, ovako zna koju treba
#sada umesto glavnog templatea mogu da pozovem ovaj specifican u views

#ponovo sam promanila urls, sada imam parametar koji je dinamicki deo urla, tako mogu da npr koristim meni i sad moram da menjam i view
#kada u page.html stavim plejsholder content to i prikazuje ono sto je u bazi

#sada popravljamo meni da funkcionise, u index u view dodajem i page_list, zatim u base dodajem {% block sidenav %} oko liste
# zatim to overridujem u page.html

#kad dodam ovo pg = get_object_or_404(Page, permalink=pagename) u view moram da menjam i settings DEBUG = False, ALLOWED_HOSTS = ['127.0.0.1']
#posto 404 ne izgleda bas najbolje, u templates pravim i 404.html
#ovo u settingsu menjam samo da vidim kako ce drugi videti ovu stranicu i pokrecem u cmdu preko python manage.py runserver --insecure
#ovo mogu da uradim i za 500 server error i ostale, ali kad zavrsim vracam debbug na true, tako vidim gresku djanga koja je detaljna

#kreiramo kontakt formu, ona je po sintaksi slicna modelu, ovde pokuplja podatke i salje ih na mejl
#moramo da dodamo url, zatim u base.html dodajemo formu u meni i na kraju dodajemo contact view i dodaj css

#cesca upotreba formi je za pokupljanje podataka i njihovo skladistenje u bazi, django ima posebnu klasu sa ovo model forms
#tako moze da se kreira model, a onda i forma koja nasledjuje ovo
#na ovom primeru se pravi potpuno nova app, jer je ovaj task za pokupljanje podataka dosta drugaciji od aplikacije koja prikazuje pod na stranici
#python manage.py startapp quotes, request for quotation su zahtevi za ponudu
#uploads folder ce sluziti da se cuvaju uploadovani fajlovi sa ponudama, i dodaj ponovo u installed apps
#pravimo model i migriramo, zatim dodajemo ovaj model adminu, tako da on moze da upravlja ponudama, menjam admin.py
#kreiramo forms.py, dodajemo view, pravimo template, i linkujemo sve to u urls u django_project(jer je nova app), a pravim u urls.py u appu
#i za kraj dodajem u base.html u meniju

#najprostije receno view je deo koda koji prima zahteve i vraca odgovore, svi viewovi koje smo mi do sada napravili bili su function based
#ali u Djangu postoje class based, prednosti ovoga je sto get i post mogu da se naprave kao metode klase umesto uslovnih grananja
#apstrakcija cestih paterna u genericke poglede, da bi view development bio laksi za ceste slucajeve i mi cemo se sada baviti ovim
#znaci ovi genericki pogledi vec postoje i oni nasledjuju view class(templateview i redirectview), tempview vraca template i context
#redirectview usmerava na dati url, cesto se koriste i detailview i listview
#mi cemo u quotes koristiti listview
#dodajem u views klasu, dodajem u urls, pravim template za ovo, i potrebno je da se zavrsava sa _list.html

#zatim se dodaju detalji itema iz liste, isto menjam sve ko i do sad views, urls, pravim html, dodajem css

#kreiranje usera, user grupe sluze tome da mogu da iste permissione da grupisem i samo dodelim 
#dodajemo zabranu da neko vidi quotes ako nije registrovan user
#u view stavljam da moraju da se loginuju pre nego sto vide i dodaju quote znaci odnosi se na quote_req, i quotelist
#za ovo postoji built in funkcionalnost , ali cemo koristiti drugaciji pristup jer je jedna function based view a bruga class based 
#za quote_req dodajemo decorator(to je spec fja koja modifikuje ponasanje druge fje i pocinje @ simbolom i mora da bude red iznad glavne fje)
#posle toga menjam da se prikaze samo lista quotesa loginovanog usera i koristim mixin
#mixin je specijalni tip klase, zatim dodajemo registration views
#user creationform koja vec postoji nema svoj view zato pravimo jedan
#dodajem sve u urls ali django_pr, isto tu pravim folder registration i dodajem potrebne html fajlove, menjam i base, da prikazuje pod o useru



#deploying 
#django kod moze da radi na svakom serveru koji podrzava wsgi(pythons web server gateway interface) i to preko wsgi.py
#PythonAnywhere ima free pocetnicki nalog i zahteva neki setup
#prvo se radi ciscenje, gde se brisu test baze tako da mogu da se rade nove migracije za mysql
#i dalje se ponavljaju procesi sa pocetka samo u konzoli pythonanywherea, isprati knjigu ako ti treba
