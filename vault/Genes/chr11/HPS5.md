---
symbol: "HPS5"
type: "gene"
col: 3164
ensembl_id: "ENSG00000110756"
name: "HPS5 biogenesis of lysosomal organelles complex 2 subunit 2"
location: "11p15.1"
module: 139
arm: "+"
pooled_cpm: 52.35
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# HPS5

*HPS5 biogenesis of lysosomal organelles complex 2 subunit 2* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.83× (z +32.9, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.751× (z -6.4, q 9e-08, down in 26 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.788× (z -5.3, q 2e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.190×, Panc 03.27 0.226×, HCT15 0.171×, PANC-1 0.485×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.168×, A498 0.482×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.402×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.396×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND8]] (+0.54, fdr 2e-05), [[UGP2]] (+0.53, fdr 2e-05), [[LPIN2]] (+0.52, fdr 3e-05); moves opposite to [[SGPL1]] (-0.49, fdr 3e-05), [[PSEN2]] (-0.44, fdr 2e-04), [[GAB2]] (-0.43, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MT1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +32.9 | 0e+00 | 44/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +22.6 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +22.0 | 0e+00 | 39/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.47×** | +20.2 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.32×** | +18.8 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +14.6 | 0e+00 | 41/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +13.7 | 8e-41 | 36/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.85×** | +13.2 | 8e-38 | 39/47 (SW480, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +12.1 | 4e-32 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +11.9 | 5e-31 | 38/49 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +11.8 | 3e-30 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +8.9 | 4e-17 | 33/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +8.3 | 5e-15 | 31/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.44×** | +7.9 | 2e-13 | 27/46 (RKO, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.3 | 1e-11 | 32/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +6.2 | 1e-08 | 24/48 (RKO, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.8 | 2e-07 | 24/49 (NCI-H460, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.8 | 4e-05 | 16/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.6 | 9e-05 | 15/48 (A-172, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.4 | 2e-04 | 14/48 (NCI-H460, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3164.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 0.190×, Panc 03.27 0.226×, HCT15 0.171×, PANC-1 0.485×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.168×, A498 0.482×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.402×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.396×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.751×** | -6.4 | 9e-08 | 26/48 (SNU-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.765×** | -5.8 | 2e-06 | 25/47 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -5.3 | 2e-05 | 25/48 (C32, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.786×** | -5.0 | 9e-05 | 21/43 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.849× | -3.7 | 0.029 | 12/48 (C32, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.858× | -3.3 | 0.090 | 20/41 (C-33 A, Panc 03.27, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.2 | 17 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +34.2) | — |
| [[PANC-1 (line)]] | alt | 73.6 | 11 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.485× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 32.9 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +20.2) | — |
| [[HOP62 (line)]] | alt | 31.5 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +19.5) | — |
| [[J82 (line)]] | alt | 61.3 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +23.4) | — |
| [[SW480 (line)]] | alt | 50.0 | 9 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.22× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +20.5) | — |
| [[HS-578T (line)]] | alt | 36.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.3) | — |
| [[LoVo (line)]] | wt | 32.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 48.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +18.9) | — |
| [[A498 (line)]] | wt | 113 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 59.6 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 38.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.5) | — |
| [[LS 180 (line)]] | wt | 33.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.8) | — |
| [[RKO (line)]] | wt | 37.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 76.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.27× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 67.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +20.6) | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 40.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 64.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 50.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 24.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 58.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.9) | — |
| [[HCT15 (line)]] | alt | 40.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.53× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 20.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 137 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.7) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.561× (z -8.9) |
| [[SW 900 (line)]] | alt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.4) | — |
| [[A-427 (line)]] | wt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.6) | — |
| [[H4 (line)]] | wt | 48.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 95.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +13.6) | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND8]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[UGP2]] | +0.53 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[LPIN2]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[STAT3]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[PLIN2]] | +0.51 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SAA4]] | +0.51 | +0.54 / +0.53 | both halves | 1e-05 | ⚠ same locus (41.9 kb, same strand: neighbours can correlate without regulation) |
| [[PHF21A]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[POLR3GL]] | +0.51 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SAA2-SAA4]] | +0.51 | +0.54 / +0.52 | both halves | 1e-05 | ⚠ same locus (30.0 kb, same strand: neighbours can correlate without regulation) |
| [[SAA2]] | +0.50 | +0.53 / +0.53 | both halves | 1e-05 | ⚠ same locus (30.0 kb, same strand: neighbours can correlate without regulation) |
| [[MAFB]] | +0.50 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TPCN1]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[BCL6]] | +0.49 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[HS3ST3B1]] | +0.47 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[INTS6L]] | +0.47 | +0.42 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPL1]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PSEN2]] | -0.44 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[GAB2]] | -0.43 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TUSC3]] | -0.42 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[UBE2E3]] | -0.42 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[RNF182]] | -0.42 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[VKORC1L1]] | -0.41 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[TTC7B]] | -0.41 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[CDC42BPA]] | -0.40 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[HERC2P9-1]] | -0.40 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[LINC02728]] | -0.40 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[NCK2]] | -0.39 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1E]] | B | MT1E activity lowers HPS5's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.41× higher at baseline in the lines without MT1E | 0.006 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[IRAK3]] | B | IRAK3 activity lowers HPS5's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.17× higher at baseline in the lines without IRAK3 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 15.2); signed map (15.9, 28.6). **Vector** length 81.8, 19.6% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +11.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +13.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.5 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | +0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HPS5 biogenesis of lysosomal organelles complex 2 subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,278,668-18,322,198 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BLOC2S2, AIBP63, RU2 |
| Gene groups (HGNC) | WD repeat domain containing; Biogenesis of lysosomal organelles complex 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPZ3](https://www.uniprot.org/uniprotkb/Q9UPZ3) (BLOC-2 complex member HPS5):

> May regulate the synthesis and function of lysosomes and of highly specialized organelles, such as melanosomes and platelet dense granules. Regulates intracellular vesicular trafficking in fibroblasts. May be involved in the regulation of general functions of integrins.

**Summary**, from NCBI Gene [11234](https://www.ncbi.nlm.nih.gov/gene/11234):

> This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. This protein interacts with Hermansky-Pudlak syndrome 6 protein and may interact with the cytoplasmic domain of integrin, alpha-3. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 5. Multiple transcript variants encoding two distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17022) · Entrez [11234](https://www.ncbi.nlm.nih.gov/gene/11234) · UniProt [Q9UPZ3](https://www.uniprot.org/uniprotkb/Q9UPZ3) · Ensembl [ENSG00000110756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110756)

## Data

Gene col 3164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3164); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3164]; `tensor/DDL_lfc|DDL_z.npy` [3164]; `embed/gene_vectors.npy` [3164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3164 or target_col == 3164). Every well: [[HPS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
