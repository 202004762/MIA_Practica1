class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.cabeza:
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                if actual == self.cabeza:
                    self.cabeza = actual.siguiente

                return
            
            actual = actual.siguiente

        print("Valor no encontrado")

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
            
        print("NULL")
