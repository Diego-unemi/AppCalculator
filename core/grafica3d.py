import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox as mb
import re
def limpiar_expr(expr_raw):
    expr = expr_raw.replace("^", "**")
    expr = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", expr)         # 2x → 2*x, 3sin(x) → 3*sin(x)
    expr = re.sub(r"([a-zA-Z\)])(\()", r"\1*(", expr)         # x(y+1) → x*(y+1), sin(x)(cos(x)) → sin(x)*cos(x)
    expr = re.sub(r"(\))([a-zA-Z\(])", r"\1*\2", expr)        # (x+1)sin(x) → (x+1)*sin(x)
    expr = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", expr)          # x2 → x*2 (poco común pero válido)
    return expr
def plot_3d_function(app):
    for widget in app.plot3d_frame.winfo_children():
        widget.destroy()

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')

    try:
        x = y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        func_str = app.func3d_entry.get()
        func_str = limpiar_expr(func_str)
        Z = eval(func_str, {"x": X, "y": Y, **math.__dict__, **np.__dict__})
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title(f"f(x, y) = {func_str}")

        canvas = FigureCanvasTkAgg(fig, master=app.plot3d_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    except Exception as e:
        mb.showerror("Error", f"No se pudo graficar: {e}")
