
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base, descripcion):
        if not codigo or not codigo.strip():
            raise ValueError("El codigo es obligatorio.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool) or precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_base = precio_base
        self.__descripcion = descripcion

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    def describir_servicio(self):
        return self.__descripcion

    def validar_disponibilidad(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        return True

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

class ReservaSala(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        return self.precio_base * duracion


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        return self.precio_base * duracion


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        return self.precio_base * duracion
