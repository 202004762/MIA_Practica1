class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente

                else:
                    self.cabeza = actual.siguiente

                return
            
            anterior = actual
            actual = actual.siguiente

        print("Valor no encontrado")

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
            
        print("NULL")
