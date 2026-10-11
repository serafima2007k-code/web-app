from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def test(request):
    return HttpResponse("Тестовая страница")

# Create your views here.

