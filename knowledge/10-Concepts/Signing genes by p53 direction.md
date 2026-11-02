---
type: concept
tags: [concept, p53, method, per-gene]
status: current
---

# Signing genes by p53 direction

> [!summary] In one line
> "Up with MG53" means more p53 output for a p53-induced gene and *less* for a p53-repressed one, so a tally
> that ignores direction adds the two together and reads as noise whatever the truth is.

## The problem

Every per-gene slope in this study is in **that gene's own units**: log2 of the gene per doubling of measured
MG53. Collect the genes that reach significance and count how many are positive and how many negative, and
you have a number that cannot be interpreted — because the two arms of [[p53 program P]] respond to p53 in
opposite directions.

- A gene p53 **induces**: more of it ⇒ more p53 output.
- A gene p53 **represses**: more of it ⇒ **less** p53 output.

So a positive slope on a repressed gene and a negative slope on an induced gene are *the same finding* about
p53's output, and an unsigned tally puts them on opposite sides of the ledger.

## What signing reveals here

Unsigned, the 195 program genes gave "34 positive, 33 negative" — which looks like noise and was reported
that way. Signed into p53-output units:

| Direction p53 moves the gene | genes | with a verdict | toward MORE p53 output | toward LESS |
|---|---|---|---|---|
| induced by p53 (arm P) | 180 | 62 | 32 | 30 |
| repressed by p53 (arm P-down) | 15 | 5 | 3 | 2 |
| **all 195** | 195 | **67** | **35** | **32** |
| *the 29 curated effectors* | *29* | *8* | *5* | *3* |

The conclusion is the same but it now means something. **A coherent change in p53 output would push the two
arms in opposite gene-level directions and so land almost entirely on one side of this split.** It lands on
both sides equally — in the full program and in the curated effector list alike. That is the signature of a
non-specific association, and it is invisible without the signing. Three of the unsigned "positives" are
repressed genes that move p53 output the other way.

## Where direction comes from

**Data-defined**, from the arm a gene was selected into. In this dataset the arms are clean:

- disjoint, and no gene is significant in both directions (`q_up` and `q_down` are never both < 0.1);
- well separated — induction-arm genes are moved up by 64–99% of the 98 reference compounds (median 79%),
  repression-arm genes moved *down* by 70–81%.

**Curated, where the data is silent.** Not one of the 15 repression-arm genes appears in any curated
p53-activated set, CollecTRI's 723 TP53 targets included, so curation and data never conflict here
(`direction_conflicts_curation` is 0 of 195). Curation also fills gaps: [[PMAIP1]] (NOXA), [[TP53I3]] and
[[SPATA18]] are canonical targets that the data-defined program does not contain, and without a curated
fallback they would drop out of a signed tally for want of a sign. The `p53_direction_source` column records
which rule applied to each gene.

## "Mixed" is a property of the gene, not a defect

`frac_compounds_wt_up` is the share of the 98 reference compounds that move a gene **up** in TP53-wild-type
lines. At 0.5 the gene goes each way equally often, and its direction is not a fact about the gene.

- **65 of the 195** program genes sit between 0.35 and 0.65.
- **11 of the 29** curated effectors do — including **[[BAX]] at 0.541**, [[EDA2R]] 0.541, [[RPS27L]] 0.510,
  [[XPC]] 0.571, [[PMAIP1]] 0.571, [[GDF15]] 0.592, [[TRIAP1]] 0.612, [[PHLDA3]] 0.622, [[GADD45A]] 0.633.

A canonical p53 apoptosis target that goes up in barely half the compounds is the reason not to read any
single gene as a p53 readout. The programme score exists because individual genes are this noisy.

## And membership itself is often unstable

`n_folds_kept` counts how many of the 5 cross-fitting folds re-selected a gene into the program. Of the 67
genes with a verdict, **20 were kept in 0 or 1 folds** — and those 20 split 11 toward less output and 9
toward more, the same even split as the stable ones (15 against 20). So instability is not what is producing
the even split; the even split is the result.

One asymmetry to know: `loco_frequency` (leave-one-compound-out stability) is computed for the **induction
arm only**, so every repression-arm gene reads blank there and must be judged on `n_folds_kept` alone. Of the
five repression-arm genes with a verdict, [[MBOAT1]] was kept in 1 fold of 5 and [[SMC1A]] in 2.

## Links

- [[p53 program P]] · [[The p21-DREAM axis]] · [[Cross-fitting and circularity]]
- [[Downstream of MG53]] — where the signed tally does its work
- [[Genes — Map of Content]] — genes grouped by direction, by mixedness, and by signed effect
- `tables/tableD_signed_tally.csv`, `tables/p53_effectors_signed_tally.csv`
- Implemented in `sign_by_p53_direction()` and `signed_tally()` in `mg53_p53/findings/make_tables.py`
