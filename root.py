

a = -1
b = 1
norm = 1

def f(x): return ((1+(x[0])**2)/(0.001+(x[0])**2))

def neuman(norm, a, b):
    fmax = f([ 0 ], [norm])
    while True:
        mu = gRandom.Uniform(0, fmax)
        r = gRandom.Uniform(a, b)
        if mu<=f( [ r ], [norm] ):
            return r


def g(x): return 1+x**2
def suchestv_viborka():
    fmax = g(b)
    while True:
        r = (gRandom.Uniform(0,1))
        m = gRandom.Uniform(0, fmax)
        if (m < g(r)):
            return r