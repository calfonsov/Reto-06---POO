# Reto-06---POO
Desarrollo del ejercicio del reto 06:

## Reto 06:
1. Agregue las excepciones requeridas en las asignaciones de código Reto 1.
2. En el paquete, **Shape** identifique al menos los casos en los que se necesiten excepciones (quizás al validar datos de entrada o procedimientos matemáticos), explíquelas claramente mediante comentarios y agréguelas al código.

# Desarrollo Primer Item:
Se manejaron las excepciones en cada código dependiendo de lo que se requeria:

## Primer Código:
En este caso solo se manejo la excepción de la división entre cero que ya pertenece al sistema de Python, y se utilizó de igual manera la excepción de *NameError* perteneciente también al sistema pero se acopló a la funcionalidad del ejercicio.

```python
def Calculator(a: int, b: int, operation: str):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        else:
            return a / b
    else:
        raise NameError("Operación inválida")

try:
    print(Calculator(2, 3, "+"))
    print(Calculator(4, 7, "-"))
    print(Calculator(2, 6, "*"))
    print(Calculator(3, 0, "/"))
    print(Calculator(8, 4, "/"))
    print(Calculator(0, 7, "^"))
except ZeroDivisionError as error:
    print(error)
except NameError as error:
    print(error)
```

## Segundo Código:
En este ejercicio, se creo la excepción acorde a la funcionalidad del método mediante la creación de una clase en especifico que hereda de una excepción ya existente en el sistema. Solo se manejo un caso de excepción.

```python
class PalindromoError(Exception):
    pass

def Palindromo(word: str):
    letters = list()
    for letter in word:
        letters.append(letter)
    new_word = list()
    for letter in range(len(letters) - 1, -1, -1):
        new_word.append(letters[letter])
    if new_word == letters:
        return True
    else:
        raise PalindromoError("La palabra NO es Palíndromo")

try:
    word: str = input("Ingrese una palabra: ")
    print(Palindromo(word))
except PalindromoError as error:
    print(error)
```

## Tercer, Cuarto y Quinto Código:
En estos tres últimos códigos se uso la misma metodología para manejar las excepciones; se crearon perosnalizadas de acuerdo a la funcionalidad de los métodos y luego se usaron dentro del código.

### Tercer Código:
```python
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
```
### Cuarto Código:
```python
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

```

### Quinto Código:
```python
class AnagramaError(Exception):
    pass

def Anagrama():
    list_word = list(map(str, input("Ingrese palabras: ").split()))

    if len(list_word) < 2:
        raise AnagramaError("Debe ingresar al menos dos palabras.")

    anagram = []
    for i in range(len(list_word)):
        base = sorted(list_word[i])
        grupo = []
        for palabra in list_word:
            if sorted(palabra) == base:
                grupo.append(palabra)
        if len(grupo) > 1 and grupo not in anagram:
            anagram.append(grupo)

    if len(anagram) == 0:
        raise AnagramaError("No se encontraron anagramas.")
    
    return anagram


try:
    print(Anagrama())
except AnagramaError as error:
    print(error)
```

# Desarrollo Segundo Item:
En este caso simplemente se establecieron las excepciones necesarias con sus comentarios respectivos. Se utilizó la forma #1 del ejericio en Shape del reto 05, es decir todo modulado en un solo paquete. EL código se encuentra en los archivos subidos al repositorio, para no saturar el README de código.

### Correr el código:
Para poder correr este código ejecute el siguiente comando en la terminal de Visual:

```python
python -m Shape.main
```



