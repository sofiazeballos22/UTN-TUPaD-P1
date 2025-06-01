import tkinter as tk
import copy

# Lista original de compras
compras_original = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Hacemos una copia profunda para no modificar la original
compras_modificada = copy.deepcopy(compras_original)

# a) Agregar "jugo" al tercer cliente
compras_modificada[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
indice_fideos = compras_modificada[1].index("fideos")
compras_modificada[1][indice_fideos] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras_modificada[0].remove("pan")

# Crear ventana
ventana = tk.Tk()
ventana.title("Comparación: Lista Original vs Modificada")

# Crear widget de texto
texto = tk.Text(ventana, height=30, width=60)
texto.pack(padx=10, pady=10)

# Mostrar lista original
texto.insert(tk.END, "🟦 Lista original de compras:\n\n")
for i, cliente in enumerate(compras_original, start=1):
    texto.insert(tk.END, f"Cliente {i}: {cliente}\n")

# Separador
texto.insert(tk.END, "\n🔁 Modificaciones aplicadas...\n\n")

# Mostrar lista modificada
texto.insert(tk.END, "🟩 Lista modificada de compras:\n\n")
for i, cliente in enumerate(compras_modificada, start=1):
    texto.insert(tk.END, f"Cliente {i}: {cliente}\n")

# Ejecutar ventana
ventana.mainloop()
