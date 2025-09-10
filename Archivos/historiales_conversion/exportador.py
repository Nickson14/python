import csv
import os

def exportar_csv(nombre_archivo, historial, campos):
    """Exporta un historial de conversiones a un archivo CSV"""
    carpeta = "ArchivosExportados"
    os.makedirs(carpeta, exist_ok=True)

    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(historial)

    print(f"\n✅ Historial exportado correctamente en: {ruta}")
