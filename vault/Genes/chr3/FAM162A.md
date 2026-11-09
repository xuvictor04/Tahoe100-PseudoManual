---
symbol: "FAM162A"
type: "gene"
col: 3517
ensembl_id: "ENSG00000114023"
name: "family with sequence similarity 162 member A"
location: "3q21.1"
module: 79
arm: "+"
pooled_cpm: 166.75
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# FAM162A

*family with sequence similarity 162 member A* — 3q21.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.02×, NCI-H1792 4.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 4.10×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 3.37×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.232× (z -18.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HILPDA]] (+0.86, fdr 7e-06), [[INSIG2]] (+0.83, fdr 7e-06), [[PDK3]] (+0.83, fdr 7e-06); moves opposite to [[PARVA]] (-0.68, fdr 1e-05), [[SLC25A24]] (-0.61, fdr 1e-05), [[UTP20]] (-0.60, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DTNA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3517.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.02×, NCI-H1792 4.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Ouabain (Octahydrate) (drug)]] 0.05 µM in 1 line (NCI-H460 4.10×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 3.37×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.44× | +3.2 | 0.50 | 31/48 (H4, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | 1.40× | +3.1 | 0.50 | 33/47 (SHP-77, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.232×** | -18.9 | 0e+00 | 47/47 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.263×** | -12.2 | 1e-31 | 46/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.279×** | -11.2 | 6e-27 | 47/47 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.448×** | -7.0 | 3e-10 | 42/46 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -6.9 | 5e-10 | 39/48 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -5.8 | 6e-07 | 33/43 (SK-MEL-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.354×** | -4.9 | 6e-05 | 45/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.652×** | -3.9 | 0.008 | 43/47 (C-33 A, H4, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.454×** | -3.8 | 0.011 | 42/48 (HEC-1-A, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.570×** | -3.4 | 0.044 | 37/47 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -3.3 | 0.050 | 28/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 306 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -18.2) |
| [[NCI-H460 (line)]] | wt | 116 | 5 (5 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.10× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -19.2) |
| [[C32 (line)]] | wt | 283 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -24.2) |
| [[RPMI-7951 (line)]] | alt | 322 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -23.2) |
| [[H4 (line)]] | wt | 239 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -27.0) |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.164× (z -20.0) |
| [[A-172 (line)]] | wt | 209 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -20.8) |
| [[C-33 A (line)]] | alt | 304 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 397 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -12.6) |
| [[CHP-212 (line)]] | wt | 221 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -24.4) |
| [[SHP-77 (line)]] | alt | 169 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0510× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.6) |
| [[A-427 (line)]] | wt | 180 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -14.1) |
| [[AN3 CA (line)]] | alt | 220 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.1) |
| [[BT-474 (line)]] | alt | 117 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.7) |
| [[HCT15 (line)]] | alt | 215 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 236 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.3) |
| [[HS-578T (line)]] | alt | 225 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.3) |
| [[KATO III (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 242 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -25.2) |
| [[MIA PaCa-2 (line)]] | alt | 234 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.7) |
| [[PANC-1 (line)]] | alt | 148 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.5) |
| [[RKO (line)]] | wt | 150 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0858× (z -24.8) |
| [[SNU-1 (line)]] | wt | 212 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -17.6) |
| [[SW 900 (line)]] | alt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -20.9) |
| [[J82 (line)]] | alt | 237 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 164 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.18× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -15.6) |
| [[SNU-423 (line)]] | alt | 210 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -23.5) |
| [[SW480 (line)]] | alt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.2) |
| [[A549 (line)]] | wt | 95.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.0) |
| [[COLO 205 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.7) |
| [[HOP62 (line)]] | alt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.7) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.9) |
| [[HT-29 (line)]] | alt | 164 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.1) |
| [[LoVo (line)]] | wt | 94.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.4) |
| [[LS 180 (line)]] | wt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 67.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.6) |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) |
| [[SW 1271 (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.9) |
| [[SW48 (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.0) |
| [[A498 (line)]] | wt | 18.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HILPDA]] | +0.86 | +0.87 / +0.78 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.83 | +0.85 / +0.78 | both halves | 7e-06 |  |
| [[PDK3]] | +0.83 | +0.90 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[BNIP3]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | STRING 495 |
| [[WDR45B]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[FUT11]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.76 | +0.82 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[P4HA1]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[CNOT8]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.75 | +0.81 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVA]] | -0.68 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[UTP20]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[AVEN]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNA]] | B | DTNA activity raises FAM162A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without DTNA | 0.060 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, -16.5); signed map (-35.7, 24.0). **Vector** length 154, 61.4% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.69 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.9 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.2 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.0 | -18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.6 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.6 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -7.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.8 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 162 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,384,161-122,412,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E2IG5, HGTD-P; previously C3orf28 |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A26](https://www.uniprot.org/uniprotkb/Q96A26) (Protein FAM162A):

> Proposed to be involved in regulation of apoptosis; the exact mechanism may differ between cell types/tissues. May be involved in hypoxia-induced cell death of transformed cells implicating cytochrome C release and caspase activation (such as CASP9) and inducing mitochondrial permeability transition. May be involved in hypoxia-induced cell death of neuronal cells probably by promoting release of AIFM1 from mitochondria to cytoplasm and its translocation to the nucleus; however, the involvement …

**Summary**, from NCBI Gene [26355](https://www.ncbi.nlm.nih.gov/gene/26355):

> Involved in cellular response to hypoxia; positive regulation of apoptotic process; and positive regulation of release of cytochrome c from mitochondria. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17865) · Entrez [26355](https://www.ncbi.nlm.nih.gov/gene/26355) · UniProt [Q96A26](https://www.uniprot.org/uniprotkb/Q96A26) · Ensembl [ENSG00000114023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114023)

## Data

Gene col 3517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3517); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3517]; `tensor/DDL_lfc|DDL_z.npy` [3517]; `embed/gene_vectors.npy` [3517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3517 or target_col == 3517). Every well: [[FAM162A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM162A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
