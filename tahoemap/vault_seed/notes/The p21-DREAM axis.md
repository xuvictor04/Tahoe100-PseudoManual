---
type: concept
tags: [concept, p53, cell-cycle]
status: current
---

# The p21-DREAM axis

> [!summary] In one line
> p53 does not repress genes directly so much as it induces p21, which keeps the DREAM complex sitting on
> cell-cycle promoters — which is why the "repressed" arm of any p53 signature is indirect, smaller, and
> easy to misread.

## The mechanism

p53's activation arm is straightforward: it binds response elements and raises transcription. Its
*repression* arm mostly is not direct. The accepted route runs:

```
p53 ──▶ CDKN1A (p21) ──▶ inhibits CDK2/CDK4 ──▶ RB and p130 stay unphosphorylated
                                              ──▶ DREAM stays assembled on CHR/CDE promoter elements
                                              ──▶ cell-cycle genes stay OFF
```

DREAM is the complex of DP, RB-like p130, E2F4 and the MuvB core. Assembled, it occupies cell-cycle
homology region (CHR) elements in the promoters of genes needed for S phase and mitosis and keeps them
silent. Because CDK activity is what disassembles it, anything that raises p21 — p53 being the obvious
example — keeps it in place.

Meta-analyses of p53 binding and expression data have argued that essentially **no** gene is directly
repressed by p53 binding its promoter; the apparent repression is this indirect arm, plus RB-family effects.
That claim is strong and has been influential, though the "no direct repression at all" version is still
argued over.

## Why it matters for reading the tables

**1. The repression arm should be smaller, and it is.** Second-order effects attenuate. In the earlier MG53/p53
study the 15 repression-arm genes of its p53 programme moved by 0.87× to 0.96× in wild-type lines, against up to
1.255× for the induction arm. A reader who expects symmetric arms will think the repression arm failed; it did
not, it is just downstream of an intermediate.

**2. The repression arm is the cell-cycle machinery, which is also what cytotoxic drugs hit.** [[HJURP]],
[[SGO1]], [[CENPN]], [[KIF11]], [[CCNE2]], [[EXO1]], [[FANCD2]], [[BRCA2]], [[USP1]], [[RAD54B]], [[SMC1A]] — all of
these fall when a cell arrests, for any reason. A drug that arrests cells without touching p53 (a CDK4/6 inhibitor,
an antimitotic) moves them too, so on their own they are weak evidence about p53. The atlas's `cell-cycle shift`
flag marks drug-doses whose S-phase or G2/M module moved enough that cycle genes follow the cycle mix.

**3. Direction must be signed before any tally.** The arms respond oppositely: a fall in a repression-arm gene is
the p53-active direction. A count of "genes up" that mixes the arms is meaningless.

## What it predicts in this vault

The induction arm (p21 and the other direct targets) and the repression arm (the DREAM targets) respond to the same
drugs in **opposite** directions. So:

- in the **vector space** they point opposite ways: a p53 target's "genes that move opposite" should include
  cell-cycle genes, with negative cosines;
- on the **nodal map** (distance 1 − |cos|) they can land in the same island, as the + and − arms of one module;
- the validation stage tests this directly (the p53-up / DREAM-down opposite-arm test). On data where
  cell-cycle arrest is driven mostly by non-p53 drugs, the two arms can instead separate into different modules —
  which is itself informative.

## The honest caveat

p21 is [[CDKN1A]], and CDKN1A is itself not a clean switch: in the earlier study it was moved up by 71% of
compounds in wild-type lines, and it has strong p53-independent inducers. The repression arm's membership stability
was also never measured the way the induction arm's was. Treat conclusions resting on the repression arm as the
weakest per-gene claims.

## References

- Fischer, 2017, *Oncogene* — the meta-analysis of direct p53 targets, and the argument that p53-dependent
  repression is indirect.
- Engeland, 2018, *Cell Death & Differentiation* — p53-dependent repression through p21, DREAM and RB; the
  clearest statement of the axis.
- Litovchick et al., 2007, *Molecular Cell* — identification of the DREAM complex.
- Müller & Engeland, 2010, *Biochimica et Biophysica Acta* — CHR elements as the cell-cycle promoter module
  DREAM acts on.
