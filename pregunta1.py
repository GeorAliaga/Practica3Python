def calcular_porcentaje():
    while True:
        try:
            fraccion_str = input("Ingrese una fraccion en formato X/Y: ")
            
            x, y = map(int, fraccion_str.split('/'))


            if not (isinstance(x, int) and isinstance(y, int)):
                raise ValueError("X e Y deben ser numeros enteros.")
            if x > y or y == 0:
                raise ValueError("X debe ser menor o igual a Y, y Y no puede ser 0.")

            porcentaje = (x / y) * 100

            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{int(round(porcentaje))}%")


            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0.")
        except Exception as e:
            print(f"Error inesperado: {e}")


calcular_porcentaje()
