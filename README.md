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

El sistema no utiliza bases de datos. La información se administra mediante objetos y listas internas. Los archivos se utilizan para registrar eventos y errores del sistema.

## 7. Estructura de archivos

- `entidad.py`: contiene la clase abstracta Entidad.
- `cliente.py`: implementa la gestión y validación de clientes.
- `servicio.py`: contiene la clase abstracta Servicio y sus tres clases especializadas.
- `reserva.py`: gestiona la creación, cálculo de costos, confirmación y cancelación de reservas.
- `excepciones.py`: contiene las excepciones personalizadas.
- `logs.py`: configura el registro de eventos y errores.
-