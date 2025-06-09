# 🔁 Práctico 11 - Recursividad en Python

Este proyecto fue desarrollado de forma individual como parte del trabajo práctico de **Programación I** en la **UTN - TUPaD**, dentro de la carpeta `11 Recursividad`.

El objetivo del trabajo fue **aplicar recursividad en la resolución de problemas**, entendiendo su lógica y comportamiento. Se incluyeron **validaciones de entrada, manejo de errores y separación de responsabilidades**, estructurando el código de forma reutilizable y profesional.

---

## 🎯 Descripción General

Se desarrollaron funciones recursivas para resolver distintas problemáticas matemáticas y algorítmicas.  
El código fue dividido en dos archivos:

- `recursividad.py`: contiene las funciones puras y validadas
- `main.py`: ejecuta ejemplos prácticos de cada función

Esta separación permite **reutilizar la lógica** en otros programas o incluso en futuros desarrollos con interfaz gráfica o tests automáticos.

---

##  Funcionalidades principales

- ✅ Implementación de funciones recursivas puras
- 🛡️ Validaciones estrictas con `ValueError` ante entradas inválidas
- 📋 Separación de lógica (`recursividad.py`) y pruebas (`main.py`)
- 🔢 Manejo de errores con `try/except`
- 🧩 Aplicación práctica de recursividad con ejemplos reales

---

## 🔧 Herramientas y técnicas utilizadas

### 📚 Funciones y estructuras principales (con número de línea aproximado):

| Línea | Función | Descripción |
|-------|---------|-------------|
| 5     | `factorial(n)` | Calcula el factorial de un número entero positivo |
| 13    | `fibonacci(pos)` | Retorna el valor de la serie de Fibonacci en una posición dada |
| 21    | `potencia(base, exponente)` | Calcula base elevado a exponente de forma recursiva |
| 27    | `decimal_a_binario(n)` | Convierte un número decimal a binario como string |
| 33    | `es_palindromo(palabra)` | Verifica si una palabra es un palíndromo |
| 40    | `suma_digitos(n)` | Suma los dígitos de un número entero sin convertir a string |
| 46    | `contar_bloques(n)` | Calcula bloques necesarios para una pirámide de altura `n` |
| 51    | `contar_digito(numero, digito)` | Cuenta cuántas veces aparece un dígito dentro de un número |

---

## 💡 Palabras clave y conceptos utilizados

- `recursión`: función que se llama a sí misma
- `if / else`: estructuras de control
- `raise ValueError(...)`: para forzar errores ante entradas inválidas
- `isinstance()`: validación del tipo de dato
- `try / except`: manejo de errores en ejecución
- `modularización`: separar la lógica de ejecución

---

## 📦 Estructura del proyecto

11 Recursividad/
├── recursividad.py # Lógica pura: funciones recursivas validadas
├── main.py # Pruebas y llamadas a funciones
└── README.md # Documentación del proyecto



---

## 📌 Requisitos

- Python 3.x
- Editor como VSCode, Thonny o PyCharm
- Consola o terminal para ejecutar `main.py`

---

## 🧪 Ejemplo de flujo

**Ejecución en consola:**

```bash
python main.py


 1) Factorial de 5: 120
 2) Serie Fibonacci hasta posición 7:
Fibonacci(0) = 0
Fibonacci(1) = 1
...
Fibonacci(7) = 13
 3) Potencia 2^4: 16
 4) Decimal 13 a binario: 1101
 5) ¿Es 'radar' un palíndromo?: True
 6) Suma de dígitos de 1234: 10
 7) Bloques para pirámide de altura 4: 10
 8) El dígito 3 aparece 3 veces en 31353


## 🙌 Créditos

Proyecto realizado por **Ana Sofía Zeballos, comisión 5** *   
Trabajo práctico de **Programación I - UTN TUPaD**  
Tema: Tema: Aplicación de funciones recursivas en Python
