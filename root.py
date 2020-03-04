

a = -1
b = 1
norm = 1

def f(x,p): return p[0]*((1+(x[0])**2)/(0.001+(x[0])**2))

def neuman(norm, a, b):
    fmax = f([0], [norm])
    while True:
        mu = gRandom.Uniform(0, fmax)
        r = gRandom.Uniform(a, b)
        if mu <= f([r], [norm]):
            return r


def g(x): return 1+x**2
def suchestv_viborka():
    fmax = g(b)
    while True:
        r = gRandom.Uniform(0, 1)
        m = gRandom.Uniform(0, fmax)
        if m < g(r):
            return r

c = ROOT.TCanvas("myfunc", "The Canvas Title", 1200, 500)
ff = TF1("ff1", f, -1, 1)
ff.SetNpx(10000)
ff.SetParameter(0, norm);
ff.Draw()
c.Draw()

c = ROOT.TCanvas("myfunc","The Canvas Title", 1200, 500)
ff = TF1("ff1", f, -1, 1)
ff.SetNpx(10000)
ff.SetParameter(0, norm)
h1 = TH1F("h1", "fnneuman method", 500, -1, 1)
for i in range(0, 10000):
    h1.Fill(neuman(norm, a, b))
h1.Draw()
h1.Fit(ff)
c.Draw()

c = ROOT.TCanvas("myfunc","The Canvas Title", 1200, 500)
ff2 = TF1("ff2", f, -1, 1, 1)
ff2.SetNpx(10000)
ff2.SetParameter(0, norm)
h2 = TH1F("h2", "Method suchestv viborki", 500, -1, 1)

for i in range(0, 10000):
    h2.Fill(suchestv_viborka())
h2.Draw()
h2.Fit(ff2)
c.Draw()
