import numpy as np 

def jacobi(A, B, x_init, epsilon=0.001, max_iterations=500):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    for i in range(max_iterations):
        D_inv = np.diag(1 / np.diag(D)) #inverse diagonal
        x_new = np.dot(D_inv, B - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
        x = x_new
        print(i, x)

a = np.array([
    [11, 2.6, 0.4, -3.3],
    [-4.1, 22, 2.2, -3.5],
    [-1.2, -15.7, 33, -0.1],
    [-7.7, -6.3, 4.8, 44]
])
b = np.array([51.27, -64.66, -104.96, -27.12])

x_init = np.zeros(len(b)) #starting vector
print("a:",a,"\n b:" ,b, "\n")
x = jacobi(a, b, x_init)
print("\nfinal:", x)
