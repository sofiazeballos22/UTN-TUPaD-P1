import tkinter as tk
from tkinter import messagebox

productos = [
    {"title": "Hamburguesa con queso", "price": 1500, "stock": 10, "descuento": 15},
    {"title": "Ensalada César", "price": 1300, "stock": 0, "descuento": 0},
    {"title": "Pizza napolitana", "price": 1800, "stock": 3, "descuento": 10},
    {"title": "Empanadas de carne", "price": 1200, "stock": 15, "descuento": 0},
    {"title": "Tarta de verduras", "price": 1100, "stock": 5, "descuento": 5},
]

def buscar_productos_start(productos, termino):
    if not termino.isalpha():
        messagebox.showwarning("Entrada inválida", "⚠️ El término debe contener solo letras.")
        return []

    resultados = [
        p for p in productos
        if any(palabra.lower().startswith(termino.lower()) for palabra in p["title"].split())
    ]
    return resultados

def mostrar_resultados():
    termino = entry.get().strip()
    resultados = buscar_productos_start(productos, termino)

    output.delete("1.0", tk.END)
    if not resultados:
        output.insert(tk.END, "❌ No se encontraron productos que coincidan con el término buscado.\n")
    else:
        for p in resultados:
            output.insert(tk.END, f"- {p['title']}\n")
            output.insert(tk.END, f"  Precio: ${p['price']}\n")
            if p["descuento"] > 0:
                output.insert(tk.END, f"  Descuento: {p['descuento']}%\n")
            if p["stock"] <= 0:
                output.insert(tk.END, "  Sin stock ❌\n")
            else:
                output.insert(tk.END, f"  Stock: {p['stock']} unidades\n")
            output.insert(tk.END, "\n")

# Interfaz gráfica
root = tk.Tk()
root.title("Buscador de productos")
root.geometry("500x400")

label = tk.Label(root, text="Ingrese un término de búsqueda:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="Buscar", command=mostrar_resultados)
btn.pack(pady=5)

output = tk.Text(root, height=15, width=60)
output.pack(pady=10)

root.mainloop()