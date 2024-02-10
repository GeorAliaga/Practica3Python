import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


def menu():
    while True:
        print("1. Calcular el area de un círculo")
        print("2. Calcular el area de un rectángulo")
        print("3. Calcular el area de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"El area del círculo es: {circulo.calcular_area()}")
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"El area del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Rectangulo(lado, lado)
            print(f"El area del cuadrado es: {cuadrado.calcular_area()}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no válida. Por favor, seleccione una opción valida.")


if __name__ == "__main__":
    menu()
