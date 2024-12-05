#
#& Estructuras de datos 
#& Listas
lista_1 = ["manzana", "pera", "cereza"]

print("Lista completa: ", lista_1)

#! Acceder a un elemento en específico 
print("Un solo elemento: ", lista_1[1])


#! añadir un elemento 
lista_1.append("naranja")
print("Lista después de añadirle: ", lista_1)


#! Eliminsr un elemento 
lista_1.pop(1)
print("Lista depues de eliminar: ", lista_1)

#& Diccionarios
#? Clave - Valor

diccionario_1 = {"nombre": "Ana", "edad": 50, "ciudad": "bogota"}
print("Diccionario completo: ", diccionario_1)

#!Acceder a un valor 
print("Nombre: ", diccionario_1["nombre"])

#!Añadir un nuevo elemento clave-valor 
diccionario_1["profesion"] = "Desarrolladora"
print("Actualizado: ", diccionario_1)

#& Operaciones con estrcuturas de datos 

lista_1 = ["manzana", "pera"]
lista_2 = ["naranja"]

lista_nueva = lista_1 + lista_2
print("Suma de dos listas", lista_nueva)

