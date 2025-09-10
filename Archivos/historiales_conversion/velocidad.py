from datetime import datetime

historial_velocidad = []

def kmh_a_ms(kmh: float) -> float:
    ms = kmh / 3.6
    historial_velocidad.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entrada": f"{kmh} km/h",
        "salida": f"{ms:.2f} m/s"
    })
    return ms

def ms_a_kmh(ms: float) -> float:
    kmh = ms * 3.6
    historial_velocidad.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entrada": f"{ms} m/s",
        "salida": f"{kmh:.2f} km/h"
    })
    return kmh
