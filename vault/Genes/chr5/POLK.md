---
symbol: "POLK"
type: "gene"
col: 4314
ensembl_id: "ENSG00000122008"
name: "DNA polymerase kappa"
location: "5q13.3"
module: 12
arm: "+"
pooled_cpm: 120.06
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# POLK

*DNA polymerase kappa* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.47× (z +11.5, q 7e-28, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.704× (z -10.0, q 6e-21, down in 32 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.871× (z -5.8, q 4e-07, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESD]] (+0.72, fdr 7e-06), [[WASHC3]] (+0.64, fdr 1e-05), [[CEP290]] (+0.64, fdr 1e-05); moves opposite to [[EIF4EBP2]] (-0.51, fdr 5e-05), [[AKT1]] (-0.50, fdr 3e-05), [[CCDC168]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ESRP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +11.5 | 7e-28 | 33/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +11.4 | 7e-28 | 29/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +8.5 | 3e-15 | 29/48 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +7.7 | 2e-12 | 37/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +5.7 | 1e-06 | 23/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +5.2 | 2e-05 | 18/48 (PANC-1, hTERT-HPNE, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.0 | 6e-05 | 21/48 (A498, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.7 | 2e-04 | 21/48 (A-427, SW 900, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.14× | +3.9 | 0.006 | 10/50 (C32, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.7 | 0.009 | 4/48 (A-427, SHP-77, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 19/49 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.7 | 0.011 | 10/47 (C32, C-33 A, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.7 | 0.011 | 13/49 (J82, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.019 | 16/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.13× | +3.4 | 0.023 | 16/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.024 | 9/48 (NCI-H2347, COLO 205, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.059 | 14/47 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.073 | 10/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.073 | 7/49 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.704×** | -10.0 | 6e-21 | 32/44 (A-172, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.730×** | -9.0 | 5e-17 | 36/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.722×** | -8.7 | 4e-16 | 31/45 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.772×** | -7.7 | 2e-12 | 30/49 (A-172, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.834× | -7.6 | 3e-12 | 24/49 (A549, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.782×** | -7.3 | 2e-11 | 28/48 (hTERT-HPNE, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.800×** | -6.4 | 1e-08 | 27/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.808×** | -6.1 | 8e-08 | 24/50 (A-172, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -5.8 | 4e-07 | 17/48 (A-172, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 0.852× | -4.6 | 3e-04 | 23/47 (A-172, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.859× | -4.5 | 3e-04 | 22/48 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.860× | -4.5 | 3e-04 | 18/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.862× | -4.4 | 5e-04 | 19/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.872× | -4.1 | 0.002 | 11/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.959× | -4.1 | 0.002 | 0/50 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.842× | -3.7 | 0.009 | 15/48 (HOP62, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.029 | 17/46 (SW 900, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.056 | 15/46 (SK-MEL-2, H4, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.073 | 18/48 (HCT15, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.905× | -2.9 | 0.081 | 10/48 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.906× | -2.9 | 0.081 | 7/47 (HOP62, KATO III, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | 0.896× | -2.9 | 0.081 | 7/48 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.829×** | -2.9 | 0.081 | 10/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.898× | -2.9 | 0.087 | 11/47 (SNU-423, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 210 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.534× (z -10.8) |
| [[A498 (line)]] | wt | 148 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.550× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 85.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 144 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +19.0) | [[Dinaciclib (drug)]] 0.05 µM 0.532× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 118 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 146 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.499× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 74.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 124 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 157 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 146 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.556× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 126 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Capmatinib (drug)]] 5 µM 0.106× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.480× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 0.5 µM 2.05× (z +10.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +9.0) | — |
| [[RKO (line)]] | wt | 126 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.02× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.479× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 98.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.327× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HT-29 (line)]] | alt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.336× (z -11.8) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 54.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.515× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.525× (z -9.4) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 93.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -16.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SNU-1 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW 1088 (line)]] | alt | 281 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW 1271 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.187× (z -10.8) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 131 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESD]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[WASHC3]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[CEP290]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC17]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SUCLG1]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[HCFC2]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[NEPRO]] | +0.56 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[RP9]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP2]] | -0.51 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[AKT1]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHA6]] | -0.48 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[FBRSL1]] | -0.48 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CYP2D7]] | -0.47 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[HYAL3]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP2]] | B | ESRP2 activity lowers POLK's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.47× higher at baseline in the lines without ESRP2 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[PRSS22]] | B | PRSS22 activity lowers POLK's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 1.50× higher at baseline in the lines without PRSS22 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.8, 2.6); signed map (-17.7, -10.3). **Vector** length 116, 32.2% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +11.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.4 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | -5.0 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.2 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase kappa |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,511,845-75,609,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POLQ, DINP; previously DINB1 |
| Gene groups (HGNC) | DNA polymerases; Zinc fingers UBZ4 CCHC-type |
| Reactome | 16 pathways, smallest: Translesion synthesis by POLK; Gap-filling DNA repair synthesis and ligation in GG-NER; Termination of translesion DNA synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBT6](https://www.uniprot.org/uniprotkb/Q9UBT6) (DNA polymerase kappa):

> DNA polymerase specifically involved in DNA repair. Plays an important role in translesion synthesis, where the normal high-fidelity DNA polymerases cannot proceed and DNA synthesis stalls. Depending on the context, it inserts the correct base, but causes frequent base transitions, transversions and frameshifts. Lacks 3'-5' proofreading exonuclease activity. Forms a Schiff base with 5'-deoxyribose phosphate at abasic sites, but does not have lyase activity.

**Summary**, from NCBI Gene [51426](https://www.ncbi.nlm.nih.gov/gene/51426):

> This gene encodes a member of the DNA polymerase type-Y family of proteins. The encoded protein is a specialized DNA polymerase that catalyzes translesion DNA synthesis, which allows DNA replication in the presence of DNA lesions. Human cell lines lacking a functional copy of this gene exhibit impaired genome integrity and enhanced susceptibility to oxidative damage. Mutations in this gene that impair enzyme activity may be associated with prostate cancer in human patients. [provided by RefSeq, …

**Accessions** — [HGNC:9183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9183) · Entrez [51426](https://www.ncbi.nlm.nih.gov/gene/51426) · UniProt [Q9UBT6](https://www.uniprot.org/uniprotkb/Q9UBT6) · Ensembl [ENSG00000122008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122008)

## Data

Gene col 4314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4314); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4314]; `tensor/DDL_lfc|DDL_z.npy` [4314]; `embed/gene_vectors.npy` [4314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4314 or target_col == 4314). Every well: [[POLK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
