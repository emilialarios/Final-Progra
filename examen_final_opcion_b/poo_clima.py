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
        """
        Calcula la amplitud térmica del día (diferencia entre máxima y mínima).

        Retorna:
            float: temp_max - temp_min
        """
        # TU CÓDIGO AQUÍ

    def temp_media(self):
        """
        Calcula la temperatura media del día.

        Retorna:
            float: promedio de temp_max y temp_min
        """
        # TU CÓDIGO AQUÍ

    def es_caluroso(self):
        """
        Determina si el día fue caluroso para Ciudad de Guatemala.

        Criterio: temperatura máxima mayor a 28 °C.

        Retorna:
            bool: True si temp_max > 28, False en caso contrario
        """
        # TU CÓDIGO AQUÍ

    def clasificar(self):
        """
        Clasifica el día según su precipitación.

        Usa la misma escala que aplicaste en el Ejercicio 3:
            precipitacion < 1 mm          →  'Seco'
            1 ≤ precipitacion < 5 mm      →  'Lluvia ligera'
            5 ≤ precipitacion < 20 mm     →  'Lluvia moderada'
            precipitacion ≥ 20 mm         →  'Lluvia intensa'

        Hint: usa if / elif / elif / else sobre self.precipitacion

        Retorna:
            str: categoría del día
        """
        # TU CÓDIGO AQUÍ

    def descripcion(self):
        """
        Retorna una cadena con el resumen del día.

        Formato esperado (usa el método clasificar()):
            "2024-05-15 | max=27.3°C  min=14.1°C | Lluvia moderada | Viento: 32.4 km/h"

        Hint: llama a self.clasificar() dentro del f-string.
              Usa :.1f para formatear los números a un decimal.

        Retorna:
            str: descripción formateada del día
        """
        # TU CÓDIGO AQUÍ

    def __str__(self):
        return self.descripcion()

    def __repr__(self):
        return (
            f"DiaClimatico(fecha={self.fecha!r}, temp_max={self.temp_max}, "
            f"temp_min={self.temp_min}, precipitacion={self.precipitacion})"
        )


class RegistroAnual:
    """
    Colección de objetos DiaClimatico que representa un año de registros.

    Atributos:
        ciudad (str)  : nombre de la ciudad
        anio   (int)  : año del registro
        _dias  (list) : lista interna de objetos DiaClimatico
    """

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
        """
        Encuentra el día con la temperatura máxima más alta del año.

        Usa un ciclo for para iterar sobre self._dias.
        Guarda el mayor encontrado en una variable auxiliar.
        Compara con dia.temp_max en cada iteración.

        Retorna:
            DiaClimatico : el día con la temp_max más alta
            None         : si el registro está vacío
        """
        if not self._dias:
            return None
        # TU CÓDIGO AQUÍ

    def dias_por_tipo(self, tipo):
        """
        Retorna una lista con todos los días del tipo dado.

        Parámetro:
            tipo (str): 'Seco', 'Lluvia ligera', 'Lluvia moderada' o 'Lluvia intensa'

        Hint: usa un ciclo for y llama a dia.clasificar() en cada iteración.
              Agrega a una lista auxiliar los que coincidan.

        Retorna:
            list: lista de objetos DiaClimatico filtrada (puede estar vacía)
        """
        # TU CÓDIGO AQUÍ

    def temp_promedio_anual(self):
        """
        Calcula la temperatura máxima promedio del año.

        Usa un ciclo for para sumar las temp_max de todos los días
        y divide entre el total de días al final.

        Retorna:
            float: promedio redondeado a 1 decimal
            0     : si el registro está vacío
        """
        if not self._dias:
            return 0
        # TU CÓDIGO AQUÍ

    def resumen(self):
        """
        Imprime un resumen del registro anual.

        Debe mostrar:
            1. Ciudad, año y total de días             (usa len(self))
            2. El día más caluroso                     (usa dia_mas_caluroso())
            3. Temperatura máxima promedio             (usa temp_promedio_anual())
            4. Cantidad de días por cada tipo          (usa dias_por_tipo())

        Hint: itera sobre los tipos con un for:
            tipos = ['Seco', 'Lluvia ligera', 'Lluvia moderada', 'Lluvia intensa']
        """
        # TU CÓDIGO AQUÍ
