---
symbol: "PSMD4"
type: "gene"
col: 8248
ensembl_id: "ENSG00000159352"
name: "proteasome 26S subunit ubiquitin receptor, non-ATPase 4"
location: "1q21.3"
module: 64
arm: "+"
pooled_cpm: 51.45
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PSMD4

*proteasome 26S subunit ubiquitin receptor, non-ATPase 4* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.27× (z +12.0, q 3e-30, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.717× (z -5.1, q 2e-04, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.103×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.467×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL45]] (+0.74, fdr 7e-06), [[UBXN4]] (+0.72, fdr 7e-06), [[PSMC5]] (+0.71, fdr 7e-06); moves opposite to [[CD9]] (-0.58, fdr 2e-05), [[SMARCD2]] (-0.58, fdr 3e-05), [[SPATA33]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ERAL1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +12.0 | 3e-30 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.59×** | +11.6 | 8e-29 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.11×** | +11.4 | 1e-27 | 45/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.66×** | +10.9 | 1e-25 | 43/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.99×** | +10.0 | 1e-21 | 36/42 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +10.0 | 1e-21 | 44/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.02×** | +8.6 | 5e-16 | 45/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 2e-10 | 39/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.8 | 5e-10 | 39/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.54×** | +6.0 | 1e-07 | 30/44 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.1 | 2e-05 | 27/46 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.35×** | +4.5 | 3e-04 | 27/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +4.4 | 4e-04 | 26/48 (HEC-1-A, COLO 205, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +3.7 | 0.010 | 29/49 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.024 | 18/48 (SW480, HOP62, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.090 | 6/49 (SHP-77, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8248.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H661 0.103×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.467×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.717×** | -5.1 | 2e-04 | 30/48 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.045 | 23/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.798× | -3.4 | 0.11 | 22/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.860× | -3.2 | 0.12 | 11/48 (Hs 766T, Panc 03.27, …) | top dose only | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.860× | -3.2 | 0.12 | 9/49 (SHP-77, C32, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.809× | -3.2 | 0.12 | 22/47 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.676× | -3.1 | 0.15 | 17/48 (CHP-212, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 0.812× | -3.1 | 0.16 | 15/48 (HepG2/C3A, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 59.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.77× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 73.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.07× (z +12.1) | — |
| [[A-172 (line)]] | wt | 86.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +9.9) | — |
| [[A498 (line)]] | wt | 53.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 41.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.98× (z +8.6) | — |
| [[A549 (line)]] | wt | 45.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.23× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 50.9 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.70× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 80.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.60× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 38.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.68× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 46.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +9.1) | — |
| [[J82 (line)]] | alt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 43.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.56× (z +11.2) | — |
| [[RKO (line)]] | wt | 46.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.40× (z +9.5) | — |
| [[SW480 (line)]] | alt | 47.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Digitoxin (drug)]] 0.5 µM 0.467× (z -8.5) |
| [[A-427 (line)]] | wt | 75.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 42.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +9.4) | — |
| [[KATO III (line)]] | alt | 49.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.48× (z +8.7) | — |
| [[LoVo (line)]] | wt | 41.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 35.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.99× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 87.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.103× (z -8.8) |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL45]] | +0.74 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[PSMC5]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[PSMD7]] | +0.70 | +0.80 / +0.65 | both halves | 7e-06 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[PSMD6]] | +0.69 | +0.78 / +0.59 | both halves | 7e-06 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[FBXO38]] | +0.68 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[ACOT13]] | +0.67 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[ZSCAN26]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ANXA7]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[PSMC3]] | +0.65 | +0.73 / +0.55 | both halves | 1e-05 | same gene group; pathway: Proteasome assembly; STRING 999 |
| [[ASNSD1]] | +0.64 | +0.75 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD9]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.58 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[SPATA33]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ATP1B3]] | -0.54 | -0.60 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERAL1]] | C | ERAL1's natural level strengthens PSMD4's drug response | ERAL1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.06; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-30.2, 4.4); signed map (6.8, -29.9). **Vector** length 101, 29.2% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Vif-mediated degradation of APOBEC3G* (reactome, mean cos +0.53 to 9); *Signaling by Hedgehog* (reactome, mean cos +0.52 to 12); *Hedgehog 'on' state* (reactome, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +7.4 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.3 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.8 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.1 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.4 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit ubiquitin receptor, non-ATPase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,254,709-151,267,479 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S5A, AF-1, AF, Rpn10 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P55036](https://www.uniprot.org/uniprotkb/P55036) (26S proteasome non-ATPase regulatory subunit 4):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMD4 acts as an …

**Summary**, from NCBI Gene [5710](https://www.ncbi.nlm.nih.gov/gene/5710):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9561) · Entrez [5710](https://www.ncbi.nlm.nih.gov/gene/5710) · UniProt [P55036](https://www.uniprot.org/uniprotkb/P55036) · Ensembl [ENSG00000159352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159352)

## Data

Gene col 8248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8248); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8248]; `tensor/DDL_lfc|DDL_z.npy` [8248]; `embed/gene_vectors.npy` [8248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8248 or target_col == 8248). Every well: [[PSMD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
