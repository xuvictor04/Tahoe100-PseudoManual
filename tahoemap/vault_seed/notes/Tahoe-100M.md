---
type: concept
tags: [concept, dataset]
status: current
---

# Tahoe-100M

> [!summary] In one line
> About 100 million single-cell transcriptomes from 50 pooled cancer cell lines exposed to 379 drugs at three
> doses — the dataset every note in this vault is built on, and the source of all of its limits.

## The design

| | |
|---|---|
| Cell lines | 50, **pooled in the same well** and demultiplexed afterwards |
| Drugs | 379, each at **three doses**: 0.05, 0.5 and 5 µM |
| Drug-doses | 1,132 usable |
| Plates | 14 × 96 wells; each plate holds one dose |
| Time point | **24 h**, and only 24 h |
| Readout | single-cell mRNA (3′-biased short reads) |
| Controls | DMSO wells on every plate (two per plate) |

Pooling is the design's great strength: all 50 lines in a well share the same drug, the same incubation and
the same library preparation, so comparing lines *within* a well removes almost every batch variable by
construction. That is what makes the per-cell-line fold changes in this vault comparable across lines.

## The consequences that shape every result here

**One time point.** Everything is a 24 h snapshot of mRNA. A transcriptional change that is transient, or
that happens at the protein level, is invisible. For a gene whose known biology is mostly post-translational
(the earlier MG53/p53 study's [[TRIM72]] is the extreme case), this is the central limitation and not a footnote.

**No genetic perturbation.** Tahoe perturbs with drugs, not with knockdowns or knockouts. Every gene–gene
relation in this vault is therefore an *association* across drugs and cell lines — two genes that respond alike —
and causal language is never appropriate for it. The nearest thing to a knockout available is genotype: lines with
no intact allele of a gene (for [[TP53]], ten of the 50) can serve as a control arm; see
[[p53 nullification in cancer cell lines]].

**Replication is thin where it matters.** 1,024 of the 1,132 drug-doses sit in a **single well**. So for most
exposures there is no replicate to check a result against: a drug-dose's z rests on the spread of the *other* drug
wells, not on its own replicates. In the earlier MG53/p53 study, the 89 cross-batch pairs that do exist agreed only
moderately for a trace gene (Spearman +0.358 for MG53, 95% limits of agreement −0.779 to +0.824 log2). Low-level
genes should be read with that in mind.

**Plate structure is strong.** Lines and drugs are not balanced across the 14 plates, each plate holds one dose,
and some genes carry very large untreated plate-to-plate differences (the largest found was 3.124 log2, for
TRIM72). Any correlation computed across exposures without accounting for plate is partly a correlation across
plates — see [[Plate batch effects]].

**Depth is low per cell.** A trace transcript may be 0 or 1 UMIs in most cells; MG53 had a median of 5 UMIs per
profile and 12.4% of profiles at zero, and two thirds of the variance in its measured fold change was plain
counting noise. Genes near the detection floor carry the same limitation; see [[Reliability and disattenuation]].

**Pooled lines mean composition matters.** A drug that kills one line changes the mix of cells in the well,
which moves every pooled average. The pipeline carries a composition-shift correction and a per-line baseline for
exactly this reason.

**Readthrough.** Short 3′ reads cannot tell a gene's own transcript from polymerase that ran past a highly
expressed 5′ neighbour on the same strand; see [[Readthrough spillover]].

## How tahoemap processes it

The cells are read once into counts per well × cell line × gene (the *build*), then the earlier project's
method v3 (*effects*) computes the corrected effect of every drug-dose on every gene. The quantity used almost
everywhere is a corrected log2 fold change:

- baseline = the same cell line's median over that plate's **drug** wells (not the vehicle wells),
- minus a composition-shift (library) correction and a well-position correction,
- pooled over lines (median per well) for the drug-dose tables, and kept per line in the tensor.

That baseline choice is worth remembering when reading any fold change here: it measures "more than a typical
drug does", not "more than untreated". In the earlier study it is why the median p53-programme gene read only
about 1.06× under p53-activating compounds.

## Sources

- The dataset: [tahoebio/Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) on Hugging Face.
- The method: `docs/method.md` in the tahoemap repository; the run's own `atlas/build_info.json` and
  `atlas/effects/info.json`.
- MG53 figures: the earlier MG53/p53 study (`mg53_p53/findings/` of the old pipeline), quoted as examples.
