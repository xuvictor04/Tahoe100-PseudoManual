---
symbol: "DIPK2A"
type: "gene"
col: 11209
ensembl_id: "ENSG00000181744"
name: "divergent protein kinase domain 2A"
location: "3q24"
module: 144
arm: "+"
pooled_cpm: 72.54
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# DIPK2A

*divergent protein kinase domain 2A* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +28.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.408× (z -15.7, q 0e+00, down in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.713× (z -6.1, q 1e-07, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK4]] (+0.68, fdr 1e-05), [[ACBD5]] (+0.64, fdr 1e-05), [[STBD1]] (+0.64, fdr 3e-05); moves opposite to [[GGA1]] (-0.57, fdr 4e-05), [[ADAMTSL5]] (-0.55, fdr 3e-05), [[EP400]] (-0.49, fdr 5e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MLLT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +28.4 | 0e+00 | 45/47 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +14.0 | 8e-42 | 33/46 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +11.0 | 1e-25 | 38/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.1 | 6e-22 | 39/46 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +9.1 | 8e-18 | 35/47 (C32, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.5 | 1e-08 | 31/46 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.94×** | +6.3 | 3e-08 | 33/46 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 4e-08 | 29/46 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.6 | 2e-06 | 24/43 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.5 | 2e-06 | 27/46 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 9e-06 | 23/46 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.0 | 2e-05 | 28/46 (HS-578T, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +4.5 | 4e-04 | 23/46 (LoVo, LS 180, …) | top dose only | composition shift |
| [[Roxadustat (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 23/46 (HOP62, BT-474, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.002 | 23/46 (NCI-H23, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.007 | 18/46 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.063 | 8/47 (LOX-IMVI, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 1.19× | +3.0 | 0.077 | 4/47 (A-172, HEC-1-A, …) | rises with dose | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -15.7 | 0e+00 | 35/42 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -11.8 | 8e-30 | 37/47 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.713×** | -6.1 | 1e-07 | 25/46 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -5.5 | 6e-06 | 25/45 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.787×** | -4.4 | 0.001 | 24/46 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.850× | -4.2 | 0.003 | 17/46 (J82, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.038 | 22/46 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 5 µM |  | 0.724× | -3.1 | 0.15 | 16/44 (SHP-77, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 86.5 | 7 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.0506× (z -30.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 105 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0841× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 68.5 | 3 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 102 | 3 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0859× (z -25.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +24.7) | — |
| [[C32 (line)]] | wt | 124 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.7× (z +14.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -14.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 77.9 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -17.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 81.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +19.9) | — |
| [[LoVo (line)]] | wt | 53.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 93.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 70.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 73.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.298× (z -11.3) |
| [[SNU-423 (line)]] | alt | 133 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -8.9) |
| [[COLO 205 (line)]] | alt | 33.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 147 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +14.0) | — |
| [[J82 (line)]] | alt | 273 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 94.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 72.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 49.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -16.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 1 | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 269 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.3) |
| [[CHP-212 (line)]] | wt | 99.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -17.1) |
| [[HepG2_C3A (line)]] | wt | 55.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.5) |
| [[HT-29 (line)]] | alt | 35.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +18.4) | — |
| [[hTERT-HPNE (line)]] | wt | 86.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.5) | — |
| [[KATO III (line)]] | alt | 26.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 60.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -17.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +17.1) | — |
| [[A549 (line)]] | wt | 51.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.1) | — |
| [[H4 (line)]] | wt | 94.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 60.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.9) |
| [[Hs 766T (line)]] | wt | 49.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 65.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.0) | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0879× (z -9.6) |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.4) | — |
| [[SW48 (line)]] | wt | 49.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +12.8) | — |
| [[SW480 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK4]] | +0.68 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ACBD5]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[STBD1]] | +0.64 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[FAM216A]] | +0.63 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[HELZ]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[IPMK]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TPI1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TENT5A]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.58 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ZNF395]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[BBX]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RBPJ]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGA1]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ADAMTSL5]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[EP400]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC18]] | -0.49 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DNAJC16]] | -0.49 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[RTEL1]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[KCTD21]] | -0.49 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[GIPC1]] | -0.48 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[R3HDM4]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[SIN3B]] | -0.47 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[RNF123]] | -0.47 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[TREX2]] | -0.47 | -0.40 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | MLLT3 activity raises DIPK2A's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MLLT3 | 0.043 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[BNIP3]] | B | BNIP3 activity raises DIPK2A's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without BNIP3 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1 |
| [[HDAC6]] | B | HDAC6 activity raises DIPK2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLOD2]] | B | PLOD2 activity raises DIPK2A's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without PLOD2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[CRYBG3]] | C | CRYBG3 activity raises DIPK2A's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 2.67× lower at baseline in the lines without CRYBG3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -19.3); signed map (-41.2, 28.1). **Vector** length 119, 34.0% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +28.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.9 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +4.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | divergent protein kinase domain 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:143,971,823-144,048,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33365, DIA1, HASF; previously C3orf58 |
| Gene groups (HGNC) | Divergent protein kinase domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDZ4](https://www.uniprot.org/uniprotkb/Q8NDZ4) (Divergent protein kinase domain 2A):

> May play a role in cardiomyocyte proliferation through paracrine signaling and activation of the PPI3K-AKT-CDK7 signaling cascade.

**Summary**, from NCBI Gene [205428](https://www.ncbi.nlm.nih.gov/gene/205428):

> Involved in several processes, including cardiac muscle cell proliferation; negative regulation of smooth muscle cell apoptotic process; and positive regulation of protein kinase C activity. Located in Golgi membrane and obsolete extracellular space. Part of COPI vesicle coat. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28490) · Entrez [205428](https://www.ncbi.nlm.nih.gov/gene/205428) · UniProt [Q8NDZ4](https://www.uniprot.org/uniprotkb/Q8NDZ4) · Ensembl [ENSG00000181744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181744)

## Data

Gene col 11209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11209); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11209]; `tensor/DDL_lfc|DDL_z.npy` [11209]; `embed/gene_vectors.npy` [11209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11209 or target_col == 11209). Every well: [[DIPK2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIPK2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
