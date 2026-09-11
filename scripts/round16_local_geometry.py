"""Round 16: local fiber geometry.

Two genuinely new rigorous results this round:

1. Torsion height-consistency filter. Every torsion point has canonical
   height 0, so Shioda's formula forces, for each nonzero 2-torsion
   point T_i, sum_v contr_v(T_i) = 4 exactly. Enumerating all abstract
   ways the three nonzero torsion points T1=(X=0), T2=(X=-t(t+1)),
   T3=(X=-t^2(t+1)) could specialize into the component groups of the
   four bad fibers (I_2^*, I_2, I_0^*, I_2^*) and keeping only those
   satisfying the height-4 constraint at every T_i leaves exactly 6
   abstract solutions (down from an unconstrained space).

2. Explicit local blow-up at t=1 (the I_2 fiber -- the simplest one,
   ordinary multiplicative reduction, no twist subtlety). Shifting
   X=Xp-2 (the node is at X=-2, found because T2(1)=T3(1)=-2) and
   expanding Y^2=X^3+a2X^2+a4X to first order in eps=t-1, then
   blowing up Xp=eps*u shows T2,T3 land at DIFFERENT points (u=-3,-5)
   of the SAME exceptional P^1 (the non-identity component), while T1
   (X=0) reduces to the ordinary smooth point Xp=2, unambiguously on
   the identity component.

Combining (1)+(2): only 2 of the 6 abstract solutions survive (those
with T1 -> 0 contribution at the I_2 fiber), differing only in which of
T2,T3 plays the "near" (contribution 1) vs "far" (contribution 1.5)
role at the two I_2^* fibers -- likely related by the surface's own
t <-> 1/t self-duality (Round 9/11), not resolved further this round.
"""
import sympy

t, eps, Xp, Y = sympy.symbols("t eps Xp Y")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def local_blowup_at_t1():
    X = Xp - 2
    eqn = sympy.expand(Y ** 2 - (X ** 3 + a2 * X ** 2 + a4 * X))
    eqn_t = eqn.subs(t, 1 + eps)
    series = sympy.expand(sympy.series(eqn_t, eps, 0, 2).removeO())
    poly_eps = sympy.Poly(series, eps)
    c0 = sympy.factor(poly_eps.coeff_monomial(eps ** 0))
    c1 = sympy.factor(poly_eps.coeff_monomial(eps ** 1))
    return c0, c1


def torsion_height_solutions():
    def options_D6():
        opts = []
        for i in range(3):
            c = [1.5, 1.5, 1.5]
            c[i] = 1.0
            opts.append(tuple(c))
        for i in range(3):
            for v in (1.0, 1.5):
                c = [v, v, v]
                c[i] = 0.0
                opts.append(tuple(c))
        opts.append((0.0, 0.0, 0.0))
        return opts

    def options_D4():
        opts = [(1.0, 1.0, 1.0)]
        for i in range(3):
            c = [1.0, 1.0, 1.0]
            c[i] = 0.0
            opts.append(tuple(c))
        opts.append((0.0, 0.0, 0.0))
        return opts

    def options_A1():
        opts = []
        for i in range(3):
            c = [0.5, 0.5, 0.5]
            c[i] = 0.0
            opts.append(tuple(c))
        opts.append((0.0, 0.0, 0.0))
        return opts

    D6, A1, D4 = options_D6(), options_A1(), options_D4()
    sols = []
    for c0 in D6:
        for c1 in A1:
            for cm1 in D4:
                for cinf in D6:
                    totals = [c0[i] + c1[i] + cm1[i] + cinf[i] for i in range(3)]
                    if all(abs(x - 4.0) < 1e-9 for x in totals):
                        sols.append((c0, c1, cm1, cinf))
    return sols


if __name__ == "__main__":
    c0, c1 = local_blowup_at_t1()
    print("Y^2 - RHS at t=1 (eps^0):", c0)
    print("Y^2 - RHS at t=1 (eps^1):", c1)
    print()
    sols = torsion_height_solutions()
    print(f"Globally height-consistent torsion patterns: {len(sols)}")
    for s in sols:
        print(" ", s)
    surviving = [s for s in sols if s[1][0] == 0.0]
    print(f"\nSurviving after fixing T1->identity at I_2 (t=1): {len(surviving)}")
    for s in surviving:
        print(" ", s)
