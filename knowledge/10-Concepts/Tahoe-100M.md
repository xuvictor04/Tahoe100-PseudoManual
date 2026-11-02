---
type: concept
tags: [concept, dataset]
status: current
---

# Tahoe-100M

> [!summary] In one line
> About 100 million single-cell transcriptomes from 50 pooled cancer cell lines exposed to 379 drugs at three
> doses — the dataset this entire study is built on, and the source of all of its limits.

## The design

| | |
|---|---|
| Cell lines | 50, **pooled in the same well** and demultiplexed afterwards |
| Drugs | 379, each at **three doses**: 0.05, 0.5 and 5 µM |
| Drug-doses | 1,132 usable |
| Plates | 14 |
| Time point | **24 h**, and only 24 h |
| Readout | single-cell mRNA (3′-biased short reads) |
| Controls | DMSO wells on every plate |

Pooling is the design's great strength: all 50 lines in a well share the same drug, the same incubation and
the same library preparation, so comparing lines *within* a well removes almost every batch variable by
construction. That is what makes the within-drug-dose contrasts in this study possible at all.

## The consequences that shape every result here

**One time point.** Everything is a 24 h snapshot of mRNA. A transcriptional change that is transient, or
that happens at the protein level, is invisible. For a gene like [[MG53 (TRIM72)]], whose known biology is
almost entirely post-translational, this is the central limitation and not a footnote.

**No genetic perturbation.** Tahoe perturbs with drugs, not with knockdowns or knockouts. Nothing in it
perturbs MG53. Every MG53 result in this study is therefore an *association* across drugs and cell lines, and
causal language is never appropriate for it. The nearest thing to a knockout available is genotype: the ten
lines with no intact TP53 allele, used as a control arm in [[The measurement with controls]].

**Replication is thin where it matters.** 1,024 of the 1,132 drug-doses sit in a **single well**. So for most
exposures there is no replicate to check a result against, and the 89 cross-batch pairs that do exist agree
only moderately for a trace gene — Spearman +0.358 for MG53, with 95% limits of agreement of −0.779 to
+0.824 log2. See [[Why MG53 is hard to measure here]].

**Plate structure is strong.** Lines and drugs are not balanced across the 14 plates, and some genes carry
very large untreated plate-to-plate differences. MG53's is the largest in the dataset at 3.124 log2. Any
correlation computed across exposures without accounting for plate is partly a correlation across plates —
see [[Plate batch effects]], where this produces one of the study's near-misses.

**Depth is low per cell.** A trace transcript may be 0 or 1 UMIs in most cells; MG53 has a median of 5 UMIs
per profile and 12.4% of profiles at zero. Two thirds of the variance in its measured fold change is plain
counting noise, with no over-dispersion needed to explain it.

**Pooled lines mean composition matters.** A drug that kills one line changes the mix of cells in the well,
which moves every pooled average. The pipeline carries a composition-shift correction and a per-line
baseline for exactly this reason.

## How this study processes it

Rather than re-reading the cells, the pipeline builds an **atlas** once (`tahoe_atlas.py`) and a **gene
panel** extract (`tahoe_gene_panel.py`), then nine analysis steps read those. The quantity used almost
everywhere is a corrected log2 fold change, `r2`:

- baseline = the same cell line's median over that plate's **drug** wells (not the vehicle wells),
- with a composition-shift correction and a well-position correction applied.

That baseline choice is worth remembering when reading any fold change here: it measures "more than a typical
drug does", not "more than untreated". It is why the median p53-program gene reads only about 1.06× under
p53-activating compounds. See [[The screen model]].

## Links

- [[Why MG53 is hard to measure here]] · [[Plate batch effects]] · [[Reliability and disattenuation]]
- [[The screen model]] · [[Two-way fixed effects]]
- [[What this study found]]
- `docs/method-v3.md` in the repository for what the current method version changed

## Sources

- The dataset: [tahoebio/Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) on Hugging Face.
- Design and plate census: `export/metadata/plates.csv`, `export/metadata/drug_doses.csv`,
  `export/metadata/cell_lines.csv`.
- This study's run: `export/run_info.json`, `export/checks.csv`.
