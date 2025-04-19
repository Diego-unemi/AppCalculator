import customtkinter as ctk
import tkinter.messagebox as mb
from core.sistema_ecuaciones import resolver_sistema

def setup_sistema_tab(app):
    tab = app.tabview.tab("Sistema Ecuaciones")
    tab.grid_columnconfigure((0,1,2), weight=1)
    tab.grid_rowconfigure((0,1,2,3), weight=1)

    ctrl = ctk.CTkFrame(tab, corner_radius=10)
    ctrl.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
    for i in range(3): ctrl.grid_columnconfigure(i, weight=1)

    vals = [str(i) for i in range(1,7)]
    app.sys_size = ctk.CTkOptionMenu(ctrl, values=vals, width=60, command=lambda _: draw_system(app))
    app.sys_size.set("3")
    ctk.CTkLabel(ctrl, text="Variables (n):").grid(row=0, column=0)
    app.sys_size.grid(row=0, column=1)
    ctk.CTkButton(ctrl, text="Actualizar", command=lambda: draw_system(app)).grid(row=0, column=2)

    cont = ctk.CTkFrame(tab, corner_radius=10)
    cont.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
    cont.grid_columnconfigure((0,2), weight=1)
    cont.grid_columnconfigure(1, weight=0)
    cont.grid_rowconfigure(0, weight=1)

    app.sys_frameA = ctk.CTkFrame(cont, corner_radius=10)
    app.sys_frameA.grid(row=0, column=0, sticky="nsew", padx=(10,5))
    app.sys_frameB = ctk.CTkFrame(cont, corner_radius=10)
    app.sys_frameB.grid(row=0, column=2, sticky="nsew", padx=(5,10))

    ctk.CTkButton(tab, text="Resolver Sistema", command=lambda: solve_system(app)).grid(row=2, column=1, pady=10)

    app.sys_res = ctk.CTkFrame(tab, corner_radius=10)
    app.sys_res.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=(0,10))

    draw_system(app)

def draw_system(app):
    for f in (app.sys_frameA, app.sys_frameB, app.sys_res):
        for w in f.winfo_children(): w.destroy()

    n = int(app.sys_size.get())
    app.sys_A = []
    app.sys_B = []

    for i in range(n):
        app.sys_frameA.grid_rowconfigure(i, weight=1)
        for j in range(n):
            app.sys_frameA.grid_columnconfigure(j, weight=1)
            e = ctk.CTkEntry(app.sys_frameA, width=60, height=40, justify='center')
            e.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
            e.insert(0, '0')
            app.sys_A.append(e)

    for i in range(n):
        app.sys_frameB.grid_rowconfigure(i, weight=1)
        e = ctk.CTkEntry(app.sys_frameB, width=60, height=40, justify='center')
        e.grid(row=i, column=0, padx=4, pady=4, sticky='nsew')
        e.insert(0, '0')
        app.sys_B.append(e)

def solve_system(app):
    n = int(app.sys_size.get())
    try:
        A_vals = [float(e.get()) for e in app.sys_A]
        B_vals = [float(e.get()) for e in app.sys_B]
        X = resolver_sistema(A_vals, B_vals, n)
    except ValueError as e:
        mb.showerror("Error", str(e))
        return

    for i in range(n): app.sys_res.grid_rowconfigure(i, weight=1)
    app.sys_res.grid_columnconfigure(0, weight=1)
    for w in app.sys_res.winfo_children(): w.destroy()

    for i, val in enumerate(X):
        lbl = ctk.CTkLabel(app.sys_res, text=f"x{i+1} = {round(val, 4)}", justify='center')
        lbl.grid(row=i, column=0, sticky='nsew', padx=5, pady=5)
