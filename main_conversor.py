#PAQUETE conversor de longitud
from conversor_longitud import kilómetros,metros,millas,pies as logitud

#Paquete Conversor de temperatura
from Conversor_De_Temperatura import celcius,Fahrenheit,Kelvin as Temperatura




def menu_longitud():
    print("\nOpciones de conversión de longitud:")
    print("1. Metros a kilómetros")
    print("2. Kilómetros a metros")
    print("3. Millas a kilómetros")
    print("4. Pies a metros")

def menu_temperatura():
    print("\nOpciones de conversión de temperatura:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")

while True:
    print("\n¿Qué deseas calcular? (longitud/temperatura/salir)")
    eleccion = input(">> ").strip().lower()

    if eleccion == "salir":
        print("Cerrando, Gracias por salir.")
        break

    elif eleccion == "longitud":
        menu_longitud()
        opcion = input("Elige una opción (1-4): ").strip()
        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            print(f"{valor} metros = {metros.m_to_km(valor)} kilómetros")
        elif opcion == "2":
            print(f"{valor} km = {kilómetros.km_to_m(valor)} metros")
        elif opcion == "3":
            print(f"{valor} millas = {millas.mi_to_km(valor)} kilómetros")
        elif opcion == "4":
            print(f"{valor} pies = {logitud.ft_to_m(valor)} metros") # type: ignore
        else:
            print("Opción no válida en longitud.")

    elif eleccion == "temperatura":
        menu_temperatura()
        opcion = input("Elige una opción (1-4): ").strip()
        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            print(f"{valor} °C = {celcius.C_to_F(valor)} °F")
        elif opcion == "2":
            print(f"{valor} °F = {Fahrenheit.F_To_(valor)} °C")
        elif opcion == "3":
            print(f"{valor} °C = {celcius.C_to_K(valor)} K")
        elif opcion == "4":
            print(f"{valor} K = {Temperatura.K_to_C(valor)} °C")
        else:
            print("Opción no válida en temperatura.")

    else:
        print("Por favor, elige entre 'longitud', 'temperatura' o 'salir'.")