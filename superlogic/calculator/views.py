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

          if option == 1:
              oper_list = intersection(set1, set2)
              if oper_list:
                   response = intersection(set1, set2)
              else:
                   response = "No hay interseccion!"

              context = {'set1':set1,'set2':set2,'option':option,'result':response}
              return render(request, 'sets.html', context)

          elif option == 2:
              oper_list = union(set1, set2)
              response = union(set1, set2)

    
              context = {'set1':set1,'set2':set2,'option':option,'result':response}
              return render(request, 'sets.html', context)

         

          else:
              context = {'set1':set1,'set2':set2,'option':option}
              return render(request, 'sets.html', context)

       elif random_option == 2:
            set1, set2 = auto_Generate()

            if option == 1:
                oper_list = intersection(set1, set2)
                if oper_list:
                     response = intersection(set1, set2)
                else:
                     response = "No hay interseccion!"

                context = {'set1':set1,'set2':set2,'option':option,'result':response}
                return render(request, 'sets.html', context)

            elif option == 2:
                oper_list = union(set1, set2)
                response = union(set1, set2)

    
                context = {'set1':set1,'set2':set2,'option':option,'result':response}
                return render(request, 'sets.html', context)

         

            else:
                context = {'set1':set1,'set2':set2,'option':option}
                return render(request, 'sets.html', context)





    else:
       return render(request, 'sets.html')





