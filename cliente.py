import re
from entidad import Entidad
from logs import registrar_evento, registrar_error


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        try:
            super().__init__(identificacion, nombre)

            if not isinstance(correo, str) or not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+", correo.strip()
            ):
                raise ValueError("El correo electronico no es valido.")

            if not isinstance(telefono, str) or not telefono.strip():
                raise ValueError("El telefono es obligatorio.")

            self.__correo = correo.strip()
            self.__telefono = telefono.strip()

            registrar_evento(
                "Cliente registrado correctamente: " + self.nombre
            )

        except ValueError as error:
            registrar_error("Error al registrar cliente: " + str(error))
            raise

        except Exception as error:
            registrar_error("Error inesperado al registrar cliente: " + str(error))
            raise

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        print("\n--- INFORMACION DEL CLIENTE ---")
        print("Identificacion:", self.identificacion)
        print("Nombre:", self.nombre)
        print("Correo:", self.correo)
        print("Telefono:", self.telefono)

    def __str__(self):
        return self.nombre
