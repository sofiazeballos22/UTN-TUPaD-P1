# 🧮 Práctico 2 - Funciones en Python

Este proyecto fue desarrollado de forma individual como parte del trabajo práctico de **Programación I** en la **UTN - TUPaD**, dentro de la carpeta `05 Funciones`.

El objetivo del trabajo fue **aplicar funciones, validaciones y estructuras de control en Python**, cubriendo casos de la vida real como cálculos, operaciones matemáticas, conversiones y validación de datos del usuario.

---

## 🎯 Descripción General

Se desarrolló un programa interactivo por consola, donde el usuario puede:

- Ingresar sus datos personales con validación de entrada
- Calcular área y perímetro de un círculo
- Convertir segundos a horas
- Ver tablas de multiplicar
- Ejecutar operaciones básicas
- Calcular IMC y promedio
- Convertir temperaturas
- Validar nombres y edades mínimas

Se aplicaron **técnicas de validación, manejo de errores y control de flujo** para asegurar que los datos ingresados sean correctos y el programa no falle ante entradas inválidas.

---

## 🧠 Funcionalidades principales

- ✅ Validación de nombre y apellido: mínimo 3 letras, solo caracteres alfabéticos
- 🔞 Edad mínima requerida para continuar: 16 años
- 🔢 Conversión de datos con manejo de errores (`try/except`)
- 🧮 Cálculos matemáticos variados
- 📋 Uso de funciones y condicionales para modularizar el código

---

## 🔧 Herramientas y técnicas utilizadas

### 📚 Funciones y estructuras principales (con número de línea aproximado):

| Línea | Función | Descripción |
|-------|---------|-------------|
| 4     | `imprimir_hola_mundo()` | Imprime un saludo simple |
| 9     | `saludar_usuario(nombre)` | Saludo personalizado |
| 14    | `informacion_personal(...)` | Imprime nombre, edad y residencia |
| 19    | `calcular_area_circulo(radio)` | Calcula el área de un círculo |
| 22    | `calcular_perimetro_circulo(radio)` | Calcula el perímetro de un círculo |
| 27    | `segundos_a_horas(segundos)` | Convierte segundos a horas |
| 32    | `tabla_multiplicar(numero)` | Imprime la tabla del número |
| 37    | `operaciones_basicas(a, b)` | Devuelve suma, resta, multiplicación y división |
| 41    | `calcular_imc(peso, altura)` | Índice de masa corporal con 2 decimales |
| 45    | `celsius_a_fahrenheit(celsius)` | Conversión de temperatura |
| 49    | `calcular_promedio(a, b, c)` | Promedio de 3 valores |
| 53    | `validar_nombre(texto)` | Verifica si un nombre es válido |
| 56    | `input_nombre(mensaje)` | Solicita un nombre y lo valida |
| 63    | `input_numero(mensaje, tipo)` | Solicita un número y valida errores |

---

## 💡 Palabras clave y conceptos utilizados

- `def`: para definir funciones reutilizables
- `isalpha()`: validación para que los nombres solo tengan letras
- `strip()`: remueve espacios en blanco
- `try / except`: manejo de errores para entradas numéricas
- `exit()`: para finalizar el programa si la edad es menor a la permitida
- `round()`: para redondear resultados numéricos
- `if / else`: estructuras de control

---

## 📦 Estructura del proyecto

05 Funciones/
├── Funciones.py # Código principal del trabajo práctico
└── README.md # Documentación del proyecto



---

## 📌 Requisitos

- Python 3.x
- Editor de texto o entorno como VSCode, PyCharm o Thonny
- Consola o terminal para ejecutar el programa

---

## 🧪 Ejemplo de flujo

**Entrada válida:**

Nombre: Sofía
Apellido: Gómez
Edad: 20
Residencia: Mendoza

**Entrada inválida:**

Nombre: @nita
❌ Solo se aceptan letras. Mínimo 3 caracteres, sin espacios vacíos ni símbolos.
Edad: 15
⚠️ Tenés que tener al menos 16 años para continuar.


---

## 📖 Metodología y aprendizaje

Este trabajo lo realicé **de forma individual**, resolviendo paso a paso cada punto de la consigna y aplicando funciones para dividir la lógica del programa. Me enfoqué especialmente en que el código fuera claro, reutilizable y robusto ante errores del usuario.

Fue una excelente forma de practicar:
- El diseño de funciones
- El uso de condicionales
- Validaciones de entrada
- Flujo lógico de ejecución

---

## 🙌 Créditos

Proyecto realizado por **Ana Sofía Zeballos**  
Comisión: **5**  
Trabajo práctico de **Programación I - UTN TUPaD**  
Tema: Aplicación de funciones y estructuras de control en Python

---



