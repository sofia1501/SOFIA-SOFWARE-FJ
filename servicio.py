from abc import ABC, abstractmethod
from logs import registrar_evento, registrar_error


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base, descripcion):
        try:
            if not isinstance(codigo, str) or not codigo.strip():
                raise ValueError("El codigo es obligatorio.")

            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("El nombre es obligatorio.")

            if (not isinstance(precio_base, (int, float))
                    or isinstance(precio_base, bool) or precio_base <= 0):
                raise ValueError("El precio debe ser mayor que cero.")

            if not isinstance(descripcion, str) or not descripcion.strip():
                raise ValueError("La descripcion es obligatoria.")

            self.__codigo = codigo.strip()
            self.__nombre = nombre.strip()
            self.__precio_base = precio_base
            self.__descripcion = descripcion.strip()

            registrar_evento(
                "Servicio registrado correctamente: " + self.__nombre
            )

        except Exception as error:
            registrar_error(
                "Error al registrar servicio: " + str(error)
            )
            raise

    def __str__(self):
        return self.nombre

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    @property
    def descripcion(self):
        return self.__descripcion

    def describir_servicio(self):
        return self.descripcion

    def validar_disponibilidad(self, duracion):
        try:
            if (not isinstance(duracion, (int, float))
                    or isinstance(duracion, bool) or duracion <= 0):
                raise ValueError(
                    "La duracion debe ser mayor que cero."
                )
            return True

        except ValueError as error:
            registrar_error(str(error))
            raise

    @abstractmethod
    def calcular_costo(self, duracion):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        costo = self.precio_base * duracion
        registrar_evento("Costo de reserva de sala calculado.")
        return costo

    def describir_servicio(self):
        return self.descripcion + " (Costo por hora de reserva)."

    def validar_disponibilidad(self, duracion):
        super().validar_disponibilidad(duracion)

        if duracion > 12:
            error = ValueError(
                "La reserva de sala no puede superar 12 horas."
            )
            registrar_error(str(error))
            raise error

        return True


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        cargo_mantenimiento = 10000
        costo = (self.precio_base * duracion) + cargo_mantenimiento
        registrar_evento("Costo de alquiler de equipo calculado.")
        return costo

    def describir_servicio(self):
        return self.descripcion + " (Incluye cargo de mantenimiento)."

    def validar_disponibilidad(self, duracion):
        super().validar_disponibilidad(duracion)

        if duracion > 24:
            error = ValueError(
                "El alquiler del equipo no puede superar 24 horas."
            )
            registrar_error(str(error))
            raise error

        return True


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion):
        self.validar_disponibilidad(duracion)
        recargo_especializado = 0.20
        costo_base = self.precio_base * duracion
        costo = costo_base + (costo_base * recargo_especializado)
        registrar_evento("Costo de asesoria especializada calculado.")
        return costo

    def describir_servicio(self):
        return self.descripcion + " (Incluye recargo por especializacion)."

    def validar_disponibilidad(self, duracion):
        super().validar_disponibilidad(duracion)

        if duracion > 8:
            error = ValueError(
                "La asesoria no puede superar 8 horas."
            )
            registrar_error(str(error))
            raise error

        return True
