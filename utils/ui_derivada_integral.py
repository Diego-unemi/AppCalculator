import customtkinter as ctk
from core.derivada_integrales import derivar_funcion, integrar_funcion

def setup_symbolic_tab(app):
    tab = app.tabview.tab("Derivación/Integración")
    tab.grid_columnconfigure(0, weight=1)

    frame = ctk.CTkFrame(tab, corner_radius=10)
    frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    frame.grid_columnconfigure(1, weight=1)

    # Entrada de función con sugerencia clara
    ctk.CTkLabel(frame, text="f(x) =").grid(row=0, column=0, padx=10, pady=5)
    app.expr_entry = ctk.CTkEntry(frame, width=300, placeholder_text="Ej: x^2 + sin(x)")
    app.expr_entry.grid(row=0, column=1, padx=10, pady=5)

    # Variable con sugerencia
    ctk.CTkLabel(frame, text="Variable:").grid(row=1, column=0, padx=10, pady=5)
    app.var_entry = ctk.CTkEntry(frame, width=100, placeholder_text="x")
    app.var_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    # Límites de integral
    ctk.CTkLabel(frame, text="Límite inferior:").grid(row=2, column=0, padx=10, pady=5)
    app.lower_limit = ctk.CTkEntry(frame, width=100, placeholder_text="opcional")
    app.lower_limit.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    ctk.CTkLabel(frame, text="Límite superior:").grid(row=3, column=0, padx=10, pady=5)
    app.upper_limit = ctk.CTkEntry(frame, width=100, placeholder_text="opcional")
    app.upper_limit.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    # Botones
    btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
    btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

    ctk.CTkButton(btn_frame, text="Derivar", command=lambda: derivar_funcion(app)).pack(side="left", padx=10)
    ctk.CTkButton(btn_frame, text="Integrar", command=lambda: integrar_funcion(app)).pack(side="left", padx=10)

    # Resultado
    app.result_box = ctk.CTkTextbox(tab, height=150, wrap="word")
    app.result_box.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
    app.result_box.insert("1.0", "Resultado aparecerá aquí...")
    app.result_box.configure(state="disabled")
