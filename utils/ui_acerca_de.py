import customtkinter as ctk

def setup_about_tab(app):
        tab = app.tabview.tab("Acerca de")
        info = (
            "Calculadora Científica\n"
            "Autor: Tu Nombre\n"
            "Materia: Modelos Matemáticos y Simulación\n"
            "Profesor: Morales Torres\n"
            "2025"
        )
        ctk.CTkLabel(tab, text=info, justify="center").pack(expand=True)