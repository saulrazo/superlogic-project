import random
from functools import reduce

def menu(set1,set2,option):
    if option == 1: # INTERSECCIÓN DE CONJUNTOS
        oper_list = intersection(set1, set2)
        if oper_list:
            response = intersection(set1, set2)
        else:
            response = "No hay interseccion!"

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context 

    elif option == 2: # UNIÓN DE CONJUTNOS
        response = union(set1, set2)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 3: # DIFERIENCIA A-B
        response = difference(set1, set2)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 4: #DIFERIENCIA B-A
        response = difference(set2, set1)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 5: #DIFERIENCIA SIMÉTRICA
        list_diff_a = difference(set1, set2)
        list_diff_b = difference(set2, set1)
        
        response = union(list_diff_a, list_diff_b)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 6: #COMPLEMENTO DE A ///
        response = complement(set1)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 7: # COMPLEMENTO DE B ///
        oper_list = union(set1, set2)
        response = union(set1, set2)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    elif option == 8: #PRODUCTO CARTESIANO AXB
        response = cartesian(set1, set2)

        context = {'set1':set1,'set2':set2,'option':option,'result':response}
        return context

    else:
        context = {'set1':set1,'set2':set2,'option':option}
        return context



def auto_Generate():
    size_A = random.randint(1, 20)
    size_B = random.randint(1, 20)
    conj_A = []
    conj_B = []
    for i in range(size_A):
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99)
            if rand not in conj_A:
                conj_A.append(rand)
                rep = 1

    for i in range(size_B):
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99)
            if rand not in conj_B:
                conj_B.append(rand)
                rep = 1
    return conj_A, conj_B



def intersection(conj_A, conj_B):
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    list_inter = []
    if card_A > card_B:
        for i in range(card_A):
            if conj_A[i] in conj_B:
                list_inter.append(conj_A[i])

        if not list_inter:
            return False
        else:
            return list_inter

    if card_A < card_B:
        for i in range(card_B):
            if conj_B[i] in conj_A:
                list_inter.append(conj_B[i])

        if not list_inter:
            return False
        else:
            return list_inter

    elif card_A == card_B:
        for i in range(card_A):
            if conj_A[i] in conj_B:
                list_inter.append(conj_A[i])

        if not list_inter:
            return False
        else:
            return list_inter


def union(conj_A, conj_B):
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    list_union = conj_A

    for i in range(card_B):
        if conj_B[i] not in list_union:
            list_union.append(conj_B[i])

    return list_union


def difference(conj_A, conj_B):
    card = int(len(conj_A))
    conj_diff = []

    for i in range(card):
        if conj_A[i] not in conj_B:
            conj_diff.append(conj_A[i])

    return conj_diff


def complement(conj):
    card = int(len(conj))
    universe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    comp = universe.copy()

    for i in range(card):
        comp.remove(conj[i])

    return comp


def cartesian(conj_A, conj_B):
    card_A = int(len(conj_A))
    card_B = int(len(conj_B))
    conj_carte = []

    for i in range(card_A):
        for j in range(card_B):
            elem_temp = "(", str(conj_A[i]), ", ", str(conj_B[j]), ")"
            elem = ''.join(elem_temp)
            conj_carte.append(elem)

    return conj_carte


def contention(conj_A, conj_B):
    card = int(len(conj_A))
    gatito = 0

    for i in range(card):
        if conj_A[i] not in conj_B:
            gatito = 1
            break

    if gatito == 0:
        return True
    else:
        return False


def power(conj):
    power_list = reduce(lambda P, x: P + [subset | {x} for subset in P], conj, [set()])

    return power_list