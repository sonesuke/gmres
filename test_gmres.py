from gmres import *



def test_gmres():
    A = [
            2.0, 0.0, 0.0,
            0.0, 2.0, 0.0,
            0.0, 0.0, 2.0]
    b = [1.0, 2.0, 3.0]
    x0 = [1.0, 1.0, 1.0]

    gmres(3, A, x0, b, 3)
    r = [0 for i in range(0, 3)]
    matmul(3, A, x0, r)
    q = [0 for i in range(0, 3)]
    vecsub(3, b, r, q)
    print q
    assert False
