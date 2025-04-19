import customtkinter as ctk
import tkinter.messagebox as mb
from core import vectores as v

def setup_vectors_tab(app):
    tab = app.tabview.tab("Vectores")
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_rowconfigure((0, 1), weight=1)

    frame = ctk.CTkFrame(tab, corner_radius=10)
    frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    frame.grid_columnconfigure((0, 1), weight=1)

    ctk.CTkLabel(frame, text="Vector A (separado por comas)").grid(row=0, column=0, padx=10, pady=5)
    app.vecA_entry = ctk.CTkEntry(frame, width=300)
    app.vecA_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(frame, text="Vector B (separado por comas)").grid(row=1, column=0, padx=10, pady=5)
    app.vecB_entry = ctk.CTkEntry(frame, width=300)
    app.vecB_entry.grid(row=1, column=1, padx=10, pady=5)

    ops_frame = ctk.CTkFrame(frame)
    ops_frame.grid(row=2, column=0, columnspan=2, pady=10)
    
    ctk.CTkButton(ops_frame, text="A + B", command=lambda: calculate_vector(app, "add")).grid(row=0, column=0, padx=5)
    ctk.CTkButton(ops_frame, text="A - B", command=lambda: calculate_vector(app, "sub")).grid(row=0, column=1, padx=5)
    ctk.CTkButton(ops_frame, text="A · B", command=lambda: calculate_vector(app, "dot")).grid(row=0, column=2, padx=5)
    ctk.CTkButton(ops_frame, text="A × B", command=lambda: calculate_vector(app, "cross")).grid(row=0, column=3, padx=5)

    app.vec_result = ctk.CTkLabel(tab, text="Resultado:", font=ctk.CTkFont(size=16))
    app.vec_result.grid(row=1, column=0, pady=10)


def calculate_vector(app, operation):
    try:
        A = v.parse_vector(app.vecA_entry.get())
        B = v.parse_vector(app.vecB_entry.get())

        if operation == "add":
            result = v.add_vectors(A, B)
            label = "Resultado"
        elif operation == "sub":
            result = v.subtract_vectors(A, B)
            label = "Resultado"
        elif operation == "dot":
            result = v.dot_product(A, B)
            label = "Producto punto"
        elif operation == "cross":
            result = v.cross_product(A, B)
            label = "Producto cruz"
        else:
            raise ValueError("Operación no reconocida")

        app.vec_result.configure(text=f"{label}: {result}")

    except Exception as e:
        mb.showerror("Error", str(e))
