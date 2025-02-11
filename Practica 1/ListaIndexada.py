class ListaIndexada:
    def __init__(self):
        self.lista = []
        self.indice = []

    def insertar(self, valor):
        if len(self.lista) < 10:
            self.lista.append(valor)
            self.indice.append(len(self.lista))
            
        else:
            print("Lista llena")

    def eliminar(self, valor):
        if valor in self.lista:
            idx = self.lista.index(valor)
            self.lista.pop(idx)
            self.indice.pop(idx)

        else:
            print("Valor no encontrado")

    def mostrar(self):
        for i in range(len(self.lista)):
            print(f"Indice: {self.indice[i]} -> Valor: {self.lista[i]}")
