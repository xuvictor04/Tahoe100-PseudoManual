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
- Every drug-dose carries **flags** (exact strings, below). The **flags of record** are the atlas's flags plus the
  tables stage's neighbouring-well and translation-inhibitor tokens (§4; `tables/drugdoses.parquet` flags; the
  atlas's own are `atlas_flags`). "Clean" in the outputs means: none of the artifact flags (`common.ARTIFACT_FLAGS`:
  the atlas's seven and 'like a neighbouring well'; for that gene: the drug-dose's flags plus the gene's own, with the
  cell-cycle shift and the neighbouring-well flag judged gene by gene, §4).
  **A flag never removes anything from what is shown.** Every table keeps flagged rows; the vault, the map, the
  look-ups and the review dossiers show a flagged item in its ranked place with an alert, '⚠' plus the flags in plain
  words (e.g. '⚠ toxic; transcription drop', '⚠ cell-cycle shift, explains ~60% of this change'), and every list
  says how many items it holds and how many carry an alert. A list capped at N shows the N strongest overall and any
  of the N strongest without an alert that would otherwise fall below the cut, sorted together, so flagged items
  never push clean ones out of view either. The same holds for every other reason to doubt: a partner without the
  same sign in both halves of the compounds, a lineage pair, a read-sharing copy, neighbours on the genome, a gene in the vector space only through flagged drug-doses, a gene
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
| `like a neighbouring well` | Many genes this drug-dose changes are changed the same way, more strongly, in a well right next to it on the same plate (another compound), and the drug's higher doses do not change them. The signal may have come from that well (carried over, or a local problem on that part of the plate). Artifact flag for these genes. | yes, for the genes the neighbour moves the same way (§4) |
| `like a neighbouring well (not this gene)` | This drug-dose shares much of its signature with a neighbouring well, but the neighbour does not change this gene the same way, so this value is not under that suspicion. Not an artifact flag. | caveat |
| `like a neighbouring well (top dose)` | At the drug's top dose many genes it changes are changed the same way in a neighbouring well (another compound), and its lower doses do not change them. With no higher dose to check, the data cannot tell a carried-over signal from a real effect. Not an artifact flag. | caveat |
| `translation inhibitor` | The drug stops protein synthesis (tahoemap/data/drug_classes.json). Not an artifact flag. | caveat (a class, not a technical flag) |
| `rise under a translation inhibitor` | Rise under a translation inhibitor: the drug stops protein synthesis, which raises many short-lived mRNAs whatever their pathway (the proteins that switch their genes off or break them down are no longer made). Read it as possible mRNA stabilisation, not as activation of the gene's pathway. Not an artifact flag. | caveat |

The last five rows are added by the tables stage (since tables version 5); their words are `common.FLAG_TEXT`, and
every surface shows those words with the token (a caveat once under the list that shows it).

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
  least 20) gives its slopes (`genes.parquet` cc_slope_S, cc_slope_G2M). At each drug-dose flagged `cell-cycle shift`,
  the slopes predict how much of the gene's change the shift explains (`drug_effects.parquet` cc_share; 0 when the
  prediction goes the other way), fitted again without that drug-dose (leave-one-out, so a strong change of the gene's
  own there does not pull its slopes toward explaining it). Fitted slopes are attenuated by noise, so the rule doubles
  them: when even the doubled prediction explains less than half of the change, and what is left is still ≥ 1.2×, the
  shift is not the explanation; the gene's flags then read `cell-cycle shift (explains ~N% here)`, which is no artifact
  flag, and the value can be clean. Otherwise the artifact flag stays and the alert says how much it explains. On
  planted data, 0 of the 154 significant changes of the S-phase and G2/M programme genes at such drug-doses are cleared.
  On the real data, Idarubicin 5 µM raises TRIM72 (MG53) 12.2× with the cell-cycle flag; its slopes predict ~4% of that
  change, so the rise is the gene's own response, not the cycle mix.

### Neighbouring wells (tables version 5)

Two wells that touch on a plate (side by side, above / below, or at a corner) can share a signal: liquid carried
over, or a local problem on that part of the plate. The tables stage judges every pair of touching wells of two
different compounds (not DMSO, not on an unreliable plate; `tables.neighbour_wells`):

- It judges the weaker drug-dose a of the pair when a has at least 30 significant genes and its neighbour b at least
  as many.
- a resembles b when b moves at least 50% of a's significant genes the same way at |z| ≥ 3 (and at least 10
  genes), and a moves at least 30% of b's 30 strongest significant genes the same way.
- Then a's own other doses decide: a real drug effect shows at the drug's higher doses. If a has higher doses and none
  of them moves 20% or more of the shared genes, a gets `like a neighbouring well`: an artifact flag, but only for the
  genes the neighbour moves the same way at |z| ≥ 2. Its other genes read `like a neighbouring well (not this gene)`.
- At the drug's top dose there is no higher dose to check: when its lower doses move less than 20% of the shared
  genes, a gets `like a neighbouring well (top dose)`: an alert, not an artifact flag (the row stays clean). When one of its lower doses already moves at least 3
  of its 10 strongest shared genes the same way (|z| ≥ 3), the drug's own effect grows with the dose: tier 'dose
  response', a note, no token (tables version 6; before, RMC-6236 5 µM carried the top-dose caveat on 498 genes). The
  top-dose alert also gives the rate at which pairs 3 or more wells apart pass. When the two compounds share a
  mechanism (Tahoe's moa_fine, Tahoe's targets or a drug class), it is probably a real class effect: a note, no token.
- If b's own other doses also show less than 20% of the shared genes, b gets the same tier with a as its partner.
- `drugdoses.parquet` nb_tier, nb_partner, nb_where (the plates and wells), nb_alert (the reasons in words) and the
  counts in `tables/info.json` neighbour_rule. The rate of resembling pairs 3 or more wells apart gives the passes
  expected by chance (an upper bound: far pairs include real class copies).

Old rule: clean = no atlas artifact flag. New rule: also not 'like a neighbouring well' for that gene. Reason:
touching wells share signatures 3.5 to 4 times more often than wells 3 or more apart (validation report, section 4),
e.g. Citalopram 0.05 µM next to Clobetasol propionate on plate10. On the published tables (an earlier version; the
rule reproduced from their rows) it marks 13 drug-doses 'artifact' (1,830 drug_effects rows lose clean) and 11 'top
dose'; the full run gives the final count from the dense matrices.

### Translation inhibitors

A drug that stops protein synthesis raises many short-lived mRNAs whatever their pathway: the proteins that switch
their genes off or break them down are no longer made (Edwards and Mahadevan 1992, doi:10.1002/j.1460-2075.1992.tb05306.x).
The class TRANSLATION_ELONGATION of `tahoemap/data/drug_classes.json` (harringtonine, homoharringtonine and other
ribosome blockers, by cited code constants and ChEMBL's mechanisms) is read by `tahoemap/mechanisms.py`. Every
drug-dose of a member carries `translation inhibitor`; each gene that rises there (lfc > 0; a per-line cell reads its
own per-line change, tables version 6) reads `rise under a translation inhibitor`, and a gene that falls carries
neither. Both are caveats: they never change clean. Tahoe's
label 'Protein synthesis inhibitor' is not a class rule: it also covers four MNK / eIF4E inhibitors (Tomivosertib,
ETC-206, 4EGI-1, SBI-0640756) that do not stop protein synthesis (listed under 'not_members' with the reason). On the
published tables 25,534 drug_effects rows of Homoharringtonine and Harringtonine read 'rise under a translation
inhibitor'.

### Drug annotations: Tahoe and ChEMBL

`drugs.parquet` (and every surface) shows two annotations of each drug. targets, moa_fine and moa_broad are Tahoe's,
verbatim. The chembl_* columns come from ChEMBL (the reference stage, §9): molecule, mechanisms, actions, targets,
ATC codes; annotation_status and annotation_alert say where they agree or disagree ('Targets differ', 'Mechanism
differs', 'Action differs', 'Identity unsure'); mechanism_classes names the drug's classes with their sources. Tahoe's
annotation is never changed. A rule that needs a class reads `mechanisms.classes_by_drug` and names the source of
each membership (a cited code constant, a ChEMBL mechanism, a WHO ATC code via ChEMBL).

### Dose and plate; the rough DMSO fold change

Each dose of a drug sits on its own plate (`drugs.parquet` dose_plates, e.g. '0.05: plate1 D2, plate2 E7 / 0.5:
plate3 F12, plate4 H5 / 5: plate5 B1, plate6 C8'; doses_share_a_plate), so a pattern over the doses compares plates
as much as doses. Most drug-doses are one well (`n_wells`): the lines in that well are not replicate treatments.
`drug_effects.parquet` lfc_vs_dmso = lfc + the mean offset of the used wells' plates between the plate's DMSO wells
and its drug-well median (atlas plate_offset): a rough DMSO-referenced fold change, a sign check. When most drugs on a
plate raise a gene, lfc reads lower than lfc_vs_dmso. `tables/info.json` dmso_sign_changes counts the rows whose sign
flips at 1.2× or more.

### Growth, response strength and line selectivity (drug_line_response)

`tables/drug_line_response.parquet` has one row per drug-dose × line: n_genes (genes beyond the calibrated per-line
cut), rel_log2 (against the line's typical drug-dose), sel_z ((rel_log2 − its median over the drug-dose's lines) /
max(1.4826 × MAD, 0.25)); selective = sel_z ≥ 3 and n_genes ≥ 20. The atlas's growth and response values are copied
bit for bit: log2_rel_abundance (DD_A), abundance_z (DD_Az), depleted (abundance_z ≤ −3), response_strength (DD_beta)
and response_r (DD_rcor). `drugdoses.parquet` selective_lines names the lines each drug-dose singles out.
`lines.parquet` tp53_status reads 'altered', 'not recorded' or 'unknown': before tables version 5 it read 'wild type'
where no TP53 alteration was recorded. Reason: the metadata lists driver alterations, and a line may carry one that
is not listed, so 'not recorded' is not confirmed wild type.

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

**Drug-doses that act alike** (embed version 5). `embed/drug_similarity.parquet` lists each drug-dose's 50 most
similar drug-doses: the cosine of their pooled signatures (z clipped at ±10), over the per-line contexts, and the
significant genes they share. A drug-dose gets a note (resembles_note) when at least 4 of its 10 most similar
drug-doses of other compounds (cosine ≥ 0.5, sharing ≥ 10 significant genes changed the same way) share one Tahoe
class (moa_fine) other than its own; salt
forms of one compound whose signatures or strength disagree get an alert (salt_form_alert). The neighbouring-well rule
cannot catch a copy from a well that does not touch: these notes can.

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
'Both halves' means the same sign in both halves of the compounds: the halves share the lines and plates, so this
guards against single-compound effects, not against everything (98% of the top-100 partners pass it). (Before
relations version 5 the docs called it 'replicated'; the wording changed, the rule did not.)
**Lineage pairs** (relations version 5): two genes each expressed in at most 60% of the lines (30 of 50), whose line
sets overlap (Jaccard ≥ 0.5), move together whatever their regulation. Such a pair gets lineage_pair, an alert, and
lineage_p = (1 + null pairs in the same Jaccard bin with |cos| at least the pair's) / (1 + null pairs in the bin),
over every pair of restricted genes (a seeded sample of 8,000 genes when there are more): how unusual the pair is
among pairs that share their lines as much. **Read-sharing copies**: near-identical paralogues (Ensembl Compara identity ≥ 95%), a pseudogene and its
parent, a read-through transcript and its part (HGNC) can share reads; such a pair gets read_sharing and an alert.
Counts come in two units in `relations/info.json`: rows (a gene and one of its partners) and pairs.
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
graph linking each gene to its 15 strongest partners by |cos| ≥ 0.3 that have the same sign in both halves of the
compounds (`both halves`) or are very strong in one half (|cos| ≥ 0.5). A module has a − arm only when ≥ 5 members sit on the negative side of its main direction
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
module falls from 9.5% to 0.4% (nodal map). **How much a map keeps** (graph version 6): `graph/info.json`
partner_preservation, the share of a gene's 15 strongest partners among its 50 nearest genes on each layout (published
tables: 0.36 nodal, 0.36 signed, 0.31 and 0.31 spread; 0.003 by chance). **Module covariates**: the correlation of
each module's score over the trusted drug-doses with the wells' UMI and genes per cell, the cells left, the
composition shift and the S and G2/M shifts; a module with min(|r|, |rank r|) ≥ 0.3 gets a tag (covariate_tag, a
note); 200 shuffles give the largest |r| chance reaches (`graph/info.json` covariate_null_max_r; 0.12-0.16 on the
published tables). `graph/modules.gmt` holds each module arm as a gene set.

## 8. Direction — which gene probably acts on which

The relations above have no direction. The direction stage adds arrows SOURCE → TARGET from what the screen's 50 cell
lines differ in, each from a statistical test (p, a Benjamini–Hochberg q < 0.10 in its family), with a grade (A
strong, B read its alerts, C a glimpse), a sign (what the source's activity does to the target: raises, lowers, or
not inferred) and its alerts. The source can be:

- **a recorded mutation** of the source gene (loss or gain of function, from Tahoe's cell-line metadata): lines with
  it are compared with lines without any record of the gene, by permuting which lines count as altered (within
  organs where possible), for every target gene's drug response and baseline level and for the cells' numbers under
  every drug-dose. The mutation was there before the experiment, so the arrow points one way;
- **the source's absence** from some lines (natural knockouts: lines that read only the ambient RNA of the gene),
  tested the same way towards the source's related partners;
- **compounds that target the source** (two or more of one mechanism moving the target the same way, more often than
  compounds in general);
- **the source's natural level** across the lines (lineage-adjusted correlation with a related gene's response,
  computed in both directions, or with the cells' numbers under a drug-dose; a glimpse, grade C).

A line that responds less to every drug (fewer cells, drug efflux, a resistant genotype) would make every gene look
dependent on what that line carries, so each response is first set against the line's general responsiveness at the
same drug-doses. Random groups of lines tested in the same way, and the same level tests with shuffled levels, give
the number of false arrows to expect per kind; the TP53 → p53 targets arrows are the positive control. Nothing that
passes is dropped for doubt: an arrow keeps its place with ⚠ and the reason. The arrows are a *probable* direction,
not proof of direct regulation (A → B → C looks like A → C; 'not recorded' is not 'wild type'; one time point; drugs
act on proteins). [direction.md](direction.md) explains every kind, grade and alert with examples;
`tahoemap/direction.py` has the method in full.

Version 5 corrects readings the reviews found wrong, each with its old rule, new rule and reason in
[direction.md](direction.md#what-changed-in-version-5-old-rule-new-rule-why): drugs that trap their target on DNA
(TOP1 / TOP2 poisons, PARP trappers, microtubule stabilisers) give no sign; the drug-target test uses how strongly
each compound moves the gene (top-j); Tahoe's and ChEMBL's annotations are used side by side; grade A needs the
whole of the evidence to agree; two genes within 1 Mb, or a gene inside an expression programme, give no sign;
natural knockouts and drug targets say 'may'. It adds the response-strength kinds (a mutation, or a gene's absence,
→ how strongly the lines respond to a drug-dose), allele groups, each group's expected false share, the natural
knockouts' random controls, alerts for heavily mutated lines and for evidence carried by translation inhibitors, and
`direction/gene_tests.parquet` (every gene's tests and arrows).

## 9. Reference, validation, vault, map

Public annotations (HGNC, Ensembl GRCh38 r112 coordinates, UniProt function, NCBI summaries, Reactome, MSigDB
Hallmark, STRING v12) are downloaded once and cached; every source is optional. The reference stage runs right after
tensor (it reads only atlas/), so the tables and every later stage can use it. It also writes
`reference/gene_coords.parquet` (every gene of the Ensembl r112 GTF on the primary chromosomes, measured or not: the
direction stage places driver genes Tahoe does not measure), `reference/paralogues.parquet` (human paralogue pairs
among Tahoe's genes from Ensembl Compara r112, both identities and the homology type) and each drug's ChEMBL record
(`drug_annotations.parquet`, `drug_mechanisms.parquet`, `drug_classes.parquet`: matched by structure, PubChem id →
InChIKey, and by name; on the real data 377 of 379 drugs matched, 284 with a curated mechanism (3 more have only
ChEMBL's Unknown, which counts as no mechanism), 19 with an alert).
Validation scores the space against curated control programmes that were not derived from Tahoe
(`tahoemap/data/control_sets.json`) and against Hallmark and Reactome, tests the opposite-arm prediction, labels
modules by enrichment, by the drug class that drives them, or as lineage-restricted (with alerts for near-identical
copies, lineage and Y-chromosome genes), checks the drug classes of Tahoe and of ChEMBL, shows the neighbouring-well
rule and known line-selective responses, lists novel candidates (its lists keep flagged items with an alert too), and
reports the direction stage's controls. Rule changed in validate version 7: a curated control set that is a candidate
and not weak wins over Hallmark / Reactome; before, the smallest p won whatever the source, which named the
metallothionein module 'hypoxia'. The vault and the HTML map
present all of it, the probable directions included (a gene note's Direction (probable) section; the map's side
panel and arrows). The map has, besides the two
maps and their Spread slider, a **k-D tour** (the genes' unit vectors in all dimensions projected onto a 2-D plane
that turns smoothly, or one component against another exactly), and three physics simulations: a gene's
neighbourhood (its partners and theirs, to depth 1-4, up to 2,000 genes), one module, and all genes.

## Caveats that apply everywhere

- **Correlation is not mechanism.** There are no genetic perturbations in Tahoe-100M; "moves with" means the two
  genes respond alike across ~1,100 drug-doses in 50 lines, not that one regulates the other. "Upstream" and
  "downstream" are used only for the direction stage's arrows (§8), which are probable directions from the cell
  lines' natural differences, never for chromosomal position (that is "5′ of" / "3′ of").
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
- **Neighbouring wells** can share a signal (§4): the flag marks the genes a touching well moves the same way; at a
  top dose the data cannot tell a carried-over signal from a real effect.
- **Translation inhibitors** raise short-lived mRNAs whatever their pathway (§4): read such a rise as possible mRNA
  stabilisation.
- **Lineage pairs and read-sharing copies** (§6) correlate without regulation: they carry an alert.

## What is and is not controlled

Each list has its own test, null and false-discovery family. What a list does not control is said here, and the
outputs mark it with an alert rather than leave it out.

| List | Test and null | Family (FDR) | Not controlled |
|---|---|---|---|
| Drugs that raise / lower a gene (`drug_effects`) | robust z against the spread of the plate's drug wells, Stouffer over the drug-dose's wells | Benjamini–Hochberg within each gene over the drug-doses (q_up, q_down) | single-well noise (most drug-doses are one well: the z rests on other drugs' wells, not replicates); dose = plate; neighbouring wells beyond the rule; ties in q (equal q, different evidence: lists break ties by effect size) |
| Per-line calls (`line_effects`, `drug_line_top`) | per-line z against the line's own drug wells | none: the cut is calibrated so that ≤ 0.05 chance passes are expected per (gene, line) over the clean drug-doses | many lines × drug-doses: a few chance cells per gene remain; the lines in one well are not replicates |
| Partners (`gene_relations`) | cosine in the full space; sign in two halves of the compounds | sign-concordance FDR (one half selects, the other checks; FDR(t) = (disagreeing + 1) / agreeing) | lineage pairs (lineage_p gives their null, not an FDR); read-sharing copies; membership of one large programme (specificity and mutual rank say it) |
| Novel candidates | the partner tests plus mutual top 10, specificity ≥ 4, no literature link | the partners' FDR ≤ 0.05 | the same; and novelty only as far as HGNC, Ensembl, STRING and Hallmark / Reactome go |
| Probable direction (`direction/edges`) | permutation of the lines' labels (within organs), hypergeometric top-j, lineage-adjusted correlation | BH within each kind (q), and within each group (q_group) for the genotype kinds; random pseudo-groups, permuted levels, random genes and random line sets give the false arrows to expect | A → B → C looks like A → C; co-occurring alterations (alerted); heavily mutated lines (alerted); one time point |
| Neighbouring wells | resemblance of touching wells against the drug's other doses | none: the pass rate of pairs 3 or more wells apart gives the passes expected by chance (an upper bound) | copies from wells that do not touch (embed's resembles_note can catch them) |
| Module labels | hypergeometric overlap with control, Hallmark and Reactome sets | BH over the sets; a strong label needs q < 0.01, ≥ 5× the chance overlap, ≥ 3 independent genes | near-identical copies inflate an overlap (counted once; alerted); lineage-restricted modules (alerted) |
| Line-selective controls | AUROC of sel_z and of response strength for the expected lines | permutation p (2,000), no family correction | 50 lines: few lines per control |
| `tahoe signature` | mean clipped z of the up genes minus the down genes | p from 1,000 random gene sets matched by pooled-CPM decile, per drug-dose; no correction across the 1,132 drug-doses | read the p with the number of drug-doses in mind (about 5% of drug-doses reach p ≤ 0.05 for a random signature) |

## Provenance

`tahoemap/atlas_core.py` and `tahoemap/tlib.py` are the build and effects code of `tahoe_atlas.py` and
`tahoe_mtap_gankyrin.py` at commit `28cd834` (branch `claude/tahoe100m-gene-pipeline-lodlx7`), copied function by
function by syntax tree (`tools/port_from_old.py`, manifest `tahoemap/PORT_MANIFEST.tsv`); only the import header
is new. On the synthetic test data, every array and table the ported `build` and `effects` write is identical,
bit for bit, to the old scripts' output.
