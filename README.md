# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción

Proyecto académico desarrollado en Python para gestionar clientes, servicios y reservas de la empresa ficticia Software FJ.

El sistema utiliza programación orientada a objetos y una arquitectura modular que permite registrar clientes, administrar diferentes tipos de servicios, calcular costos y gestionar reservas.

## 2. Objetivo general

Desarrollar una aplicación modular que permita gestionar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos y el manejo de excepciones.

## 3. Objetivos específicos

- Implementar clases abstractas y clases derivadas.
- Aplicar abstracción, herencia, encapsulación y polimorfismo.
- Desarrollar validaciones para los datos ingresados.
- Gestionar la creación, confirmación y cancelación de reservas.
- Implementar excepciones personalizadas.
- Registrar eventos y errores mediante archivos de logs.
- Realizar pruebas para verificar el funcionamiento del sistema.

## 4. Integrante

- Sofía Espinel Ávila.

## 5. Lenguaje y herramientas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git y GitHub.

## 6. Almacenamiento

El sistema no utiliza bases de datos. La información se administra mediante objetos y estructuras de datos internas. Los archivos se utilizan para registrar eventos y errores del sistema.

## 7. Estructura de archivos

- `entidad.py`: contiene la clase abstracta Entidad.
- `cliente.py`: implementa la gestión y validación de clientes.
- `servicio.py`: contiene la clase abstracta Servicio y sus tres clases especializadas.
- `reserva.py`: gestiona la creación, cálculo de costos, confirmación y cancelación de reservas.
- `excepciones.py`: contiene las excepciones personalizadas.
- `logs.py`: configura el registro de eventos y errores.
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

El proyecto utiliza objetos, structuras de datos internas y archivos de registro, sin conexión a bases de datos.
