import globales
import json
import random

def generar_aleatorios():
    productos = [
      "Café Americano",
      "Té Chai",
      "Croissant",
     "Jugo Naranja",
      "Panini de Pavo y Queso",
     "Pastel de Zanahoria",
     "Espresso Doble",
     "Ba;do de Frutas",
     "Muffin",
     "Ensalada",
     "Chocolate Caliente",
     "Tarta de Frambuesa",
     "Sándwich de Huevo",
     "Galletas de Avena",
      "Frappé de Caramelo"
     ]
    todos_los_productos = []
    
    for nombre in productos:
        valor = random.randint(20, 100) * 100
        iva = valor*0.19

        nuevo_producto = {
          "nombre": nombre,
          "valor": valor,
          "iva": iva
           }
        todos_los_productos.append(nuevo_producto)  
       
    fieldnames = ["nombre", "valor", "iva"]    
    globales.guardar_archivo_json("productos.json", todos_los_productos)  
    globales.guardar_archivo_csv("productos.csv", todos_los_productos, fieldnames) 
    print("productos generados")

   
         
generar_aleatorios()         
        
     
