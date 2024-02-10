class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Informacion del estudiante:\nNombre: {self.nombre}\nNumero de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"   Nota {i}: {nota}")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas = list(notas)



try:
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_registro = input("Ingrese el número de registro del estudiante: ")
    alumno = Alumno(nombre, numero_registro)

    alumno.display()

    edad = int(input("Ingrese la edad del estudiante: "))
    alumno.set_age(edad)

    notas = map(float, input("Ingrese las notas del estudiante separadas por espacios: ").split())
    alumno.set_notas(*notas)

    alumno.display()

except ValueError:
    print("Error: Ingrese valores numericos para la edad y las notas.")
