def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def conic_affine_count(p):
    # W^2 = -2u(u+8) mod p
    cnt=0
    for u in range(p):
        rhs = (-2*u*(u+8))%p
        if rhs==0: cnt+=1
        elif legendre(rhs,p)==1: cnt+=2
    return cnt

def naive_V1_count(p):
    # y^2 = 2x(x+1)^2 mod p
    cnt=0
    for x in range(p):
        rhs=(2*x*(x+1)**2)%p
        if rhs==0: cnt+=1
        elif legendre(rhs,p)==1: cnt+=2
    return cnt

for p in [3,5,7,11,13,17,19,23]:
    chi_m2 = legendre(-2,p)
    aff = conic_affine_count(p)
    aff_formula = p - chi_m2
    inf_formula = 1+chi_m2
    C2_total = aff+inf_formula
    N_I2_new = 2*p+1-chi_m2
    N_I2_old = 2*p
    naive = naive_V1_count(p)
    naive_formula = p-chi_m2
    print(f"p={p:3d} chi(-2)={chi_m2:2d}  conic_affine={aff:3d} (formula {aff_formula:3d})  "
          f"C2_total={C2_total:3d}(=p+1={p+1})  naiveV1={naive:3d}(formula {naive_formula:3d})  "
          f"N_I2_new={N_I2_new:3d}  N_I2_old={N_I2_old:3d}")
    assert aff==aff_formula
    assert C2_total==p+1
    assert naive==naive_formula
print("all sub-checks passed")
