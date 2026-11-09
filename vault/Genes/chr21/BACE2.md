---
symbol: "BACE2"
type: "gene"
col: 11263
ensembl_id: "ENSG00000182240"
name: "beta-secretase 2"
location: "21q22.2-q22.3"
module: 34
arm: "+"
pooled_cpm: 252.77
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 47
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# BACE2

*beta-secretase 2* — 21q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.54× (z +4.6, q 0.002, up in 20 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.98×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.93×; ⚠ cell-cycle shift, explains ~40% of this change); [[NG25 (drug)]] 5 µM in 1 line (LoVo 3.62×; ⚠ cell-cycle shift, explains ~38% of this change); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 2.23×); [[BAY1125976 (drug)]] 5 µM in 1 line (LoVo 3.43×).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.128× (z -59.2, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEMIP]] (+0.57, fdr 1e-05), [[PPARD]] (+0.57, fdr 2e-05), [[LAT]] (+0.56, fdr 1e-05); moves opposite to [[ZNF644]] (-0.60, fdr 1e-05), [[CARF]] (-0.54, fdr 8e-05), [[SCAF8]] (-0.52, fdr 7e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PLAC4]] → it (grade B ⚠); 10 go from it, the strongest it → [[ST3GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.98×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 1.93×; ⚠ cell-cycle shift, explains ~40% of this change); [[NG25 (drug)]] 5 µM in 1 line (LoVo 3.62×; ⚠ cell-cycle shift, explains ~38% of this change); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 2.23×); [[BAY1125976 (drug)]] 5 µM in 1 line (LoVo 3.43×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.54×** | +4.6 | 0.002 | 20/38 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.029 | 19/39 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.070 | 14/38 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.070 | 14/39 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.3 | 0.10 | 15/38 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.10 | 15/37 (LoVo, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.10 | 12/38 (A549, A-172, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.14 | 11/38 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.15 | 11/38 (LoVo, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.128×** | -59.2 | 0e+00 | 38/38 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.177×** | -34.0 | 0e+00 | 38/38 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.199×** | -32.9 | 0e+00 | 38/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.222×** | -30.7 | 0e+00 | 37/38 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.267×** | -24.8 | 0e+00 | 37/38 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.351×** | -21.3 | 0e+00 | 36/38 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.410×** | -18.2 | 0e+00 | 35/38 (SHP-77, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -16.0 | 0e+00 | 31/39 (CFPAC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.460×** | -15.8 | 0e+00 | 35/38 (BT-474, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.469×** | -14.8 | 0e+00 | 32/37 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.508×** | -13.8 | 1e-41 | 31/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.528×** | -12.5 | 5e-34 | 37/37 (LoVo, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.662×** | -11.9 | 9e-31 | 33/38 (Panc 03.27, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.548×** | -11.3 | 4e-28 | 28/36 (CFPAC-1, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.577×** | -11.2 | 2e-27 | 31/39 (LoVo, CFPAC-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.380×** | -10.3 | 3e-23 | 36/39 (CFPAC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.727×** | -6.5 | 3e-09 | 26/38 (C32, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.795×** | -5.5 | 7e-07 | 20/38 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.766×** | -5.4 | 2e-06 | 23/39 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -5.3 | 3e-06 | 20/38 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.763×** | -5.3 | 3e-06 | 24/38 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -5.2 | 4e-06 | 20/38 (HOP62, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 364 | 0 | 30 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -35.3) |
| [[NCI-H1573 (line)]] | alt | 288 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -35.8) |
| [[A549 (line)]] | wt | 302 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0512× (z -46.6) |
| [[Panc 03.27 (line)]] | alt | 446 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -37.3) |
| [[BT-474 (line)]] | alt | 197 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -29.1) |
| [[CFPAC-1 (line)]] | alt | 777 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -44.6) |
| [[NCI-H1792 (line)]] | alt | 428 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -38.3) |
| [[NCI-H460 (line)]] | wt | 235 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -35.8) |
| [[KATO III (line)]] | alt | 356 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -47.7) |
| [[LoVo (line)]] | wt | 549 | 2 (1 ⚠) | 14 (8 ⚠) | [[NG25 (drug)]] 5 µM 3.62× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[BAY1125976 (drug)]] 5 µM 3.43× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -45.8) |
| [[SNU-423 (line)]] | alt | 409 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -39.8) |
| [[A-172 (line)]] | wt | 447 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0838× (z -41.0) |
| [[HOP62 (line)]] | alt | 376 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0726× (z -29.8) |
| [[C32 (line)]] | wt | 771 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -31.2) |
| [[SHP-77 (line)]] | alt | 344 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -32.3) |
| [[AsPC-1 (line)]] | alt | 195 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -35.2) |
| [[LOX-IMVI (line)]] | wt | 261 | 1 (1 ⚠) | 12 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.94× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -41.0) |
| [[SK-MEL-2 (line)]] | alt | 537 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -31.3) |
| [[COLO 205 (line)]] | alt | 294 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -34.7) |
| [[HS-578T (line)]] | alt | 278 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0908× (z -43.4) |
| [[HT-29 (line)]] | alt | 223 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -35.4) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 | 8 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.23× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -32.5) |
| [[RKO (line)]] | wt | 137 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -31.3) |
| [[SW 900 (line)]] | alt | 166 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -32.7) |
| [[HCT15 (line)]] | alt | 233 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0851× (z -29.3) |
| [[LS 180 (line)]] | wt | 367 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -30.6) |
| [[SW1417 (line)]] | alt | 196 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -25.5) |
| [[SW48 (line)]] | wt | 119 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -26.2) |
| [[RPMI-7951 (line)]] | alt | 254 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -27.4) |
| [[SNU-1 (line)]] | wt | 102 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0373× (z -26.3) |
| [[A498 (line)]] | wt | 99.1 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -27.6) |
| [[Hs 766T (line)]] | wt | 169 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -31.5) |
| [[J82 (line)]] | alt | 75.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -21.6) |
| [[H4 (line)]] | wt | 495 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 78.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -22.4) |
| [[PANC-1 (line)]] | alt | 66.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.6) |
| [[SW 1088 (line)]] | alt | 406 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.6) |
| [[CHP-212 (line)]] | wt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -13.6) |
| [[A-427 (line)]] | wt | 62.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 40.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 26.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 56.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,049 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 48.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEMIP]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PPARD]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[LAT]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ABHD17C]] | +0.55 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLCO4A1]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ST3GAL1]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RASA3]] | +0.53 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[CALB2]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TM4SF19-DYNLT2B]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.52 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[CARF]] | -0.54 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[SCAF8]] | -0.52 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[ZNF236]] | -0.52 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RDX]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NFIB]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[LINC00886]] | -0.50 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[LUC7L2]] | -0.50 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[NAALADL2]] | -0.50 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[RBM33]] | -0.49 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[TLK1]] | -0.49 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[HOXC4]] | -0.49 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | PLAC4 activity raises BACE2's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 4.93× lower at baseline in the lines without PLAC4 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[PAEP]] | B | PAEP activity raises BACE2's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without PAEP | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[PLEK2]] | B | PLEK2 activity raises BACE2's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without PLEK2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[ABHD17C]] | B | ABHD17C activity raises BACE2's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.64× lower at baseline in the lines without ABHD17C | 0.036 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises BACE2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without CEMIP | 0.037 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[NDRG1]] | B | NDRG1 activity raises BACE2's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 4.11× lower at baseline in the lines without NDRG1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[ABTB3]] | B | ABTB3 activity raises BACE2's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without ABTB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises BACE2's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 3.88× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[FAM89A]] | B | FAM89A activity raises BACE2's level | lines that do not express FAM89A (5) vs lines expressing it (45) | 4.73× lower at baseline in the lines without FAM89A | 0.089 | ⚠ within organs, on part of the lines; also absent: DPP7, IL17RD, B3GNT5; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises BACE2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | BACE2 activity raises ST3GAL1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 3.07× lower at baseline in the lines without BACE2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[NDRG1]] | B | BACE2 activity raises NDRG1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without BACE2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[NIBAN2]] | B | BACE2 activity raises NIBAN2's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 2.73× lower at baseline in the lines without BACE2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[RABGEF1P3]] | B | BACE2 activity raises RABGEF1P3's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without BACE2 | 0.067 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[UBA6]] | B | BACE2 activity raises UBA6's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without BACE2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[ARID1A]] | B | BACE2 activity lowers ARID1A's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.42× higher at baseline in the lines without BACE2 | 0.077 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[TNFRSF11A]] | B | BACE2 activity raises TNFRSF11A's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without BACE2 | 0.082 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[PLEKHM1P1]] | B | BACE2 activity raises PLEKHM1P1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without BACE2 | 0.087 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[SPSB1]] | B | BACE2 activity raises SPSB1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without BACE2 | 0.095 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[FLNB-AS1]] | B | BACE2 activity raises FLNB-AS1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without BACE2 | 0.099 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.7, 3.2); signed map (0.8, 50.7). **Vector** length 107, 37.1% of its response variance represented; |z| ≥ 3 in 1,844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | -16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +5.6 | -11.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.5 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.4 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.3 | -4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | beta-secretase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2-q22.3 — chr21:41,167,801-41,282,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASP1, DRAP, ALP56, CEAP1; previously AEPLC |
| Gene groups (HGNC) | Peptidase family A1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Z0](https://www.uniprot.org/uniprotkb/Q9Y5Z0) (Beta-secretase 2):

> Responsible for the proteolytic processing of the amyloid precursor protein (APP). Cleaves APP, between residues 690 and 691, leading to the generation and extracellular release of beta-cleaved soluble APP, and a corresponding cell-associated C-terminal fragment which is later released by gamma-secretase. It has also been shown that it can cleave APP between residues 671 and 672. Involved in the proteolytic shedding of PMEL at early stages of melanosome biogenesis. Cleaves PMEL within the …

**Summary**, from NCBI Gene [25825](https://www.ncbi.nlm.nih.gov/gene/25825):

> This gene encodes an integral membrane glycoprotein that functions as an aspartic protease. The encoded protein cleaves amyloid precursor protein into amyloid beta peptide, which is a critical step in the etiology of Alzheimer's disease and Down syndrome. The protein precursor is further processed into an active mature peptide. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:934) · Entrez [25825](https://www.ncbi.nlm.nih.gov/gene/25825) · UniProt [Q9Y5Z0](https://www.uniprot.org/uniprotkb/Q9Y5Z0) · Ensembl [ENSG00000182240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182240)

## Data

Gene col 11263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11263); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11263]; `tensor/DDL_lfc|DDL_z.npy` [11263]; `embed/gene_vectors.npy` [11263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11263 or target_col == 11263). Every well: [[BACE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BACE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
