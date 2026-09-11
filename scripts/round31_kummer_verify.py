import itertools

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p-1)//2, p)
    return 1 if r == 1 else -1

def E_points_Fp(p):
    # y^2 = x^3+4x^2+2x over F_p, plus point at infinity
    pts = set()
    for x in range(p):
        rhs = (x**3 + 4*x**2 + 2*x) % p
        if rhs == 0:
            pts.add((x,0))
        else:
            if legendre(rhs,p) == 1:
                # find sqrt by brute force (small p)
                for y in range(p):
                    if (y*y) % p == rhs:
                        pts.add((x,y))
    return pts  # affine points; add 1 for infinity when counting

# E over F_{p^2}: represent F_{p^2} = F_p[w]/(w^2-n), n a non-residue mod p
def find_nonresidue(p):
    for n in range(2,p):
        if legendre(n,p) == -1:
            return n
    return None

def fp2_mul(a,b,n,p):
    # a,b = (re,im)
    ar,ai = a; br,bi = b
    re = (ar*br + ai*bi*n) % p
    im = (ar*bi + ai*br) % p
    return (re,im)

def fp2_add(a,b,p):
    return ((a[0]+b[0])%p, (a[1]+b[1])%p)

def fp2_sq(a,n,p):
    return fp2_mul(a,a,n,p)

def E_points_Fp2(p):
    n = find_nonresidue(p)
    elems = [(a,b) for a in range(p) for b in range(p)]
    pts = []
    for x in elems:
        x3 = fp2_mul(fp2_mul(x,x,n,p),x,n,p)
        x2 = fp2_mul(x,x,n,p)
        rhs = fp2_add(fp2_add(x3, fp2_mul((4,0),x2,n,p),p), fp2_mul((2,0),x,n,p),p)
        for y in elems:
            if fp2_sq(y,n,p) == rhs:
                pts.append((x,y))
    return pts, n

def frob_fp2(elem, p):
    # Frobenius on F_{p^2}: (a+bw)^p = a - bw  (since w^p = -w when w^2=n nonresidue, standard)
    a,b = elem
    return (a % p, (-b) % p)

results = []
for p in [3,5,7,11,13]:
    chi2 = legendre(2,p)
    chim2 = legendre(-2,p)
    affine = E_points_Fp(p)
    N_E = len(affine) + 1  # + infinity
    a_p_E = p + 1 - N_E

    pts2, n = E_points_Fp2(p)
    N_E2 = len(pts2) + 1  # + infinity, over F_{p^2}
    # standard check: N_E2 should equal p^2+1-(a_p_E^2-2p)
    N_E2_expected = p**2 + 1 - (a_p_E**2 - 2*p)

    # count P in E(F_{p^2}) (affine) with Frobenius(P) = -P
    cnt_antifixed = 0
    for (x,y) in pts2:
        fx, fy = frob_fp2(x,p), frob_fp2(y,p)
        negy = ((-y[0])%p, (-y[1])%p)
        if fx == x and fy == negy:
            cnt_antifixed += 1
    # infinity point: Frobenius(O)=O=-O always, is it "antifixed"? O=-O trivially, counted separately.
    # We only count affine here to compare with formula p+1+a_p(E) - 1(for O counted how?) 
    # ker(pi+1) has order p+1+a_p(E), includes O. So affine antifixed count should be (p+1+a_p_E) - 1
    N_E_prime = p + 1 + a_p_E
    expected_affine_antifixed = N_E_prime - 1

    # 2-torsion rational count over F_p: roots of x^2+4x+2=0 mod p, plus x=0
    disc = 16 - 8  # =8
    two_tors_extra = 1 if legendre(8,p)==1 else 0  # whether x^2+4x+2 splits
    m = 2 + 2*two_tors_extra   # m in {2,4}
    n2 = m*m
    n2_formula = 10 + 6*chi2

    results.append(dict(p=p, chi2=chi2, chim2=chim2, a_p_E=a_p_E, N_E=N_E,
                         N_E2=N_E2, N_E2_expected=N_E2_expected,
                         cnt_antifixed=cnt_antifixed, expected_affine_antifixed=expected_affine_antifixed,
                         m=m, n2=n2, n2_formula=n2_formula))

for r in results:
    print(r)
    assert r['N_E2'] == r['N_E2_expected'], "N_E2 mismatch"
    assert r['cnt_antifixed'] == r['expected_affine_antifixed'], f"antifixed mismatch at p={r['p']}"
    assert r['n2'] == r['n2_formula'], "n2 formula mismatch"
print("ALL CHECKS PASSED")
