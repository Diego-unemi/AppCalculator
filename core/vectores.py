import numpy as np

def parse_vector(entry_text):
    try:
        return np.array([float(x.strip()) for x in entry_text.split(",")])
    except:
        raise ValueError("Entrada no válida. Usa números separados por comas.")

def add_vectors(A, B):
    return A + B

def subtract_vectors(A, B):
    return A - B

def dot_product(A, B):
    return np.dot(A, B)

def cross_product(A, B):
    return np.cross(A, B)
