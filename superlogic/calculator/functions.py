import random

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