---
symbol: "ATF7IP2"
type: "gene"
col: 9340
ensembl_id: "ENSG00000166669"
name: "activating transcription factor 7 interacting protein 2"
location: "16p13.2-p13.13"
module: 23
arm: "+"
pooled_cpm: 48.68
n_lines_expressing: 38
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ATF7IP2

*activating transcription factor 7 interacting protein 2* — 16p13.2-p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.85× (z +25.2, q 0e+00, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.729× (z -5.7, q 6e-06, down in 16 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.797× (z -4.3, q 0.005, down in 17 of 36 measured lines).
> Its strongest partners by |cos| (68 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5-GPRASP2]] (+0.52, fdr 3e-05), [[SPTY2D1OS]] (+0.49, fdr 3e-05), [[GPRASP3]] (+0.49, fdr 8e-05); moves opposite to [[NOMO3]] (-0.50, fdr 2e-04), [[FANCE]] (-0.46, fdr 1e-03, ⚠ not reproduced), [[CAMSAP1]] (-0.44, fdr 5e-04), [[HTT]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SGK2]] → it (grade B ⚠); 6 go from it, the strongest it → [[FAM169A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.85×** | +25.2 | 0e+00 | 32/36 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +24.5 | 0e+00 | 30/36 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +15.6 | 0e+00 | 32/36 (SW1417, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +14.3 | 2e-44 | 30/36 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +13.6 | 7e-40 | 31/36 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +12.7 | 4e-35 | 28/36 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.0 | 4e-31 | 26/36 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +11.1 | 8e-27 | 26/36 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +11.0 | 1e-26 | 21/36 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.2 | 2e-18 | 24/35 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +8.8 | 1e-16 | 27/36 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.8 | 1e-16 | 27/36 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +8.0 | 4e-14 | 26/36 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +7.9 | 9e-14 | 20/36 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +7.7 | 5e-13 | 22/36 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.49×** | +7.4 | 4e-12 | 26/36 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.4 | 2e-06 | 18/36 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.729×** | -5.7 | 6e-06 | 16/30 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.797×** | -4.3 | 0.005 | 17/36 (SK-MEL-2, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.806×** | -3.7 | 0.034 | 15/34 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.6 | 0.049 | 1/36 (SW 1271) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -3.5 | 0.058 | 11/36 (KATO III, PANC-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.062 | 11/36 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.062 | 8/36 (MIA PaCa-2, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | 0.838× | -3.3 | 0.062 | 17/35 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[vincristine (drug)]] 5 µM |  | **0.717×** | -3.3 | 0.069 | 13/35 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | 0.845× | -3.2 | 0.085 | 13/35 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.8 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +20.0) | — |
| [[HOP62 (line)]] | alt | 25.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 18.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +18.2) | — |
| [[RPMI-7951 (line)]] | alt | 52.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 92.1 | 4 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 6.05× (z +16.6) | [[Lonafarnib (drug)]] 5 µM 0.0879× (z -11.8) ⚠ toxic |
| [[A549 (line)]] | wt | 72.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 32.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +20.4) | — |
| [[SNU-1 (line)]] | wt | 64.9 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.14× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 53.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +20.9) | — |
| [[SW1417 (line)]] | alt | 24.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.6) | — |
| [[C32 (line)]] | wt | 23.8 | 3 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 41.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.36× (z +15.3) | — |
| [[KATO III (line)]] | alt | 403 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 51.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 66.9 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.85× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.2) |
| [[SW 900 (line)]] | alt | 39.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.25× (z +16.2) | — |
| [[A-427 (line)]] | wt | 65.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.99× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[COLO 205 (line)]] | alt | 52.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.2) | — |
| [[LoVo (line)]] | wt | 15.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.10× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 70.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[AN3 CA (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0765× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 61.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.144× (z -8.8) |
| [[HCT15 (line)]] | alt | 53.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.07× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 65.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.5) | — |
| [[RKO (line)]] | wt | 86.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.41× (z +15.5) | — |
| [[A-172 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5-GPRASP2]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[SPTY2D1OS]] | +0.49 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[GPRASP3]] | +0.49 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[OOEP]] | +0.48 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[GIPC2]] | +0.48 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[BTN2A3P-1]] | +0.47 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[ZNF207]] | +0.46 | +0.22 / +0.22 | both halves | 6e-04 |  |
| [[STX17-DT]] | +0.45 | +0.48 / +0.32 | both halves | 2e-04 |  |
| [[UST]] | +0.45 | +0.37 / +0.45 | both halves | 7e-05 |  |
| [[GABRB3]] | +0.45 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[BTN2A3P]] | +0.45 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[KMT2E-AS1]] | +0.45 | +0.43 / +0.07 | ⚠ not reproduced | 0.004 |  |
| [[SGK2]] | +0.44 | +0.50 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO3]] | -0.50 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[FANCE]] | -0.46 | -0.42 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[CAMSAP1]] | -0.44 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[HTT]] | -0.44 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[SNX11]] | -0.43 | -0.38 / -0.22 | both halves | 6e-04 |  |
| [[RMDN3]] | -0.43 | -0.21 / -0.37 | both halves | 6e-04 |  |
| [[PPM1G]] | -0.43 | -0.11 / -0.26 | ⚠ not reproduced | 0.002 |  |
| [[TBC1D24]] | -0.42 | -0.35 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[WRNIP1]] | -0.42 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[EMC8]] | -0.41 | -0.05 / -0.48 | ⚠ not reproduced | 0.005 |  |
| [[ZNF324B]] | -0.41 | -0.05 / -0.35 | ⚠ not reproduced | 0.005 |  |
| [[SFXN3]] | -0.41 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[NUP93]] | -0.41 | -0.29 / -0.25 | both halves | 4e-04 |  |
| [[CTXN1]] | -0.40 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[APPL1]] | -0.40 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[CTU2]] | -0.40 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[ESS2]] | -0.40 | -0.21 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGK2]] | B | SGK2 activity raises ATF7IP2's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without SGK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[LRRC4B]] | B | LRRC4B activity raises ATF7IP2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without LRRC4B | 0.019 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[ZC3H12B]] | B | ZC3H12B activity raises ATF7IP2's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without ZC3H12B | 0.052 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises ATF7IP2's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.24× lower at baseline in the lines without SYT9-AS1 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | ATF7IP2 activity raises FAM169A's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 2.76× lower at baseline in the lines without ATF7IP2 | 0.036 | ⚠ within organs, on part of the lines |
| [[CACHD1]] | B | ATF7IP2 activity raises CACHD1's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 2.11× lower at baseline in the lines without ATF7IP2 | 0.038 | ⚠ within organs, on part of the lines |
| [[GCC2-AS1]] | B | ATF7IP2 activity raises GCC2-AS1's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without ATF7IP2 | 0.076 | ⚠ within organs, on part of the lines |
| [[LINC00466]] | B | ATF7IP2 activity raises LINC00466's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without ATF7IP2 | 0.077 | ⚠ within organs, on part of the lines |
| [[CD72]] | B | ATF7IP2 activity raises CD72's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without ATF7IP2 | 0.085 | ⚠ within organs, on part of the lines |
| [[ENPP7P4]] | B | ATF7IP2 activity raises ENPP7P4's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without ATF7IP2 | 0.085 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.365). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (13.0, 21.5); signed map (32.2, -14.9). **Vector** length 72.9, 14.2% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.7 | +15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +25.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +24.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +13.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.5 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | +14.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | +12.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 7 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2-p13.13 — chr16:10,326,434-10,483,638 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12668, MCAF2 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5U623](https://www.uniprot.org/uniprotkb/Q5U623) (Activating transcription factor 7-interacting protein 2):

> Recruiter that couples transcriptional factors to general transcription apparatus and thereby modulates transcription regulation and chromatin formation. Can both act as an activator or a repressor depending on the context. Mediates MBD1-dependent transcriptional repression, probably by recruiting complexes containing SETDB1. The complex formed with MBD1 and SETDB1 represses transcription and probably couples DNA methylation and histone H3 'Lys-9' trimethylation (H3K9me3) activity (Probable).

**Summary**, from NCBI Gene [80063](https://www.ncbi.nlm.nih.gov/gene/80063):

> Predicted to enable transcription coregulator activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be part of transcription regulator complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20397) · Entrez [80063](https://www.ncbi.nlm.nih.gov/gene/80063) · UniProt [Q5U623](https://www.uniprot.org/uniprotkb/Q5U623) · Ensembl [ENSG00000166669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166669)

## Data

Gene col 9340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9340); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9340]; `tensor/DDL_lfc|DDL_z.npy` [9340]; `embed/gene_vectors.npy` [9340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9340 or target_col == 9340). Every well: [[ATF7IP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF7IP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
