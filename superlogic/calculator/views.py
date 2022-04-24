from django.shortcuts import render
from .trueFunctions import *
from .setsFunctions import *


def index(request): #PÁGINA INICIAL
    return render(request, 'index.html')




def true(request): #CALCULADORA DE TABLAS DE VERDAD
    """
    Se alamacen con método GET en data la información
    ingresada en la calculadora para posteriormente darle
    formato excluyendo caracteres propios de QUERYS de Django
    """
    
    data = str(list(request.GET.values()))
    datas = data.replace("[", "")
    datas = datas.replace("]", "")
    datas = datas.replace("'", "")

    # El inicio de nuestro programa, aqui se toma la entrada inicial de los valores y la proposicion y se llaman a
    # todas las otras funciones

    if datas != "":
         num_Variables = 0
         operation = datas
         operation = operation.lower()
         if "p" in operation:
                num_Variables += 1
         if "q" in operation:
                num_Variables += 1
         if "r" in operation:
                num_Variables += 1

         if not validate_Expression(operation):
                print("No es valida")
         else:
                start_Values = (get_Tables(operation, num_Variables))
                original = get_Tables(operation, num_Variables)
                final = eval_Operation(operation, start_Values,num_Variables)
                dat = dict(list(original.items()) + list(final.items()))

                fin_lst = []
                space = "  "
                """
             El siguiente FOR integra los diccionarios en listas
             para su óptimo uso al momento de direccionarlos a
             index.html
             """
                for prop, lst in dat.items():
                    sec_lst = []
                    sec_lst.append(prop)  # Agrega proposicion a lista
                    sec_lst.append(space)  # Agrega espacio en la lista
                    for char in lst:
                        # Ciclo de adición de caracteres V o F
                        sec_lst.append(char)
                    # Adición de lista a la lista final a enviarse
                    fin_lst.append(sec_lst)

                context = {'lsts': fin_lst}  # Envía la lista a index.html
                return render(request, 'trueTables.html', context)

    else:
      return render(request, 'trueTables.html')




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





