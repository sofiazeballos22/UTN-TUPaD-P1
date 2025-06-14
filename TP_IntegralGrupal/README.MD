# 🔍 Buscador de Productos con Tkinter

Este proyecto desarrollado en grupo, forma parte del trabajo práctico de Programación I en la UTN - TUPaD.  
El objetivo es aplicar estructuras condicionales, listas, funciones y métodos en Python para crear una **interfaz gráfica que permita buscar productos por su nombre**.

---


Link de mi Drive: [https://drive.google.com/drive/folders/1j6iQXrM5g1laj9iuZQ-Mkw6JpJ1fNPAl?usp=sharing]


--

## 🎯 Descripción

El programa permite al usuario ingresar un término (por ejemplo, "Pizza" o "Empanadas") y luego busca en una lista predefinida de productos todos aquellos que comienzan con ese término.  
Si encuentra coincidencias, muestra los detalles: nombre, precio, stock y descuento si lo hay.

---

## 🧠 Funcionalidades principales

- ✅ Búsqueda sensible a palabras que **empiecen** con el término ingresado
- 🔠 Validación de entrada: solo se aceptan **letras**
- 🚫 Muestra advertencias si la entrada es inválida o si no hay coincidencias
- 🧾 Muestra los productos encontrados con:
  - Precio
  - Stock
  - Descuento (si aplica)

---

## 🧩 Palabras clave, funciones y métodos utilizados

### 📚 Funciones y estructuras:
- `buscar_productos_start(productos, termino)`: función principal que filtra los productos.
- `mostrar_resultados()`: función que se ejecuta al presionar el botón "Buscar".
- `for` + `if`: para recorrer los productos y evaluar condiciones.

### 🧠 Métodos:
- `isalpha()`: verifica si la entrada del usuario contiene solo letras.
- `startswith()`: se utiliza para verificar si alguna palabra del título del producto **comienza** con el término buscado.
- `strip()`: limpia los espacios al inicio y final del texto ingresado.

### 💬 Funciones del módulo `tkinter.messagebox`:
- `messagebox.showwarning()`: muestra una ventana emergente si la entrada es inválida.

---

## 🖼️ Interfaz gráfica (Tkinter)

- `tk.Tk()`: crea la ventana principal.
- `tk.Label`, `tk.Entry`, `tk.Button`, `tk.Text`: componentes principales de la UI.
- `.pack()`: método para organizar visualmente los widgets en la ventana.
- `.get()` y `.delete()`: para obtener o limpiar el contenido de los campos.

---

## 📦 Estructura del proyecto

Tp_Intregador
│
├── buscador_productos.py # Código principal del buscador
└── README.md # Documentación del proyecto



---

## 📌 Requisitos

- Python 3.x
- Tkinter (incluido por defecto en Python)

---

## 🧪 Ejemplo de búsqueda válida

**Entrada**: `Pizza`  
**Resultado**:
Pizza napolitana
Precio: $1800
Descuento: 10%
Stock: 3 unidades


---

## 🚫 Ejemplo de búsqueda inválida

**Entrada**: `123pizza`

**Resultado**: Ventana emergente  
> ⚠️ El término debe contener solo letras.

---



## Metodología de estudio
La metodología que usamos fue grupal, aunque yo me encargué del desarrollo del buscador y parte de la documentación. El trabajo se dividió en una parte teórica, donde investigamos conceptos de búsqueda, ordenamiento y eficiencia algorítmica, y una parte práctica donde apliqué esos conceptos en Python usando la biblioteca tkinter. Consultamos bibliografía como Cormen y documentación oficial de Python. Elegí estos temas porque me parecieron los más aplicables al desarrollo real, como los filtros que usamos todos los días en apps. Fui documentando cada paso con ejemplos, justificaciones y pruebas funcionales.




## 🙌 Créditos

Proyecto realizado por **Ana Sofía Zeballos, comisión 5**  ,  **Carlos Bruno Fernández Paolini, comisión 25**   

Trabajo práctico de **Programación I - UTN TUPaD**  
Tema: Aplicación de funciones, métodos y estructuras condicionales en Python con Tkinter.
Eficiencia y Optimización de algoritmos 
