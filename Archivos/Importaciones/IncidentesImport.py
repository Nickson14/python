import csv
import Gestores.GestorIncidentes as GG
import datetime

def importIncidentes():
    try:
        with open("Archivos\Incidentes.csv", mode="r", encoding="utf-8") as archivo:
            lectura = csv.DictReader(archivo)
            for fila in lectura:
                try:
                    GG.dicIncidentes[GG.idIncrement] = {
                        "subject": fila["subject"],
                        "descripcion": fila["descripcion"],
                        "user": fila["user"],
                        "fechaCreacion": datetime.datetime.now()}
                    # Mantener el idIncrement actualizado
                    GG.idIncrement = GG.idIncrement + 1
                except Exception as e:
                    print(f"⚠ Error en registro {fila}: {e}")
    except FileNotFoundError as e:
        print('El archivo Incidentes.csv no se encuentra en el directorio')
    print('Importacion realizada corrrectamente')
        