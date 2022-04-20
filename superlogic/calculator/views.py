from django.shortcuts import render
from .functions import *


def index(request): #PÁGINA INICIAL
    return render(request, 'index.html')



def sets(request): #PÁGINA DE CONJUNTOS

    if request.GET:
       set1 = list(set(((list(request.GET.values()))[0]).split(sep=',')))
       set2 = list(set(((list(request.GET.values()))[1]).split(sep=',')))
       random_option = int((list(request.GET.values()))[2])
       option = int((list(request.GET.values()))[3])

       if random_option == 1:
           context = menu(set1,set2,option)
           return render(request, 'sets.html', context)


       elif random_option == 2:
            set1, set2 = auto_Generate()
            context = menu(set1,set2,option)
            return render(request, 'sets.html', context)


    else:
       return render(request, 'sets.html')





