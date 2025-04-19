import customtkinter as ctk
from core.ecuaciones import update_eq_ui, solve_equation

def setup_equations_tab(app):
    tab = app.tabview.tab("Ecuaciones")
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure((0, 1), weight=1)

    frame = ctk.CTkFrame(tab, corner_radius=10)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
    frame.grid_columnconfigure((1, 2, 3), weight=1)

    types = ["Lineal", "Cuadrática"]
    app.eq_type = ctk.CTkOptionMenu(
        frame,
        values=types,
        command=lambda choice: update_eq_ui(app, choice),
        width=100
    )
    app.eq_type.set("Lineal")
    ctk.CTkLabel(frame, text="Tipo:").grid(row=0, column=0, padx=(10, 5), pady=5)
    app.eq_type.grid(row=0, column=1, pady=5)

    app.coef_frame = ctk.CTkFrame(frame)
    app.coef_frame.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky="ew")

    ctk.CTkButton(frame, text="Resolver", command=lambda: solve_equation(app)).grid(
        row=2, column=0, columnspan=4, pady=(5, 10)
    )

    app.eq_res_frame = ctk.CTkFrame(tab, corner_radius=10)
    app.eq_res_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))

    update_eq_ui(app, "Lineal")
