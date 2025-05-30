# Ana Sofía Zeballos
# UTN - TUPaD - Programación I



# Actividad 1 - Estructuras Repetitivas
# Mostrar los números del 0 al 100 (uno por línea)
#--------------------------------------------------------------------------------------------------------------------------------


for numero in range(0, 101):
    print(numero)


# Actividad 2 - Contar dígitos de un número entero
# ------------------------------------------------------------------------------

while True:
    entrada = input("Ingresá un número entero: ")
    try:
        numero = int(entrada)  
        break              
    except ValueError:
        print("❌ Error: eso no es un número entero. Intentá de nuevo.")


cantidad_digitos = len(str(abs(numero)))  # usamos abs() para ignorar el signo negativo
print(f" El número tiene {cantidad_digitos} dígito(s).")





# Actividad 3 - Sumar números entre dos valores (sin incluirlos)
# ------------------------------------------------------------------------------

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("❌ Error: eso no es un número entero. Intentá de nuevo.")


inicio = pedir_entero("Ingresá el primer número: ")
fin = pedir_entero("Ingresá el segundo número: ")

# Aseguramos el orden correcto (menor a mayor)
menor = min(inicio, fin)
mayor = max(inicio, fin)

# Sumamos los valores entre ambos, sin incluir los extremos
suma = 0
for i in range(menor + 1, mayor):
    suma += i

# Mostramos el resultado
if menor + 1 >= mayor:
    print(f"No hay números enteros entre {inicio} y {fin} para sumar.")
else:
    print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")



# Actividad 4 - Sumar números hasta que el usuario ingrese 0
# ------------------------------------------------------------------------------

total = 0

while True:
    entrada = input("Ingresá un número (0 para terminar): ")
    try:
        numero = int(entrada)
    except ValueError:
        print("❌ Error: eso no es un número entero. Intentá de nuevo.")
        continue  # vuelve al principio del while

    if numero == 0:
        break  # termina el bucle si el número es cero

    total += numero

print(f" La suma total es: {total}")





# Actividad 5 - Imprimir pares en orden descendente


print("Números pares del 0 al 100 en orden decreciente:")
for numero in range(100, -1, -2):
    print(numero)





# Actividad 7 - Suma de números desde 0 hasta un número indicado por el usuario
# --------------------------------------------------------------------------------

while True:
    entrada = input("Ingresá un número entero positivo: ")
    try:
        limite = int(entrada)
        if limite <= 0:
            print("❌ El número debe ser mayor que 0. Intentá de nuevo.")
            continue
        break
    except ValueError:
        print("❌ Eso no es un número entero válido. Intentá de nuevo.")

# Calculamos la suma de todos los números desde 1 hasta (limite - 1)
suma = 0
for i in range(1, limite):
    suma += i

print(f" La suma de los números entre 0 y {limite}, sin incluir {limite}, es: {suma}")



# Actividad 8 - Clasificar 100 números enteros
# ------------------------------------------------------------------------------

TOTAL_NUMEROS = 5  # Cambiá este valor para probar con menos números

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresá {TOTAL_NUMEROS} números enteros:")

for i in range(1, TOTAL_NUMEROS + 1):
    while True:
        entrada = input(f"{i}. Ingresá un número entero: ")
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("❌ Eso no es un número entero. Intentá de nuevo.")

    # Clasificamos el número
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Si es 0, no suma ni a positivos ni a negativos

# Resultados finales
print("\n📊 Resultados:")
print(f"🔢 Pares: {pares}")
print(f"🔢 Impares: {impares}")
print(f"➕ Positivos: {positivos}")
print(f"➖ Negativos: {negativos}")






# Actividad 9 - Calcular la media de N números enteros
# -----------------------------------------------------------------------------------

CANTIDAD_NUMEROS = 5  # Cambiá este valor a 100 

numeros = []
print(f"Ingresá {CANTIDAD_NUMEROS} números enteros:")

for i in range(1, CANTIDAD_NUMEROS + 1):
    while True:
        entrada = input(f"{i}. Ingresá un número entero: ")
        try:
            numero = int(entrada)
            numeros.append(numero)
            break
        except ValueError:
            print("❌ Eso no es un número entero válido. Intentá de nuevo.")

# Calculamos la media
suma = sum(numeros)
media = suma / CANTIDAD_NUMEROS

# Mostramos resultado
print("\n📊 Resultado final:")
print(f"🧮 Suma total: {suma}")
print(f"📈 Media (promedio): {media}")




# Actividad 10 - Invertir los dígitos de un número entero (mínimo 2 dígitos)
# ---------------------------------------------------------------------------

while True:
    entrada = input("Ingresá un número entero de al menos 2 dígitos: ")
    try:
        numero = int(entrada)
        # Validar cantidad de dígitos 
        if len(str(abs(numero))) < 2:
            print("⚠️ El número debe tener al menos 2 dígitos. Intentá de nuevo.")
            continue
        break
    except ValueError:
        print("❌ Eso no es un número entero válido. Intentá de nuevo.")

# Invertimos el número
numero_invertido = str(abs(numero))[::-1]

# Agregamos el signo si era negativo
if numero < 0:
    numero_invertido = "-" + numero_invertido

print(f"🔁 Número invertido: {numero_invertido}")
