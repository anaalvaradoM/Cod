#
#& VARIABLES
#& Espacio de memoria donde se almacna información 
#& pueden cambiar durante la ejecución del programa

nombre = "Ana"
edad = 15
es_estudiante = False
print(nombre, edad, es_estudiante)

Edad = 40
print(Edad)
Edad = 50
print(Edad)

#* Tipos de datos:

#!Entero 
numero_entero = -10
print("Entero: ", numero_entero)

#!Flotante 
numero_flotante = 10.5
print("Flotante: ", numero_flotante)

#!cadena 
cadena = "Hola, mundo"
print("Cadena ", cadena)

#!Booleano
booleano = True
print("Boolenano", booleano)

#& Operaciones con enteros y flotantes 

numero1 = 5
numero2 = 3
suma = numero1 + numero2
print("la suma es: ", suma)

numero1 = 5.5
numero2 = 3.6
suma = numero1 + numero2
print("la suma es: ", suma)

#& Suma de Booleanos 
booleano1 = True
booleano2 = True
booleano3 = True

print(booleano1 + booleano2 + booleano3)

#& Operaciones con cadenas 
cadena1 = "Hola"
cadena2 = "mundo"
resultado = cadena1 + " " + cadena2
print("Concatenación: ", resultado)

numero1 = "1"
numero2 = "2"

#String --> cadena de carateres 

#& Determinar el tipo de dato  type()

print("Tipo de dato de 10", type(10))
print("Tipo de dato de 10.5", type(10.5))
print("Tipo de dato de Hola", type("hola"))
print("Tipo de dato de true", type(True))