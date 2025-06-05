import tkinter as tk
from tkinter import messagebox
from collections import Counter
import datetime
import itertools

# DNIs fijos de los integrantes del grupo
dni1 = "43964446"
dni2 = "38246227"

# Años de nacimiento de los integrantes
datos_integrantes = [
    {"nombre": "Integrante 1", "dni": dni1, "anio": 2001},
    {"nombre": "Integrante 2", "dni": dni2, "anio": 1994}
]

# Extrae los dígitos únicos del DNI
def extraer_digitos_unicos(dni):
    return set(dni)

def contar_frecuencia(dni):
    return Counter(dni)

def suma_digitos(dni):
    return sum(int(d) for d in dni)

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def mostrar_conjuntos():
    global A, B
    A = extraer_digitos_unicos(dni1)
    B = extraer_digitos_unicos(dni2)

    txt_conjuntos.delete("1.0", tk.END)
    for integrante in datos_integrantes:
        txt_conjuntos.insert(tk.END, f"\n• {integrante['nombre']} (DNI: {integrante['dni']}, Año de nacimiento: {integrante['anio']})\n")
        conjunto = extraer_digitos_unicos(integrante['dni'])
        frecuencia = dict(contar_frecuencia(integrante['dni']))
        suma = suma_digitos(integrante['dni'])
        txt_conjuntos.insert(tk.END, f"Conjunto: {sorted(conjunto)}\nFrecuencia: {frecuencia}\nSuma total de dígitos: {suma}\n\n")

    evaluar_anios_nacimiento()
    evaluar_expresiones_logicas()

def operar_conjuntos(op):
    if A is None or B is None:
        messagebox.showwarning("Aviso", "Primero debes generar los conjuntos")
        return

    resultado = ""
    if op == "union":
        resultado = f"A ∪ B = {sorted(A | B)}"
    elif op == "interseccion":
        resultado = f"A ∩ B = {sorted(A & B)}"
    elif op == "diferencia":
        resultado = f"A - B = {sorted(A - B)}\nB - A = {sorted(B - A)}"
    elif op == "simetrica":
        resultado = f"A ∆ B = {sorted(A ^ B)}"

    txt_resultado.delete("1.0", tk.END)
    txt_resultado.insert(tk.END, resultado)

def evaluar_anios_nacimiento():
    txt_anios.delete("1.0", tk.END)
    txt_anios.insert(tk.END, "\n--- Análisis de años de nacimiento ---\n")

    anos = [p['anio'] for p in datos_integrantes]
    pares = [p for p in datos_integrantes if p['anio'] % 2 == 0]
    impares = [p for p in datos_integrantes if p['anio'] % 2 != 0]

    txt_anios.insert(tk.END, f"Cantidad que nacieron en años pares: {len(pares)}\n")
    for p in pares:
        txt_anios.insert(tk.END, f"{p['nombre']} nació en un año par.\n")

    txt_anios.insert(tk.END, f"Cantidad que nacieron en años impares: {len(impares)}\n")
    for p in impares:
        txt_anios.insert(tk.END, f"{p['nombre']} nació en un año impar.\n")

    if all(p['anio'] > 2000 for p in datos_integrantes):
        txt_anios.insert(tk.END, "Grupo Z (todos nacieron después del 2000).\n")
    else:
        for p in datos_integrantes:
            if p['anio'] > 2000:
                txt_anios.insert(tk.END, f"{p['nombre']} pertenece al Grupo Z.\n")

    bisiestos = [(p['nombre'], p['anio']) for p in datos_integrantes if es_bisiesto(p['anio'])]
    if bisiestos:
        txt_anios.insert(tk.END, "Tenemos un año especial:\n")
        for nombre, anio in bisiestos:
            txt_anios.insert(tk.END, f"- {nombre} nació en el año bisiesto {anio}.\n")
    else:
        txt_anios.insert(tk.END, "Ninguno de los dos años coincide con un año bisiesto.\n")

    anio_actual = datetime.datetime.now().year
    edades = [anio_actual - a for a in anos]
    producto_cartesiano = list(itertools.product(anos, edades))
    txt_anios.insert(tk.END, f"Producto cartesiano (año, edad): {producto_cartesiano}\n")


def evaluar_expresiones_logicas():
    log_txt.delete("1.0", tk.END)

    if len(A) >= 5 and len(B) >= 5:
        log_txt.insert(tk.END, "Alta diversidad numérica detectada (ambos conjuntos tienen al menos 5 elementos).\n")
    else:
        log_txt.insert(tk.END, "Diversidad numérica insuficiente.\n")

    digitos_comunes = A & B
    if digitos_comunes:
        log_txt.insert(tk.END, f"Dígito(s) compartido(s): {sorted(digitos_comunes)}\n")
    else:
        log_txt.insert(tk.END, "No hay dígitos compartidos entre A y B.\n")

# Ventana principal
root = tk.Tk()
root.title("Proyecto Conjuntos y Lógica - Tkinter")
root.geometry("720x730")
root.configure(bg="#C6FAF6")

A = B = None

lbl_info = tk.Label(root, text="Dígitos únicos generados automáticamente a partir de los DNIs del grupo:", font=("Arial", 12, "bold"), bg="#C6FAF6")
lbl_info.pack(pady=10)

style = {"font": ("Arial", 10, "bold"), "bg": "#009999", "fg": "white", "bd": 0, "activebackground": "#007f7f", "activeforeground": "white"}

btn_generar = tk.Button(root, text="Generar conjuntos", command=mostrar_conjuntos, **style)
btn_generar.pack(pady=5, ipadx=15, ipady=5)

txt_conjuntos = tk.Text(root, height=10, width=80, bg="white", font=("Consolas", 10))
txt_conjuntos.pack(pady=5)

frame_botones = tk.Frame(root, bg="#C6FAF6")
frame_botones.pack(pady=5)

button_opts = {"font": ("Arial", 10, "bold"), "bg": "#009999", "fg": "white", "bd": 0, "activebackground": "#007f7f", "activeforeground": "white"}

btn_union = tk.Button(frame_botones, text="Unión", command=lambda: operar_conjuntos("union"), **button_opts)
btn_inter = tk.Button(frame_botones, text="Intersección", command=lambda: operar_conjuntos("interseccion"), **button_opts)
btn_dif = tk.Button(frame_botones, text="Diferencia", command=lambda: operar_conjuntos("diferencia"), **button_opts)
btn_sim = tk.Button(frame_botones, text="Diferencia Simétrica", command=lambda: operar_conjuntos("simetrica"), **button_opts)

for i, btn in enumerate([btn_union, btn_inter, btn_dif, btn_sim]):
    btn.grid(row=0, column=i, padx=5, ipadx=10, ipady=5)

txt_resultado = tk.Text(root, height=6, width=80, bg="white", font=("Consolas", 10))
txt_resultado.pack(pady=5)

anio_label = tk.Label(root, text="Análisis de años de nacimiento:", font=("Arial", 10, "bold"), bg="#C6FAF6")
anio_label.pack()

txt_anios = tk.Text(root, height=10, width=80, bg="white", font=("Consolas", 10))
txt_anios.pack(pady=5)

log_label = tk.Label(root, text="Evaluación lógica automática:", font=("Arial", 10, "bold"), bg="#C6FAF6")
log_label.pack()

log_txt = tk.Text(root, height=6, width=80, fg="darkgreen", bg="white", font=("Consolas", 10))
log_txt.pack(pady=5)

root.mainloop()
