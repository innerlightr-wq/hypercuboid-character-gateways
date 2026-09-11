import json, sys
from pathlib import Path
sys.path.insert(0,"scripts")

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def S_of(p):
    def chi(a,pp=p):
        a%=pp
        if a==0: return 0
        return 1 if pow(a,(pp-1)//2,pp)==1 else -1
    def g(t):
        return sum(chi(x*(x+1)*(x+t)%p) for x in range(p))
    return sum(chi(t*(t+1)%p)*g(t) for t in range(p))

data = json.load(open("/tmp/newform_8_3_d_a.json"))
traces = data["data"][0]["traces"]

print(f"{'p':>4}{'chi(-2)':>8}{'S(p)':>7}{'master(chi(-1)(af+p))':>23}{'match':>7}  "
      f"{'19p+1 ledger Tr_T':>20}{'chi(-1)af (Livne)':>19}{'match2':>7}")
for p in [3,5,7,11,13,17,19,23,29,31,37,41]:
    af = traces[p-1]
    Sp = S_of(p)
    cm1 = legendre(-1,p)
    cm2 = legendre(-2,p)
    master = cm1*(af+p)
    m1 = (master==Sp)
    # forced Tr_T from NEW ledger (19p+1) + TrNS=(19+chi(-1))p:
    # #X = p^2+S(p)+19p+1 = 1+p^2+(19+chi(-1))p+Tr_T  => Tr_T = S(p)-chi(-1)p
    TrT_forced = Sp - cm1*p
    TrT_livne = cm1*af
    m2 = (TrT_forced==TrT_livne)
    print(f"{p:>4}{cm2:>8}{Sp:>7}{master:>23}{str(m1):>7}  {TrT_forced:>20}{TrT_livne:>19}{str(m2):>7}")
