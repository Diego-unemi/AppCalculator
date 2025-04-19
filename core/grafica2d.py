import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox as mb
import re
def limpiar_expr(func_str):
    expr = func_str.replace("^", "**")
    expr = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", expr)         # 2x → 2*x, 3sin(x) → 3*sin(x)
    expr = re.sub(r"([a-zA-Z\)])(\()", r"\1*(", expr)         # x(y+1) → x*(y+1), sin(x)(cos(x)) → sin(x)*cos(x)
    expr = re.sub(r"(\))([a-zA-Z\(])", r"\1*\2", expr)        # (x+1)sin(x) → (x+1)*sin(x)
    expr = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", expr)          # x2 → x*2 (poco común pero válido)
    return expr
def plot_2d_function(app):
    for widget in app.plot2d_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(5, 4))
    try:

        x_vals = np.linspace(-10, 10, 400)
        func_str = app.func2d_entry.get()
        func_str = limpiar_expr(func_str)
        y_vals = [eval(func_str, {"x": x, **math.__dict__, **np.__dict__}) for x in x_vals]
        ax.plot(x_vals, y_vals)
        ax.grid(True)
        ax.set_title(f"f(x) = {func_str}")

        canvas = FigureCanvasTkAgg(fig, master=app.plot2d_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    except Exception as e:
        mb.showerror("Error", f"No se pudo graficar: {e}")
