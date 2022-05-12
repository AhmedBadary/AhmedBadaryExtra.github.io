from numpy import *

def importance(A):
    return linalg.eig(A)[1][:,0]

def iter(A, x0,r=20):
    x = x0
    print(x0)
    for i in range(r):
        x = A.dot(x)
        print(x)

def iter(A, x0, eps=10**-5):
    x, old_x = A.dot(x0), x0
    print(x0)
    while not allclose(x, old_x, rtol=1e-010, atol=1e-18):
        old_x = x
        x = A.dot(x)
        print(x)
    return x

def sanity_check(A, x_2, x_3):
    return allclose(A.dot(x_2), 1*x_2) and allclose(A.dot(x_3), 1*x_3)

x0 = 1/6*ones(6)
A = array([[0,0,0,1/3,0,0],[1,0,0,0,0,0],[0,1/2,0,0,0,0],[0,0,1,0,0,1],[0,0,0,1/3,0,0],[0,1/2,0,1/3,1,0]])

x_2 = importance(A)
x_3 = iter(A, x0)
print(x_3.dot(x_3.T))

