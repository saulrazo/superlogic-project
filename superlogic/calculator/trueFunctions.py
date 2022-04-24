
def validate_Expression(operation):
    # En esta funcion, se evalua la expresion y se analiza si es que hay 2 variables juntas, lo cual la volveria una
    # proposicion invalida
    op_List = []
    op_List[:0] = operation
    possible = ["p", "q", "r"]
    long_Operation = int(len(op_List))
    for i in range(long_Operation):
        if op_List[i] in possible:
            if (i + 1) >= long_Operation:
                return True
            if op_List[i + 1] in possible:
                return False
    return True


def get_Tables(operation, num_Variables):
    # En esta funcion, dependiendo del numero de variables, se le asignan los valores iniciales a las variables
    # introducidas en formato de lista
    possible = ["p", "q", "r"]
    op_List = []
    op_List[:0] = operation
    long_Operation = int(len(op_List))
    if num_Variables == 1:
        for i in range(long_Operation):
            if op_List[i] in possible:
                var1 = op_List[i]
                break
        start_Values = {var1: ["V", "F"]}
        return start_Values

    if num_Variables == 2:
        for g in range(long_Operation):
            if op_List[g] in possible:
                var1 = op_List[g]
                break
        for j in range(long_Operation):
            if op_List[j] in possible:
                if op_List[j] != var1:
                    var2 = op_List[j]
                    break
        start_Values = {var1: ["V", "V", "F", "F"], var2: ["V", "F", "V", "F"]}
        return start_Values
    if num_Variables == 3:
        start_Values = {"p": ["V", "V", "V", "V", "F", "F", "F", "F"], "q": ["V", "V", "F", "F", "V", "V", "F", "F"],
                        "r": ["V", "F", "V", "F", "V", "F", "V", "F"]}
        return start_Values


def format_Results(List):
    # Esta funcion se llama para tomar las listas con los resultados en bits y convertirlas a V y F, para que sea mas
    # facil su visualizacion
    actual_Values = []
    for i in List:
        if i == 0:
            actual_Values.append("F")
        if i == 1:
            actual_Values.append("V")
    return actual_Values


def eval_Operation(operation, start_Values,num_Variables):
    # En esta funcion se hace todo lo pesado, aqui se evaluan todos las diferentes listas y se evaluan las expresiones.
    # Al final, se llama a la funcion para darles formato y tomar todos los 0s y 1s y convertirlos en V y F
    for key, value in start_Values.items():
        actual_Values = []
        temp_List = start_Values[key]
        for i in temp_List:
            if i == "F":
                actual_Values.append(0)
            if i == "V":
                actual_Values.append(1)
        start_Values[key] = actual_Values

    operation = operation.replace("^", "&")
    operation = operation.replace("v", "|")
    operation = operation.replace("⊕", "^")

    if num_Variables == 1:
        value_list = []
        for key, value in start_Values.items():
            for i in range(2):
                value_list.append(value[i])

        results = []
        for i in range(2):
            p = value_list[i]
            results.append(eval(operation))

        operation = operation.replace("&", "^")
        operation = operation.replace("|", "v")
        

        results = format_Results(results)
        results_Dict = {operation: results}
        return results_Dict

    if num_Variables == 2:

        operation = operation.replace("p→q", "~p|q")
        operation = operation.replace("q→p", "~q|p")
        operation = operation.replace("~p↔q", "(p|q)&(~q|~p)")
        operation = operation.replace("p↔~q", "(~p|~q)&(q|p)")
        operation = operation.replace("p↔q", "(~p|q)&(~q|p)")
        operation = operation.replace("q↔p", "(~p|q)&(~q|p)")

        value_list1 = []
        value_list2 = []
        check_key = 0
        for key, value in start_Values.items():
            if check_key == 0:
                for i in range(4):
                    value_list1.append(value[i])
                    if i == 3:
                        check_key = 1
            else:
                for i in range(4):
                    value_list2.append(value[i])

        results = []
        for i in range(4):
            p = value_list1[i]
            q = value_list2[i]
            results.append(eval(operation))

        for i in range(len(results)):
            if results[i] < 0:
                results[i] += 2

        operation = operation.replace("&", "^")
        operation = operation.replace("|", "v")
        

        results = format_Results(results)
        results_Dict = {operation: results}
        return results_Dict

    if num_Variables == 3:
        if "→" or "↔" in operation:
            negacion = 0
            ubicacion = 0
            long_Eval = 0
            op_List = []
            op_List[:0] = operation
            long_Operation = len(op_List)
            for i in range(long_Operation):
                if op_List[i] == "→" or op_List[i] == "↔":
                    ubicacion = i
                    break
            if ubicacion > 2:
                value_list1 = []
                value_list2 = []
                value_list3 = []
                check_key = 0
                for key, value in start_Values.items():
                    if check_key == 0:
                        for i in range(8):
                            value_list1.append(value[i])
                            if i == 3:
                                check_key = 1
                    elif check_key == 1:
                        for i in range(8):
                            value_list2.append(value[i])
                            check_key = 2
                    else:
                        for i in range(8):
                            value_list3.append(value[i])

                operation_Temp = operation[0:3]

                results = []
                for i in range(8):
                    p = value_list1[i]
                    q = value_list2[i]
                    results.append(eval(operation_Temp))

                for i in range(len(results)):
                    if results[i] < 0:
                        results[i] += 2

                temp_Variables = op_List[0:3]
                temp_Variables = ''.join(temp_Variables)
                if op_List[4] == "~":
                    temp_Variables_2 = op_List[4:6]
                    temp_Variables_2 = ''.join(temp_Variables_2)
                    negacion = 1
                else:
                    if len(op_List) > 6:

                        operation_Temp = operation[4:7]
                        operation_Temp = ''.join(operation_Temp)

                        results_2 = []
                        for i in range(8):
                            if "p" in operation_Temp and "q" in operation_Temp:
                                p = value_list1[i]
                                q = value_list2[i]
                                operation_Temp_2 = operation_Temp
                            elif "p" in operation_Temp and "r" in operation_Temp:
                                operation_Temp_2 = operation_Temp.replace("r", "q")
                                p = value_list1[i]
                                q = value_list3[i]
                            else:
                                operation_Temp_2 = operation_Temp.replace("r", "p")
                                p = value_list2[i]
                                q = value_list3[i]
                            results_2.append(eval(operation_Temp_2))
                        long_Eval = 1

                        for i in range(len(results_2)):
                            if results_2[i] < 0:
                                results_2[i] += 2

                    else:
                        negacion = 2
                        temp_Variables_2 = op_List[4]

                if long_Eval == 1:
                    operation_nueva = operation.replace(temp_Variables, "p")
                    operation_nueva = operation_nueva.replace(operation_Temp, "q")
                    operation_nueva = operation_nueva.replace("p→q", "~p|q")
                    operation_nueva = operation_nueva.replace("p↔q", "(p|~q)&(q|~p)")
                else:
                    operation_nueva = operation.replace(temp_Variables, "p")
                    operation_nueva = operation_nueva.replace(temp_Variables_2, "q")
                    operation_nueva = operation_nueva.replace("p→q", "~p|q")
                    operation_nueva = operation_nueva.replace("p↔q", "(p|~q)&(q|~p)")

                final_Results = []

                if negacion == 1:
                    actual_list3 = []
                    for i in value_list3:
                        if i == 0:
                            actual_list3.append(1)
                        if i == 1:
                            actual_list3.append(0)
                elif negacion == 2:
                    actual_list3 = value_list3
                else:
                    actual_list3 = results_2

                for i in range(8):
                    p = results[i]
                    q = actual_list3[i]
                    final_Results.append(eval(operation_nueva))

                for i in range(len(final_Results)):
                    if final_Results[i] < 0:
                        final_Results[i] += 2

                if negacion == 1:

                    temp_Variables = temp_Variables.replace("&", "^")
                    temp_Variables = temp_Variables.replace("|", "v")
                    temp_Variables = temp_Variables.replace("^", "⊕")

                    operation = operation.replace("&", "^")
                    operation = operation.replace("|", "v")
                    operation = operation.replace("^", "⊕")
                    actual_list3 = format_Results(actual_list3)
                    results = format_Results(results)
                    final_Results = format_Results(final_Results)
                    results_Dict = {temp_Variables_2: actual_list3, temp_Variables: results, operation: final_Results}
                    return results_Dict
                elif negacion == 0:
                    temp_Variables = temp_Variables.replace("&", "^")
                    temp_Variables = temp_Variables.replace("|", "v")

                    operation = operation.replace("&", "^")
                    operation = operation.replace("|", "v")

                    operation_Temp = operation_Temp.replace("&", "^")
                    operation_Temp = operation_Temp.replace("|", "v")

                    actual_list3 = format_Results(actual_list3)
                    results = format_Results(results)
                    final_Results = format_Results(final_Results)
                    results_Dict = {operation_Temp: actual_list3, temp_Variables: results, operation: final_Results}
                    return results_Dict
                else:

                    temp_Variables = temp_Variables.replace("&", "^")
                    temp_Variables = temp_Variables.replace("|", "v")
                    temp_Variables = temp_Variables.replace("^", "⊕")

                    operation = operation.replace("&", "^")
                    operation = operation.replace("|", "v")
                    operation = operation.replace("^", "⊕")
                    results_Dict = {temp_Variables: results, operation: final_Results}
                    return results_Dict

        value_list1 = []
        value_list2 = []
        value_list3 = []
        check_key = 0
        for key, value in start_Values.items():
            if check_key == 0:
                for i in range(8):
                    value_list1.append(value[i])
                    if i == 3:
                        check_key = 1
            elif check_key == 1:
                for i in range(8):
                    value_list2.append(value[i])
                    check_key = 2
            else:
                for i in range(8):
                    value_list3.append(value[i])

        results = []
        for i in range(8):
            p = value_list1[i]
            q = value_list2[i]
            r = value_list3[i]
            results.append(eval(operation))

        for i in range(len(results)):
            if results[i] < 0:
                results[i] += 2

        return results


if __name__ == '__main__':
    # El inicio de nuestro programa, aqui se toma la entrada inicial de los valores y la proposicion y se llaman a
    # todas las otras funciones
    num_Variables = 0
    operation = input("Proposicion: ")
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
        print(get_Tables(operation, num_Variables))
        print(eval_Operation(operation, start_Values))

# p^q^rvq
