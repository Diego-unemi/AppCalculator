import customtkinter as ctk
from core.grafica2d import plot_2d_function
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def setup_plot2d_tab(app):
    tab = app.tabview.tab("Gráfica 2D")
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure((0, 1), weight=1)

    frame = ctk.CTkFrame(tab, corner_radius=10)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
    frame.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(frame, text="f(x) =").grid(row=0, column=0, padx=10, pady=5)
    app.func2d_entry = ctk.CTkEntry(frame, width=300)
    app.func2d_entry.grid(row=0, column=1, padx=10, pady=5)
    app.func2d_entry.insert(0, "sin(x)")

    ctk.CTkButton(frame, text="Graficar", command=lambda: plot_2d_function(app)).grid(row=1, column=0, columnspan=2, pady=10)

    app.plot2d_frame = ctk.CTkFrame(tab, corner_radius=10)
    app.plot2d_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
