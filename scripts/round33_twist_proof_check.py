import json

def chi(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def a_p_E(p):
    return -sum(chi((x**3+4*x**2+2*x)%p,p) for x in range(p))

def S_of(p):
    def g(t):
        return sum(chi(x*(x+1)*(x+t)%p,p) for x in range(p))
    return sum(chi(t*(t+1)%p,p)*g(t) for t in range(p))

data = json.load(open("/tmp/newform_8_3_d_a.json"))
traces = data["data"][0]["traces"]

print(f"{'p':>4}{'chi(-1)':>8}{'chi(2)':>7}{'chi(-2)':>8}{'S(p)':>7}"
      f"{'-chi(2)p+chi(-1)apE^2':>22}{'match':>7}")
allok=True
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
    Sp = S_of(p)
    apE = a_p_E(p)
    cm1,c2,cm2 = chi(-1,p), chi(2,p), chi(-2,p)
    pred = -c2*p + cm1*apE**2
    ok = (pred==Sp)
    allok &= ok
    print(f"{p:>4}{cm1:>8}{c2:>7}{cm2:>8}{Sp:>7}{pred:>22}{str(ok):>7}")
print("ALL MATCH:", allok)

# Sigma_I, Sigma_II closed forms
print()
print(f"{'p':>4}{'SigmaI=(p-1)S(p)':>18}{'closed=(p-1)(-chi2 p+chi(-1)apE^2)':>36}{'match':>7}"
      f"{'SigmaII=chi(-1)SigmaI':>22}{'closed2=(p-1)(apE^2-chi(-2)p)':>30}{'match2':>7}")
for p in [3,5,7,11,13,17,19,23]:
    Sp=S_of(p); apE=a_p_E(p); cm1,c2,cm2=chi(-1,p),chi(2,p),chi(-2,p)
    SigI=(p-1)*Sp
    closed=(p-1)*(-c2*p+cm1*apE**2)
    SigII=cm1*SigI
    closed2=(p-1)*(apE**2-cm2*p)
    print(f"{p:>4}{SigI:>18}{closed:>36}{str(SigI==closed):>7}{SigII:>22}{closed2:>30}{str(SigII==closed2):>7}")
