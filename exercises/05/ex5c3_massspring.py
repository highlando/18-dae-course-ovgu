import numpy as np
import matplotlib.pyplot as plt
from ex5c1_pendulum import impliciteuler


def radau2amats():
    gamma = np.array([1./3, 1]).reshape((2, 1))
    beta = np.array([3./4, 1./4]).reshape((2, 1))
    alpha = np.array([[5./12, -1./12],
                      [3./4, 1./4]])
    return alpha, beta, gamma


def impeulmats():
    gamma = np.array([[1.]])
    beta = np.array([[1.]])
    alpha = np.array([[1.]])
    return alpha, beta, gamma


def RKM(E=None, A=None, rhs=None, inival=None, interval=[0, 1], Nts=100,
        plotplease=False):
    """
    Parameters:
    ---
    rhs: callable
        the right hand side of the problem in the form f(t)
    Nts: integer
        Number of time steps, defaults to `100`.
    """

    t0, te = interval[0], interval[1]
    h = 1./Nts*(te-t0)
    N = inival.size
    sollist = [inival.reshape((1, N))]
    tlist = [t0]
    xk = inival.reshape((N, 1))
    alpha, beta, gamma = radau2amats()
    # alpha, beta, gamma = impeulmats()
    s = beta.size

    for k in range(Nts):  # python starts counting with zero...
        tk = t0 + k*h
        Zkl = []
        for gammaj in gamma:
            Zkl.append(np.dot(A, xk) + rhs(tk+gammaj*h))
        Zk = np.vstack(Zkl)
        dXk = np.linalg.solve(np.kron(np.eye(s), E) - h*np.kron(alpha, A), Zk)
        xkk = xk + h*np.dot(dXk.reshape((N, s), order='F'), beta)

        sollist.append(xkk.reshape((1, N)))
        tlist.append(tk)
        xk = xkk

    sol = np.vstack(sollist)
    if plotplease:
        plt.plot(tlist, sol)
        plt.xlabel('t'), plt.ylabel('x')
        plt.show(block=False)
    return sol


m1, m2, d, k = 2., 1., 0.5, 1.
x10, x20, v10, v20 = 0., 0.5, 0., 0.
g0, gf = .5, 2.5
t0, tf = 0., 4.
mnvrstart, mnvrend = 1., 3.
perturb = True  # whether to add a perturbation to the rhs


def mnvrpoly(s, g0, gf):
    return g0 + (1716*s**7 - 9009*s**8 + 20020*s**9
                 - 24024*s**10 + 16380*s**11
                 - 6006*s**12 + 924*s**13)*(gf - g0)


def targettrj(t):
    if t < mnvrstart:
        return g0
    elif t > mnvrend:
        return gf
    else:
        trft = (t-mnvrstart) / (mnvrend-mnvrstart)
        return mnvrpoly(trft, g0, gf)

# ## the mass spring problem
E = np.array([[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, m1, 0, 0],
              [0, 0, 0, m2, 0],
              [0, 0, 0, 0, 0]])

A = np.array([[0, 0, 1, 0, 0],
              [0, 0, 0, 1, 0],
              [-k, k, 0, 0, 1],
              [k, -k, 0, 0, 0],
              [0, 1, 0, 0, 0]])


def f(t):
    ft = np.array([[0., 0., -k*d, k*d, -targettrj(t)]]).T
    if perturb:
        return ft + 1e-10*np.random.randn(5, 1)
    else:
        return ft


def F(t, x, xdot):
    return E.dot(xdot) - A.dot(x) - f(t).flatten()

interval, Nts = [t0, tf], 800
tmesh = np.linspace(interval[0], interval[1], Nts+1)

inival = np.array([x10, x20, v10, v20, 0])

impeul = True
radau = True


if impeul:
    sol = impliciteuler(F=F, inival=inival, interval=interval, Nts=Nts)
    solx2 = sol[:, 0:2]
    plt.figure(2)
    plt.plot(tmesh, solx2)

    plt.figure(22)
    compf = sol[:, -1]
    plt.plot(tmesh, compf)
    plt.show(block=False)


if radau:
    solradau = RKM(E=E, A=A, rhs=f, inival=inival,
                   interval=interval, Nts=Nts)
    solx12 = solradau[:, 0:2]
    plt.figure(3)
    plt.plot(tmesh, solx12)
    plt.show(block=False)

    plt.figure(33)
    compf = sol[:, -1]
    plt.plot(tmesh, compf)
    plt.show(block=False)
