#ja pravila nzm jel radi
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")