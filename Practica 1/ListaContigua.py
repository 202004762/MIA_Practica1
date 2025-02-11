class ListaContigua:
    def __init__(self):
        self.lista = []

    def insertar(self, valor):
        if len(self.lista) < 10:
            self.lista.append(valor)

        else:
            print("Lista llena")

    def eliminar(self, valor):
        if valor in self.lista:
            self.lista.remove(valor)
            
        else:
            print("Valor no encontrado")

    def mostrar(self):
        print("Lista Contigua:", self.lista)
