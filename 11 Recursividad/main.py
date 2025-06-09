# main.py
# Punto de entrada del trabajo práctico - Recursividad
# Autor: Ana Sofía Zeballos

from Recursividad import (
    factorial, fibonacci, potencia, decimal_a_binario,
    es_palindromo, suma_digitos, contar_bloques, contar_digito
)

def ejecutar_ejemplos():
    print(" 1) Factorial de 5:", factorial(5))
    
    print("\n 2) Serie Fibonacci hasta posición 7:")
    for i in range(8):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    print("\n 3) Potencia 2^4:", potencia(2, 4))

    print("\n 4) Decimal 13 a binario:", decimal_a_binario(13))

    print("\n 5) ¿Es 'radar' un palíndromo?:", es_palindromo("radar"))
    print(" ¿Es 'python' un palíndromo?:", es_palindromo("python"))

    print("\n 6) Suma de dígitos de 1234:", suma_digitos(1234))

    print("\n 7) Bloques necesarios para pirámide de altura 4:", contar_bloques(4))

    print("\n 8) Cuántas veces aparece el dígito 3 en el número 31353:", contar_digito(31353, 3))

if __name__ == "__main__":
    try:
        ejecutar_ejemplos()
    except Exception as e:
        print(f"❌ Error detectado: {e}")
