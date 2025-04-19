import customtkinter as ctk
import numpy as np



def _setup_matrices_tab():
        tab = tabview.tab("Matrices")
        tab.grid_columnconfigure((0,1,2), weight=1)
        tab.grid_rowconfigure((0,1,2,3), weight=1)

        dims = ctk.CTkFrame(tab, corner_radius=10)
        dims.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
        for i in range(8): dims.grid_columnconfigure(i, weight=1)
        vals = [str(i) for i in range(1,11)]
        a_rows = ctk.CTkOptionMenu(dims, values=vals, command=lambda _: _draw_matrices(), width=60)
        a_cols = ctk.CTkOptionMenu(dims, values=vals, command=lambda _: _draw_matrices(), width=60)
        b_rows = ctk.CTkOptionMenu(dims, values=vals, command=lambda _: _draw_matrices(), width=60)
        b_cols = ctk.CTkOptionMenu(dims, values=vals, command=lambda _: _draw_matrices(), width=60)
        for o in (a_rows, a_cols, b_rows, b_cols): o.set("3")
        labels = ["A filas","A cols","B filas","B cols"]
        widgets = [a_rows, a_cols, b_rows, b_cols]
        for idx,(lab,widget) in enumerate(zip(labels, widgets)):
            ctk.CTkLabel(dims, text=lab).grid(row=0, column=2*idx)
            widget.grid(row=0, column=2*idx+1)

        cont = ctk.CTkFrame(tab, corner_radius=10)
        cont.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
        cont.grid_columnconfigure((0,2), weight=1)
        cont.grid_columnconfigure(1, weight=0)
        cont.grid_rowconfigure(0, weight=1)
        frameA = ctk.CTkFrame(cont, corner_radius=10)
        frameA.grid(row=0, column=0, sticky="nsew", padx=(10,5))
        frameB = ctk.CTkFrame(cont, corner_radius=10)
        frameB.grid(row=0, column=2, sticky="nsew", padx=(5,10))

        ops = ctk.CTkFrame(tab, corner_radius=10)
        ops.grid(row=2, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
        for i in range(4): ops.grid_columnconfigure(i, weight=1)
        btns = [
            ("Aleatorio", lambda: _fill_matrices('random')),
            ("Ceros",    lambda: _fill_matrices('zeros')),
            ("Unos",     lambda: _fill_matrices('ones')),
            ("Det A",    _determinant),
            ("Inv A",    _inverse),
            ("A + B",    _sum),
            ("A - B",    _sub),
            ("A × B",    _mul)
        ]
        for idx,(text,cmd) in enumerate(btns):
            row = 0 if idx < 4 else 1
            col = idx % 4
            ctk.CTkButton(ops, text=text, command=cmd, width=100, height=30).grid(row=row, column=col, padx=5, pady=5)

        res_frame = ctk.CTkFrame(tab, corner_radius=10)
        res_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=20, pady=(0,10))
        _draw_matrices()
    def _draw_matrices():
        for f in (frameA, frameB, res_frame):
            for w in f.winfo_children(): w.destroy()
        rA, cA = int(a_rows.get()), int(a_cols.get())
        matA_entries = []
        for i in range(rA):
            frameA.grid_rowconfigure(i, weight=1)
            for j in range(cA):
                frameA.grid_columnconfigure(j, weight=1)
                e = ctk.CTkEntry(frameA, width=60, height=40, justify='center')
                e.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
                e.insert(0, '0')
                matA_entries.append(e)
        rB, cB = int(b_rows.get()), int(b_cols.get())
        matB_entries = []
        for i in range(rB):
            frameB.grid_rowconfigure(i, weight=1)
            for j in range(cB):
                frameB.grid_columnconfigure(j, weight=1)
                e = ctk.CTkEntry(frameB, width=60, height=40, justify='center')
                e.grid(row=i, column=j, padx=4, pady=4, sticky='nsew')
                e.insert(0, '0')
                matB_entries.append(e)

    def _get_matrix(, entries, rows, cols):
        try:
            vals = [int(float(e.get())) for e in entries]
            return np.array(vals).reshape((rows, cols))
        except:
            return None

    def _fill_matrices(, mode):
        for entries in (matA_entries, matB_entries):
            for e in entries:
                e.delete(0, 'end')
                if mode == 'random': e.insert(0, str(np.random.randint(-9, 10)))
                elif mode == 'zeros': e.insert(0, '0')
                elif mode == 'ones':  e.insert(0, '1')
        _draw_matrices()

    def _show(, M):
        for w in res_frame.winfo_children(): w.destroy()
        rows, cols = M.shape
        for i in range(rows): res_frame.grid_rowconfigure(i, weight=1)
        for j in range(cols): res_frame.grid_columnconfigure(j, weight=1)
        for i in range(rows):
            for j in range(cols):
                lbl = ctk.CTkLabel(res_frame, text=str(int(M[i, j])), justify='center')
                lbl.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)

    def _determinant():
        A = _get_matrix(matA_entries, int(a_rows.get()), int(a_cols.get()))
        if A is None or A.shape[0] != A.shape[1]: return
        det = int(round(np.linalg.det(A)))
        _show(np.array([[det]]))

    def _inverse():
        A = _get_matrix(matA_entries, int(a_rows.get()), int(a_cols.get()))
        if A is None or A.shape[0] != A.shape[1]: return
        inv = np.rint(np.linalg.inv(A)).astype(int)
        _show(inv)

    def _sum():
        A = _get_matrix(matA_entries, int(a_rows.get()), int(a_cols.get()))
        B = _get_matrix(matB_entries, int(b_rows.get()), int(b_cols.get()))
        if A is None or B is None or A.shape != B.shape: return
        _show(A + B)

    def _sub():
        A = _get_matrix(matA_entries, int(a_rows.get()), int(a_cols.get()))
        B = _get_matrix(matB_entries, int(b_rows.get()), int(b_cols.get()))
        if A is None or B is None or A.shape != B.shape: return
        _show(A - B)

    def _mul():
        A = _get_matrix(matA_entries, int(a_rows.get()), int(a_cols.get()))
        B = _get_matrix(matB_entries, int(b_rows.get()), int(b_cols.get()))
        if A is None or B is None or A.shape[1] != B.shape[0]: return
        _show(A.dot(B))

