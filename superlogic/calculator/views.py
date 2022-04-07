from django.shortcuts import render
from django.http import HttpResponse


def index(request): #PÁGINA INICIAL
    return render(request, 'index.html')



def sets(request): #PÁGINA DE CONJUNTOS

    if request.GET:
       set1 = (list(request.GET.values()))[0]
       set2 = (list(request.GET.values()))[1]
       option = (list(request.GET.values()))[2]
       context = {'set1':set1,'set2':set2,'option':option}

       return render(request, 'sets.html', context)

    else:
       return render(request, 'sets.html')





