import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def impliciteuler(F=None, inival=None, interval=[0, 1], Nts=100,
                  plotplease=False, dFdx=None, dFdxdot=None):
    """
    Parameters:
    ---
    F: callable
        the problem in the form F(t,x,x')
    Nts: integer
        Number of time steps, defaults to `100`.
    """
    t0, te = interval[0], interval[1]
    h = 1./Nts*(te-t0)
    N = inival.size

    sollist = [inival.reshape((1, N))]
    tlist = [t0]
    xk = inival
    for k in range(1, Nts+1):  # python starts counting with zero...
        tkk = t0 + k*h

        def impeuler_increment(xkkn):
            """ the implicit Euler update for a general F """
            return F(tkk, xkkn, 1./h*(xkkn-xk)).flatten()

        xkk, _, flag, msg = fsolve(func=impeuler_increment,
                                   x0=xk, full_output=True)
        # call a nonlinear solver for the system f(x)=0
        if not flag == 1:
            print('Caution at t={0}: '.format(tkk) + msg)
        sollist.append(xkk.reshape((1, N)))
        tlist.append(tkk)
        xk = xkk

    sol = np.vstack(sollist)
    if plotplease:
        plt.plot(tlist, sol)
        plt.xlabel('t'), plt.ylabel('x')
        plt.show(block=False)
    return sol


if __name__ == '__main__':

    m, l, rx, ry, g = 1, 1, 0, 0, 9.81
    x0, y0 = l, 0.
    u0, v0 = 0., 0.
    lbd0 = 0.

    def pendulumres(t, x, xdot):
        '''
        x = [x, y, u, v, lambda]
        '''
        return np.array([[xdot[0] - x[2]],
                         [xdot[1] - x[3]],
                         [m*xdot[2] + 2*(x[0]-rx)*x[4]],
                         [m*xdot[3] + 2*(x[1]-ry)*x[4] + m*g],
                         [(x[0]-rx)**2 + (x[1]-ry)**2 - l**2]])

    interval, Nts = [0, 50], 5000
    inival = np.array([x0, y0, u0, v0, lbd0])

    sol = impliciteuler(F=pendulumres, inival=inival,
                        interval=interval, Nts=Nts)
    tmesh = np.linspace(interval[0], interval[1], Nts+1)
    solxy = sol[:, :2]
    plt.figure(1)
    plt.plot(tmesh, solxy)
    gx = (sol[:, 0]-rx)**2 + (sol[:, 1]-ry)**2 - l**2
    plt.plot(tmesh, gx)
    plt.xlabel('t'), plt.ylabel('x, y, g(x,y)')
    plt.show(block=False)

    def pendulumres_ind2(t, x, xdot):
        '''
        x = [x, y, u, v, lambda]
        '''
        return np.array([[xdot[0] - x[2]],
                         [xdot[1] - x[3]],
                         [m*xdot[2] + 2*(x[0]-rx)*x[4]],
                         [m*xdot[3] + 2*(x[1]-ry)*x[4] + m*g],
                         [2*(x[0]-rx)*xdot[0] + 2*(x[1]-ry)*xdot[1]]])

    sol = impliciteuler(F=pendulumres_ind2, inival=inival, interval=interval,
                        Nts=Nts)
    tmesh = np.linspace(interval[0], interval[1], Nts+1)
    solxy = sol[:, :2]
    plt.figure(2)
    plt.plot(tmesh, solxy)
    gx = (sol[:, 0]-rx)**2 + (sol[:, 1]-ry)**2 - l**2
    plt.plot(tmesh, gx)
    plt.xlabel('t'), plt.ylabel('x, y, g(x,y)')
    plt.show(block=False)
