---
symbol: "STK24"
type: "gene"
col: 2257
ensembl_id: "ENSG00000102572"
name: "serine/threonine kinase 24"
location: "13q32.2"
module: 31
arm: "+"
pooled_cpm: 209.8
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# STK24

*serine/threonine kinase 24* — 13q32.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 1.82×, C32 1.81×, NCI-H460 1.60×, NCI-H2030 1.95×; ⚠ cell-cycle shift, explains ~1% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.65×, NCI-H460 1.77×; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 3.16×, A-427 2.40×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (C32 7.09×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.56×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.20×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.589× (z -9.3, q 1e-17, down in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.630× (z -8.4, q 1e-14, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2A]] (+0.58, fdr 2e-05), [[DNM2]] (+0.57, fdr 1e-05), [[MAPKAPK2]] (+0.56, fdr 2e-05); moves opposite to [[STAT5B]] (-0.51, fdr 3e-05), [[RUFY1]] (-0.50, fdr 3e-05), [[BTN2A3P-1]] (-0.49, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2257.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (MIA PaCa-2 1.82×, C32 1.81×, NCI-H460 1.60×, NCI-H2030 1.95×; ⚠ cell-cycle shift, explains ~1% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.65×, NCI-H460 1.77×; ⚠ cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 3.16×, A-427 2.40×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (C32 7.09×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.56×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.20×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 1.47× | +3.6 | 0.16 | 24/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -9.3 | 1e-17 | 41/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -8.4 | 1e-14 | 41/48 (COLO 205, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.8 | 1e-12 | 31/44 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.722×** | -5.9 | 4e-07 | 31/49 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 1e-05 | 35/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.815×** | -5.3 | 1e-05 | 25/48 (HepG2/C3A, HT-29, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.747×** | -5.1 | 3e-05 | 33/48 (A-172, HT-29, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -5.0 | 4e-05 | 25/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.4 | 8e-04 | 27/48 (A498, LoVo, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.005 | 26/48 (HT-29, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.810×** | -3.8 | 0.006 | 24/48 (HT-29, LoVo, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.867× | -3.7 | 0.011 | 11/48 (HOP62, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.6 | 0.015 | 20/48 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.840× | -3.2 | 0.059 | 20/49 (SW 900, HOP62, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.1 | 0.076 | 20/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.888× | -3.1 | 0.076 | 12/48 (A-172, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 1,103 | 0 | 13 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -14.9) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.134× (z -13.5) |
| [[LoVo (line)]] | wt | 249 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 98.3 | 8 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.70× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 111 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.09× (z +11.9) | — |
| [[KATO III (line)]] | alt | 436 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -11.4) |
| [[A-172 (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.390× (z -12.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.491× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 218 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -11.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 260 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 84.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +9.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.314× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 246 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 85.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.3) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -9.6) |
| [[SW 1271 (line)]] | alt | 542 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -13.8) ⚠ transcription drop; cell-cycle shift, explains ~74% of this change |
| [[COLO 205 (line)]] | alt | 976 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 213 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -8.5) |
| [[HOP62 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 273 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -9.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 402 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 407 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.16× (z +9.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 106 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0704× (z -11.2) |
| [[HCT15 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.1) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[NCI-H2030 (line)]] | alt | 64.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.5) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[RKO (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.2) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[SHP-77 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.484× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A498 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 224 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2A]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[DNM2]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[TGM2]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RANBP9]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[B3GNT2]] | +0.55 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[PACSIN2]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.53 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[ANXA11]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TNFRSF1A]] | +0.53 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HIP1R]] | +0.53 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[EML4]] | +0.53 | +0.57 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT5B]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[RUFY1]] | -0.50 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[BTN2A3P-1]] | -0.49 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SBF2-AS1]] | -0.49 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ZNF573]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[B9D1]] | -0.48 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ABRAXAS2]] | -0.48 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[TRMT10B]] | -0.48 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[BTN2A3P]] | -0.47 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZCCHC9]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.46 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SETDB1]] | -0.46 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity raises STK24's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without ST14 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[SCNN1A]] | B | SCNN1A activity raises STK24's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without SCNN1A | 0.017 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[HSD17B2]] | B | HSD17B2 activity raises STK24's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without HSD17B2 | 0.032 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[B3GNT3]] | B | B3GNT3 activity raises STK24's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without B3GNT3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[RAPGEF5]] | B | RAPGEF5 activity strengthens STK24's drug response | lines that do not express RAPGEF5 (17) vs lines expressing it (32) | the lines without RAPGEF5 respond 0.38× as strongly (z diff +2.74); strongest at Homoharringtonine 5 µM: 0.99x vs 0.69x (z diff +4.5) | 0.034 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MUC5B]] | B | MUC5B activity raises STK24's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.75× lower at baseline in the lines without MUC5B | 0.051 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[SERPINA5]] | B | SERPINA5 activity raises STK24's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.53× lower at baseline in the lines without SERPINA5 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[RBMS3]] | B | RBMS3 activity lowers STK24's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.92× higher at baseline in the lines without RBMS3 | 0.091 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.3, 30.4); signed map (-15.6, 38.5). **Vector** length 129, 42.5% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +5.4 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.5 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.2 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.2 — chr13:98,445,185-98,577,940 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MST-3, MST3, MST3B, STK3, STE20 |
| Gene groups (HGNC) | STRIPAK complex; STK24/STK25/ST26 kinase family |
| Reactome | 4 pathways, smallest: Apoptotic cleavage of cellular proteins; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6E0](https://www.uniprot.org/uniprotkb/Q9Y6E0) (Serine/threonine-protein kinase 24):

> Serine/threonine-protein kinase that acts on both serine and threonine residues and promotes apoptosis in response to stress stimuli and caspase activation. Mediates oxidative-stress-induced cell death by modulating phosphorylation of JNK1-JNK2 (MAPK8 and MAPK9), p38 (MAPK11, MAPK12, MAPK13 and MAPK14) during oxidative stress. Plays a role in a staurosporine-induced caspase-independent apoptotic pathway by regulating the nuclear translocation of AIFM1 and ENDOG and the DNase activity associated …

**Summary**, from NCBI Gene [8428](https://www.ncbi.nlm.nih.gov/gene/8428):

> This gene encodes a serine/threonine protein kinase that functions upstream of mitogen-activated protein kinase (MAPK) signaling. The encoded protein is cleaved into two chains by caspases; the N-terminal fragment (MST3/N) translocates to the nucleus and promotes programmed cells death. There is a pseudogene for this gene on chromosome X. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:11403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11403) · Entrez [8428](https://www.ncbi.nlm.nih.gov/gene/8428) · UniProt [Q9Y6E0](https://www.uniprot.org/uniprotkb/Q9Y6E0) · Ensembl [ENSG00000102572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102572)

## Data

Gene col 2257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2257); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2257]; `tensor/DDL_lfc|DDL_z.npy` [2257]; `embed/gene_vectors.npy` [2257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2257 or target_col == 2257). Every well: [[STK24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
