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
