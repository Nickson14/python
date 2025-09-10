import csv
import Gestores.GestorIncidentes as GG
import datetime

FechaActual = datetime.datetime.now()

def exportIncidentes():
    try:
        with open(f"ArchivosExportados\IncidentesExportados{FechaActual.strftime('%Y%m%d%H%M')}.csv",mode="w",newline='',encoding="utf-8") as archivo:
            campos = ['subject', 'descripcion', 'user']
            escritura = csv.writer(archivo)
            escritura.writerow(campos)
            
            for clave,valor in GG.dicIncidentes.items():
                escritura.writerow([valor['subject'], valor['descripcion'], valor['user']])       
    
    except Exception as e:
        print(f"⚠ Error al abrir el archivo")
    print('Exportacion realizada corrrectamente')