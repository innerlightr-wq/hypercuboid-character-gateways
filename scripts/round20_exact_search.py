"""Round 20: exact, systematic elimination of all 23 height-1 patterns.

For x(t) = a4 t^4 + a3 t^3 + a2 t^2 + a1 t + a0, each of the four local
component choices imposes forced coefficient values (derived in Rounds
17-19):

  c0 (I_2^* at t=0):
    O  -> a0 free, != 0
    N  -> a0=0, a1=-1
    F1 -> a0=0, a1=0, a2=0
    F2 -> a0=0, a1=0, a2=-1

  cinf (I_2^* at t=infinity, via x_inf = x(t)/t^4):
    O  -> a4 free, != 0   (deg(x)=4)
    N  -> a4=0, a3=-1     (deg(x)=3)
    F1 -> a4=0, a3=0, a2=0
    F2 -> a4=0, a3=0, a2=-1

  c1 (I_2 at t=1):     O -> x(1)!=-2 (open);      N -> x(1)=-2 (equation)
  cm1 (I_0^* at t=-1): O -> x(-1)!=0 (open);  Named -> x(-1)=0 (equation)

For each of the 23 raw patterns:
  1. impose c0, cinf coefficient constraints; if they conflict on a
     shared coefficient (e.g. a2), the pattern is IMMEDIATELY
     INCONSISTENT (no algebra needed);
  2. impose the c1, cm1 equations on the remaining free coefficients;
     if over-determined and inconsistent, INCONSISTENT;
  3. if a unique x(t) results, check the open (!=) conditions directly;
  4. check whether R_x(t) = x^3+t(t+1)^2 x^2+t^3(t+1)^2 x is a perfect
     square polynomial over Q (exact, via square-free factorization).
"""
import sympy

t = sympy.symbols("t")


def coeff_constraints_0(cat):
    # returns dict of {index: value} forced, index 0..2 relevant (a0,a1,a2)
    if cat == "O":
        return {}, ["a0!=0"]
    if cat == "N":
        return {0: 0, 1: -1}, []
    if cat == "F1":
        return {0: 0, 1: 0, 2: 0}, []
    if cat == "F2":
        return {0: 0, 1: 0, 2: -1}, []
    raise ValueError(cat)


def coeff_constraints_inf(cat):
    if cat == "O":
        return {}, ["a4!=0"]
    if cat == "N":
        return {4: 0, 3: -1}, []
    if cat == "F1":
        return {4: 0, 3: 0, 2: 0}, []
    if cat == "F2":
        return {4: 0, 3: 0, 2: -1}, []
    raise ValueError(cat)


def is_real_perfect_square(poly_expr):
    p = sympy.Poly(sympy.expand(poly_expr), t)
    if p.is_zero:
        return False, "identically zero"
    if p.degree() % 2 != 0:
        return False, "odd degree"
    content, factors = sympy.factor_list(poly_expr)
    if content < 0:
        return False, f"negative leading content {content}"
    cr = sympy.Rational(content)
    if sympy.sqrt(cr.p) != int(sympy.sqrt(cr.p)) or sympy.sqrt(cr.q) != int(sympy.sqrt(cr.q)):
        return False, f"content {content} not a rational square"
    for fac, mult in factors:
        if mult % 2 != 0:
            return False, f"factor {fac} has odd multiplicity {mult}"
    return True, "perfect square"


def analyze_pattern(c0, c1, cm1, cinf):
    a = {i: sympy.Symbol(f"a{i}") for i in range(5)}
    forced = {}
    opens = []

    d0, o0 = coeff_constraints_0(c0)
    dI, oI = coeff_constraints_inf(cinf)
    opens += o0 + oI

    for idx, val in list(d0.items()) + list(dI.items()):
        if idx in forced and forced[idx] != val:
            return "IMMEDIATELY INCONSISTENT (c0/cinf conflict)", None, None
        forced[idx] = val

    subs = {a[i]: v for i, v in forced.items()}
    X = sum((subs.get(a[i], a[i])) * t ** i for i in range(5))

    free_syms = sorted(X.free_symbols - {t}, key=lambda s: s.name)

    eq_pairs = []
    if c1 == "N":
        eq_pairs.append((X.subs(t, 1), sympy.Integer(-2)))
    if cm1 != "O":
        eq_pairs.append((X.subs(t, -1), sympy.Integer(0)))

    if not eq_pairs:
        Xfinal = X
    elif not free_syms:
        # X already fully determined by c0/cinf; eq_pairs are pure consistency checks
        if not all(sympy.simplify(lhs - rhs) == 0 for lhs, rhs in eq_pairs):
            return "INCONSISTENT (forced X violates c1/cm1 equations)", X, None
        Xfinal = X
    else:
        eqs = [sympy.Eq(lhs, rhs) for lhs, rhs in eq_pairs]
        sol_list = sympy.solve(eqs, free_syms, dict=True)
        if not sol_list:
            return "INCONSISTENT (c1/cm1 equations unsolvable)", None, None
        sol = sol_list[0]
        Xfinal = X.subs(sol)

    remaining_free = sorted(Xfinal.free_symbols - {t}, key=lambda s: s.name)
    if remaining_free:
        return f"POSITIVE-DIMENSIONAL FAMILY (free: {remaining_free})", Xfinal, None

    Xfinal = sympy.expand(Xfinal)

    # check open conditions
    if c0 == "O" and Xfinal.subs(t, 0) == 0:
        return "INCONSISTENT (forced X(0)=0 contradicts O@0)", Xfinal, None
    if cinf == "O" and sympy.Poly(Xfinal, t).degree() < 4:
        return "INCONSISTENT (forced deg<4 contradicts O@infinity)", Xfinal, None
    if c1 == "O" and Xfinal.subs(t, 1) == -2:
        return "INCONSISTENT (forced X(1)=-2 contradicts O@1)", Xfinal, None
    if cm1 == "O" and Xfinal.subs(t, -1) == 0:
        return "INCONSISTENT (forced X(-1)=0 contradicts O@-1)", Xfinal, None

    a2 = t * (t + 1) ** 2
    a4c = t ** 3 * (t + 1) ** 2
    RHS = sympy.expand(Xfinal ** 3 + a2 * Xfinal ** 2 + a4c * Xfinal)
    if RHS == 0:
        return "TORSION (RHS=0 identically -- X is a 2-torsion x-coordinate)", Xfinal, RHS
    ok, reason = is_real_perfect_square(RHS)
    if ok:
        return "CANDIDATE SECTION FOUND", Xfinal, RHS
    return f"EXACTLY IMPOSSIBLE ({reason})", Xfinal, RHS


if __name__ == "__main__":
    from itertools import product
    opts_I2star = ["O", "N", "F1", "F2"]
    opts_I2 = ["O", "N"]
    opts_I0star = ["O", "N1", "N2", "N3"]
    vals = {"O": 0, "N": 1, "F1": 1.5, "F2": 1.5, "N1": 1, "N2": 1, "N3": 1}
    valsI2 = {"O": 0, "N": 0.5}

    count = 0
    results = []
    for c0 in opts_I2star:
        for c1 in opts_I2:
            for cm1 in opts_I0star:
                for cinf in opts_I2star:
                    s = vals[c0] + valsI2[c1] + vals[cm1] + vals[cinf]
                    if abs(s - 3.0) > 1e-9:
                        continue
                    count += 1
                    cm1_cat = "O" if cm1 == "O" else "Named"
                    status, Xfinal, RHS = analyze_pattern(c0, c1, cm1_cat, cinf)
                    results.append(((c0, c1, cm1, cinf), status, Xfinal))
                    print(f"{(c0,c1,cm1,cinf)!s:35s} -> {status}   X={Xfinal}")
    print(f"\ntotal patterns: {count}")
