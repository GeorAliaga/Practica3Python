def procesar_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese una lista de calificaciones separales por comas: ")
            calificaciones_lista = calificaciones_str.split(',')

            calificaciones_entero = [int(calificacion) for calificacion in calificaciones_lista]
            print("Calificaciones enteras:", calificaciones_entero)

            break

        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

procesar_calificaciones()
