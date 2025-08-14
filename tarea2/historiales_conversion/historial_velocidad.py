historial_velocidad = []

def agregar_historial_velocidad(cantidad, unidad_origen, resultado):
    historial_velocidad.append({
        "cantidad": cantidad,
        "unidad_origen": unidad_origen,
        "resultado": resultado
    })

def mostrar_historial_velocidad():
    if not historial_velocidad:
        print("No hay historial de conversiones de velocidad.")
    else:
        print("\nHistorial de conversiones de velocidad:")
        for i, registro in enumerate(historial_velocidad, 1):
            print(f"{i}. {registro['cantidad']} {registro['unidad_origen']} -> {registro['resultado']}")
