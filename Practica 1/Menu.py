from ListaContigua import ListaContigua
from ListaLigada import ListaLigada
from ListaDoble import ListaDoble
from ListaIndexada import ListaIndexada


def menu():
    while True:
        print("--------------Menu--------------")
        print("|1. Lista Contigua             |")
        print("|2. Lista Ligada               |")
        print("|3. Lista Doblemente Ligada    |")
        print("|4. Lista Indexada             |")
        print("|5. Salir                      |")
        print("--------------------------------")
        opcion = int(input("Ingrese su opcion: "))
        
        if opcion == 1:
            lista = ListaContigua()

        elif opcion == 2:
            lista = ListaLigada()

        elif opcion == 3:
            lista = ListaDoble()

        elif opcion == 4:
            lista = ListaIndexada()

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida")
            continue
        
        while True:
            print("---------------------------------")
            print("|1. Insertar dato               |")
            print("|2. Eliminar dato               |")
            print("|3. Mostrar lista               |")
            print("|4. Volver al menu principal    |")
            print("---------------------------------")
            subopcion = int(input("Ingrese su opcion: "))
            
            if subopcion == 1:
                valor = int(input("Ingrese el valor: "))
                lista.insertar(valor)

            elif subopcion == 2:
                valor = int(input("Ingrese el valor a eliminar: "))
                lista.eliminar(valor)

            elif subopcion == 3:
                lista.mostrar()

            elif subopcion == 4:
                break

            else:
                print("Opcion invalida")

if __name__ == "__main__":
    menu()

