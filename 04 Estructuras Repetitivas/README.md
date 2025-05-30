# Ana Sofía Zeballos  
## UTN - TUPaD - Programación I  
### Trabajo Práctico Nº 4 - Estructuras Repetitivas

---

### 🔍 Descripción general

Este trabajo práctico se enfoca en el uso de **estructuras repetitivas** en Python, conocidas como bucles o ciclos (`while` y `for`).  
Estas estructuras son fundamentales cuando se deben realizar acciones múltiples veces, especialmente cuando **no se conoce de antemano cuántas veces** va a repetirse, como por ejemplo cuando el usuario debe ingresar una contraseña correctamente o interactuar con un formulario.
### 📘 ¿Qué es `range()` y por qué es importante?

`range()` es una función muy utilizada en Python que genera una secuencia de números.  
Es clave para trabajar con bucles `for`, permitiendo definir:
- Desde qué número empezar (`start`)
- Hasta cuál número llegar (`stop`)
- Y cada cuánto avanzar (`step`)
Ideal para recorrer listas, generar índices, crear secuencias automáticas, validar formularios repetidamente o ejecutar tareas programadas.

> 💡 Se trabajaron **10 consignas** en total, todas utilizando lógica iterativa y validación de entradas.


---

### ✅ Actividades incluidas

| N° | Actividad                                                                 |
|----|---------------------------------------------------------------------------|
| 1  | Mostrar los números del 0 al 100 con un bucle `for`.                     |
| 2  | Contar los dígitos de un número entero con validación.                   |
| 3  | Sumar los números entre dos valores ingresados (excluyendo los extremos).|
| 4  | Sumar números hasta que el usuario ingrese 0.                            |
| 5  | Imprimir los números pares desde 100 hasta 0 (decreciente).              |
| 6  | **Juego interactivo** que muestra botones con íconos y oculta un número aleatorio entre 0 y 9. Se contabilizan los intentos hasta encontrarlo. |
| 7  | Sumar todos los números desde 0 hasta uno ingresado por el usuario.      |
| 8  | Ingresar una lista de números y clasificar cuántos son pares, impares, positivos y negativos. |
| 9  | Calcular la media (promedio) de una lista de `n` números enteros ingresados. |
| 10 | Invertir los dígitos de un número de al menos 2 cifras (con validación). |

---

### 📁 Estructura de carpetas y archivos del proyecto

UTN-TUPaD-P1/
└── 04 Estructuras Repetitivas/
    ├── SZeballos_TP04.py # Actividades 1 a 5, 7 a 10
    ├── Juego.py # Actividad 6 (juego con GUI)
    └── README.md # Descripción del trabajo práctico



---

### 👩‍💻 Comentario final

Este trabajo permitió afianzar conceptos esenciales de programación como bucles, validación de entradas y lógica iterativa. Se aplicaron estructuras `while` y `for` y funciones como range...Se combinaron con condiciones, listas y manejo de errores.  
En la actividad 6 se implementó además una pequeña interfaz visual interactiva que simula un juego donde el usuario debe encontrar un número oculto, contabilizando la cantidad de intentos requeridos. El mismo se encuentra en el archivo "Juego.py"

---
