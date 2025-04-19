import customtkinter as ctk
from core import matrices as m

def setup_matrices_tab(app):
    tab = app.tabview.tab("Matrices")
    tab.grid_columnconfigure((0, 1, 2), weight=1)
    tab.grid_rowconfigure((0, 1, 2, 3), weight=1)

    # Controles de dimensiones
    ctrl = ctk.CTkFrame(tab, corner_radius=10)
    ctrl.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
    for i in range(8):
        ctrl.grid_columnconfigure(i, weight=1)

    vals = [str(i) for i in range(1, 11)]
    app.dimA_rows = ctk.CTkOptionMenu(ctrl, values=vals, command=lambda _: draw_matrices(app), width=70)
    app.dimA_cols = ctk.CTkOptionMenu(ctrl, values=vals, command=lambda _: draw_matrices(app), width=70)
    app.dimB_rows = ctk.CTkOptionMenu(ctrl, values=vals, command=lambda _: draw_matrices(app), width=70)
    app.dimB_cols = ctk.CTkOptionMenu(ctrl, values=vals, command=lambda _: draw_matrices(app), width=70)
    for o in (app.dimA_rows, app.dimA_cols, app.dimB_rows, app.dimB_cols):
        o.set("3")

    labels = ["A filas", "A cols", "B filas", "B cols"]
    widgets = [app.dimA_rows, app.dimA_cols, app.dimB_rows, app.dimB_cols]
    for idx, (lab, widget) in enumerate(zip(labels, widgets)):
        ctk.CTkLabel(ctrl, text=lab).grid(row=0, column=2 * idx)
        widget.grid(row=0, column=2 * idx + 1)

    # Marcos matrices
    middle = ctk.CTkFrame(tab, corner_radius=10)
    middle.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
    middle.grid_columnconfigure((0, 2), weight=1)
    middle.grid_rowconfigure(0, weight=1)

    app.frameA = ctk.CTkFrame(middle, corner_radius=10)
    app.frameA.grid(row=0, column=0, sticky="nsew", padx=(10, 5))
    app.frameB = ctk.CTkFrame(middle, corner_radius=10)
    app.frameB.grid(row=0, column=2, sticky="nsew", padx=(5, 10))

    # Botones
    ops = ctk.CTkFrame(tab, corner_radius=10)
    ops.grid(row=2, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
    for i in range(4): ops.grid_columnconfigure(i, weight=1)

    btns = [
        ("Aleatorio", lambda: fill_all(app, 'random')),
        ("Ceros", lambda: fill_all(app, 'zeros')),
        ("Unos", lambda: fill_all(app, 'ones')),
        ("Det A", lambda: show_result(app, [[m.determinant(m.get_matrix(app.matA_entries))]])),
        ("Inv A", lambda: show_result(app, m.inverse(m.get_matrix(app.matA_entries)))),
        ("A + B", lambda: show_result(app, m.add_matrices(m.get_matrix(app.matA_entries), m.get_matrix(app.matB_entries)))),
        ("A - B", lambda: show_result(app, m.subtract_matrices(m.get_matrix(app.matA_entries), m.get_matrix(app.matB_entries)))),
        ("A × B", lambda: show_result(app, m.multiply_matrices(m.get_matrix(app.matA_entries), m.get_matrix(app.matB_entries)))),
    ]

    for idx, (lab, cmd) in enumerate(btns):
        row = 0 if idx < 4 else 1
        col = idx % 4
        ctk.CTkButton(ops, text=lab, command=cmd, width=100, height=30).grid(row=row, column=col, padx=5, pady=5)

    app.res_frame = ctk.CTkFrame(tab, corner_radius=10)
    app.res_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=(0, 10))

    draw_matrices(app)


def draw_matrices(app):
    for f in (app.frameA, app.frameB, app.res_frame):
        for w in f.winfo_children():
            w.destroy()

    rA, cA = int(app.dimA_rows.get()), int(app.dimA_cols.get())
    app.matA_entries = []
    for i in range(rA):
        app.frameA.grid_rowconfigure(i, weight=1)
        row = []
        for j in range(cA):
            app.frameA.grid_columnconfigure(j, weight=1)
            e = ctk.CTkEntry(app.frameA, width=60, height=40, justify='center')
            e.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
            row.append(e)
        app.matA_entries.append(row)

    rB, cB = int(app.dimB_rows.get()), int(app.dimB_cols.get())
    app.matB_entries = []
    for i in range(rB):
        app.frameB.grid_rowconfigure(i, weight=1)
        row = []
        for j in range(cB):
            app.frameB.grid_columnconfigure(j, weight=1)
            e = ctk.CTkEntry(app.frameB, width=60, height=40, justify='center')
            e.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
            row.append(e)
        app.matB_entries.append(row)


def fill_all(app, mode):
    for entries in (app.matA_entries, app.matB_entries):
        m.fill_matrix(entries, mode)

def show_result(app, mat):
    for w in app.res_frame.winfo_children():
        w.destroy()
    sub = ctk.CTkFrame(app.res_frame)
    sub.place(relx=0.5, rely=0.5, anchor='center')
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            ctk.CTkLabel(sub, text=str(int(val)), width=60, height=40, justify='center').grid(row=i, column=j, padx=4, pady=4)
