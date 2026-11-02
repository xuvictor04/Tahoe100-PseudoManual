---
type: method
tags: [method, p53, program, selection, circularity]
status: current
---

# Program P derivation

> [!summary] In one line
> [[p53 program P]] was built in three nested selections — which drug-doses activate p53, then which genes
> respond wild-type-specifically to those drug-doses — and the TP53 genotype labels are used at **every**
> one of them, which is the fact that decides what the programme's columns can and cannot be used to argue.

What the programme *is* and what it is for is [[p53 program P]]. This note is how it was made, in order,
with the stability machinery and the exact list of columns the labels contaminate.

## Step 0 — the contrast z, the raw material

For every gene × drug-dose, one number [`genome_wide/genome_wide.py` section B]:

```
z = (mean r2 of the TP53-WT lines − mean r2 of the TP53-altered lines)
    / (SD over the drug-dose's line values x sqrt(1/n_WT + 1/n_alt))
```

The SD is taken over *all* the drug-dose's lines without reference to the labels, so the denominator is
label-free even though the numerator is not. The same genes and the same drug-doses are used for the true
labels and for all 100 label permutations, so nothing differs between the observed and permuted runs except
the labelling.

Two exclusions set the base: **`keep` drug-doses** are those that are not unreliable-plate-only and not
position-not-correctable, and **lines with no TP53 group are dropped** from this step and from the screen
([[The screen model]]) — `two_way` instead counts them as altered, and `checks.csv` names them. That
difference is why a few numbers do not match between the two steps.

## Step 1 — S1: which drug-doses diverge by genotype at all

Per drug-dose, a single genome-wide divergence statistic: **`divergence_D` = log of the mean of the top 1%
of z² over genes** (at least 10 genes) [`genome_wide/genome_wide.py`:143, `TOPK_FRAC`]. It asks whether
*anything* in the transcriptome separates wild-type from altered lines under that treatment, with no gene
list.

That statistic is calibrated against the label permutations (`zD`), given a pooled permutation p (`pD`),
and taken through a **permutation FDR** at q < 0.05 (`qD`) — each permuted labelling treated as the truth
and calibrated against the others, BH over the pooled p. The permutation FDR is used rather than an
analytic one because it keeps the skew of the null and the fact that every drug-dose shares one labelling;
see [[Nulls and calibration]].

`in_S1` = `qD` < 0.05. **Fallback:** if S1 holds fewer than 2 compounds, the top 10 by `zD` are taken
instead and the run flags it in `checks.csv`, `key_results.csv` and `GENOME_WIDE.md`.

## Step 2 — the compound folds, dealt after S1 is known

Five folds of **compounds** (not drug-doses, not wells): the S1 compounds are dealt round-robin by
divergence so each fold gets a comparable spread of strength, and the remaining compounds are dealt by a
seeded permutation. `F_eff = min(5, number of S1 compounds)`
[`genome_wide/genome_wide.py` section B; `SEED` 20261030].

Dealing the folds *after* S1 is deliberate and is also the limit of what the cross-fitting buys: the folds
hold **compounds** out, never labels.

## Step 3 — S2: which drug-doses activate p53, scored out of fold

Each drug-dose is scored with the top-N signature (N = max(25, 0.15% of genes)) derived from the S1
compounds **outside its own fold** [`genome_wide.py`:144, `TOPN_FRAC`]. That gives
`s_oof_program_contrast`, its permutation-calibrated version `zs_oof`, and a permutation FDR `qs_oof`.

`in_S2_p53_activating` = `qs_oof` < 0.05 **and** the score positive. Result: **142 drug-doses over 98
compounds** — the set every fold-change column in the programme tables averages over. `in_S2_minus_foldF`
holds each fold's own training drug-doses, selected with nested signatures.

When S1 was a fallback, S2 and P are both flagged exploratory, because the signatures were then chosen with
the true labels on a set too small to hold out properly.

## Step 4 — the two arms

A gene enters the **induction arm P** when all four conditions hold across the 142 S2 drug-doses, on a
drug-equal, permutation-calibrated contrast (`z_program`) [`genome_wide.py` section B]:

| Condition | Column |
|---|---|
| BH q < 0.05 in the up direction | `q_up` |
| wild-type minus altered > 0 | `wt_minus_alt_log2` |
| moved up in at least half the 98 compounds | `frac_compounds_up` ≥ 0.5 |
| **and the wild-type arm itself up** — drug-weighted WT mean > 0, positive in ≥ half the compounds | `wt_mean_log2`, `frac_compounds_wt_up` ≥ 0.5 |

**P-down is the exact mirror** in the down direction. The exposure ([[TRIM72]]) is excluded from both by
construction, and the BH is taken over genes with the exposure left out.

The fourth condition is the one that makes the arm mean something: a genotype *difference* could be produced
by the altered lines moving down just as well as by the wild-type lines moving up, and without that clause
the arm would mix the two.

**Result: 180 genes in P, 15 in P-down.** A programme with fewer than 10 passing genes becomes a
**fallback** — the top 25 by z, flagged — and is to be read as exploratory
[`genome_wide.py`:139, `PROG_MIN`/`PROG_FALLBACK`].

The arms separate cleanly on how often each gene moves: induction-arm genes are moved **up** by 64–99% of
the 98 compounds (median 79%), repression-arm genes **down** by 70–81%, and no gene is significant in both
directions — `q_up` and `q_down` are never both < 0.1
[`genome_wide/tables/b_p53_program_genes.csv.gz`; `MG53_p53_TABLES.md`, signed-tally section].

### The scores built from the arms

`P_r2` and `P_down_r2` are the mean `r2` of the arm's members **that the line expresses**, per well, then
the drug-dose mean. The primary outcome `P53PROG_UP_cf` scores each drug-dose with the programme
**cross-fitted for its own fold**, and the uncross-fitted `P53PROG_UP`, `_noX`, `_core` and
`P53PROG_DOWN(_cf)` run alongside as secondary [`genome_wide/tables/c_program_models.csv`].

## The 5-fold cross-fitting

`P_-f` is the whole derivation repeated using **no drug-dose of fold f** — its drug-doses selected with
nested signatures from S1 minus fold f. Five re-derivations, so each gene gets `in_P_minus_fold0..4`,
summarised as `n_folds_kept` out of 5.

> [!warning] Cross-fitting bounds compound-driven instability. It does not remove the circularity.
> The TP53 labels are used inside every fold. What `n_folds_kept` tells you is whether a gene's membership
> is a stable feature of the data or a fit to a handful of compounds — and it is frequently the latter.
> Of the 67 programme genes that carry an MG53 verdict, **20 were kept in 0 or 1 of the 5 folds**, and
> those 20 split 11 toward less p53 output against 9 toward more — the same even split as the stable ones
> (15 against 20) [`MG53_p53_TABLES.md`, signed-tally section].

`b_program_stability.csv` carries the fold-to-P Jaccards, the leave-one-compound-out Jaccards, P
re-derived without the exposure-moving drug-doses (`in_P_noX`, atlas |DD_z| ≥ 3), and — the most useful row
— the **null programme sizes**: 20 permuted labellings each treated as the truth with S2 held fixed,
selected by z alone at q < 0.05, next to the observed count under the same rule
[`genome_wide.py`:138, `N_NULL_PROG`].

## Leave-one-compound-out stability

`loco_frequency` repeats the gene selection 98 times, dropping one compound each time, and records the share
of those programmes that keep the gene [`b_p53_program_genes.csv.gz`, `loco_frequency`]. Induction-arm
membership is mostly not the work of single compounds — the arm averages 0.97 ([[Cross-fitting and circularity]]), and all 25 of the strongest genes by fold change sit at 1.000
[`MG53_p53_TABLES.md`, "The 25 strongest p53 target genes by fold change"].

> [!important] `loco_frequency` is computed for the **induction arm only.**
> Every one of the 15 repression-arm genes reads blank, because the leave-one-compound-out programmes are
> derived in the induction direction. A blank there is not missing data and it is not a zero — those genes
> must be judged on `n_folds_kept` alone. `rank_in_P` is blank for the same 15 for the same kind of reason
> (it is a rank within the induction arm).

**The repression arm is the weakest part of the derivation** and should be used with that in mind: only 4 of
its 15 genes are kept by all 5 cross-fitted programmes, and those fold programmes were **top-25 fallbacks
in 4 of the 5 folds** [`export/downstream/program_flags.csv`, `flag`]. Of the five repression-arm genes with
an MG53 verdict, MBOAT1 was kept in 1 fold of 5 and SMC1A in 2.

## Is TP53 the grouping that explains P best?

`b_feature_specificity.csv` runs the same divergence statistic for **every** line grouping the atlas offers
— drivers, protein changes, organs, MTAP loss — with 20 permutations each, on the checked S1 and S2
drug-doses and on P itself, and puts TP53's own z on the same 20-permutation scale beside them
[`genome_wide.py`:137, `N_FEAT_PERM`]. P is selected for TP53 by construction, so TP53 must win; the
question the table answers is by how much. **A grouping that comes close is a warning that P could equally
be a lineage or driver response**, and that is the check to read before treating P as a p53 readout.

## Exactly which columns are circular, and where the labels entered

The labels enter **twice**: at the drug-dose selections (S1's divergence and S2's signature scoring) and
again at the gene-level contrast. A column is circular as evidence of p53 specificity if either applies.

| Column | Labels entered at | Why it is still worth having |
|---|---|---|
| `arm`, `in_P`, `in_P_down`, `in_P1_stage1` | steps 1, 3 and 4 | it is the programme's definition |
| `z_program`, `q_up`, `q_down` (`q_arm`) | the contrast, calibrated on label permutations | ranks genes within the programme |
| `wt_minus_alt_log2`, `wt_minus_alt_fold` | **this is the selection functional itself** | describes the size of the genotype split |
| `wt_mean_log2`, `wt_fold` | a one-arm mean, but inherited through the **S2** drug-dose set | the fold change every gene note quotes, as description |
| `frac_compounds_up`, `frac_compounds_wt_up`, `frac_compounds_down` | the programme rule needs both ≥ 0.5 | mixedness — see [[Signing genes by p53 direction]] |
| `rank_in_P` | rank on `z_program` | ordering only; blank for P-down |
| `n_folds_kept`, `in_P_minus_fold0..4` | labels used inside every fold | bounds **compound**-driven instability |
| `loco_frequency` | same | bounds single-compound dependence; induction arm only |
| the programme score `P_r2` used as an outcome | arm membership | the outcome of the primary test |

**Not circular, because the labels selected nothing in them**: the whole MG53 screen block — `b_common`,
`se_common`, `q_common`, `q_xperm_common`, `b_WT`, `b_alt`, `diff`, `se_diff`, `q_diff`, `q_label_diff` —
and `median_line_cpm`, `n_lines_expressing`, the `crit_*` / `mde80_*` bounds, the `placebo_pct_*` columns and
`readthrough_geometry`. The one thread connecting them to the labels runs the safe way: the `resp_bg`
covariate's background gene set *excludes* the label-selected programmes
[`MG53_p53_TABLES.md`, column glossary; [[The screen model]]].

The practical rule, and the reason this note exists: **the labels are used to choose the read-out, never to
test MG53 against it.** `diff` is label-*tested*, not label-*selected*, which is a different thing. The
consequences for reading any gene note are in [[Cross-fitting and circularity]].

## Reading the fold changes the derivation produces

They are small, and not for the reason first published.

| | Induction arm P (180) | Repression arm P-down (15) |
|---|---|---|
| `wt_fold` range | 1.001× to **1.255×** | 0.872× to 0.965× |
| median | **1.060×** | 0.935× |
| at or above 1.10× | 42 of 180 | — |
| below 1.02× | 19 of 180 | — |

[`genome_wide/tables/b_p53_program_genes.csv.gz`, `wt_mean_log2`; recomputed]

Two reasons, both structural: the baseline is **the plate's drug-well median for the same line**, not
vehicle, so a fold change means "more than a typical drug well"; and the mean is **compound-equal** over the
142 S2 drug-doses, each of 98 compounds carrying 1/98, so one strong activator is averaged with 97 weaker
ones. An earlier write-up said instead that the average was diluted by drug-doses that mostly do not
activate p53 — that was wrong, the 142 are the p53-activating ones specifically
[`genome_wide/genome_wide.py`:1976 → `set_stats`:957-984]. See [[Corrections and retractions]].

Ranking by fold change is also not the same as ranking by the programme's own selection statistic:
Spearman(`z_program`, `wt_mean_log2`) within P is **0.552** [same file; recomputed]. Both orderings are
carried in the tables because neither is the programme's ranking.

One further caution on low counts: 13 of the 180 induction-arm genes sit below 5 CPM and one below 1 (PINCR,
0.65), where a zero count still receives a log2 CPM set by library size alone.

## Links

- [[p53 program P]] — what the programme is, and the direction trap
- [[Cross-fitting and circularity]] — what the circular columns may and may not be used for
- [[Nulls and calibration]] — the permutation FDR used in every selection here
- [[The screen model]] · [[How the numbers are decided]] · [[Signing genes by p53 direction]]
- [[The p53 pathway]] · [[Per-line p53 function]] · [[The measurement with controls]] — where the score is
  used as an outcome
- [[Genes — Map of Content]] · [[Methods — Map of Content]]

## Sources

- `mg53_p53/genome_wide/genome_wide.py` — module docstring section B (the full derivation in order); the
  constants at lines 137-144 (`TOPK_FRAC`, `TOPN_FRAC`, `PROG_MIN`, `PROG_FALLBACK`, `N_NULL_PROG`,
  `N_FEAT_PERM`, `Q_SEL`); the section B table documentation at lines 2030-2085.
- `mg53_p53/genome_wide/tables/b_drugdose_p53_activation.csv` — S1 and S2 per drug-dose, with the fold
  assignment and the out-of-fold scores.
- `mg53_p53/genome_wide/tables/b_p53_program_genes.csv.gz` — per gene: `z_program`, `q_up`/`q_down`,
  `wt_mean_log2`, `wt_minus_alt_log2`, `frac_compounds_*`, `in_P`, `in_P_down`, `in_P_minus_foldF`,
  `in_P_noX`, `loco_frequency`, `rank_in_P`.
- `mg53_p53/genome_wide/tables/b_p53_program.csv` — the members of both arms with their stability columns.
- `mg53_p53/genome_wide/tables/b_program_stability.csv` — fold and leave-one-compound-out Jaccards, null S1
  / S2 and null programme sizes.
- `mg53_p53/genome_wide/tables/b_feature_specificity.csv` — every other line grouping on the same scale.
- `mg53_p53/findings/MG53_p53_TABLES.md` — the full-programme section, its column glossary and its caveats.
