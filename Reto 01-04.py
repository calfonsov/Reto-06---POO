class SumParError(Exception):
    pass

def Sum_Par():
    try:
        list_num = list(map(int, input("Ingrese números: ").split()))
    except ValueError:
        raise SumParError("Debe ingresar solo números enteros separados por espacios.")

    if len(list_num) < 2:
        raise SumParError("Debe ingresar al menos dos números.")

    result = list_num[0] + list_num[1]
    for i in range(len(list_num) - 1):
        current_sum = list_num[i] + list_num[i + 1]
        if current_sum > result:
            result = current_sum

    return result

try:
    print(Sum_Par())
except SumParError as error:
    print(error)
