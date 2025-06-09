# Trabajo Práctico Nº5 – Listas  
**Estudiante**: Ana Sofía Zeballos  
**Comisión**: Comisión 5 
**Carrera**: Tecnicatura Universitaria en Programación  
**Materia**: Programación 1  

---

## Archivo: listas.py  

### Actividad 1. Crear una lista con los números del 1 al 100 que sean múltiplos de 4.  
Se usó `range()` con paso de 4 y se convirtió en lista.  
```python
multiplos_de_4 = list(range(4, 101, 4))
Herramientas: range(), list(), print().


---

 Actividad 2. Crear una lista con los 5 elementos que más te gustan
    Lista con comidas favoritas y acceso al penúltimo valor usando indexación negativa.


    print("El penúltimo favorito es:", favoritos[-2])
    erramientas: listas, indexación negativa.

----


Actividad 3. Crear una lista vacía y agregarle tres palabras utilizando el método append.
Se utilizó append() tres veces.

palabras.append("python")
palabras.append("suprema")
palabras.append("tarta")
Herramientas: listas, método append().

----

Actividad 4. Reemplazar valores en una lista.
Se reemplazaron elementos por índice positivo y negativo.

animales[1] = "loro"
animales[-1] = "oso"
Herramientas: asignación por índice, print().

----

Actividad 6. Crear una lista del 10 al 30 con pasos de 5 y mostrar los dos primeros elementos.
Se generó una lista con range() y se accedió a índices 0 y 1.


numeros = list(range(10, 31, 5))
print("Primeros dos números:", numeros[0], numeros[1])
Herramientas: listas, range(), acceso por índice.

----

Actividad 7. Reemplazar valores en una lista de autos.
Se modificaron los elementos de las posiciones 1 y 2.


autos[1] = "camioneta"
autos[2] = "coupe"
Herramientas: listas, indexación.

----

Actividad 8. Crear una lista vacía y agregarle el doble de (5, 10, 15) como cadenas.
Se calcularon los dobles, se convirtieron a strings y se agregaron.

doble.append(str(5 * 2))
doble.append(str(10 * 2))
doble.append(str(15 * 2))
Herramientas: append(), str(), operaciones aritméticas.

----

Actividad 10. Crear una lista anidada con diferentes tipos de datos.
Lista que incluye un entero, booleanos y una lista de flotantes.


lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
Herramientas: listas anidadas, distintos tipos de datos.

Archivo: lista_de_compra.py
Este archivo contiene una simulación de compras de tres clientes utilizando listas anidadas. Se utiliza copy.deepcopy() para modificar la lista sin alterar la original, y tkinter para mostrar los datos gráficamente.

Modificaciones realizadas:
Se agregó "jugo" a la lista del tercer cliente.

Se reemplazó "fideos" por "tallarines" en el segundo cliente.

Se eliminó "pan" del primer cliente.

Código principal:

compras_original = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras_modificada = copy.deepcopy(compras_original)

compras_modificada[2].append("jugo")
indice_fideos = compras_modificada[1].index("fideos")
compras_modificada[1][indice_fideos] = "tallarines"
compras_modificada[0].remove("pan")
Herramientas utilizadas:
copy.deepcopy() para crear una copia segura sin modificar la original.

Métodos de lista: append(), remove(), index().

tkinter para crear la ventana gráfica con Text().

enumerate() y for para recorrer y mostrar los datos.

Interfaz gráfica:
Se creó una ventana con tkinter donde se imprimen la lista original y la modificada, utilizando un widget Text() y formato visual con emojis.


------



## Observación personal  ##

Este trabajo me ayudó a comprender en profundidad cómo funcionan las listas en Python, y cómo se pueden manipular de manera flexible y eficiente. A diferencia de otros lenguajes que he utilizado anteriormente, como HTML, donde para representar una lista había que escribir mucho código manualmente (por ejemplo, usar muchas etiquetas `<li>` dentro de `<ul>` o `<ol>`), en Python la estructura es mucho más simple, corta y poderosa. Esto es posible gracias a su capacidad de abstracción y a que es un lenguaje de programación orientado a objetos.

Una de las cosas que más destaco es el uso de métodos integrados como `append()`, `remove()` o `index()`, que permiten modificar y gestionar las listas de manera dinámica, algo que no se puede hacer en HTML, ya que este último no es un lenguaje de programación sino de marcado, y no tiene lógica de ejecución ni estructuras como listas en tiempo real.

También me pareció interesante poder trabajar con listas anidadas, ver cómo acceder a sus elementos y modificarlos, y cómo todo esto puede combinarse con estructuras visuales como interfaces gráficas en `tkinter`.
Este trabajo no solo me permitió aplicar conocimientos sobre indexación, acceso y modificación de listas, sino que me ayudó a entender cómo manejar estructuras de datos simples en Python de forma profesional y escalable. Comparado con mis experiencias anteriores, trabajar con listas en Python me pareció mucho más ordenado, limpio y adaptable a problemas reales.
