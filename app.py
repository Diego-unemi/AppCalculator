import customtkinter as ctk
from utils.ui_matrices import setup_matrices_tab
from utils.ui_vectores import setup_vectors_tab
from utils.ui_sistema import setup_sistema_tab
from utils.ui_ecuaciones import setup_equations_tab
from utils.ui_derivada_integral import setup_symbolic_tab
from utils.ui_grafica_3d import setup_plot3d_tab
from utils.ui_grafica_2d import setup_plot2d_tab
from utils.ui_acerca_de import setup_about_tab
class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Científica")
        self.geometry("1000x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._create_widgets()

    def _create_widgets(self):
        main = ctk.CTkFrame(self, corner_radius=20)
        main.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(0, weight=1)

        self.tabview = ctk.CTkTabview(main)
        for name in ["Matrices", "Vectores", "Sistema Ecuaciones", "Ecuaciones", "Derivación/Integración", "Gráfica 2D", "Gráfica 3D", "Acerca de"]:
            self.tabview.add(name)
        self.tabview.grid(row=0, column=0, sticky="nsew")

        setup_matrices_tab(self)
        setup_vectors_tab(self)
        setup_sistema_tab(self)
        setup_equations_tab(self)
        setup_symbolic_tab(self)
        setup_plot2d_tab(self)
        setup_plot3d_tab(self)
        setup_about_tab(self)


        self.tabview.set("Matrices")
