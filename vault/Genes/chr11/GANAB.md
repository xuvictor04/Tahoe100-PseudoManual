---
symbol: "GANAB"
type: "gene"
col: 1591
ensembl_id: "ENSG00000089597"
name: "glucosidase II alpha subunit"
location: "11q12.3"
module: 50
arm: "+"
pooled_cpm: 121.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GANAB

*glucosidase II alpha subunit* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +19.8, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +5.9, q 5e-07, up in 30 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.663× (z -11.8, q 3e-29, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDOST]] (+0.74, fdr 7e-06), [[BPNT2]] (+0.70, fdr 7e-06), [[BSG]] (+0.69, fdr 7e-06); moves opposite to [[PSMA7]] (-0.60, fdr 1e-05), [[PIGBOS1]] (-0.60, fdr 3e-05), [[PDRG1]] (-0.58, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +19.8 | 0e+00 | 47/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +17.9 | 0e+00 | 42/44 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +11.8 | 6e-30 | 41/45 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +5.9 | 5e-07 | 41/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.9 | 5e-07 | 30/50 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.4 | 6e-06 | 24/49 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 0.001 | 32/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 29/49 (LoVo, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 26/48 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.027 | 25/48 (LS 180, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.055 | 13/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.060 | 15/48 (CHP-212, SW48, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.060 | 15/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.076 | 20/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.085 | 16/49 (PANC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.663×** | -11.8 | 3e-29 | 42/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -10.3 | 3e-22 | 38/48 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.615×** | -9.5 | 4e-19 | 43/49 (HS-578T, AN3 CA, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -9.3 | 2e-18 | 1/50 (RPMI-7951) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -8.2 | 2e-14 | 40/48 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -7.1 | 8e-11 | 38/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -6.3 | 2e-08 | 34/48 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -4.6 | 3e-04 | 27/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.805×** | -4.4 | 7e-04 | 27/48 (LS 180, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.816×** | -4.1 | 0.002 | 25/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.814×** | -4.0 | 0.003 | 22/47 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.819×** | -3.8 | 0.006 | 24/48 (KATO III, C32, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.7 | 0.011 | 11/49 (H4, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.5 | 0.020 | 24/45 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | 0.841× | -3.4 | 0.026 | 20/47 (C-33 A, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.057 | 23/49 (KATO III, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 131 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.68× (z +11.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.415× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 106 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +16.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.332× (z -14.5) |
| [[J82 (line)]] | alt | 173 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.9) |
| [[KATO III (line)]] | alt | 140 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +16.0) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 0.5 µM 0.346× (z -14.7) |
| [[HOP62 (line)]] | alt | 198 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -12.5) |
| [[LS 180 (line)]] | wt | 116 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -11.9) |
| [[SW480 (line)]] | alt | 122 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -9.6) |
| [[C-33 A (line)]] | alt | 132 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 116 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.7) |
| [[HS-578T (line)]] | alt | 192 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +13.8) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.385× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 98.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 92.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 115 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +15.0) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.518× (z -8.9) |
| [[PANC-1 (line)]] | alt | 153 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +16.9) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.531× (z -9.8) |
| [[A549 (line)]] | wt | 93.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +17.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 174 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -10.4) |
| [[H4 (line)]] | wt | 192 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.9) |
| [[HT-29 (line)]] | alt | 137 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +11.6) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.474× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 129 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +14.2) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.471× (z -10.1) |
| [[SHP-77 (line)]] | alt | 106 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +14.2) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.420× (z -9.7) |
| [[SNU-423 (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 121 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -8.6) |
| [[SW1417 (line)]] | alt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.5) |
| [[A498 (line)]] | wt | 85.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +12.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 163 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.228× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 71.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +11.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 84.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.2) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0746× (z -11.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 184 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.2) |
| [[Hs 766T (line)]] | wt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 94.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.5) |
| [[SW48 (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 69.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -8.9) |
| [[CHP-212 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 93.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 165 | 0 | 1 | — | [[Indacaterol (maleate) (drug)]] 0.05 µM 0.131× (z -10.5) |
| [[NCI-H2122 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDOST]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 692 |
| [[BPNT2]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[BSG]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PRKCSH]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 999 |
| [[LRPAP1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SELENON]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.67 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RPN2]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 662 |
| [[EMC1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[AGPAT1]] | +0.67 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[PRPF8]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA7]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[PIGBOS1]] | -0.60 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[PDRG1]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[GLRX2]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | -0.58 | -0.45 / -0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 | STRING 517 |
| [[NSUN5]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[RPF1]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ATF4]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[FDX2]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PDCD5]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GANAB's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MMP2]] | B | MMP2 activity raises GANAB's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without MMP2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[PSMB5]] | B | PSMB5 activity raises GANAB's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.6, -22.3); signed map (-26.5, -38.2). **Vector** length 120, 36.0% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.53 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.52 to 7); *epithelial mesenchymal transition* (hallmark, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.8 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +0.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.4 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.9 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | glucosidase II alpha subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,624,826-62,646,726 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluII, G2AN, KIAA0088, GIIA, GIIalpha |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Reactome | 20 pathways, smallest: Maturation of spike protein_9683686; Calnexin/calreticulin cycle; Translation of Structural Proteins_9683701 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14697](https://www.uniprot.org/uniprotkb/Q14697) (Neutral alpha-glucosidase AB):

> Catalytic subunit of glucosidase II that cleaves sequentially the 2 innermost alpha-1,3-linked glucose residues from the Glc(2)Man(9)GlcNAc(2) oligosaccharide precursor of immature glycoproteins. Required for PKD1/Polycystin-1 and PKD2/Polycystin-2 maturation and localization to the cell surface and cilia.

**Summary**, from NCBI Gene [23193](https://www.ncbi.nlm.nih.gov/gene/23193):

> This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mutations in this gene cause autosomal-dominant polycystic kidney and liver disease. [provided by …

**Accessions** — [HGNC:4138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4138) · Entrez [23193](https://www.ncbi.nlm.nih.gov/gene/23193) · UniProt [Q14697](https://www.uniprot.org/uniprotkb/Q14697) · Ensembl [ENSG00000089597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089597)

## Data

Gene col 1591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1591); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1591]; `tensor/DDL_lfc|DDL_z.npy` [1591]; `embed/gene_vectors.npy` [1591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1591 or target_col == 1591). Every well: [[GANAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GANAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
