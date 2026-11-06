# Method: from 96 million cells to a gene map

Every number in the outputs comes from one chain of steps. The first two (build, effects) are the earlier project's
method v3, carried over **verbatim** (see [Provenance](#provenance)); the rest are new and work from its outputs.

## 1. Build — counts per well × cell line × gene

One pass over all ~96M cells sums each cell's raw UMI counts into its (well, cell line) profile: 1,344 wells × 50
lines × 62,713 gene tokens, stored per plate (`atlas/pseudobulk/`). The well's position on the plate (A1…H12) is read
from the cell barcode. `--stream` does the same pass over files fetched from Hugging Face one at a time, so the
430 GB download is not needed (the summing code is the same function; only the file opener differs).

## 2. Effects — the corrected effect of every drug-dose on every gene (method v3)

For each plate, each profile's level is `log2 CPM` (counts + 0.5 over total + 1, × 10⁶), set to "not measured" when
the line has < 30 cells in the well or does not express the gene (below 25% of the median line). Then:

- **Baseline** = the same line's median over the plate's drug wells (never DMSO: two DMSO wells per plate are too
  few, and the median drug well is a typical "nothing much happened" well). Every fold change in the outputs is
  relative to this baseline.
- **Composition shift**: a median-of-ratios size factor per profile (as DESeq2), so a drug that makes a few genes
  take most of the reads does not make every other gene look lower.
- **Well-position correction**: the plates share layouts, so a drug sits at the same position on every plate. The
  position effect of a well is the median of the *other* drugs' wells at that position, computed twice — the second
  time only from donors that are themselves unremarkable for that gene, so a strong neighbour cannot leak in.
- **Robust z** against the spread of the drug wells on reliable plates, widened per plate and dose by a **plate
  factor** (plates 2 and 3 were ~1.4–2× noisier), and per gene where that gene alone is noisier on a plate.
- **Plate 13 is unreliable** (its replicate wells do not reproduce: median r −0.06); its wells are used only for
  drug-doses that have no other well, and flagged.
- **Drug-dose** = mean over its wells (log2 fold change) and Stouffer over its wells (z); **BH FDR within each gene**
  across drug-doses; significant = q < 0.10 and ≥ 1.2×.
- Every drug-dose carries **flags** (exact strings, below). "Clean" in the outputs means: none of the artifact flags.

| Flag | Means | Artifact? |
|---|---|---|
| `toxic` | < −1 log2 cells vs the plate (beyond its row's shift), the best well < −0.5 too, no higher dose recovering | yes |
| `transcription drop` | genes or UMIs per cell fall vs the plate and its row (< −0.3 / < −0.5 log2): global shutdown | yes |
| `cell-cycle shift` | S or G2/M module moved > 0.5 log2 (or > 0.25 with \|z\| ≥ 4): cycle genes follow the cycle mix | yes |
| `unreliable plate only` | only wells on an unreliable plate (plate 13) | yes |
| `position not correctable` | < 3 other-drug wells at the position | yes |
| `position correction uncertain` | (per gene) < 3 clean donors at the position: not corrected | yes |
| `wells disagree` | ≥ 2 wells whose z over the top 500 genes correlate at r < 0.1 | yes |
| `low cells (technical?)` | < half the plate's cells, not confirmed as dose-consistent loss | caveat |
| `plate-row cell shift` | the plate row moved together (technical) | caveat |
| `composition shift` | composition shift ≥ 0.2 log2: effects are relative to the median gene | caveat |
| `noisy plate (z scaled)` | plate factor > 1.2: its z were divided by it | caveat |
| `position effect removed` | (per gene) the position correction moved the value by > 0.2 log2 | caveat |

## 3. Tensor — the per-cell-line layer

The atlas kept only the median over cell lines. The tensor stage re-derives, from the same build and with the same
functions, every profile's residual and subtracts the same position effect, so that for every gene *g*, well *w*,
line *l* and drug-dose *d*:

- `R[g, w, l]` = corrected log2 effect in that well and line,
- `DDL_lfc[g, d, l]` = mean over the drug-dose's wells = log2 fold change in that line vs its own baseline,
- `DDL_z[g, d, l]` = Stouffer over its wells of (R − c) / s / plate factor, with c, s the robust centre and spread of
  that gene in that line over the reference wells.

It checks itself while running: the median over lines of its residuals must reproduce the atlas's W1 on every plate,
and its re-derived position effect must reproduce W2 — both to float32 precision, or the run stops.

## 4. Tables — the fold-change tables

Per gene × drug-dose (pooled over lines), per gene × cell line, the top (drug-dose, line) cells per gene, per drug,
per line, per plate, per well. `tables/README.md` (written by the stage) documents every column. "Lines up" counts
the lines where that drug-dose moves the gene by ≥ 1.2× with per-line z ≥ 2.

## 5. Embed — the vector space

Each gene is described by its per-line z in every (drug-dose, cell line) context of an *active, trustworthy*
drug-dose (≥ 10 significant genes; not `unreliable plate only`, `position not correctable` or `wells disagree`).
Genes that never respond (|z| ≥ 3 in < 5 contexts) and noise RNAs are left out of the space (they keep their tables).
Each gene's row is centred and scaled; broad components that a large share of genes follow (global toxicity or
shutdown; the earlier atlas's rule) are removed; then a truncated SVD, `X ≈ U S Vᵀ`, gives (64 dimensions by
default):

| Vector | Definition | Meaning |
|---|---|---|
| gene | `g = U S` | its direction is the gene's response pattern; cosine between two genes = correlation of their denoised response profiles |
| context (drug-dose × line) | `c = V` | `g · c` ≈ the gene's z in that context |
| drug-dose | `d = S⁻¹ Uᵀ x` (x = its pooled z profile) | `g · d` ≈ the drug-dose's z on the gene ("vector comparison reproduces activity") |
| line (response) | per component, the slope of the line's context vectors on the drug-doses' mean | 1 = typical line, 0 = that programme does not respond in this line |
| line (baseline) | its untreated profile projected the same way | which programmes are constitutively high in the line |

The space is also fitted on two **halves of the compounds** (salt forms kept together), so that every relation can
be checked on independent perturbations.

## 6. Relations — gene × gene

For each gene, its 100 partners with the largest |cosine|, each with: the signed cosine; `z_gene` (how exceptional
the partner is for this gene); the cosines in the two half-spaces; **evidence** (`both halves` = same sign in the full
space and both halves with |cos| ≥ 0.2 in each; `one half` = strong in one half only, i.e. a relation seen with one
drug family); a **sign-concordance FDR** (pairs are selected in one half and checked in the other, whose noise is
independent; under no relation the sign agrees half the time, so FDR(t) = disagreeing / agreeing pairs above t); and
genomic and literature flags (same locus ≤ 50 kb; readthrough risk = same strand, ≤ 20 kb, the 5′ gene ≥ 8× more
expressed; shared HGNC gene group; shared Hallmark or Reactome pathway of ≤ 300 genes; STRING score ≥ 400).
A **novel candidate** is a pair with evidence in both halves, FDR ≤ 0.05, |cos| ≥ 0.5, no literature link, not the
same locus, and both genes described by HGNC.

## 7. Graph — the nodal map

See [vector-space-and-nodal-map.md](vector-space-and-nodal-map.md). In short: modules are Louvain communities of the
graph linking each gene to its 15 strongest partners by |cos| (excluding "not reproduced"); each module has a + and a
− arm (the sign of each member on the module's main direction); the nodal map is a t-SNE layout of 1 − |cos|; the
signed map is the same on 1 − cos.

## 8. Reference, validation, vault, map

Public annotations (HGNC, Ensembl GRCh38 r112 coordinates, UniProt function, NCBI summaries, Reactome, MSigDB
Hallmark, STRING v12) are downloaded once and cached; every source is optional. Validation scores the space against
curated control programmes that were not derived from Tahoe (`tahoemap/data/control_sets.json`) and against Hallmark
and Reactome, tests the opposite-arm prediction, labels modules by enrichment, and lists novel candidates. The vault
and the HTML map present all of it.

## Caveats that apply everywhere

- **Correlation is not mechanism.** There are no genetic perturbations in Tahoe-100M; "moves with" means the two
  genes respond alike across ~1,100 drug-doses in 50 lines, not that one regulates the other. "Upstream" and
  "downstream" are reserved for regulatory claims, never chromosomal position (that is "5′ of" / "3′ of").
- **One time point** (24 h): a gene that responds late or transiently can look unrelated to its regulator.
- **Most drug-doses sit in one well** (1,024 of 1,132): their significance rests on the spread of other drug wells,
  not on replicates.
- **Dose is confounded with plate** (each plate holds one dose).
- **Readthrough**: transcription running past a highly expressed 5′ gene on the same strand is counted as the 3′
  gene's mRNA, so such pairs correlate without regulation. They are flagged, never called novel.
- **Ambient RNA**: lines that do not express a gene read only the well's ambient RNA; they are not measured for that
  gene (NaN), which also means re-expression of a silenced gene in that line is not detected by these tables.

## Provenance

`tahoemap/atlas_core.py` and `tahoemap/tlib.py` are the build and effects code of `tahoe_atlas.py` and
`tahoe_mtap_gankyrin.py` at commit `28cd834` (branch `claude/tahoe100m-gene-pipeline-lodlx7`), copied function by
function by syntax tree (`tools/port_from_old.py`, manifest `tahoemap/PORT_MANIFEST.tsv`); only the import header
is new. On the synthetic test data, every array and table the ported `build` and `effects` write is identical,
bit for bit, to the old scripts' output.
