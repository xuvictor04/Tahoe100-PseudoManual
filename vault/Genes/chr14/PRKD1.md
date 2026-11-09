---
symbol: "PRKD1"
type: "gene"
col: 11516
ensembl_id: "ENSG00000184304"
name: "protein kinase D1"
location: "14q12"
module: 9
arm: "+"
pooled_cpm: 86.29
n_lines_expressing: 37
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PRKD1

*protein kinase D1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +9.2, q 2e-17, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.405× (z -16.1, q 0e+00, down in 26 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.671× (z -10.5, q 2e-23, down in 21 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPE3]] (+0.59, fdr 1e-05), [[NCAM2]] (+0.58, fdr 2e-05), [[GPC6]] (+0.57, fdr 1e-05); moves opposite to [[CRYGS]] (-0.46, fdr 2e-04), [[LINC00412]] (-0.45, fdr 8e-05), [[SLC35F5]] (-0.45, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CTNNA2]] → it (grade B ⚠); 7 go from it, the strongest it → [[TTLL7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +9.2 | 2e-17 | 23/35 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.5 | 4e-15 | 22/35 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +7.8 | 1e-12 | 24/35 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 5e-09 | 27/36 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +6.3 | 3e-08 | 24/35 (A498, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.9 | 3e-07 | 24/34 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.6 | 2e-06 | 18/32 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +5.5 | 3e-06 | 18/35 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +4.9 | 5e-05 | 14/35 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 1e-04 | 18/35 (A498, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 20/36 (NCI-H1792, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.011 | 15/34 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +3.6 | 0.013 | 13/37 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.5 | 0.019 | 13/35 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.023 | 12/36 (CFPAC-1, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.028 | 10/35 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.029 | 9/35 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.046 | 15/35 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.048 | 12/36 (A498, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -16.1 | 0e+00 | 26/32 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.410×** | -14.9 | 0e+00 | 28/36 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -10.5 | 2e-23 | 21/36 (C32, SHP-77, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -10.0 | 3e-21 | 26/34 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.567×** | -9.7 | 2e-20 | 26/32 (A498, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.598×** | -9.5 | 1e-19 | 28/35 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.603×** | -9.4 | 5e-19 | 26/35 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.608×** | -9.2 | 2e-18 | 26/35 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -8.1 | 3e-14 | 26/35 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -7.7 | 5e-13 | 20/36 (NCI-H1573, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -7.6 | 1e-12 | 25/37 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -6.9 | 3e-10 | 22/35 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -6.6 | 2e-09 | 20/35 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -5.5 | 2e-06 | 18/30 (BT-474, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.756×** | -5.2 | 8e-06 | 23/35 (C32, CHP-212, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -5.1 | 1e-05 | 17/35 (C32, NCI-H1573, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -4.1 | 0.001 | 15/35 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.017 | 17/35 (SHP-77, AN3 CA, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.706×** | -3.4 | 0.020 | 15/35 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.024 | 13/35 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.024 | 14/35 (SHP-77, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.835× | -3.2 | 0.032 | 12/35 (SHP-77, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.039 | 14/35 (NCI-H1573, CHP-212, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.795×** | -3.0 | 0.053 | 12/35 (NCI-H1573, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.847× | -3.0 | 0.060 | 10/36 (J82, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 15 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.9) |
| [[C32 (line)]] | wt | 516 | 1 | 12 (7 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.29× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 202 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -22.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 217 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -16.7) |
| [[PANC-1 (line)]] | alt | 133 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 93.8 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -13.3) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -10.5) |
| [[SHP-77 (line)]] | alt | 386 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -17.7) |
| [[A-172 (line)]] | wt | 131 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.2) |
| [[A498 (line)]] | wt | 89.9 | 3 (1 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -9.6) |
| [[CHP-212 (line)]] | wt | 188 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0595× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 93.7 | 4 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.97× (z +13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.71× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -28.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.234× (z -11.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 215 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.9) |
| [[AN3 CA (line)]] | alt | 222 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 116 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.66× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.7) |
| [[A-427 (line)]] | wt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.4) |
| [[A549 (line)]] | wt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 58.9 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.98× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -11.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 84.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 72.3 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.27× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.242× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 81.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Lonafarnib (drug)]] 5 µM 0.109× (z -10.0) ⚠ toxic |
| [[H4 (line)]] | wt | 92.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 58.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H661 (line)]] | alt | 457 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.32 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPE3]] | +0.59 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[GPC6]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PPP2R2B]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ANO5]] | +0.57 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[MMP16]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.56 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[AR]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 | STRING 491 |
| [[TMEM108]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[SOX5]] | +0.54 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[STOX2]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[KLHL13]] | +0.54 | +0.38 / +0.59 | both halves | 6e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYGS]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[LINC00412]] | -0.45 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SLC35F5]] | -0.45 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[PSKH1]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MORN1]] | -0.44 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ERVK13-1]] | -0.43 | -0.32 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTNNA2]] | B | CTNNA2 activity raises PRKD1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.65× lower at baseline in the lines without CTNNA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[KIAA0319]] | B | KIAA0319 activity raises PRKD1's level | lines that do not express KIAA0319 (19) vs lines expressing it (31) | 1.39× lower at baseline in the lines without KIAA0319 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANKRD20A21P, DOCK3, ARHGAP8 |
| [[PI15]] | B | PI15 activity raises PRKD1's level | lines that do not express PI15 (36) vs lines expressing it (14) | 3.93× lower at baseline in the lines without PI15 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1 |
| [[NREP]] | C | NREP activity raises PRKD1's level | lines that do not express NREP (13) vs lines expressing it (37) | 6.11× lower at baseline in the lines without NREP | 0.027 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL7]] | B | PRKD1 activity raises TTLL7's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 3.90× lower at baseline in the lines without PRKD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[TTBK2]] | B | PRKD1 activity raises TTBK2's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without PRKD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[ATRNL1]] | B | PRKD1 activity raises ATRNL1's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 3.68× lower at baseline in the lines without PRKD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[KIAA0319]] | B | PRKD1 activity raises KIAA0319's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without PRKD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[NREP]] | C | PRKD1 activity raises NREP's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 5.53× lower at baseline in the lines without PRKD1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD; co-absent with the target |
| [[MPDZ]] | C | PRKD1 activity raises MPDZ's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 10.13× lower at baseline in the lines without PRKD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD; co-absent with the target |
| [[FIGN]] | C | PRKD1 activity raises FIGN's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 7.63× lower at baseline in the lines without PRKD1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 34.7); signed map (38.4, 36.7). **Vector** length 112, 31.4% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.5 | +6.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.4 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | -3.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.1 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -2.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.8 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.5 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:29,576,479-30,191,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKD1, PKCM, PKD, PKC-mu; previously PRKCM |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Protein kinase D family |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15139](https://www.uniprot.org/uniprotkb/Q15139) (Serine/threonine-protein kinase D1):

> Serine/threonine-protein kinase that converts transient diacylglycerol (DAG) signals into prolonged physiological effects downstream of PKC, and is involved in the regulation of MAPK8/JNK1 and Ras signaling, Golgi membrane integrity and trafficking, cell survival through NF-kappa-B activation, cell migration, cell differentiation by mediating HDAC7 nuclear export, cell proliferation via MAPK1/3 (ERK1/2) signaling, and plays a role in cardiac hypertrophy, VEGFA-induced angiogenesis, …

**Summary**, from NCBI Gene [5587](https://www.ncbi.nlm.nih.gov/gene/5587):

> The protein encoded by this gene is a serine/threonine protein kinase involved in many cellular processes, including Golgi body membrane integrity and transport, cell migration and differentiation, MAPK8/JNK1 and Ras pathway signaling, MAPK1/3 (ERK1/2) pathway signaling, cell survival, and regulation of cell shape and adhesion. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:9407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9407) · Entrez [5587](https://www.ncbi.nlm.nih.gov/gene/5587) · UniProt [Q15139](https://www.uniprot.org/uniprotkb/Q15139) · Ensembl [ENSG00000184304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184304)

## Data

Gene col 11516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11516); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11516]; `tensor/DDL_lfc|DDL_z.npy` [11516]; `embed/gene_vectors.npy` [11516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11516 or target_col == 11516). Every well: [[PRKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
