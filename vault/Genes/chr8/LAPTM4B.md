---
symbol: "LAPTM4B"
type: "gene"
col: 2445
ensembl_id: "ENSG00000104341"
name: "lysosomal protein transmembrane 4 beta"
location: "8q22.1"
module: 29
arm: "+"
pooled_cpm: 48.43
n_lines_expressing: 46
n_dd_up: 40
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# LAPTM4B

*lysosomal protein transmembrane 4 beta* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.15× (z +25.7, q 0e+00, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +16.0, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.797× (z -5.1, q 2e-04, down in 22 of 44 measured lines) ⚠ cell-cycle shift, explains ~14% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.664× (z -4.8, q 4e-04, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.72, fdr 7e-06), [[PRDX3]] (+0.70, fdr 8e-06), [[FUCA2]] (+0.68, fdr 7e-06); moves opposite to [[GOLGB1]] (-0.66, fdr 7e-06), [[CCDC174]] (-0.65, fdr 7e-06), [[NFKBIL1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[STYXL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.15×** | +25.7 | 0e+00 | 41/42 (A498, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.35×** | +18.4 | 0e+00 | 32/39 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.41×** | +18.2 | 0e+00 | 38/42 (A498, HEC-1-A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +16.0 | 0e+00 | 39/44 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +14.9 | 0e+00 | 37/43 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.68×** | +11.6 | 5e-29 | 32/44 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.62×** | +10.7 | 5e-25 | 35/43 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +10.7 | 7e-25 | 34/44 (HT-29, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.59×** | +10.4 | 2e-23 | 31/43 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +10.1 | 2e-22 | 34/44 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.57×** | +10.1 | 5e-22 | 30/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +9.7 | 1e-20 | 30/44 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.53×** | +9.5 | 1e-19 | 32/44 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +9.0 | 1e-17 | 30/44 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +8.9 | 1e-17 | 32/44 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.6 | 7e-13 | 24/44 (HOP62, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 1e-08 | 24/44 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +5.8 | 1e-07 | 24/44 (HOP62, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +5.5 | 7e-07 | 20/43 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 1e-05 | 21/44 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +4.8 | 3e-05 | 16/43 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +4.2 | 4e-04 | 14/43 (J82, C32, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 4e-04 | 12/44 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.001 | 12/44 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.797×** | -5.1 | 2e-04 | 22/44 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.664×** | -4.8 | 4e-04 | 21/44 (A498, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.817×** | -4.4 | 0.002 | 18/44 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.874× | -4.3 | 0.002 | 14/44 (SW480, PANC-1, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.768×** | -4.2 | 0.002 | 16/44 (A498, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.815×** | -4.1 | 0.005 | 13/44 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.758×** | -3.3 | 0.087 | 9/44 (NCI-H2030, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.764× | -3.2 | 0.10 | 4/44 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.766× | -3.1 | 0.11 | 6/44 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 41.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 57.0 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 42.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.7) | — |
| [[A498 (line)]] | wt | 81.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +12.6) | — |
| [[A549 (line)]] | wt | 37.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.61× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 23.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.57× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[C32 (line)]] | wt | 70.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 25.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 32.0 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +12.3) | — |
| [[KATO III (line)]] | alt | 57.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.6) | — |
| [[SW480 (line)]] | alt | 37.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +8.6) | — |
| [[A-172 (line)]] | wt | 25.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[A-427 (line)]] | wt | 77.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -8.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HEC-1-A (line)]] | alt | 87.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.63× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 56.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 147 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -8.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[CFPAC-1 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 62.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.81× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 81.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.18× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[FUCA2]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.66 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[RNPEP]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[HACD3]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[APP]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[GPC4]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PTGFRN]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[OGFOD3]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PLBD2]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | -0.66 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.63 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ATF4]] | -0.63 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.63 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[FRG1]] | -0.62 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[CREB3]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[HELQ]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LAPTM4B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity raises LAPTM4B's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NSRP1]] | C | NSRP1's natural level strengthens LAPTM4B's drug response | NSRP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.76, reverse -0.20; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STYXL1]] | C | LAPTM4B activity raises STYXL1's level | lines that do not express LAPTM4B (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without LAPTM4B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: BMS1P23; its own permutation p |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.4, -21.7); signed map (-22.4, -38.6). **Vector** length 99.1, 26.9% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +8.0 | +25.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +7.8 | +18.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +7.5 | +18.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +9.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +5.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -6.9 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | lysosomal protein transmembrane 4 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:97,775,057-97,853,013 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LC27 |
| Gene groups (HGNC) | Lysosomal protein transmembrane family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VI4](https://www.uniprot.org/uniprotkb/Q86VI4) (Lysosomal-associated transmembrane protein 4B):

> Required for optimal lysosomal function. Blocks EGF-stimulated EGFR intraluminal sorting and degradation. Conversely by binding with the phosphatidylinositol 4,5-bisphosphate, regulates its PIP5K1C interaction, inhibits HGS ubiquitination and relieves LAPTM4B inhibition of EGFR degradation. Recruits SLC3A2 and SLC7A5 (the Leu transporter) to the lysosome, promoting entry of leucine and other essential amino acid (EAA) into the lysosome, stimulating activation of proton-transporting vacuolar …

**Summary**, from NCBI Gene [55353](https://www.ncbi.nlm.nih.gov/gene/55353):

> Enables ceramide binding activity; enzyme binding activity; and phosphatidylinositol bisphosphate binding activity. Involved in several processes, including endosome transport via multivesicular body sorting pathway; negative regulation of lysosomal protein catabolic process; and negative regulation of transforming growth factor beta1 production. Located in endosome; lysosomal membrane; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13646) · Entrez [55353](https://www.ncbi.nlm.nih.gov/gene/55353) · UniProt [Q86VI4](https://www.uniprot.org/uniprotkb/Q86VI4) · Ensembl [ENSG00000104341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104341)

## Data

Gene col 2445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2445); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2445]; `tensor/DDL_lfc|DDL_z.npy` [2445]; `embed/gene_vectors.npy` [2445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2445 or target_col == 2445). Every well: [[LAPTM4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAPTM4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
