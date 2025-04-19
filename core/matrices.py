import numpy as np

def get_matrix(entries):
    try:
        return np.array([[int(float(e.get() or 0)) for e in row] for row in entries])
    except:
        return None

def fill_matrix(entries, mode):
    for row in entries:
        for e in row:
            e.delete(0, 'end')
            if mode == 'random':
                e.insert(0, str(np.random.randint(-9, 10)))
            elif mode == 'zeros':
                e.insert(0, '0')
            elif mode == 'ones':
                e.insert(0, '1')

def determinant(matrix):
    return int(round(np.linalg.det(matrix)))

def inverse(matrix):
    return np.rint(np.linalg.inv(matrix)).astype(int)

def add_matrices(A, B):
    return A + B

def subtract_matrices(A, B):
    return A - B

def multiply_matrices(A, B):
    return A.dot(B)
