# logs.py

import logging
import os

# Crear la carpeta de registros
os.makedirs("logs", exist_ok=True)

# Configurar el archivo de registro
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar eventos importantes
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores del sistema
def registrar_error(mensaje):
    logging.error(mensaje)
    
- `main.py`: integra los módulos y ejecuta las pruebas generales del sistema.
- `prueba_cliente.py`: contiene las pruebas individuales del módulo de clientes.
- `prueba_servicio.py`: contiene las pruebas individuales del módulo de servicios.

## 8. Funcionalidades

- Registro y validación de clientes.
- Administración de reservas de salas.
- Alquiler de equipos.
- Gestión de asesorías especializadas.
- Cálculo de costos según el tipo de servicio.
- Aplicación de descuentos e impuestos.
- Confirmación y cancelación de reservas.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores.

## 9. Ejecución

Para ejecutar el programa principal desde la terminal:

```bash
python3 main.py
```

Para ejecutar las pruebas individuales:

```bash
python3 prueba_cliente.py
python3 prueba_servicio.py
```

## 10. Estado del proyecto

El sistema cuenta con sus módulos principales desarrollados e integrados. Se realizaron pruebas individuales de clientes y servicios, así como 14 pruebas en el programa principal.

El proyecto utiliza objetos, listas internas y archivos de registro, sin conexión a bases de datos.

