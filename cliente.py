
import re
from entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)

        if not correo or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", correo.strip()
        ):
            raise ValueError("El correo electronico no es valido.")

        if not telefono or not telefono.strip():
            raise ValueError("El telefono es obligatorio.")

        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

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