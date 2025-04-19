import customtkinter as ctk
import tkinter.messagebox as mb
from core.derivada_integrales import solve_derivative,solve_integral


def setup_symbolic_tab(app):
        tab = app.tabview.tab("Derivación/Integración")
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure((0, 1, 2), weight=1)

        frame = ctk.CTkFrame(tab, corner_radius=10)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="Expresión (en x):").grid(row=0, column=0, padx=10, pady=5)
        app.sym_entry = ctk.CTkEntry(frame, width=400)
        app.sym_entry.grid(row=0, column=1, padx=10, pady=5)
        app.sym_entry.insert(0, "x**2 + 3*x + 1")

        button_frame = ctk.CTkFrame(frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        ctk.CTkButton(button_frame, text="Derivar", command=lambda: solve_derivative(app)).grid(row=0, column=0, padx=10)
        ctk.CTkButton(button_frame, text="Integrar", command=lambda: solve_integral(app)).grid(row=0, column=1, padx=10)

        app.sym_result = ctk.CTkLabel(tab, text="Resultado:", font=ctk.CTkFont(size=16))
        app.sym_result.grid(row=1, column=0, pady=10)

import customtkinter as ctk
import sympy as sp
from tkinter import messagebox as mb

def solve_derivative(app):
        x = sp.symbols('x')
        expr_str = app.sym_entry.get()
        try:
            expr = sp.sympify(expr_str)
            deriv = sp.diff(expr, x)
            app.sym_result.configure(text=f"Derivada: {sp.simplify(deriv)}")
        except Exception as e:
            mb.showerror("Error", f"No se pudo derivar: {e}")

def solve_integral(app):
        x = sp.symbols('x')
        expr_str = app.sym_entry.get()
        try:
            expr = sp.sympify(expr_str)
            integ = sp.integrate(expr, x)
            app.sym_result.configure(text=f"Integral: {sp.simplify(integ)} + C")
        except Exception as e:
            mb.showerror("Error", f"No se pudo integrar: {e}")