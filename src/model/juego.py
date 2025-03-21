from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:
    """
    Representa la lógica principal del juego de adivinanza de palabras.

    Attributes:
        DIFICULTAD_BAJA (str): Constante que representa la dificultad baja.
        DIFICULTAD_MEDIA (str): Constante que representa la dificultad media.
        DIFICULTAD_ALTA (str): Constante que representa la dificultad alta.
        __dificultad (str): Dificultad actual del juego.
        __intentos_realizados (int): Número de intentos realizados por el jugador.
        __diccionario (Diccionario): Instancia de la clase Diccionario para obtener palabras.
        __adivinanza (Adivinanza): Instancia de la clase Adivinanza que gestiona la palabra a adivinar.
    """

    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
        Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self) -> int:
        """
        Obtiene el número de intentos realizados por el jugador.

        Returns:
            int: Número de intentos realizados.
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
        Obtiene la instancia de Adivinanza actual.

        Returns:
            Adivinanza: Instancia de Adivinanza que gestiona la palabra a adivinar.
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
        Genera una palabra aleatoria del diccionario.

        Returns:
            str: Palabra generada aleatoriamente.
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
        Calcula el número de intentos permitidos según la dificultad actual.

        Returns:
            int: Número de intentos permitidos.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
        Modifica la dificultad del juego.

        Args:
            dificultad (str): Nueva dificultad del juego.
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
        Inicia una nueva partida del juego.

        Returns:
            int: Número de posiciones (letras) de la palabra a adivinar.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> list[int]:
        """
        Intenta adivinar una letra de la palabra.

        Args:
            letra (str): Letra que el jugador quiere adivinar.

        Returns:
            list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

        Raises:
            ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
        Verifica si aún quedan intentos disponibles.

        Returns:
            bool: True si quedan intentos, False en caso contrario.
        """
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        """
        Verifica si el jugador ha adivinado toda la palabra.

        Returns:
            bool: True si el jugador ha ganado, False en caso contrario.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()