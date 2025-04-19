import sympy as sp
from tkinter import messagebox as mb
import re
def limpiar_expr(expr_raw):
    expr = expr_raw.replace("^", "**")
    expr = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", expr)         # 2x → 2*x, 3sin(x) → 3*sin(x)
    expr = re.sub(r"([a-zA-Z\)])(\()", r"\1*(", expr)         # x(y+1) → x*(y+1), sin(x)(cos(x)) → sin(x)*cos(x)
    expr = re.sub(r"(\))([a-zA-Z\(])", r"\1*\2", expr)        # (x+1)sin(x) → (x+1)*sin(x)
    expr = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", expr)          # x2 → x*2 (poco común pero válido)
    return expr

def derivar_funcion(app):
    try:
        expr_raw = app.expr_entry.get()
        var_raw = app.var_entry.get() or "x"

        expr = sp.sympify(limpiar_expr(expr_raw))
        var = sp.Symbol(var_raw)

        derivada = sp.diff(expr, var)
        mostrar_resultado(app, f"Derivada de f({var}):\n{sp.pretty(derivada, use_unicode=True)}")

    except Exception as e:
        mb.showerror("Error", f"No se pudo derivar:\n{e}")

def integrar_funcion(app):
    try:
        expr_raw = app.expr_entry.get()
        var_raw = app.var_entry.get() or "x"

        expr = sp.sympify(limpiar_expr(expr_raw))
        var = sp.Symbol(var_raw)

        a = app.lower_limit.get().strip()
        b = app.upper_limit.get().strip()

        if a and b:
            integral = sp.integrate(expr, (var, float(a), float(b)))
            mostrar_resultado(app, f"Integral definida de {a} a {b}:\n{sp.pretty(integral, use_unicode=True)}")
        else:
            integral = sp.integrate(expr, var)
            mostrar_resultado(app, f"Integral indefinida:\n{sp.pretty(integral, use_unicode=True)}")

    except Exception as e:
        mb.showerror("Error", f"No se pudo integrar:\n{e}")

def mostrar_resultado(app, texto):
    app.result_box.configure(state="normal")
    app.result_box.delete("1.0", "end")
    app.result_box.insert("1.0", texto)
    app.result_box.configure(state="disabled")
