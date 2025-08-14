historial_tiempo = []

def agregar_historial_tiempo(cantidad, unidad_origen, resultado):
    historial_tiempo.append({
        "cantidad": cantidad,
        "unidad_origen": unidad_origen,
        "resultado": resultado
    })

def mostrar_historial_tiempo():
    if not historial_tiempo:
        print("No hay historial de conversiones de tiempo.")
    else:
        print("\nHistorial de conversiones de tiempo:")
        for i, registro in enumerate(historial_tiempo, 1):
            print(f"{i}. {registro['cantidad']} {registro['unidad_origen']} -> {registro['resultado']}")
