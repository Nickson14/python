from datetime import datetime

historial_tiempo = []

def horas_a_minutos(horas: float) -> float:
    minutos = horas * 60
    historial_tiempo.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entrada": f"{horas} horas",
        "salida": f"{minutos} minutos"
    })
    return minutos

def minutos_a_horas(minutos: float) -> float:
    horas = minutos / 60
    historial_tiempo.append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entrada": f"{minutos} minutos",
        "salida": f"{horas:.2f} horas"
    })
    return horas
