---
symbol: "RFXAP"
type: "gene"
col: 5418
ensembl_id: "ENSG00000133111"
name: "regulatory factor X associated protein"
location: "13q13.3"
module: 188
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 48
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# RFXAP

*regulatory factor X associated protein* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.56× (z +7.6, q 2e-11, up in 14 of 45 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.85× (z +7.4, q 5e-11, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -11.6, q 4e-28, down in 32 of 39 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -8.8, q 4e-16, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBD2]] (+0.67, fdr 7e-06), [[RPP30]] (+0.67, fdr 1e-05), [[TMEM185A]] (+0.67, fdr 1e-05); moves opposite to [[USP11]] (-0.60, fdr 1e-05), [[C21orf91-OT1]] (-0.59, fdr 2e-05), [[TUT7]] (-0.59, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.56×** | +7.6 | 2e-11 | 14/45 (A498, J82, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.85×** | +7.4 | 5e-11 | 28/44 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +6.9 | 9e-10 | 21/45 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +6.4 | 2e-08 | 18/45 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +6.2 | 6e-08 | 19/45 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.4 | 6e-06 | 20/45 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.54×** | +5.0 | 5e-05 | 11/24 (SW480, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.8 | 1e-04 | 12/38 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +4.6 | 2e-04 | 3/44 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.3 | 8e-04 | 5/27 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.3 | 8e-04 | 13/42 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 7/45 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.8 | 0.007 | 1/8 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.008 | 8/43 (NCI-H23, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.7 | 0.008 | 8/29 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.008 | 2/45 (HT-29, RKO) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.009 | 5/45 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.011 | 4/45 (MIA PaCa-2, SHP-77, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.015 | 3/45 (SW480, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.015 | 4/45 (A-172, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.506×** | -11.6 | 4e-28 | 32/39 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -8.8 | 4e-16 | 30/45 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.572×** | -6.4 | 2e-08 | 19/43 (LOX-IMVI, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -5.7 | 2e-06 | 19/44 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.651×** | -5.1 | 3e-05 | 20/38 (HCT15, LOX-IMVI, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -4.7 | 3e-04 | 14/40 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **0.725×** | -3.9 | 0.009 | 12/40 (SW48, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.079 | 15/37 (Panc 03.27, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.2 | 0.079 | 9/46 (HepG2/C3A, C-33 A, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.773× | -3.1 | 0.12 | 7/45 (HepG2/C3A, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.777× | -3.0 | 0.13 | 11/44 (NCI-H460, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.02 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -13.3) ⚠ cell-cycle shift, explains ~89% of this change |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0988× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 5.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 4.27 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0689× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 1 | — | [[Drospirenone (drug)]] 0.05 µM 0.0576× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 4.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 4.26 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBD2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RPP30]] | +0.67 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[OTUD6B]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SKP2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MRS2]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TMEM218]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CROT]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SNX4]] | +0.61 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[C21orf91-OT1]] | -0.59 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[TUT7]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[OFD1]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ARMC5]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[C11orf91]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ERI2]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[RGL2]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CYTH2]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity lowers RFXAP's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without C11orf91 | 0.051 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[KATNAL1]] | B | KATNAL1 activity raises RFXAP's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without KATNAL1 | 0.071 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers RFXAP's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without ZNF341-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises RFXAP's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without DLX6-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.8, -12.0); signed map (-34.0, -18.4). **Vector** length 58.8, 8.06% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.3 | +7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.3 | -11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -3.2 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,819,222-36,829,104 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O00287](https://www.uniprot.org/uniprotkb/O00287) (Regulatory factor X-associated protein):

> Part of the RFX complex that binds to the X-box of MHC II promoters.

**Summary**, from NCBI Gene [5994](https://www.ncbi.nlm.nih.gov/gene/5994):

> Major histocompatibility (MHC) class II molecules are transmembrane proteins that have a central role in development and control of the immune system. The protein encoded by this gene, along with regulatory factor X-associated ankyrin-containing protein and regulatory factor-5, forms a complex that binds to the X box motif of certain MHC class II gene promoters and activates their transcription. Once bound to the promoter, this complex associates with the non-DNA-binding factor MHC class II …

**Accessions** — [HGNC:9988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9988) · Entrez [5994](https://www.ncbi.nlm.nih.gov/gene/5994) · UniProt [O00287](https://www.uniprot.org/uniprotkb/O00287) · Ensembl [ENSG00000133111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133111)

## Data

Gene col 5418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5418); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5418]; `tensor/DDL_lfc|DDL_z.npy` [5418]; `embed/gene_vectors.npy` [5418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5418 or target_col == 5418). Every well: [[RFXAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFXAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
