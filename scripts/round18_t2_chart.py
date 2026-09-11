"""Round 18: complete the T_2 chart at t=0 for the I_2^* fiber.

Setup: X=t(W-1) centers at the Tate-cubic's simple root T=-1 (W=T so
W=0 <-> T=0 double root; we want W=-1, i.e. set W=w-1... to match
Round 17's notation we use X=t(w-1) so w=0 <-> T=-1 exactly). Writing
w = -1+omega and then omega=-1+sigma (sigma measures deviation from
T2's own path exactly, since T2 <-> w=-t <-> omega=-1 <-> sigma=0)
reduces (after full symbolic expansion, verified below) to an equation
that is singular in the naive (t,sigma,Y=t*Y2) chart, but becomes
SMOOTH once Y is rescaled as Y=t^2*tau and sigma is left as a
dependent coordinate satisfying (at t=0) sigma=tau^2 -- i.e. the
correct local coordinate is tau=Y/t^2, not sigma or omega directly.

Verified smooth at (t,sigma,tau)=(0,0,0), which is exactly T2's image.
"""
import sympy

t, sigma, tau = sympy.symbols("t sigma tau")
a2 = t * (t + 1) ** 2
a4 = t ** 3 * (t + 1) ** 2


def RHS_of(X):
    return sympy.expand(X ** 3 + a2 * X ** 2 + a4 * X)


if __name__ == "__main__":
    w = sympy.symbols("w")
    X_w = t * (w - 1)
    RHS_w = RHS_of(X_w)
    print("RHS(t,w) factored:", sympy.factor(RHS_w))

    # w = -1+omega ; omega = -1+sigma  =>  w = sigma-2 ... (Round18 uses
    # the omega=-1+sigma substitution directly on w=t*omega, matching
    # the T2 direction w=-t exactly at sigma=0)
    omega = -1 + sigma
    w_val = t * omega
    X = t * (w_val - 1)
    RHS = RHS_of(X)
    print("\nRHS(t,sigma) factored:", sympy.factor(RHS))

    # Final chart: Y = t^2 * tau
    H = sympy.expand(tau ** 2 - sympy.simplify(RHS / t ** 4))
    print("\nH(t,sigma,tau) = tau^2 - RHS/t^4 =", sympy.factor(H))
    print("H(0,sigma,tau) =", H.subs(t, 0))

    pt = {t: 0, sigma: 0, tau: 0}
    dHdt = sympy.diff(H, t).subs(pt)
    dHds = sympy.diff(H, sigma).subs(pt)
    dHdtau = sympy.diff(H, tau).subs(pt)
    print(f"\nAt (t,sigma,tau)=(0,0,0) [T2's image]:")
    print(f"  dH/dt = {dHdt}, dH/dsigma = {dHds}, dH/dtau = {dHdtau}")
    print("  SMOOTH:", any(v != 0 for v in (dHdt, dHds, dHdtau)))

    # t=0 slice of this chart: which curve is it?
    print("\nt=0 slice: H(0,sigma,tau) =", sympy.factor(H.subs(t, 0)),
          " (a smooth parabola tau^2=sigma, single component)")
