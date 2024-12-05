#
#! Funciones ---> bloque de codigo orientado a cumplir 
#! una determinada instrcución 

#? Esta no lleva parametro 
def saludar():
    print("Hola a todxs")

def saludarConParametro(nombre):
    return f"Hola, {nombre}"

saludar()
print(saludarConParametro("Javier"))
print(saludarConParametro("Ana"))
print(saludarConParametro("James"))
print(saludarConParametro("Natalia"))
print(saludarConParametro("Andres"))

def suma(num1, num2):
    resul = num1 + num2
    return resul

resulSuma = suma(5,7)
print(resulSuma)
