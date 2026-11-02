---
type: concept
tags: [concept, trim72, locus, artefact]
status: current
---

# The TRIM72 locus

> [!summary] In one line
> TRIM72 sits a few kilobases 3′ of two much more highly expressed same-strand genes, so some of what is
> counted as MG53 mRNA is transcription that belongs to its neighbours.

## The geometry

On the plus strand, reading 5′ → 3′:

```
   FUS  ──────────▶        PYCARD-AS1 ──▶        TRIM72 ──▶
   252 CPM                                      5.33 CPM
   ←──────── 17.05 kb ────────────────────────────▶
                    ←──── 10.6 kb ────────────────▶
```

- **[[FUS]]** lies 17.05 kb 5′ of TRIM72, same strand, and runs at about **252 CPM** — roughly 47× TRIM72's
  5.33 CPM in the same pools.
- **[[PYCARD-AS1]]** lies 10.6 kb 5′ of TRIM72, same strand.
- **[[PYCARD]]** is co-positional with PYCARD-AS1 **to the base pair but on the opposite strand**, which
  turns out to be the useful control: a strand-aware quantification must move the two in opposite directions,
  and in this dataset it does.

Written the other way round, which is how this vault always writes it: TRIM72 is **3′ of** FUS and
PYCARD-AS1; they are **5′ of** it. The word "downstream" is never used for this relationship, because in
this project "downstream" means regulatory consequence and nothing else.

## Why the geometry is a measurement problem

Transcription does not always stop where the annotation says. When RNA polymerase fails to terminate at the
end of FUS or PYCARD-AS1, it keeps going into the region annotated as TRIM72, and a short-read 3′-biased
assay assigns those reads to TRIM72. The donor is ~47× the recipient's level, so a small proportional leak
from FUS is a large proportional gain for TRIM72. The pipeline calls genes in this position
**`sense_exposed`**: within 20 kb 3′ of an expressed same-strand gene running at ≥ 8× their own level. TRIM72
is one of them.

This is not a hypothesis the study invented to explain away a result — it is a structural property of the
locus, and it is the single most important caveat on everything "upstream of MG53". See
[[Readthrough spillover]] for what it does to the results and how far it has actually been quantified
(order-of-magnitude consistent; **not** quantitatively accounted for).

## The evidence that it is really happening here

In the wells where MG53 rises most:

- The plus-strand genes on the readthrough path rise together — a median excess of **+0.856 log2**, in 14 of
  15 wells, one-sided Wilcoxon p 9×10⁻⁵ with the well as the shuffle unit.
- **PYCARD**, co-positional on the minus strand, *falls* — median −0.495 log2, negative in 14 of 15 wells,
  p 0.0013.

Two genes at the same coordinates moving in opposite directions is what establishes that the quantification
is strand-aware, and so that the plus-strand co-movement is a real transcriptional phenomenon rather than a
mapping smear.

What is *not* established is the magnitude. A flux model calibrated three independent ways on the
plate-batch contrast over-predicts the observed MG53 rise by about 59% at the median, with per-well
attributable fractions ranging from −140% to +742%. So readthrough is the leading account of the rise and the
arithmetic does not yet close.

## The other thing the locus does

It makes MG53's **plate batch gap** the largest in the dataset — 3.124 log2 untreated, rank 1 of 16,656
genes. A gene whose signal is partly its neighbours' transcriptional noise inherits that noise. See
[[Plate batch effects]].

## Links

- [[Readthrough spillover]] — the mechanism and what it explains
- [[MG53 (TRIM72)]] — what the protein actually does
- [[Why MG53 is hard to measure here]] · [[Plate batch effects]]
- [[Upstream of MG53]] — the findings this geometry dominates
- Gene notes: [[TRIM72]], [[FUS]], [[PYCARD]], [[PYCARD-AS1]]

## Sources

- `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv` — row 0 gives TRIM72's pooled CPM 5.33,
  `DoG_class` `sense_exposed`, nearest expressed same-strand 5′ gene FUS, and the rank-1 plate gap.
- `upstream_coregulation/tables/c_locus_obs_over_exp_raiser_wells.csv` — the per-well strand contrast.
- The readthrough-corrected covariate set `gw_rt` in `genome_wide/tables/c_screen_genes.csv.gz` is the
  screen's attempt to subtract this; results that survive it are flagged as such throughout.
