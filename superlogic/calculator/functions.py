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