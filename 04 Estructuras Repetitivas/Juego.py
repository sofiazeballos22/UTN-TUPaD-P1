import tkinter as tk
import random
from tkinter import messagebox

# ————— Parámetros del tablero —————
ROWS, COLS = 7, 11
TOTAL_CELLS = ROWS * COLS


contents = list(range(10)) + ['bomb'] * (TOTAL_CELLS - 10)
random.shuffle(contents)

# Estado del juego
attempts = 0
game_active = True

def end_game(found_value):
    """Desactiva todo y cierra la ventana tras avisar."""
    global game_active
    game_active = False
    # Desactivar todos los botones
    for row in buttons:
        for btn in row:
            btn.config(state='disabled')
    # Mensaje final
    messagebox.showinfo(
        "¡Ganaste! 🎉",
        f"Encontraste el número {found_value} en {attempts} intentos."
    )
    root.destroy()

def on_click(r, c):
    global attempts
    if not game_active:
        return            # ya terminó, ignora clicks

    idx = r * COLS + c
    cell = contents[idx]
    btn  = buttons[r][c]

    # 1) Incrementar y mostrar intentos
    attempts += 1
    attempts_label.config(text=f"Intentos: {attempts}")

    # 2) Revelar y desactivar este botón
    btn.config(state='disabled', text='💣' if cell == 'bomb' else str(cell))

    # 3) Si es un número, termino el juego
    if cell != 'bomb':
        end_game(cell)

# ————— Construcción de la UI —————
root = tk.Tk()
root.title("Busca un número (0–9)")

attempts_label = tk.Label(root, text="Intentos: 0", font=("Arial", 14))
attempts_label.grid(row=0, column=0, columnspan=COLS, pady=(0,10))

buttons = []
for i in range(ROWS):
    row = []
    for j in range(COLS):
        btn = tk.Button(
            root,
            text='💣',
            width=4,
            height=2,
            command=lambda i=i, j=j: on_click(i, j)
        )
        btn.grid(row=i+1, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

root.mainloop()
