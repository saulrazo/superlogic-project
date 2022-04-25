import random
from functools import reduce #Importación de funciones

def get_Conjuntos(card): #Recibir elementos de conjuntos en una lista
    conj = []
    num = 0
    for i in range(card):
        follow = i + 1
        rep = 0
        while rep == 0:
            print("Valor numero ", follow)
            num = int(input("> "))
            if num > 99 or num < 0: #Autentificar que el número se encuentre entre 1 hasta el 99
                print("Error con el rango de numeros, favor de revisar")

                return False

            else:
                if num not in conj:
                    conj.append(num)
                    rep = 1

    return conj


def auto_Generate():
    size_A = random.randint(1, 20) #Un máximo de 20 elementos
    size_B = random.randint(1, 20)
    conj_A = []
    conj_B = []
    for i in range(size_A):
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99) #Genera números del 1-99
            if rand not in conj_A:
                conj_A.append(rand) #Los ingresa en una lista
                rep = 1

    for i in range(size_B): #Mismo algoritmo del conj_A
        rep = 0
        while rep == 0:
            rand = random.randint(1, 99)
            if rand not in conj_B:
                conj_B.append(rand)
                rep = 1
    return conj_A, conj_B


def print_Menu(): #Menú de todas las operaciones disponibles con conjuntos
    print("1. Interseccion A∩B              | 2. Union A∪B")
    print("")
    print("3. Diferencia A-B                | 4. Diferencia B-A")
    print("")
    print("5. Diferencia Simetrica          | 6. Complemento de A")
    print("")
    print("7. Complemento de B              | 8. Producto Cartesiano de AxB")
    print("")
    print("9. Producto Cartesiano de BxA    | 10. Producto Cartesiano de AxA")
    print("")
    print("11. Producto Cartesiano de BxB   | 12. Conjunto potencia de A")
    print("")
    print("13. Conjunto potencia de B       | 14. Contencion de A ⊆ B")
    print("")
    print("15. Contencion de B ⊆ A          | 16. Salir")


def intersection(conj_A, conj_B): #INTERSECCIÓN DE CONJUNTOS
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
    card_B = int(len(conj_B))
    list_union = conj_A.copy()

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
    universe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
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


if __name__ == '__main__':
    validacion = 0
    print("Bienvenido al programa de Conjuntos")
    op = input("Desea introducir sus conjuntos (0) o que sean generados (1)? > ")
    if op == "1": #FUNCIÓIN RANDOM
        conj_A, conj_B = auto_Generate()
        print("Conjunto A = ", conj_A)
        print("Conjunto B = ", conj_B, "\n")
        validacion = 1

    elif op == "0": #AUTENTIFICACIÓN DE ENTRADA
        card_A = int(input("Cardinalidad del Conjunto A > "))
        card_B = int(input("Cardinalidad del Conjunto B > "))
        print("\n\nC O N J U N T O _ _ _ A \n\n")
        conj_A = get_Conjuntos(card_A)
        print("\n\nC O N J U N T O _ _ _ B\n\n")
        conj_B = get_Conjuntos(card_B)
        if not conj_A or not conj_B:
            print("\n Favor de revisar el rango de datos introducido!")
        else:
            print("Conjunto A = ", conj_A)
            print("Conjunto B = ", conj_B, "\n")
            validacion = 1

    else:
        print("Error al introducir los datos")

    if validacion == 1: #SE PRESENTAN TODAS LAS POSIBLES OPCIONES
        while op != 16:
            print_Menu()
            op = int(input("> "))

            if op == 1:
                list_inter = intersection(conj_A, conj_B)
                if list_inter:
                    print("A∩B = ", list_inter, "\n")
                else:
                    print("No hay interseccion! \n")

            elif op == 2:
                list_union = union(conj_A, conj_B)
                print("A∪B = ", list_union, "\n")

            elif op == 3:
                list_diff = difference(conj_A, conj_B)
                print("A-B = ", list_diff, "\n")

            elif op == 4:
                list_diff = difference(conj_B, conj_A)
                print("B-A = ", list_diff, "\n")

            elif op == 5:
                list_diff_a = difference(conj_A, conj_B)
                list_diff_b = difference(conj_B, conj_A)
                list_sim_diff = union(list_diff_a, list_diff_b)
                print("BΔA = ", list_sim_diff, "\n")

            elif op == 6:
                list_comp = complement(conj_A)
                print("Complemento de A = ", list_comp, "\n")

            elif op == 7:
                list_comp = complement(conj_B)
                print("Complemento de B = ", list_comp, "\n")

            elif op == 8:
                list_cartes = cartesian(conj_A, conj_B)
                print("Producto cartesiano AxB: ", list_cartes)

            elif op == 9:
                list_cartes = cartesian(conj_B, conj_A)
                print("Producto cartesiano BxA: ", list_cartes)

            elif op == 10:
                list_cartes = cartesian(conj_A, conj_A)
                print("Producto cartesiano AxA: ", list_cartes)

            elif op == 11:
                list_cartes = cartesian(conj_B, conj_B)
                print("Producto cartesiano BxB: ", list_cartes)

            elif op == 12:
                list_power = power(conj_A)
                list_power[0] = "{∅}"
                print("Conjunto potencia de A: ", list_power)

            elif op == 13:
                list_power = power(conj_B)
                list_power[0] = "{∅}"
                print("Conjunto potencia de B: ", list_power)

            elif op == 14:
                if contention(conj_A, conj_B):
                    print("A ⊆ B es verdadero!!")
                else:
                    print("A no esta contenido en B!")

            elif op == 15:
                if contention(conj_B, conj_A):
                    print("B ⊆ A es verdadero!!")
                else:
                    print("B no esta contenido en A!")

    print("\nGracias por usar nuestro programa, saludos! <3")
