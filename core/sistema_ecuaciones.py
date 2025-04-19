import numpy as np

def resolver_sistema(A_vals, B_vals, n):
    try:
        A = np.array(A_vals).reshape((n, n))
        B = np.array(B_vals)
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError:
        raise ValueError("Sistema singular o mal definido")
    except Exception as e:
        raise ValueError(str(e))
