
from cliente import Cliente

print("PRUEBAS DEL MODULO DE CLIENTES")

# Prueba 1: Cliente correcto
try:
    cliente = Cliente(
        "12345",
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )
    print("Cliente registrado correctamente.")
    cliente.mostrar_informacion()

except ValueError as error:
    print("Error:", error)

# Prueba 2: Nombre vacío
try:
    Cliente("12346", "", "ana@gmail.com", "3001234567")

except ValueError as error:
    print("Error controlado:", error)

# Prueba 3: Correo inválido
try:
    Cliente("12347", "Ana Perez", "correo-invalido", "3001234567")

except ValueError as error:
    print("Error controlado:", error)

# Prueba 4: Teléfono vacío
try:
    Cliente("12348", "Luis Perez", "luis@gmail.com", "")

except ValueError as error:
    print("Error controlado:", error)

print("Pruebas finalizadas.")
