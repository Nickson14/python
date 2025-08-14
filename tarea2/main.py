from datetime import datetime
from conversor_tiempo import convertir_desde_segundos, convertir_desde_minutos, convertir_desde_horas
from conversor_velocidad import convertir_desde_kmh, convertir_desde_ms, convertir_desde_mph
from historiales_conversion import (
    agregar_historial_tiempo, mostrar_historial_tiempo,
    agregar_historial_velocidad, mostrar_historial_velocidad
)

def menu():
    while True:
        print("\n=== Conversor de Tiempo y Velocidad ===")
        print(f"Fecha y hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("1. Conversión de Tiempo")
        print("2. Conversión de Velocidad")
        print("3. Ver Historial de Tiempo")
        print("4. Ver Historial de Velocidad")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            convertir_tiempo()
        elif opcion == "2":
            convertir_velocidad()
        elif opcion == "3":
            mostrar_historial_tiempo()
        elif opcion == "4":
            mostrar_historial_velocidad()
        elif opcion == "5":
            print("Gracias por utilizarme")
            break
        else:
            print("Opción no válida.")

def convertir_tiempo():
    cantidad = float(input("Ingrese la cantidad: "))
    unidad = input("Unidad de origen (segundos, minutos, horas): ").lower()

    if unidad == "segundos":
        resultado = convertir_desde_segundos(cantidad)
    elif unidad == "minutos":
        resultado = convertir_desde_minutos(cantidad)
    elif unidad == "horas":
        resultado = convertir_desde_horas(cantidad)
    else:
        print("Unidad no válida.")
        return

    print(f"Resultados: {resultado}")
    agregar_historial_tiempo(cantidad, unidad, resultado)

def convertir_velocidad():
    cantidad = float(input("Ingrese la cantidad: "))
    unidad = input("Unidad de origen (km/h, m/s, mph): ").lower()

    if unidad == "km/h":
        resultado = convertir_desde_kmh(cantidad)
    elif unidad == "m/s":
        resultado = convertir_desde_ms(cantidad)
    elif unidad == "mph":
        resultado = convertir_desde_mph(cantidad)
    else:
        print("Unidad no válida.")
        return

    print(f"Resultados: {resultado}")
    agregar_historial_velocidad(cantidad, unidad, resultado)

if __name__ == "__main__":
    menu()
