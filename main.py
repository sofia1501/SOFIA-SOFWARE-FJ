# SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import (
    ErrorReserva,
    ErrorOperacion,
    ErrorServicioNoDisponible
)


# Servicio utilizado para probar la falta de disponibilidad
class ServicioNoDisponible(ReservaSala):

    def validar_disponibilidad(self, duracion):
        super().validar_disponibilidad(duracion)
        return False


# Listas internas del sistema
clientes = []
servicios = []
reservas = []


print("=" * 50)
print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
print("=" * 50)


# PRUEBA 1: Registrar un cliente real
print("\nPRUEBA 1: Registrar cliente")

try:
    cliente = Cliente(
        "12345",
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )

    clientes.append(cliente)
    print("Cliente registrado correctamente.")
    cliente.mostrar_informacion()

except ValueError as error:
    print("Error controlado:", error)


# PRUEBA 2: Registrar los tres tipos de servicios
print("\nPRUEBA 2: Registrar servicios")

try:
    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000,
        "Reserva de sala por hora"
    )

    equipo = AlquilerEquipo(
        "S002",
        "Proyector",
        30000,
        "Alquiler de proyector por hora"
    )

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoria tecnica",
        80000,
        "Servicio de asesoria especializada"
    )

    servicios.extend([sala, equipo, asesoria])

    for servicio in servicios:
        print("Servicio:", servicio.nombre)
        print("Descripcion:", servicio.describir_servicio())
        print("Precio base:", servicio.precio_base)
        print("-" * 30)

except ValueError as error:
    print("Error controlado:", error)


# PRUEBA 3: Demostrar polimorfismo
print("\nPRUEBA 3: Calcular costos de diferentes servicios")

for servicio in servicios:
    try:
        costo = servicio.calcular_costo(2)
        print(servicio.nombre, "- Costo por 2 horas:", costo)

    except ValueError as error:
        print("Error:", error)


# PRUEBA 4: Crear una reserva con objetos reales
print("\nPRUEBA 4: Crear reserva")

try:
    reserva = Reserva(cliente, sala, 2)
    reservas.append(reserva)

    print("Reserva creada correctamente.")

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 5: Calcular el costo con descuento e impuesto
print("\nPRUEBA 5: Calcular costo")

try:
    costo = reserva.calcular_costo(10, 19)
    print("Costo total:", costo)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 6: Confirmar reserva
print("\nPRUEBA 6: Confirmar reserva")

try:
    reserva.confirmar()
    print("Reserva confirmada correctamente.")

except (ErrorReserva, ErrorOperacion,
        ErrorServicioNoDisponible) as error:
    print("Error controlado:", error)


# PRUEBA 7: Consultar estado
print("\nPRUEBA 7: Consultar estado")

print("Estado:", reserva.obtener_estado())


# PRUEBA 8: Mostrar informacion
print("\nPRUEBA 8: Mostrar reserva")

reserva.mostrar_informacion()


# PRUEBA 9: Intentar crear una reserva sin cliente
print("\nPRUEBA 9: Cliente invalido")

try:
    Reserva(None, sala, 2)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 10: Intentar crear una reserva con duracion negativa
print("\nPRUEBA 10: Duracion incorrecta")

try:
    Reserva(cliente, sala, -2)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 11: Calcular costo con descuento incorrecto
print("\nPRUEBA 11: Descuento incorrecto")

try:
    reserva.calcular_costo(150, 19)

except ErrorReserva as error:
    print("Error controlado:", error)


# PRUEBA 12: Intentar confirmar un servicio no disponible
print("\nPRUEBA 12: Servicio no disponible")

try:
    servicio_no_disponible = ServicioNoDisponible(
        "S004",
        "Sala ocupada",
        40000,
        "Servicio sin disponibilidad"
    )

    reserva_no_disponible = Reserva(
        cliente,
        servicio_no_disponible,
        2
    )

    reserva_no_disponible.confirmar()

except (ErrorReserva, ErrorServicioNoDisponible) as error:
    print("Error controlado:", error)


# PRUEBA 13: Cancelar reserva
print("\nPRUEBA 13: Cancelar reserva")

try:
    reserva.cancelar()
    print("Reserva cancelada correctamente.")

except ErrorOperacion as error:
    print("Error controlado:", error)


# PRUEBA 14: Intentar cancelar dos veces
print("\nPRUEBA 14: Segunda cancelacion")

try:
    reserva.cancelar()
    print("Error: Se permitio cancelar dos veces.")

except ErrorOperacion as error:
    print("Error controlado correctamente:", error)


# Resumen del sistema
print("\n" + "=" * 50)
print("RESUMEN DEL SISTEMA")
print("=" * 50)

print("Clientes registrados:", len(clientes))
print("Servicios registrados:", len(servicios))
print("Reservas creadas:", len(reservas))

print("\nPruebas finalizadas.")
