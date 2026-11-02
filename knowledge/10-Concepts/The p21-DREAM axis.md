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

## Why it matters for reading this study's tables

Three practical consequences:

**1. The repression arm should be smaller, and it is.** Second-order effects attenuate. The 15 genes of
[[p53 program P]]'s repression arm move by 0.87× to 0.96× in wild-type lines, against up to 1.255× for the
induction arm. A reader who expects symmetric arms will think the repression arm failed; it did not, it is
just downstream of an intermediate.

**2. The repression arm's membership is the cell-cycle machinery, which is also what cytotoxic drugs hit.**
HJURP, SGO1, CENPN, KIF11, CCNE2, EXO1, FANCD2, BRCA2, USP1, RAD54B, SMC1A — all of these fall when a cell
arrests, for any reason. So a drug that arrests cells without touching p53 will move the repression arm,
and the arm is correspondingly weak evidence about p53 specifically. The pipeline's `curated_cycle`
covariate set exists to absorb exactly this.

**3. Direction must be signed before any tally.** Since the arms respond oppositely, "up with MG53" means
opposite things in them. See [[Signing genes by p53 direction]].

## The honest caveat for this dataset

p21 is [[CDKN1A]], and in this dataset CDKN1A is itself only moved up by 71% of compounds in wild-type lines
— it is not a clean switch. And the repression arm's stability was never measured the way the induction
arm's was: `loco_frequency` is computed for the induction arm only, so all 15 repression-arm genes read
blank, and several were re-selected in only 1–3 of 5 cross-fitting folds. Treat conclusions resting on the
repression arm as the weakest per-gene claims in the study.

## Links

- [[The p53 pathway]] · [[p53 program P]] · [[Signing genes by p53 direction]]
- Gene notes: [[CDKN1A]], [[RB1]], [[CCNE2]], [[KIF11]], [[HJURP]], [[SMC1A]], [[BRCA2]]

## References

- Fischer, 2017, *Oncogene* — the meta-analysis of direct p53 targets, and the argument that p53-dependent
  repression is indirect.
- Engeland, 2018, *Cell Death & Differentiation* — p53-dependent repression through p21, DREAM and RB; the
  clearest statement of the axis.
- Litovchick et al., 2007, *Molecular Cell* — identification of the DREAM complex.
- Müller & Engeland, 2010, *Biochimica et Biophysica Acta* — CHR elements as the cell-cycle promoter module
  DREAM acts on.
