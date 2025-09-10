#Gestor de incidentes
import Gestores.GestorIncidentes as GI
import Importaciones.IncidentesImport as III
import Exportaciones.IncidentesExport as EIE

# Nuevo import para conversiones
from historiales_conversion import tiempo, velocidad, exportador

print('Bienvenido al gestor de incidentes 2025T3')

while True:
    op = input('1.Listar 2.Crear 3.Modificar 4.Eliminar 5.Importar 6.Exportar 7.Salir 8.Conversiones\n')

    if op == '1':
        GI.ListarIncidentes()
    elif op == '2':
        subject = input('Subject: ')
        descripcion = input('Descripcion: ')
        user = input('User: ')
        GI.CrearIncidentes(subject,descripcion,user)
    elif op == '3':
        GI.ListarIncidentes()
        clave = int(input('Digita el numero de incidente a modificar: '))
        if GI.ValidarIncidente(clave):
            op = input('1.Modificar Subject 2.Modificar Descripcion 3.Modificar User: ')
            if op == '1':
                subject = input('Digita el subject para modificar el incidente: ')
                GI.ModificarIncidentes(clave,op, subject)
            elif op == '2':
                descripcion = input('Digita la descripcion para modificar el incidente: ')
                GI.ModificarIncidentes(clave,op, descripcion)
            elif op == '3':
                user = input('Digita el user para modificar el incidente: ')
                GI.ModificarIncidentes(clave,op, user)
    elif op == '4':
        GI.ListarIncidentes()
        clave = int(input('Digita el numero de incidente a eliminar: '))
        GI.EliminarIncidentes(clave)
    elif op == '5':
        III.ImportarIncidentes()
    elif op == '6':
        EIE.ExportarIncidentes()
    elif op == '7':
        print("Saliendo del programa...")
        break
    elif op == '8':
        print("\n--- Conversiones ---")
        print("1. Tiempo")
        print("2. Velocidad")
        tipo = input("Seleccione tipo de conversión: ")

        if tipo == "1":
            valor = float(input("Ingrese el valor en horas: "))
            minutos = tiempo.horas_a_minutos(valor)
            print(f"{valor} horas = {minutos} minutos")

            valor = float(input("Ingrese el valor en minutos: "))
            horas = tiempo.minutos_a_horas(valor)
            print(f"{valor} minutos = {horas:.2f} horas")

            exportador.exportar_csv(
                "Historial_Tiempo.csv",
                tiempo.historial_tiempo,
                ["fecha", "entrada", "salida"]
            )

        elif tipo == "2":
            valor = float(input("Ingrese el valor en km/h: "))
            ms = velocidad.kmh_a_ms(valor)
            print(f"{valor} km/h = {ms:.2f} m/s")

            valor = float(input("Ingrese el valor en m/s: "))
            kmh = velocidad.ms_a_kmh(valor)
            print(f"{valor} m/s = {kmh:.2f} km/h")

            exportador.exportar_csv(
                "Historial_Velocidad.csv",
                velocidad.historial_velocidad,
                ["fecha", "entrada", "salida"]
            )
    else:
        print("❌ Opción no válida. Intente de nuevo.")

