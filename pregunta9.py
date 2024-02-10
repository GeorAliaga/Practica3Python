def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no valido."

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no valido."

def multiplicacion(a, b):  
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no valido."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as e:
        return f"Error: {e}"


if __name__ == "__main__":
    num1 = 10
    num2 = 5


    print(f"Suma: {suma(num1, num2)}")
    print(f"Resta: {resta(num1, num2)}")
    print(f"Multiplicación: {multiplicacion(num1, num2)}")  
    print(f"División: {division(num1, num2)}")
