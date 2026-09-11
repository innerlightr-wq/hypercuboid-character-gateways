def chi(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def Sigma_I_raw(p):
    # P(x0,x1,x2) = x0*x1*x2*(x0+x1)*(x0+x2)*(x1+x2)
    total=0
    for x0 in range(p):
        for x1 in range(p):
            for x2 in range(p):
                P = (x0*x1*x2*(x0+x1)*(x0+x2)*(x1+x2)) % p
                total += chi(P,p)
    return total

def S_of(p):
    def g(t):
        return sum(chi(x*(x+1)*(x+t)%p,p) for x in range(p))
    return sum(chi(t*(t+1)%p,p)*g(t) for t in range(p))

for p in [3,5,7,11,13]:
    SI = Sigma_I_raw(p)
    Sp = S_of(p)
    pred = (p-1)*Sp
    print(f"p={p:3d}  Sigma_I(raw 3-var)={SI:6d}  (p-1)*S(p)={pred:6d}  match={SI==pred}")
