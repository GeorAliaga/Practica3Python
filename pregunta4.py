class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

try:
    largo = float(input("Ingrese el largo del rectangulo: "))
    ancho = float(input("Ingrese el ancho del rectangulo: "))


    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area:.2f}")

except ValueError:
    print("Error: Ingrese valores numéricos para el largo y el ancho.")
