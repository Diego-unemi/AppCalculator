import customtkinter as ctk
import sympy as sp
from tkinter import messagebox as mb

def update_eq_ui(app, choice):
    for w in app.coef_frame.winfo_children():
        w.destroy()
    app.eq_entries = []

    if choice == "Lineal":
        labels = ["a", "b"]
        for idx, lab in enumerate(labels):
            ctk.CTkLabel(app.coef_frame, text=f"{lab}x " if idx == 0 else f"+ {lab}").grid(
                row=0, column=2 * idx
            )
            e = ctk.CTkEntry(app.coef_frame, width=60, justify="center")
            e.grid(row=0, column=2 * idx + 1, padx=2)
            e.insert(0, "0")
            app.eq_entries.append(e)
    else:
        labels = ["a", "b", "c"]
        for idx, lab in enumerate(labels):
            power = 2 - idx
            term = f"{lab}x^{power}" if power > 0 else lab
            ctk.CTkLabel(app.coef_frame, text=term).grid(row=0, column=2 * idx)
            e = ctk.CTkEntry(app.coef_frame, width=60, justify="center")
            e.grid(row=0, column=2 * idx + 1, padx=2)
            e.insert(0, "0")
            app.eq_entries.append(e)

def solve_equation(app):
    try:
        vals = [float(e.get()) for e in app.eq_entries]
        x = sp.symbols("x")
        if app.eq_type.get() == "Lineal":
            a, b = vals
            eq = sp.Eq(a * x + b, 0)
        else:
            a, b, c = vals
            eq = sp.Eq(a * x**2 + b * x + c, 0)
        sols = sp.solve(eq, x)
    except Exception as e:
        mb.showerror("Error", f"No se pudo resolver: {e}")
        return

    for w in app.eq_res_frame.winfo_children():
        w.destroy()

    ctk.CTkLabel(app.eq_res_frame, text=f"Ecuación: {sp.pretty(eq)}").pack(pady=5)
    if not sols:
        ctk.CTkLabel(app.eq_res_frame, text="Sin soluciones").pack(pady=5)
    else:
        for sol in sols:
            ctk.CTkLabel(app.eq_res_frame, text=f"x = {sp.N(sol)}").pack(pady=2)
