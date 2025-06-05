# Proyecto: Aplicación de Conjuntos y Lógica con Tkinter

## Integrantes del grupo

* **Ana Sofía Zeballos** - DNI: 43964446, comisión 5
* **Carlos Bruno Fernández Paolini** - DNI: 38246227, comisión 25

## Descripción general

Este proyecto se divide en dos partes principales:

### Parte 1 – Desarrollo Matemático (entregado en PDF)

Esta parte tiene cinco consignas:

1. Cada integrante debe anotar su número de DNI.
2. A partir de los DNIs, se deben formar tantos conjuntos de dígitos únicos como integrantes tenga el grupo.
3. Realizar entre esos conjuntos las siguientes operaciones: unión, intersección, diferencia (entre pares) y diferencia simétrica.
4. Para cada una de estas operaciones, se debe realizar un diagrama de Venn (a mano o digital).
5. Redactar al menos dos expresiones lógicas en lenguaje natural que puedan luego implementarse en Python.

**Responsabilidades:**

* El compañero se encargó de las consignas 1, 2, 3 y 5.
* **Ana Sofía Zeballos** fue responsable exclusivamente de la consigna 4: realización de los **diagramas de Venn** en formato digital utilizando **Figma** y finalmente incluído en el PDF.

### Parte 2 – Desarrollo del Programa en Python (archivo .py)

Esta parte consta de dos secciones:

#### A. Operaciones con DNIs

* Ingreso de los DNIs (reales o ficticios).
* Generación automática de los conjuntos de dígitos únicos.
* Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
* Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
* Suma total de los dígitos de cada DNI.
* Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.

#### B. Operaciones con años de nacimiento

* Ingreso de los años de nacimiento.
* Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
* Si todos nacieron después del 2000, mostrar "Grupo Z".
* Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
* Implementar una función para determinar si un año es bisiesto.
* Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

## Desarrollo hasta la línea 98: Ana Sofía Zeballos

Yo, **Ana Sofía Zeballos**, fui la encargada de desarrollar la lógica funcional hasta la línea 98 del código, que abarca principalmente la **parte A** del desarrollo en Python. Esto incluye:

### Desarrollo realizado:

* **Líneas 7 a 15:** Ingreso de los DNIs y definición de datos iniciales.
* **Líneas 20 a 30:** Funciones para calcular frecuencia y suma total de dígitos.
* **Línea 32:** Función auxiliar para detectar años bisiestos (es\_bisiesto).
* **Líneas 34 a 50:** Visualización de los conjuntos en Tkinter.
* **Líneas 52 a 63:** Lógica para las operaciones entre conjuntos (unión, intersección, diferencia y diferencia simétrica).
* **Línea 65 en adelante:** Evaluación lógica de las condiciones propuestas.

## Diagramas de Venn

También fui responsable de realizar los **diagramas de Venn** correspondientes a cada operación:

* Unión (A ∪ B)
* Intersección (A ∩ B)
* Diferencia (A - B y B - A)
* Diferencia Simétrica (A ∆ B)

Estos diagramas se realizaron digitalmente con **Figma** y se basaron en los datos obtenidos a partir de los DNIs:

* A = (DNI de Ana Sofía)
* B = (DNI de Carlos Bruno)

## Expresiones lógicas redactadas e implementadas

1. **Si todos los conjuntos tienen al menos 5 elementos, entonces se considera que hay una alta diversidad numérica.**

   * Implementada en `evaluar_expresiones_logicas()` mediante `if len(A) >= 5 and len(B) >= 5:`

2. **Si algún dígito aparece en todos los conjuntos, se marca como dígito común.**

   * Implementada mediante `digitos_comunes = A & B`

3. **Si ningún conjunto tiene el número 0, se considera un grupo sin ceros.**

   * No implementada directamente pero fácilmente integrable con: `if '0' not in A and '0' not in B:`

4. **Si la intersección entre todos los conjuntos tiene exactamente un elemento, se considera un dígito representativo del grupo.**

   * También integrable mediante `if len(A & B) == 1:`

5. **Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces se etiqueta como "grupo par".**

   * No implementada, pero puede incorporarse.

## Código a partir de la línea 99

Desde la línea 99 en adelante, el código fue desarrollado por mi compañero. Él incorporó toda la lógica correspondiente a la **parte B**:

* Evaluación de años de nacimiento (pares/impares).
* Análisis del Grupo Z.
* Detección de años bisiestos.
* Cálculo del producto cartesiano entre años y edades.


## Desarrollo realizado por el compañero:

* **Líneas 100 a 119**: Interfaz gráfica para análisis de años de nacimiento y su integración en el flujo general.

* **Líneas 120 a 150**: Evaluación de años pares e impares, verificación de "Grupo Z", detección de años bisiestos.

* **Líneas 151 a 160**: Cálculo del producto cartesiano entre años y edades actuales.

## Conclusión

Este proyecto integró correctamente teoría matemática de conjuntos con estructuras lógicas programadas en Python, presentadas en una interfaz visual construida con Tkinter. Logramos aplicar operaciones, analizar propiedades y desarrollar visualizaciones claras como los diagramas de Venn para acompañar el informe matemático.

El trabajo en equipo y la distribución de tareas fueron claves para cumplir todas las consignas y alcanzar un resultado profesional, claro y funcional.
