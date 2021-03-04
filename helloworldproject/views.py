from django.http import HttpResponse

def hel(request):
    return HttpResponse('<h1>hello world</h1>')