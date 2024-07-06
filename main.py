import os
import globales
import productos
import estadisticas

def menu_estadistica():
    while True:
        os.system("cls")
        print("Menu")
        print("1. Producto con valor màs alto")
        print("2. Producto con valor del iva mas bajo")
        print("3.·promedio valor de los productos")
        print("4.·media geometrica")
        print("5. salir")

        opcion =globales.seleccionar_opcion(5)

        if opcion == 1:
             print("1. Producto con valor màs alto")
             estadisticas.valor_mas_alto()
        elif opcion == 2:
           print("2. Producto con valor del iva mas bajo")
           estadisticas.valor_mas_bajo()
        elif opcion == 3:
            print("3.·promedio valor de los productos")
            estadisticas.promedio_valor()
        elif opcion == 4:
            print("4.·media geometrica")
            estadisticas.media_geometrica()
        elif opcion == 5:        
            print("5. salir")
            return
        input()

def menu_general():
    while True:
        os.system("cls")
        print("Menu")
        print("1. Asignar valores aleatorios")
        print("2. Ver estadisticas")
        print("3.· salir del programa")

        opcion =globales.seleccionar_opcion(3)

        if opcion == 1:
            productos.generar_aleatorios()

        elif opcion == 2:
            menu_estadistica()
        elif opcion == 3:
            print("3.· salir del programa")
            print("Desarrollado por ")
            return
        input()

if __name__ == "__main__":
    menu_general()        