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
- Every drug-dose carries **flags** (exact strings, below). "Clean" in the outputs means: none of the artifact flags
  (for that gene: the drug-dose's flags plus the gene's own, with the cell-cycle shift judged gene by gene, §4).
  **A flag never removes anything from what is shown.** Every table keeps flagged rows; the vault, the map, the
  look-ups and the review dossiers show a flagged item in its ranked place with an alert, '⚠' plus the flags in plain
  words (e.g. '⚠ toxic; transcription drop', '⚠ cell-cycle shift, explains ~60% of this change'), and every list
  says how many items it holds and how many carry an alert. A list capped at N shows the N strongest overall and any
  of the N strongest without an alert that would otherwise fall below the cut, sorted together, so flagged items
  never push clean ones out of view either. The same holds for every other reason to doubt: a partner not replicated
  in both halves, neighbours on the genome, a gene in the vector space only through flagged drug-doses, a gene
  outside the space. Estimators may still leave out data that is technically broken (the vector space leaves out the
  drug-doses flagged `unreliable plate only`, `position not correctable` or `wells disagree`; the per-line cut is
  calibrated on clean drug-doses); that is computing, not showing, and the outputs say where they do it.

| Flag | Means | Artifact? |
|---|---|---|
| `toxic` | < −1 log2 cells vs the plate (beyond its row's shift), the best well < −0.5 too, no higher dose recovering | yes |
| `transcription drop` | genes or UMIs per cell fall vs the plate and its row (< −0.3 / < −0.5 log2): global shutdown | yes |
| `cell-cycle shift` | S or G2/M module moved > 0.5 log2 (or > 0.25 with \|z\| ≥ 4): cycle genes follow the cycle mix | yes, unless the shift does not explain this gene's change (§4) |
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
and its re-derived position effect must reproduce W2 — both to float32 precision, or the run stops. (On the real
data, all 14 plates reproduce W1 with a maximum difference of 0.0.)

After that check, two kinds of per-line values are set to "not measured" (NaN), because they would otherwise look
like responses:

- **ambient-only lines**: a line whose own level of the gene is below 0.25 × the gene's pooled level reads mostly the
  well's ambient RNA, which mirrors what the other lines do (the atlas's "expressed" rule compares with the median
  line, so for a gene expressed in a minority of lines it lets ambient lines through). `tensor/line_measured.npy`
  records which lines measure which genes.
- **uncountable profiles**: where the expected count (the line's level × the profile's total UMI) is below 2, the
  +0.5 pseudocount dominates and a line thinned out by a drug shows false rises.

## 4. Tables — the fold-change tables

Per gene × drug-dose (pooled over lines), per gene × cell line, the top (drug-dose, line) cells per gene, per drug,
per line, per plate, per well. `tables/README.md` (written by the stage) documents every column.

- The **pooled** tables (`drug_effects`, the raised / lowered lists) are the atlas's: the effect is the **median over
  cell lines**, so a response seen in fewer than about half of the measured lines (e.g. one confined to TP53-wild-type
  lines) does not reach them; it appears in the per-line tables.
- "Lines up / down" next to a pooled call is descriptive: the lines where that drug-dose moves the gene by ≥ 1.2× with
  per-line z ≥ 2.
- The **per-line** tables (`line_effects`, `drug_line_top`) search ~1,100 drug-doses per gene and line, so their cut
  is calibrated on the run itself: from the per-line |z| of (gene, clean drug-dose) pairs with no pooled response, the
  threshold at which fewer than 0.05 chance hits are expected per gene and line (never below 4); it is written to
  `tables/info.json`. The per-line tables then rank **every** drug-dose: `drug_line_top` keeps each gene's 15
  strongest cells per direction over all drug-doses plus any of its 15 strongest clean cells beyond them, with their
  `flags` and `clean`; `line_effects` keeps its counts and strongest drug-dose over clean drug-doses and adds the same
  over all drug-doses (`n_dd_up_all`, `best_up_drug_all`, `best_up_flags_all` ...).
- **The cell-cycle shift, gene by gene.** A drug-dose that moves the S-phase or G2/M programme carries the flag
  `cell-cycle shift` for every gene, yet it explains the change of a cell-cycle gene, not necessarily of a gene with
  little cell-cycle dependence. For each gene a robust regression of its pooled log2 fold change on the drug-doses'
  S-phase and G2/M module changes (over the drug-doses whose only artifact flag, if any, is the cell-cycle shift; at
  least 20) gives its slopes (`genes.parquet` cc_slope_S, cc_slope_G2M). At each drug-dose flagged `cell-cycle
  shift`, the slopes predict how much of the gene's change the shift explains (`drug_effects.parquet` cc_share; 0
  when the prediction goes the other way), fitted again without that drug-dose (leave-one-out, so a strong change
  of the gene's own there does not pull its slopes toward explaining it). Fitted slopes are attenuated by noise, so the rule doubles them: when even
  the doubled prediction explains less than half of the change, and what is left is still ≥ 1.2×, the shift is not
  the explanation; the gene's flags then read `cell-cycle shift (explains ~N% here)`, which is no artifact flag, and
  the value can be clean. Otherwise the artifact flag stays and the alert says how much it explains. On planted data,
  0 of the 154 significant changes of the S-phase and G2/M programme genes at such drug-doses are cleared. On the
  real data, Idarubicin 5 µM raises TRIM72 (MG53) 12.2× with the cell-cycle flag; its slopes predict ~4% of that
  change, so the rise is the gene's own response, not the cycle mix.

## 5. Embed — the vector space

Each gene is described by its per-line z in every (drug-dose, cell line) context of an *active, trustworthy*
drug-dose: not `unreliable plate only`, `position not correctable` or `wells disagree`, and either ≥ 10 significant
genes pooled over lines, or ≥ 10 genes at per-line |z| ≥ 5 in ≥ 2 lines (so a response confined to a few lines
counts). A gene enters the space only if it responds: |z| ≥ 3 in ≥ 5 contexts **and** a significant pooled
drug-dose (q < 0.1, ≥ 1.2×) or a per-line |z| ≥ max(5, the calibrated per-line cut) in ≥ 2 lines of one drug-dose. (A
count alone is reached by chance by almost every expressed gene at full scale.) Evidence at a drug-dose with an
artifact flag for the gene counts too: a gene whose only evidence, pooled and per-line, is at such drug-doses is in
the space, marked
(`embed/genes.parquet` evidence_flagged_only) and shown with an alert wherever it appears, because its vector,
partners and module may reflect the artifact. Noise RNAs are left out. Genes outside the space keep all their
tables and notes, and are shown with '⚠ not in the vector space' and the reason.
Each gene's row is centred and scaled; broad components that a large share of genes follow (global toxicity or
shutdown; the earlier atlas's rule) are removed; then a truncated SVD, `X ≈ U S Vᵀ`, gives (64 dimensions by
default):

| Vector | Definition | Meaning |
|---|---|---|
| gene | `g = U S` | its direction is the gene's response pattern; cosine between two genes = correlation of their denoised response profiles |
| context (drug-dose × line) | `c = V` | `g · c` ≈ the gene's z in that context |
| drug-dose | `d = S⁻¹ Uᵀ x` (x = its pooled z profile) | `g · d` ≈ the drug-dose's z on the gene ("vector comparison reproduces activity") |
| drug | `Uᵀ x` of its best trustworthy dose | drug–drug cosine (weights the components by their size) |
| line (response) | per component, the slope of the line's context vectors on the drug-doses' mean | 1 = typical line, 0 = that programme does not respond in this line |
| line (baseline) | its untreated profile projected the same way | which programmes are constitutively high in the line |

The space is also fitted on two **halves of the compounds** (salt forms kept together), so that every relation can
be checked on independent perturbations.

## 6. Relations — gene × gene

For each gene, its 100 partners with the largest |cosine|, each with: the signed cosine; `z_gene` (how exceptional
the partner is for this gene); the cosines in the two half-spaces; a **sign-concordance FDR** (pairs are selected in
one half and checked in the other, whose noise is independent; under no relation the sign agrees half the time, so
FDR(t) = (disagreeing + 1) / agreeing pairs above t; a pair is scored at the smaller of its two half cosines);
**evidence** (`both halves` = same sign in the full space and both halves, |cos| ≥ 0.2 in each, **and FDR ≤ 0.10**;
`one half` = strong, |cos| ≥ 0.5, in one of the two random halves only — the halves are a hash split of compound
names, so this is not replication and carries no error estimate; often a response driven by one compound); and
genomic and literature flags (same locus ≤ 50 kb; readthrough risk = same strand, ≤ 20 kb, the 5′ gene ≥ 8× more
expressed; shared HGNC gene group; shared Hallmark or Reactome pathway of ≤ 300 genes; STRING score ≥ 400).
Each pair also carries its **specificity**: whether each gene is among the other's strongest partners (`mutual_rank`)
and how exceptional the pair is for both genes (`specificity` = the smaller of the two `z_gene`). On the full data,
broad programmes make hundreds of thousands of pairs replicable; specificity separates a particular relation from
membership of the same large programme (mutually-top pairs are ~3× more often already known).
A **novel candidate** is a pair that is mutually among the 10 strongest partners with specificity ≥ 4, has evidence
in both halves, FDR ≤ 0.05, |cos| ≥ 0.5, no literature link, is not the same locus, with both genes described by
HGNC and placed on the genome — and only when HGNC, Ensembl, STRING and
Hallmark or Reactome all loaded (otherwise `relations/info.json` and the report say novelty was not assessed).

## 7. Graph — the nodal map

See [vector-space-and-nodal-map.md](vector-space-and-nodal-map.md). In short: modules are Louvain communities of the
graph linking each gene to its 15 strongest partners by |cos| ≥ 0.3 that are replicated (`both halves`) or very strong
in one half (|cos| ≥ 0.5). A module has a − arm only when ≥ 5 members sit on the negative side of its main direction
and the two sides anti-correlate (mean cosine between them ≤ −0.2); otherwise it is single-armed (all +).
`graph/modules.parquet` gives the mean cosine within each arm and between the arms. A first Louvain pass over the
whole genome returns programme-sized communities of 1,000+ loosely related genes, so modules larger than 300 genes
or looser than a mean member |cos| of 0.3 are split again on their own subgraph (up to 4 levels); pieces under 5
genes get no module (module 0). The nodal map is a t-SNE layout of 1 − |cos|; the signed map is the same on 1 − cos.
t-SNE keeps neighbours together but can let modules touch or interleave, so each map also has a **spread** layout
(the map's Spread slider): each module keeps its own t-SNE arrangement as one block, the blocks are placed by the
modules' directions in the full vector space (classical MDS refined by SMACOF on 1 − |cos|, or 1 − cos for the signed
map, between module directions), overlapping blocks are pushed apart, and genes without a module move with their 5
nearest module genes. On planted data the share of a module gene's 5 nearest module genes that belong to another
module falls from 9.5% to 0.4% (nodal map).

## 8. Reference, validation, vault, map

Public annotations (HGNC, Ensembl GRCh38 r112 coordinates, UniProt function, NCBI summaries, Reactome, MSigDB
Hallmark, STRING v12) are downloaded once and cached; every source is optional. Validation scores the space against
curated control programmes that were not derived from Tahoe (`tahoemap/data/control_sets.json`) and against Hallmark
and Reactome, tests the opposite-arm prediction, labels modules by enrichment, and lists novel candidates (its lists
keep flagged items with an alert too). The vault and the HTML map present all of it. The map has, besides the two
maps and their Spread slider, a **k-D tour** (the genes' unit vectors in all dimensions projected onto a 2-D plane
that turns smoothly, or one component against another exactly), and three physics simulations: a gene's
neighbourhood (its partners and theirs, to depth 1-4, up to 2,000 genes), one module, and all genes.

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
- **Ambient RNA**: lines that do not express a gene (or express it below a quarter of its pooled level) read mostly
  the well's ambient RNA; they are not measured for that gene (NaN), which also means re-expression of a silenced gene
  in that line is not detected by these tables.
- **Pooled = median over lines**: a drug that moves a gene in only a few lines does not appear in the pooled lists;
  read the per-line tables (and the vault's "In which cell lines" section).

## Provenance

`tahoemap/atlas_core.py` and `tahoemap/tlib.py` are the build and effects code of `tahoe_atlas.py` and
`tahoe_mtap_gankyrin.py` at commit `28cd834` (branch `claude/tahoe100m-gene-pipeline-lodlx7`), copied function by
function by syntax tree (`tools/port_from_old.py`, manifest `tahoemap/PORT_MANIFEST.tsv`); only the import header
is new. On the synthetic test data, every array and table the ported `build` and `effects` write is identical,
bit for bit, to the old scripts' output.
