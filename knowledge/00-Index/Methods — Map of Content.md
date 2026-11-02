---
type: index
tags: [index, methods]
status: current
---

# Methods — Map of Content

How each number was produced, and the null it was tested against. Read alongside
[[How the numbers are decided]], which says which numbers to trust for what.

## The core

| Note | What it covers |
|---|---|
| [[The screen model]] | the regression every per-gene number comes from: the fixed effects, the two genotype slopes, the common slope, and what `b_common` means in words |
| [[Program P derivation]] | how the 180-gene induction arm and 15-gene repression arm were selected, with the cross-fitting and the stability measures |
| [[Nulls and calibration]] | which null applies to which statistic, and why the TP53-relabelling null is valid for the genotype difference but not for the common slope |
| [[How the numbers are decided]] | the provenance tiers — read off a table, recomputed from exported values, or derived by hand |

## The ideas those methods depend on

- [[Two-way fixed effects]] — what removing both line and drug-dose means leaves behind
- [[FDR calibration and the inflated null]] — λ = 4.44 on the common slope, and what it does to every verdict
- [[Placebo genes and reference families]] — the reference distribution a correlation has to be judged against
- [[Cross-fitting and circularity]] — the columns that cannot test what they look like they test
- [[Reliability and disattenuation]] — measured MG53 versus true MG53
- [[Signing genes by p53 direction]] — the conversion that makes a per-gene tally mean anything

## The pipeline itself

Nine steps, each a script plus its committed output tables, in `mg53_p53/` in the repository:

| Step | What it does |
|---|---|
| `setup/` | builds the atlas and gene-panel extracts the rest read |
| `upstream_tf/` | transcription-factor activity against MG53 — 679 factors, two regulon collections |
| `upstream_coregulation/` | the locus, the readthrough geometry, the plate batch gap, genome-wide co-expression |
| `upstream_perturbations/` | which drugs move MG53, and the replication census |
| `downstream_p53/` | MG53 against p53 readouts, including the per-line and single-cell units |
| `p53_dependence/` | **out of scope for the current questions** and not drawn on — see the scope note below |
| `two_way/` | the two-way fixed-effect models, reliability, and the gene nulls |
| `single_cell_all/` | the within-line single-cell analysis with its control-gene families |
| `genome_wide/` | the 16,642-gene screen, the programme derivation, and the calibration |
| `export/` | the machine-readable extract all the findings are built from |

The committed `*/tables/*.csv` are the **regression reference**: a fresh run compares itself against them
table by table and reports identical / close / differs. The last full run came back 125 identical, 23 close,
22 differing — the differences being documented numerical and scope changes rather than surprises.

> [!note] Scope
> `p53_dependence/` asks whether p53 regulates MG53. That is a different question from the two this work is
> scoped to, and its outputs are deliberately not carried into the findings. Where the p53 pathway is
> considered as a *candidate upstream regulator of MG53 expression*, that is treated in [[Upstream of MG53]]
> on its own terms.

## Reproducing the tables

```
python3 mg53_p53/findings/make_tables.py        --results ~/Tahoe-100M/mg53_p53   # the headline tables
python3 mg53_p53/findings/mdm2_mg53_levels.py   --results ~/Tahoe-100M/mg53_p53   # MDM2 against MG53
python3 mg53_p53/findings/mg53_to_p53_effect.py --results ~/Tahoe-100M/mg53_p53   # the controlled measurement
python3 knowledge/_build/build_vault.py         --results ~/Tahoe-100M/mg53_p53   # this vault's data layer
```

Each is deterministic and each prints what it wrote. [[Tables — what the study produced]] says what is in
every output file.
