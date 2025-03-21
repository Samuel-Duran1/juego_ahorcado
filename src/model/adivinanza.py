class Adivinanza:
    """
    Representa una palabra a adivinar en el juego del ahorcado.

    Attributes:
        __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
        __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
        Inicializa una instancia de la clase Adivinanza.

        Args:
            palabra (str): La palabra que se debe adivinar.
        """
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> list[int]:
        """
        Intenta adivinar una letra en la palabra.

        Args:
            letra (str): La letra que se intenta adivinar.

        Returns:
            list[int]: Lista de posiciones donde aparece la letra en la palabra. Vacía si la letra no está.
        """
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> list[str]:
        """
        Obtiene la lista de letras que conforman la palabra.

        Returns:
            list[str]: Lista de letras de la palabra.
        """
        return self.__letras

    def obtener_posiciones(self) -> list[bool]:
        """
        Obtiene la lista de booleanos que indican si cada letra ha sido adivinada.

        Returns:
            list[bool]: Lista de booleanos que indican el estado de adivinanza de cada letra.
        """
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        """
        Obtiene la cantidad de letras que tiene la palabra.

        Returns:
            int: Número de letras en la palabra.
        """
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        """
        Verifica si todas las letras de la palabra han sido adivinadas.

        Returns:
            bool: True si todas las letras han sido adivinadas, False en caso contrario.
        """
        return all(self.__posiciones)