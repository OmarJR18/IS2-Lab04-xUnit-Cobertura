class Ordenador:
    """Clase encargada de ejecutar algoritmos de ordenamiento bajo el paradigma OO."""

    def bubble_sort(self, vet: list) -> list:
        """Ordena una lista de valores numéricos enteros de forma ascendente."""
        n = len(vet)
        # Bucle exterior (i decrementa hasta 1)
        for i in range(n - 1, 0, -1):
            # Bucle interior (j recorre hasta i - 1)
            for j in range(0, i):
                # Evaluación condicional de intercambio
                if vet[j] > vet[j + 1]:
                    aux = vet[j]
                    vet[j] = vet[j + 1]
                    vet[j + 1] = aux
        return vet
