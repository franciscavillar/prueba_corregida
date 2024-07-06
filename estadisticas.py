import globales
import math

def promedio_valor():
    #todos_los_productos = globales.leer_archivo_csv("productos.csv")
    todos_los_productos = globales.leer_archivo_json("productos.json")

    cantidad = 0
    suma = 0
    for producto in todos_los_productos:
        suma += producto['valor'] #suma += int(producto['valor']) para csv
        cantidad += 1

        promedio = suma/cantidad

        print("El promedio de venta es: $", promedio)

def media_geometrica():
    #todos_los_productos = globales.leer_archivo_csv("productos.csv")
    todos_los_productos = globales.leer_archivo_json("productos.json")

    cantidad = 0
    suma = 0
    for producto in todos_los_productos:
        suma += math.log(producto['valor']) #suma += int(producto['valor']) para csv
        cantidad += 1

        promedio = math.exp(suma/cantidad)

        print("La media geometrica de venta es: $", promedio)

def valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json("productos.json")
    
    productos_ordenados = sorted(todos_los_productos, key=lambda x: int(x['valor']), reverse=True) #reverse true ordena de mayor a menor

    for producto in productos_ordenados[:1]:
        print("nombre:", producto['nombre'])  
        print("valor", producto['valor'])  
        return  

def valor_mas_bajo():
    todos_los_productos = globales.leer_archivo_json("productos.json")
    
    productos_ordenados = sorted(todos_los_productos, key=lambda x: int(x['valor']), reverse=False) #reverse false ordena de menor a mayor

    for producto in productos_ordenados[:1]:
        print("nombre:", producto['nombre'])  
        print("IVA", producto['iva'])  
        return 


promedio_valor()    
media_geometrica()
valor_mas_alto()
valor_mas_bajo()

