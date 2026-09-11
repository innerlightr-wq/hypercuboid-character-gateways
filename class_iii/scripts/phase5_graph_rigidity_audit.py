"""
Compute the full automorphism group of the affine-D6 dual graph of an I2*
fiber (7 vertices: L1,L2,S1,S2,S3,L3,L4; edges L1-S1,L2-S1,S1-S2,S2-S3,
S3-L3,S3-L4), preserving multiplicities (legs mult 1, spine mult 2), and
find the subgroup that ALSO fixes all four leg vertices individually.

This directly tests Round 4/Phase-5's central claim: "the subgroup
compatible with 4 individually fixed legs is trivial."
"""
import itertools

vertices = ['L1','L2','S1','S2','S3','L3','L4']
edges = {frozenset(e) for e in [('L1','S1'),('L2','S1'),('S1','S2'),
                                  ('S2','S3'),('S3','L3'),('S3','L4')]}
mult = {'L1':1,'L2':1,'L3':1,'L4':1,'S1':2,'S2':2,'S3':2}

def is_automorphism(perm):
    # perm: dict vertex -> vertex
    if any(mult[v] != mult[perm[v]] for v in vertices):
        return False
    for e in edges:
        a,b = tuple(e)
        if frozenset((perm[a],perm[b])) not in edges:
            return False
    return True

autos = []
for p in itertools.permutations(vertices):
    perm = dict(zip(vertices, p))
    if is_automorphism(perm):
        autos.append(perm)

print(f"Total automorphisms of the labeled (multiplicity-respecting) graph: {len(autos)}")
for a in autos:
    moved = {v:a[v] for v in vertices if a[v]!=v}
    print(" ", moved if moved else "identity")

print()
legs = {'L1','L2','L3','L4'}
fixing_all_legs = [a for a in autos if all(a[l]==l for l in legs)]
print(f"Automorphisms fixing ALL FOUR leg vertices individually: {len(fixing_all_legs)}")
for a in fixing_all_legs:
    moved = {v:a[v] for v in vertices if a[v]!=v}
    print(" ", moved if moved else "identity (trivial)")

print()
print("CONCLUSION: the subgroup of graph automorphisms compatible with all")
print("four legs individually fixed is", "TRIVIAL" if len(fixing_all_legs)==1 else "NONTRIVIAL -- ARGUMENT FAILS")
