#Ana Sofía Zeballos
#Programación 1
#TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN


# Actividad 1 - Crear una lista con los números del 1 al 100 que sean múltiplos de 4
#--------------------------------------------------------------------------------------------------------------------------------

multiplos_de_4 = list(range(4, 101, 4))

# Mostrar el resultado
print("Múltiplos de 4 del 1 al 100:", multiplos_de_4)




# Actividad 2 - Crear una lista con los 5 elementos que más te gustan
#--------------------------------------------------------------------------------------------------------------------------------

favoritos = [
    "Suprema al plato con puré",
    "Suprema a la napolitana con puré",
    "Tarta de acelga con queso",
    "Tarta de pollo y verduras con queso",
    "Tarta de choclo y queso"
]

# Mostrar el penúltimo elemento usando indexing negativo
print("El penúltimo favorito es:", favoritos[-2])



# Actividad 3 - Crear una lista vacía y agregarle tres palabras utilizando el método append
#--------------------------------------------------------------------------------------------------------------------------------
palabras = []

# Agregar tres palabras usando append
palabras.append("python")
palabras.append("suprema")
palabras.append("tarta")

# Imprimir la lista resultante
print("Lista final:", palabras)



# Actividad 4 - Reemplazar valores en una lista
#--------------------------------------------------------------------------------------------------------------------------------

# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Mostrar lista original
print("Lista original:", animales)

# Reemplazar el segundo (índice 1) con "loro"
# Reemplazar el último (índice -1) con "oso"
animales[1] = "loro"
animales[-1] = "oso"

# Mostrar lista modificada
print("Lista modificada:", animales)




# Actividad 6 - Crear una lista del 10 al 30 con pasos de 5 y mostrar los dos primeros elementos
#--------------------------------------------------------------------------------------------------------------------------------

numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Primeros dos números:", numeros[0], numeros[1])




# Actividad 7 - Reemplazar valores en una lista de autos
#--------------------------------------------------------------------------------------------------------------------------------

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en las posiciones 1 y 2
autos[1] = "camioneta"
autos[2] = "coupe"

# Mostrar lista actualizada
print("Autos actualizados:", autos)





# Actividad 8 - Crear una lista vacía y agregarle el doble de (5, 10, 15) números como cadenas
#--------------------------------------------------------------------------------------------------------------------------------

doble = []

doble.append(str(5 * 2))   # "10"
doble.append(str(10 * 2))  # "20"
doble.append(str(15 * 2))  # "30"

print("Lista con el doble de números:", doble)





# Actividad 10 - Crear una lista anidada con diferentes tipos de datos
#--------------------------------------------------------------------------------------------------------------------------------


lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

# Imprimir la lista resultante
print("Lista anidada resultante:")
print(lista_anidada)

