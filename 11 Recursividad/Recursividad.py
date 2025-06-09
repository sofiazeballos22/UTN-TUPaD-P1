# recursividad.py
# Autor: Ana Sofía Zeballos - Comisión XX
# Funciones recursivas con validación de datos

# 1) Factorial
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo acepta números enteros no negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2) Fibonacci
def fibonacci(pos):
    if not isinstance(pos, int) or pos < 0:
        raise ValueError("La posición en Fibonacci debe ser un entero no negativo.")
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

# 3) Potencia recursiva
def potencia(base, exponente):
    if not isinstance(exponente, int) or exponente < 0:
        raise ValueError("El exponente debe ser un entero no negativo.")
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Decimal a binario (como string)
def decimal_a_binario(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    if n == 0:
        return "0"
    return decimal_a_binario(n // 2) + str(n % 2) if n > 1 else "1"

# 5) Palíndromo
def es_palindromo(palabra):
    if not palabra.isalpha():
        raise ValueError("Solo se permiten palabras con letras.")
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos
def suma_digitos(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7) Contar bloques (pirámide)
def contar_bloques(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("La altura debe ser un entero mayor o igual a 1.")
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar dígitos
def contar_digito(numero, digito):
    if not all(isinstance(x, int) for x in [numero, digito]) or digito < 0 or digito > 9 or numero < 0:
        raise ValueError("Ambos deben ser enteros no negativos, y el dígito entre 0 y 9.")
    if numero == 0:
        return 1 if digito == 0 else 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)
