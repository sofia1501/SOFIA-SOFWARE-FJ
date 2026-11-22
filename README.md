# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción

Proyecto académico desarrollado en Python para la gestión de clientes, servicios y reservas de la empresa Software FJ.

El sistema permitirá administrar diferentes tipos de servicios, registrar clientes y gestionar reservas mediante una aplicación basada en programación orientada a objetos.

## 2. Objetivo general

Desarrollar una aplicación modular que permita gestionar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos y el manejo avanzado de excepciones.

## 3. Objetivos específicos

- Implementar clases abstractas y clases derivadas.
- Aplicar abstracción, herencia, encapsulación y polimorfismo.
- Desarrollar validaciones para los datos ingresados.
- Gestionar la creación, confirmación y cancelación de reservas.
- Implementar excepciones personalizadas.
- Registrar eventos y errores mediante archivos de logs.
- Realizar pruebas para verificar el funcionamiento del sistema.

## 4. Integrantes

- Sofía Espinel Ávila.


## 5. Lenguaje y herramientas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git y GitHub.

## 6. Almacenamiento

El sistema no utiliza bases de datos. La información se gestiona mediante objetos, listas internas y archivos destinados al registro de eventos y errores.

## 7. Archivos del proyecto

- `excepciones.py`: contiene las excepciones personalizadas.
- `logs.py`: permite registrar eventos y errores.
- `reserva.py`: contiene la lógica de gestión de reservas.
- `main.py`: permite ejecutar el programa y realizar las pruebas.

Los módulos de clientes y servicios se incorporarán durante el desarrollo e integración del proyecto.

## 8. Ejecución

Para ejecutar el programa desde la terminal:

```bash
python3 main.py
```

## 9. Estado del proyecto

Actualmente se encuentra desarrollado y probado el módulo inicial de reservas, con 11 pruebas ejecutadas. Los demás componentes se integrarán progresivamente para completar el sistema.

