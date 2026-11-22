
from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificacion, nombre):
        if not identificacion or not identificacion.strip():
            raise ValueError("La identificacion es obligatoria.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        self.__identificacion = identificacion
        self.__nombre = nombre

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass
