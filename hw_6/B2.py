import math, random, pylab
import numpy as np

#def rho_free(x, y, beta):
#    return math.exp(-(x - y) ** 2 / (2.0 * beta))


def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x


beta = 20.0
N = 80
dtau = beta / N
delta = 1.0
n_steps = 400000
x = [5.0] * N
data = []
Ncut = N/2

for step in range(n_steps):
    #k = random.randint(0, N - 1)
    #knext, kprev = (k + 1) % N, (k - 1) % N
    #x_new = x[k] + random.uniform(-delta, delta)
    #old_weight  = (rho_free(x[knext], x[k], dtau) *
    #               rho_free(x[k], x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x[k] ** 2))
    #new_weight  = (rho_free(x[knext], x_new, dtau) *
    #               rho_free(x_new, x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x_new ** 2))
    #if random.uniform(0.0, 1.0) < new_weight / old_weight:
    #    x[k] = x_new
    
    x = levy_harmonic_path(x[0], x[0], dtau, N)
    x = x[Ncut:] + x[:Ncut]
    
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])
    

np.save('x_positions_levy',x)



pylab.plot(x,np.arange(0,beta,dtau))
pylab.xlabel('$x$')
pylab.ylabel('Imaginary Time')
pylab.title('Path Sample for Harmonic-Path-Levy')
pylab.savefig('x_positions_levy.png')
pylab.clf()

pylab.hist(data, normed=True, bins=100, label='QMC')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('levy_harmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.savefig('plot_B2_beta%s_levy.png' % beta)
pylab.show()
