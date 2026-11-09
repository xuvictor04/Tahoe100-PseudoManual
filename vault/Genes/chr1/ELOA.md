---
symbol: "ELOA"
type: "gene"
col: 218
ensembl_id: "ENSG00000011007"
name: "elongin A"
location: "1p36.11"
module: 107
arm: "+"
pooled_cpm: 48.55
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# ELOA

*elongin A* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +16.4, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.801× (z -5.0, q 4e-04, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~14% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.260×, HS-578T 0.344×, AN3 CA 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.327×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Mozavaptan (drug)]] 0.05 µM in 1 line (A-172 0.319×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF550]] (+0.57, fdr 2e-05), [[MEN1]] (+0.56, fdr 1e-05), [[LRRC47]] (+0.54, fdr 1e-05); moves opposite to [[DNM1]] (-0.47, fdr 4e-05), [[RTKN2]] (-0.45, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RTKN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +16.4 | 0e+00 | 42/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +15.9 | 0e+00 | 46/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +12.0 | 1e-30 | 39/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +10.3 | 1e-22 | 40/48 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +8.8 | 1e-16 | 32/48 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +8.8 | 1e-16 | 29/48 (LoVo, LS 180, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +8.5 | 2e-15 | 30/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +8.3 | 7e-15 | 37/48 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +7.5 | 4e-12 | 33/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +7.4 | 8e-12 | 26/48 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +7.1 | 8e-11 | 33/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.32×** | +6.3 | 1e-08 | 23/48 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +6.1 | 6e-08 | 27/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.28×** | +5.5 | 1e-06 | 27/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.28×** | +5.5 | 2e-06 | 22/48 (LoVo, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 1e-04 | 24/48 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.004 | 14/48 (A498, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.260×, HS-578T 0.344×, AN3 CA 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.327×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.325×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Mozavaptan (drug)]] 0.05 µM in 1 line (A-172 0.319×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.801×** | -5.0 | 4e-04 | 22/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.6 | 0.090 | 17/42 (HCT15, HS-578T, …) | top dose only | composition shift; position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.896× | -3.5 | 0.090 | 2/48 (HT-29, NCI-H1792) | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | 0.861× | -3.4 | 0.11 | 14/48 (RPMI-7951, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.28 | 7/48 (AN3 CA, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 32.2 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.18× (z +17.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 63.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.6) | — |
| [[A549 (line)]] | wt | 26.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 37.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 30.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.9) | — |
| [[SW480 (line)]] | alt | 47.9 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 60.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.3× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 85.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 58.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 33.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 47.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.1) | — |
| [[A-172 (line)]] | wt | 26.8 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.319× (z -9.1) |
| [[A-427 (line)]] | wt | 47.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.2) |
| [[A498 (line)]] | wt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[C32 (line)]] | wt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.8) | — |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 50.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 65.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.6) | — |
| [[J82 (line)]] | alt | 51.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.0) | — |
| [[KATO III (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 89.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.03× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.8) | — |
| [[SW48 (line)]] | wt | 56.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF550]] | +0.57 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[MEN1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC47]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RBM22]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ZNF622]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[TEX264]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[GTF3C4]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ABT1]] | +0.50 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[TFIP11]] | +0.50 | +0.53 / +0.37 | both halves | 9e-05 |  |
| [[GID8]] | +0.50 | +0.26 / +0.54 | both halves | 3e-04 |  |
| [[MIEF1]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[PPIE]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 | STRING 530 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNM1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RTKN2]] | -0.45 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTKN2]] | B | RTKN2 activity raises ELOA's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without RTKN2 | 0.047 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.6, -4.0); signed map (-11.5, -27.1). **Vector** length 72.0, 14.1% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +7.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | +4.7 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +15.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.0 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | +0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.4 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | elongin A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,743,448-23,762,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIII, TCEB3A, ELOA1; previously TCEB3 |
| Gene groups (HGNC) | Elongin complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 22 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14241](https://www.uniprot.org/uniprotkb/Q14241) (Elongin-A):

> Component of the Elongin complex, also known as SIII, a general transcription elongation factor that increases transcription elongation by RNA polymerase II past template-encoded arresting sites; subunit A is transcriptionally active and its transcription activity is strongly enhanced by binding to the dimeric complex of the SIII regulatory subunits B and C (Elongin BC complex). As part of a multisubunit complex composed of Elongin BC complex (ELOB and ELOC), Elongin A/ELOA, RBX1 and CUL5; …

**Summary**, from NCBI Gene [6924](https://www.ncbi.nlm.nih.gov/gene/6924):

> This gene encodes the protein elongin A, which is a subunit of the transcription factor B (SIII) complex. The SIII complex is composed of elongins A/A2, B and C. It activates elongation by RNA polymerase II by suppressing transient pausing of the polymerase at many sites within transcription units. Elongin A functions as the transcriptionally active component of the SIII complex, whereas elongins B and C are regulatory subunits. Elongin A2 is specifically expressed in the testis, and capable of …

**Accessions** — [HGNC:11620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11620) · Entrez [6924](https://www.ncbi.nlm.nih.gov/gene/6924) · UniProt [Q14241](https://www.uniprot.org/uniprotkb/Q14241) · Ensembl [ENSG00000011007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011007)

## Data

Gene col 218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 218); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 218]; `tensor/DDL_lfc|DDL_z.npy` [218]; `embed/gene_vectors.npy` [218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 218 or target_col == 218). Every well: [[ELOA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
