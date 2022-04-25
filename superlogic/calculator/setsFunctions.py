from cgi import print_form
import random
from functools import reduce #Importación de funciones

def menu(set1,set2,option): #función que recibe y ejecuta cada función necesaria
    if option == 1: # INTERSECCIÓN DE CONJUNTOS
        operation = f"Intersección de {set(set1)}[{len(set1)}] & {set(set2)}[{len(set1)}]"

        oper_list = intersection(set1, set2)
        if oper_list:
            response = f"{set(intersection(set1, set2))}[{len(intersection(set1, set2))}]"
        else:
            response = "No hay intersección"

        context = {'operation':operation,'result':response} # El "context" se renderiza con el .html en cada caso
        return context 

    elif option == 2: # UNIÓN DE CONJUTNOS
        operation = f"Unión de {set(set1)}[{len(set1)}] & {set(set2)}[{len(set2)}]"
        response = f"{set(union(set1, set2))}[{len(union(set1, set2))}]"

        context = {'operation':operation,'result':response}
        return context

    elif option == 3: # DIFERENCIA A-B
        operation = f"Diferencia de {set(set1)}[{len(set1)}] & {set(set2)}[{len(set2)}]"
        response = f"{set(difference(set1, set2))}[{len(difference(set1, set2))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 4: #DIFERENCIA B-A 
        operation = f"Diferencia de {set(set2)}[{len(set2)}] & {set(set1)}[{len(set1)}]"
        response = f"{set(difference(set2, set1))}[{len(difference(set2, set1))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 5: #DIFERENCIA SIMÉTRICA
        operation = f"Diferencia simétrica de {set(set1)}[{len(set1)}] & {set(set2)}[{len(set2)}]"
        list_diff_a = difference(set1, set2)
        list_diff_b = difference(set2, set1)
        
        response = f"{set(union(list_diff_a, list_diff_b))}[{len(union(list_diff_a, list_diff_b))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 6: #COMPLEMENTO DE A 
        operation = f"Complemento de {set(set1)}[{len(set1)}]"
        response = f"{set(complement(set1))}[{len(complement(set1))-1}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 7: # COMPLEMENTO DE B 
        operation = f"Complemento de {set(set2)}[{len(set2)}]"
        response = f"{set(complement(set2))}[{len(complement(set2))-1}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 8: #PRODUCTO CARTESIANO AXB 
        operation = f"Producto cartesiano {set(set1)}[{len(set1)}] X {set(set2)}[{len(set2)}]"
        response = f"{set(cartesian(set1, set2))}[{len(cartesian(set1, set2))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 9: #PRODUCTO CARTESIANO BXA
        operation = f"Producto cartesiano {set(set2)}[{len(set2)}] X {set(set1)}[{len(set1)}]"
        response = f"{set(cartesian(set2, set1))}[{len(cartesian(set2, set1))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 10: #PRODUCTO CARTESIANO AXA
        operation = f"Producto cartesiano {set(set1)}[{len(set1)}] X {set(set1)}[{len(set1)}]"
        response = f"{set(cartesian(set1, set1))}[{len(cartesian(set1, set1))}]" 

        context = {'operation':operation,'result':response}
        return context

    elif option == 11: #PRODUCTO CARTESIANO BXB
        operation = f"Producto cartesiano {set(set2)}[{len(set2)}] X {set(set2)}[{len(set2)}]"
        response = f"{set(cartesian(set2, set2))}[{len(cartesian(set2, set2))}]"

        context = {'operation':operation,'result':response}
        return context

    elif option == 12: #CONJUNTO POTENCIA DE A 
        operation = f"Conjunto potencia de {set(set1)}[{len(set1)}]"

        result = power(set1)
        result[0] = "{∅}"
        response = f"{result}[{len(result)}]"

        context = {'operation':operation,'result':response}
        return context

    elif option == 13: #CONJUNTO POTENCIA DE B
        operation = f"Conjunto potencia de {set(set2)}[{len(set2)}]"

        result = power(set2)
        result[0] = "{∅}"
        response = f"{result}[{len(result)}]"

        context = {'operation':operation,'result':response}
        return context

    elif option == 14: #CONTENCIÓN DE A EN B
        operation = f"Contención de {set(set1)}[{len(set1)}] en {set(set2)}[{len(set2)}]"

        if contention(set1, set2):
            response = "A ⊆ B es verdadero"
        else:
            response = "A no esta contenido en B"

        context = {'operation':operation,'result':response}
        return context

    elif option == 15: #CONTENCIÓN DE B EN A
        operation = f"Contención de {set(set2)}[{len(set2)}] en {set(set1)}[{len(set1)}]"

        if contention(set2, set1):
            response = "B ⊆ A es verdadero"
        else:
            response = "B no está contenido en A"

        context = {'operation':operation,'result':response}
        return context


    else:
        context = {'set1':set1,'set2':set2,'option':option}
        return context



def auto_Generate(): 
    size_A = random.randint(1, 20) #Un máximo de 20 elementos
    size_B = random.randint(1, 20)
    conj_A = []
    conj_B = []
    for i in range(size_A):
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99)#Genera números del 1-99
            if rand not in conj_A:
                conj_A.append(str(rand))#Los ingresa en una lista
                rep = 1

    for i in range(size_B): #Mismo algoritmo del conj_A
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99) 
            if rand not in conj_B:
                conj_B.append(str(rand)) 
                rep = 1
    return conj_A, conj_B



def intersection(conj_A, conj_B):  #INTERSECCIÓN DE CONJUNTOS
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    list_inter = []
    if card_A > card_B: #Determina qué cardinalidad es mayor
        for i in range(card_A):
            if conj_A[i] in conj_B:
                list_inter.append(conj_A[i]) #Ingresa valores en intersección en la lista a regresarse

        if not list_inter:
            return False
        else:
            return list_inter

    if card_A < card_B: #Se repite el mismo algoritmo que "card_A > card_B"
        for i in range(card_B):
            if conj_B[i] in conj_A:
                list_inter.append(conj_B[i])

        if not list_inter:
            return False
        else:
            return list_inter

    elif card_A == card_B: #Si la cardinalidad es igual se compara con cualquier rango
        for i in range(card_A):
            if conj_A[i] in conj_B:
                list_inter.append(conj_A[i])

        if not list_inter:
            return False
        else:
            return list_inter


def union(conj_A, conj_B): #UNIÓN DE CONJUNTOS
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    list_union = conj_A

    for i in range(card_B):
        if conj_B[i] not in list_union:
            list_union.append(conj_B[i]) #Agrega los elementos del conjunto b a una copia del a

    return list_union


def difference(conj_A, conj_B): #DIFERIENCIA DE CONJUNTOS
    card = int(len(conj_A))
    conj_diff = []

    for i in range(card):
        if conj_A[i] not in conj_B:
            conj_diff.append(conj_A[i]) #Aquellos elementos que no se encunetren en el conjunto b se agregan a una lista

    return conj_diff


def complement(conj): #COMPLEMENTO DE CONJUNTOS
    card = int(len(conj))
    universe = []
    for element in range(100):
        universe.append(str(element+1))
    universe.append("")

    comp = universe.copy()

    for i in range(card):
        comp.remove(conj[i]) #Se crea una copia del universo como lista final y se remueven los elementos del conjunto ingresado.

    return comp


def cartesian(conj_A, conj_B): #PRODUCTO CARTEASIANO DE CONJUNTOS
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    conj_carte = []

    for i in range(card_A):
        for j in range(card_B):
            elem_temp = "(", str(conj_A[i]), ", ", str(conj_B[j]), ")"
            elem = ''.join(elem_temp)
            conj_carte.append(elem) #Se genera cada tupla mediante dos ciclos for

    return conj_carte


def contention(conj_A, conj_B): #DETERMINAR CONTENCIÓN DE UN CONJUNTO EN OTRO
    card = int(len(conj_A))
    gatito = 0

    for i in range(card):
        if conj_A[i] not in conj_B: #Si existe algún elemento que no se encuentra en el otro conjunto termina.
            gatito = 1
            break

    if gatito == 0:
        return True
    else:
        return False


def power(conj): #DETERMINA EL CONJUNTO POTENCIA DE UN CONJUNTO
    power_list = reduce(lambda P, x: P + [subset | {x} for subset in P], conj, [set()])

    return power_list