from django.shortcuts import HttpResponse, render


def index(request):
    #return HttpResponse("lol")
    return render(request, 'index.html')
