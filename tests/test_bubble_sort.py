import unittest
from src.bubble_sort import Ordenador


class TestBubbleSort(unittest.TestCase):
    """Suite de pruebas unitarias para el método bubble_sort de la clase Ordenador."""

    def setUp(self):
        """Inicializa la instancia del SUT (System Under Test)."""
        self.ordenador = Ordenador()

    def tearDown(self):
        """Limpia los recursos después de cada prueba."""
        self.ordenador = None

    def test_cp1_un_solo_elemento(self):
        # Arrange
        vet = [5]
        esperado = [5]

        # Act
        resultado = self.ordenador.bubble_sort(vet)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_cp2_lista_ya_ordenada(self):
        # Arrange
        vet = [1, 2]
        esperado = [1, 2]

        # Act
        resultado = self.ordenador.bubble_sort(vet)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_cp3_lista_desordenada_con_swap(self):
        # Arrange
        vet = [2, 1]
        esperado = [1, 2]

        # Act
        resultado = self.ordenador.bubble_sort(vet)

        # Assert
        self.assertEqual(resultado, esperado)

    def test_cp4_lista_completamente_invertida(self):
        # Arrange
        vet = [4, 3, 2, 1]
        esperado = [1, 2, 3, 4]

        # Act
        resultado = self.ordenador.bubble_sort(vet)

        # Assert
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()
