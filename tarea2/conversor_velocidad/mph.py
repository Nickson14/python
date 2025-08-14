def convertir_desde_mph(valor):
    return {
        "km/h": valor * 1.609,
        "m/s": (valor * 1.609) / 3.6
    }
