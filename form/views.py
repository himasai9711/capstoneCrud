from django.shortcuts import render
from django.http import HttpResponse


def index(request):


    url = request.POST.get('url')
    print(url)
    return render(request, 'form/index.html')