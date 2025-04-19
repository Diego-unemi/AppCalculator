import customtkinter as ctk
from core.grafica3d import plot_3d_function

def setup_plot3d_tab(app):
    tab = app.tabview.tab("Gráfica 3D")
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure((0, 1), weight=1)

    frame = ctk.CTkFrame(tab, corner_radius=10)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
    frame.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(frame, text="f(x, y) =").grid(row=0, column=0, padx=10, pady=5)
    app.func3d_entry = ctk.CTkEntry(frame, width=300)
    app.func3d_entry.grid(row=0, column=1, padx=10, pady=5)
    app.func3d_entry.insert(0, "sin(sqrt(x**2 + y**2))")

    ctk.CTkButton(frame, text="Graficar", command=lambda: plot_3d_function(app)).grid(row=1, column=0, columnspan=2, pady=10)

    app.plot3d_frame = ctk.CTkFrame(tab, corner_radius=10)
    app.plot3d_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
