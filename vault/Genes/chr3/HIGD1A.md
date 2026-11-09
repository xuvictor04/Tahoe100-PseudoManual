---
symbol: "HIGD1A"
type: "gene"
col: 11165
ensembl_id: "ENSG00000181061"
name: "HIG1 hypoxia inducible domain family member 1A"
location: "3p22.1"
module: 24
arm: "-"
pooled_cpm: 31.84
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# HIGD1A

*HIG1 hypoxia inducible domain family member 1A* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.98× (z +23.5, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +9.4, q 8e-19, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.500× (z -5.3, q 7e-05, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBNL]] (+0.61, fdr 1e-05), [[ACTR1A]] (+0.57, fdr 2e-05), [[IL13RA1]] (+0.55, fdr 3e-05); moves opposite to [[SNHG7]] (-0.61, fdr 1e-05), [[PCGF1]] (-0.59, fdr 3e-05, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[AFMID]] (-0.55, fdr 1e-05), [[ATP5MC2]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.98×** | +23.5 | 0e+00 | 44/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.65×** | +21.7 | 0e+00 | 36/37 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.59×** | +17.3 | 0e+00 | 38/42 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.4 | 8e-19 | 37/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +7.0 | 3e-10 | 35/48 (PANC-1, HOP62, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +6.5 | 6e-09 | 30/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +6.4 | 1e-08 | 37/47 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.54×** | +6.4 | 1e-08 | 31/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.57×** | +6.3 | 2e-08 | 31/47 (HOP62, LOX-IMVI, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.55×** | +6.2 | 4e-08 | 32/46 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.54×** | +6.1 | 6e-08 | 36/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.51×** | +6.0 | 9e-08 | 37/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +6.0 | 1e-07 | 32/47 (PANC-1, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.50×** | +5.9 | 1e-07 | 34/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +5.9 | 1e-07 | 33/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 4e-07 | 32/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 2e-06 | 28/48 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.1 | 1e-05 | 28/47 (SW480, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 2e-04 | 22/48 (PANC-1, A498, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.003 | 22/48 (SNU-423, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.013 | 16/44 (C-33 A, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.021 | 14/47 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.036 | 11/48 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.045 | 12/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.067 | 10/48 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.500×** | -5.3 | 7e-05 | 35/47 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | **0.766×** | -3.7 | 0.052 | 17/47 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.650× | -3.3 | 0.19 | 9/48 (HEC-1-A, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.669× | -3.1 | 0.30 | 9/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 28.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.92× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 56.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 18.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[A498 (line)]] | wt | 14.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.28× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 18.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 40.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 40.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 24.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 41.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.65× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 36.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 20.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.85× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.00× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 52.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.75× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 79.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBNL]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ACTR1A]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[IL13RA1]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CAB39]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ACTR2]] | +0.54 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[PSME3]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[RHOC]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[AAGAB]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[KRT8]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LAMC1]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[LRP10]] | +0.51 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[HSD17B12]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG7]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | -0.59 | -0.43 / -0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[AFMID]] | -0.55 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MYNN]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SCAMP3]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MAP2K7]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EPB41L4A-AS1]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SAT2]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CRTC1]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RPAIN]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[INAFM1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TMEM161B-DT]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HIGD1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | HIGD1A's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | HIGD1A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.452 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.8, -19.4); signed map (-4.4, 37.0). **Vector** length 73.8, 16.8% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.9 | +21.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.8 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +17.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.8 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +2.0 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -5.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | HIG1 hypoxia inducible domain family member 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,782,908-42,804,490 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIG1, DKFZP564K247, RCF1A |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 7 pathways, smallest: Regulation of gene expression by Hypoxia-inducible Factor; Complex IV assembly; Cellular response to hypoxia |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y241](https://www.uniprot.org/uniprotkb/Q9Y241) (HIG1 domain family member 1A, mitochondrial):

> Proposed subunit of cytochrome c oxidase (COX, complex IV), which is the terminal component of the mitochondrial respiratory chain that catalyzes the reduction of oxygen to water. May play a role in the assembly of respiratory supercomplexes.

**Summary**, from NCBI Gene [25994](https://www.ncbi.nlm.nih.gov/gene/25994):

> Acts upstream of or within negative regulation of apoptotic process. Located in mitochondrion. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29527) · Entrez [25994](https://www.ncbi.nlm.nih.gov/gene/25994) · UniProt [Q9Y241](https://www.uniprot.org/uniprotkb/Q9Y241) · Ensembl [ENSG00000181061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181061)

## Data

Gene col 11165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11165); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11165]; `tensor/DDL_lfc|DDL_z.npy` [11165]; `embed/gene_vectors.npy` [11165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11165 or target_col == 11165). Every well: [[HIGD1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIGD1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
