class PrimeError(Exception):
    pass

def Prime_Num():
    num_list = list(map(int, input("Ingrese números separados por espacios: ").split()))
    prime_list = []

    if len(num_list) == 0:
        raise PrimeError("No se ingreso ningún número")
    
    for num in num_list:
        if num < 1:
            raise PrimeError(f"El número {num} es negativo y no puede ser primo.")
        prime = False
        if num > 1:
            prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            prime_list.append(num)
    

    if len(prime_list) == 0:
        raise PrimeError("No se encontraron números primos")
    
    return " ".join(map(str, prime_list))

try:
    print(Prime_Num())
except ValueError:
    print("Debe ingresar números enteros")
except PrimeError as error:
    print(error)

