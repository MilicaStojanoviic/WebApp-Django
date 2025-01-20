from django.db import models

#polja ovde ce imati odgovarajuce kolone u bazi
class Page(models.Model):
   title = models.CharField(max_length=60)  #<title> elementi u templateu
   permalink = models.CharField(max_length=12, unique=True)  #permanent link ka odredjenoj stranici, unique je jer se tako kreira link ka stranici
   update_date = models.DateTimeField('Last Updated')  #kad je strana bila modifikovana
   bodytext = models.TextField('Page Content', blank=True)  #<body> elemeni u tepmplateu

def __str__(self):
   return self.title