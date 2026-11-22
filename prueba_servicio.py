
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

print("PRUEBAS DEL MODULO DE SERVICIOS")

servicios = [
    ReservaSala("S01", "Sala de reuniones", 50000, "Reserva de sala"),
    AlquilerEquipo("E01", "Proyector", 30000, "Alquiler de proyector"),
    AsesoriaEspecializada("A01", "Asesoria tecnica", 80000, "Asesoria especializada")
]

for servicio in servicios:
    try:
        costo = servicio.calcular_costo(2)
        print("\nServicio:", servicio.nombre)
        print("Descripcion:", servicio.describir_servicio())
        print("Costo:", costo)

    except ValueError as error:
        print("Error:", error)

# Prueba de duración inválida
try:
    servicios[0].calcular_costo(-2)

except ValueError as error:
    print("\nError controlado:", error)

# Prueba de precio inválido
try:
    ReservaSala("S02", "Sala incorrecta", -5000, "Prueba")

except ValueError as error:
    print("Error controlado:", error)

print("\nPruebas finalizadas.")
