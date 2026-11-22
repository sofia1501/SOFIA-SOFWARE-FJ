from abc import ABC, abstractmethod
from logs import registrar_evento, registrar_error


class Entidad(ABC):

    def __init__(self, identificacion, nombre):
        try:
            if not isinstance(identificacion, str) or not identificacion.strip():
                raise ValueError("La identificacion es obligatoria.")

            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre es obligatorio.")

            self.__identificacion = identificacion.strip()
            self.__nombre = nombre.strip()

            registrar_evento(
                "Entidad registrada correctamente: " + self.__nombre
            )

        except ValueError as error:
            registrar_error(
                "Error al registrar entidad: " + str(error)
            )
            raise

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass
