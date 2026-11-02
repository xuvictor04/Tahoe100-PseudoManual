---
type: concept
tags: [concept, p53, method]
status: current
---

# p53 program P

> [!summary] In one line
> The 195-gene signature this study derived from its own data to stand in for "p53 output" — 180 genes p53
> induces and 15 it represses — and the thing to remember is that it was selected using the TP53 labels.

## What it is

Rather than trusting a published p53 signature, the pipeline derives one from this dataset: genes whose
response to drugs differs between TP53-wild-type and TP53-altered lines in a consistent direction across
compounds. The result has two arms.

| Arm | Genes | What it means | Fold change, WT lines |
|---|---|---|---|
| **P** (induction) | 180 | p53 raises them | up to 1.255× ([[MDM2]], the largest) |
| **P-down** (repression) | 15 | p53 lowers them | 0.87× to 0.96× |

The arms are disjoint, and no gene is significant in both directions. They separate cleanly on how often
each gene moves: induction-arm genes are moved **up** by 64–99% of the 98 reference compounds (median 79%),
repression-arm genes are moved **down** by 70–81%.

The repression arm is biologically coherent — HJURP, SGO1, CENPN, KIF11, CCNE2, EXO1, FANCD2, BRCA2, USP1,
RAD54B, SMC1A: cell-cycle and DNA-repair genes, which is what [[The p21-DREAM axis]] predicts p53 should
lower, indirectly, through p21.

A per-line, per-exposure **score** is built from the arms (`P_r2` and `P_down_r2`) and that score, not any
single gene, is the outcome in every "p53 activity" measurement here.

## Two reasons to be careful with it

**It is circular where it touches p53.** Membership, each gene's rank, and the wild-type fold-change columns
were all computed using the TP53 genotype labels. They describe the programme accurately but cannot be used
to argue that something is *p53-specific* — that would be testing a hypothesis on the data that defined it.
Every gene note flags this, and the countermeasures are in [[Cross-fitting and circularity]]: 5-fold
cross-fitting, leave-one-compound-out stability, and a parallel **label-free** programme used to repeat the
key per-line scoring without the labels. The MG53 screen columns, by contrast, never used the TP53 labels and
are not circular.

**Membership is often unstable.** `n_folds_kept` counts how many of the 5 cross-fitting folds re-selected a
gene. Of the 67 genes with an MG53 verdict, 20 were kept in 0 or 1 folds. `loco_frequency` — stability over
98 leave-one-compound-out programmes — averages 0.97 for the induction arm but is **not computed for the
repression arm at all**, so those 15 genes read blank and must be judged on `n_folds_kept` alone.

## Reading the fold change

`wt_mean_log2` is small for every gene — the median program gene reads about 1.06× — and that is not
dilution by irrelevant drugs. It is small for two specific reasons:

1. the baseline is the plate's **drug**-well median, not vehicle, so it measures "more than a typical drug";
2. it is a **compound-equal mean** over the 142 p53-activating drug-doses, each of 98 compounds carrying
   1/98, so one strong activator is averaged with 97 weaker ones.

It is not "the fold change under a strong activator". An earlier version of the write-ups said the first part
of this wrongly; see [[Corrections and retractions]].

## The direction trap

Because the two arms respond oppositely, a per-gene tally of MG53 slopes is meaningless unless signed into
p53-output units first. Doing so is what turns "34 positive, 33 negative" into "35 toward more p53 output, 32
toward less" — the same even split, but now a statement with content. See
[[Signing genes by p53 direction]].

## Links

- [[The p53 pathway]] · [[The p21-DREAM axis]] · [[Signing genes by p53 direction]]
- [[Cross-fitting and circularity]] · [[Program P derivation]] — the mechanics
- [[Downstream of MG53]] — what the score was used for
- [[Genes — Map of Content]] — the genes, grouped by arm

## Sources

- `genome_wide/tables/b_p53_program.csv`, `b_p53_program_genes.csv.gz`, `b_program_stability.csv`
- `export/downstream/program_members.csv` — one row per member with its arm and stability columns
- `export/downstream/program_scores_per_drugdose_line.csv` — the per-line score
- `mg53_p53/findings/tables/tableD_p53_target_genes.csv` — the vault's working copy, 195 rows
