---
symbol: "TBC1D12"
type: "gene"
col: 2926
ensembl_id: "ENSG00000108239"
name: "TBC1 domain family member 12"
location: "10q23.33"
module: 204
arm: "+"
pooled_cpm: 90.7
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# TBC1D12

*TBC1 domain family member 12* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.93× (z +12.2, q 2e-31, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.89× (z +11.8, q 1e-29, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.313× (z -20.7, q 0e+00, down in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.738× (z -5.6, q 2e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf87]] (+0.72, fdr 1e-05), [[ELF2]] (+0.69, fdr 7e-06), [[DCAF5]] (+0.68, fdr 7e-06); moves opposite to [[SMU1]] (-0.63, fdr 1e-05), [[TAF2]] (-0.63, fdr 7e-06), [[REXO1]] (-0.62, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.2 | 2e-31 | 44/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +11.8 | 1e-29 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +10.6 | 9e-24 | 37/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +8.7 | 3e-16 | 29/48 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.6 | 7e-16 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.5 | 2e-15 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.6 | 2e-12 | 33/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.1 | 8e-08 | 29/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +5.9 | 2e-07 | 29/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.5 | 2e-06 | 28/49 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 4e-06 | 32/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.4 | 5e-04 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 8e-04 | 24/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 25/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.003 | 24/48 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.005 | 23/49 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.009 | 14/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.313×** | -20.7 | 0e+00 | 40/43 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.319×** | -16.9 | 0e+00 | 43/49 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -12.6 | 3e-34 | 40/45 (SW48, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -5.6 | 2e-06 | 27/48 (C32, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -5.6 | 2e-06 | 34/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.775×** | -4.7 | 2e-04 | 25/48 (SW1417, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -4.6 | 4e-04 | 26/48 (NCI-H2347, A549, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.7 | 0.013 | 16/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.021 | 19/49 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.827×** | -3.5 | 0.024 | 21/48 (SHP-77, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.829×** | -3.5 | 0.025 | 21/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.834× | -3.4 | 0.035 | 17/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.3 | 0.050 | 13/48 (LoVo, Hs 766T, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.847× | -3.1 | 0.084 | 12/48 (RPMI-7951, C32, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.084 | 14/48 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.089 | 14/48 (HOP62, SW48, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.851× | -3.0 | 0.092 | 17/49 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.889× | -3.0 | 0.092 | 10/48 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 132 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -19.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 64.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.48× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -19.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 110 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 73.0 | 5 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.15× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -19.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 82.1 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -22.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 107 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -15.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 101 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.21× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -8.8) |
| [[SW48 (line)]] | wt | 91.4 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.3× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0707× (z -19.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 128 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -28.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 95.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.64× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 111 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 80.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.53× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 86.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.9 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[A549 (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -13.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 78.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 116 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 81.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 63.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +10.2) | — |
| [[KATO III (line)]] | alt | 73.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.98× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 93.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 87.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 98.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -15.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 84.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0599× (z -18.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 40.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.23× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 52.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.99× (z +10.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 78.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | +0.72 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ELF2]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[DCAF5]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LNX2]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[USP3]] | +0.64 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[TRIM52-AS1]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TRIM33]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CNIH4]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PTPRA]] | +0.62 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[PPP2R5A]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMU1]] | -0.63 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TAF2]] | -0.63 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[REXO1]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[LINC00641]] | -0.62 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[RABL3]] | -0.62 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[PUF60]] | -0.60 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[MANBAL]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[THOC6]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NUBP1]] | -0.59 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[CLPB]] | -0.59 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -20.4); signed map (-21.4, 16.1). **Vector** length 105, 34.8% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -20.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:94,402,541-94,536,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0608 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [O60347](https://www.uniprot.org/uniprotkb/O60347) (TBC1 domain family member 12):

> RAB11A-binding protein that plays a role in neurite outgrowth.

**Summary**, from NCBI Gene [23232](https://www.ncbi.nlm.nih.gov/gene/23232):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of autophagosome assembly. Predicted to be located in endosome and vacuole. Predicted to be active in autophagosome and recycling endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29082) · Entrez [23232](https://www.ncbi.nlm.nih.gov/gene/23232) · UniProt [O60347](https://www.uniprot.org/uniprotkb/O60347) · Ensembl [ENSG00000108239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108239)

## Data

Gene col 2926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2926); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2926]; `tensor/DDL_lfc|DDL_z.npy` [2926]; `embed/gene_vectors.npy` [2926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2926 or target_col == 2926). Every well: [[TBC1D12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
