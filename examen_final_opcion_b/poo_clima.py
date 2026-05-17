"""
Ejercicio 5 — Programación Orientada a Objetos
Examen Final — Programación 1 (F12) — Variante B: Clima Open-Meteo

Instrucciones:
    Implementa todos los métodos marcados con  # TU CÓDIGO AQUÍ
    No modifiques los métodos ya implementados ni los __init__.
    Cuando termines, regresa al notebook y ejecuta el Ejercicio 5.
"""

class RegistroMeteorologico:
    """Representa un registro meteorológico genérico."""

    def __init__(self, fecha):
        self.fecha = fecha

    def clasificar(self):
        """
        Clasifica el registro según alguna variable meteorológica.
        Este método debe ser sobreescrito en la clase hija.

        Retorna:
            str: categoría del registro
        """
        pass

    def descripcion(self):
        """
        Retorna una descripción legible del registro.
        Este método debe ser sobreescrito en la clase hija.

        Retorna:
            str: descripción del registro
        """
        pass

    def __str__(self):
        return self.descripcion() or f"RegistroMeteorologico {self.fecha}"

    def __repr__(self):
        return f"{self.__class__.__name__}(fecha={self.fecha!r})"


class DiaClimatico(RegistroMeteorologico):
    """
    Representa el registro climático de un día en Ciudad de Guatemala.

    Atributos:
        fecha         (str o date) : fecha del registro (columna 'time')
        temp_max      (float)      : temperatura máxima en °C  (columna 'temperature_2m_max')
        temp_min      (float)      : temperatura mínima en °C  (columna 'temperature_2m_min')
        precipitacion (float)      : precipitación en mm       (columna 'precipitation_sum')
        viento_max    (float)      : viento máximo en km/h     (columna 'wind_speed_10m_max')
    """

    def __init__(self, fecha, temp_max, temp_min, precipitacion, viento_max):
        super().__init__(fecha)
        self.temp_max      = temp_max
        self.temp_min      = temp_min
        self.precipitacion = precipitacion
        self.viento_max    = viento_max

    def rango_termico(self):
        """Calcula la amplitud térmica del día (diferencia entre máxima y mínima)."""
        return self.temp_max - self.temp_min

    def temp_media(self):
        """Calcula la temperatura media del día."""
        return (self.temp_max + self.temp_min) / 2

    def es_caluroso(self):
        """Criterio: temperatura máxima mayor a 28 °C."""
        return self.temp_max > 28

    def clasificar(self):
        """Clasifica el día según su precipitación."""
        if self.precipitacion < 1:
            return "Seco"
        elif self.precipitacion < 5:
            return "Lluvia ligera"
        elif self.precipitacion < 20:
            return "Lluvia moderada"
        else:
            return "Lluvia intensa"

    def descripcion(self):
        """Retorna una cadena con el resumen del día."""
        return (
            f"{self.fecha} | "
            f"max={self.temp_max:.1f}°C min={self.temp_min:.1f}°C | "
            f"{self.clasificar()} | "
            f"Viento: {self.viento_max:.1f} km/h"
        )

    def __str__(self):
        return self.descripcion()

    def __repr__(self):
        return (
            f"DiaClimatico(fecha={self.fecha!r}, temp_max={self.temp_max}, "
            f"temp_min={self.temp_min}, precipitacion={self.precipitacion})"
        )


class RegistroAnual:
    """Colección de objetos DiaClimatico que representa un año de registros."""

    def __init__(self, ciudad, anio):
        self.ciudad = ciudad
        self.anio   = anio
        self._dias  = []

    def agregar_dia(self, dia):
        """Agrega un objeto DiaClimatico al registro."""
        self._dias.append(dia)

    def __len__(self):
        """Retorna el total de días en el registro."""
        return len(self._dias)

    def dia_mas_caluroso(self):
        """Encuentra el día con la temperatura máxima más alta del año."""
        if not self._dias:
            return None

        mas_caluroso = self._dias[0]
        for dia in self._dias:
            if dia.temp_max > mas_caluroso.temp_max:
                mas_caluroso = dia
        return mas_caluroso

    def dias_por_tipo(self, tipo):
        """Retorna una lista con todos los días del tipo dado."""
        lista = []
        for dia in self._dias:
            if dia.clasificar() == tipo:
                lista.append(dia)
        return lista

    def temp_promedio_anual(self):
        """Calcula la temperatura máxima promedio del año."""
        if not self._dias:
            return 0

        suma = 0
        for dia in self._dias:
            suma += dia.temp_max
        
        promedio = suma / len(self._dias)
        return round(promedio, 1)

    def resumen(self):
        """Imprime un resumen del registro anual."""
        print(f"Ciudad: {self.ciudad}")
        print(f"Año: {self.anio}")
        print(f"Total de días: {len(self)}")

        print("\nDía más caluroso:")
        print(self.dia_mas_caluroso())

        print("\nTemperatura máxima promedio:")
        print(f"{self.temp_promedio_anual()}°C")

        tipos = ['Seco', 'Lluvia ligera', 'Lluvia moderada', 'Lluvia intensa']
        print("\nCantidad de días por tipo:")
        for tipo in tipos:
            cantidad = len(self.dias_por_tipo(tipo))
            print(f"  {tipo}: {cantidad}")
