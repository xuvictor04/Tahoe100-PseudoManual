---
symbol: "SLC7A6OS"
type: "gene"
col: 2314
ensembl_id: "ENSG00000103061"
name: "solute carrier family 7 member 6 opposite strand"
location: "16q22.1"
module: 114
arm: "+"
pooled_cpm: 35.55
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# SLC7A6OS

*solute carrier family 7 member 6 opposite strand* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.99× (z +16.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.924× (z -6.4, q 8e-08, down in 0 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (CHP-212 0.0950×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC8]] (+0.58, fdr 1e-05), [[GPN2]] (+0.58, fdr 1e-05), [[DDX27]] (+0.56, fdr 3e-05); moves opposite to [[GOLIM4]] (-0.56, fdr 1e-05), [[EZH2]] (-0.55, fdr 1e-05), [[MED14]] (-0.53, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SPOUT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +16.8 | 0e+00 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +16.7 | 0e+00 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +13.5 | 2e-39 | 41/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +12.8 | 3e-35 | 40/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +12.4 | 3e-33 | 34/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +11.5 | 2e-28 | 31/46 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +11.0 | 5e-26 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +10.8 | 2e-25 | 39/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +10.4 | 1e-23 | 37/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +9.9 | 2e-21 | 35/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +9.9 | 3e-21 | 36/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +8.9 | 2e-17 | 24/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +8.8 | 4e-17 | 35/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +8.7 | 1e-16 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.8 | 4e-10 | 26/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +6.5 | 3e-09 | 27/48 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2314.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.321×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (CHP-212 0.0950×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (AN3 CA 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -6.4 | 8e-08 | 0/48 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.828×** | -3.9 | 0.031 | 9/48 (NCI-H460, LOX-IMVI, …) | two highest doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.877× | -3.2 | 0.25 | 11/48 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.879× | -3.0 | 0.34 | 9/48 (SW 1088, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +14.4) | — |
| [[A498 (line)]] | wt | 31.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +10.6) | — |
| [[KATO III (line)]] | alt | 38.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 52.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.111× (z -9.0) |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0950× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 41.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[LoVo (line)]] | wt | 28.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.52× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 32.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.1) | — |
| [[A-172 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC8]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[GPN2]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 | STRING 685 |
| [[DDX27]] | +0.56 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[MTERF4]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZNF721]] | +0.53 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZNF701]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF778]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[BRMS1]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZSCAN25]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ZSCAN32]] | +0.53 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZNF707]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLIM4]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[EZH2]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MED14]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PARP1]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[STT3B]] | -0.50 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DUT]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TANC1]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.48 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SCML1]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[GPC4]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[PDE7A]] | -0.47 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SLC44A1]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOUT1]] | C | SLC7A6OS's natural level strengthens SPOUT1's drug response | SLC7A6OS's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.04; direction not clear | 0.0999 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.6, 9.1); signed map (-2.9, -16.7). **Vector** length 76.5, 14.8% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +12.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +11.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +4.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 6 opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,284,503-68,310,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13291, Iwr1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CW6](https://www.uniprot.org/uniprotkb/Q96CW6) (Probable RNA polymerase II nuclear localization protein SLC7A6OS):

> Directs RNA polymerase II nuclear import.

**Summary**, from NCBI Gene [84138](https://www.ncbi.nlm.nih.gov/gene/84138):

> Predicted to be involved in developmental process. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be located in cytoplasm and nucleus. Implicated in progressive myoclonus epilepsy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25807) · Entrez [84138](https://www.ncbi.nlm.nih.gov/gene/84138) · UniProt [Q96CW6](https://www.uniprot.org/uniprotkb/Q96CW6) · Ensembl [ENSG00000103061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103061)

## Data

Gene col 2314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2314); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2314]; `tensor/DDL_lfc|DDL_z.npy` [2314]; `embed/gene_vectors.npy` [2314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2314 or target_col == 2314). Every well: [[SLC7A6OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A6OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
