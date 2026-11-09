---
symbol: "BAZ1A"
type: "gene"
col: 12627
ensembl_id: "ENSG00000198604"
name: "bromodomain adjacent to zinc finger domain 1A"
location: "14q13.1-q13.2"
module: 57
arm: "-"
pooled_cpm: 166.99
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# BAZ1A

*bromodomain adjacent to zinc finger domain 1A* — 14q13.1-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.62× (z +65.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.680× (z -10.2, q 9e-22, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP6]] (+0.67, fdr 1e-05), [[HIVEP1]] (+0.67, fdr 1e-05), [[PLSCR2]] (+0.65, fdr 7e-05); moves opposite to [[NDRG3]] (-0.70, fdr 1e-05), [[PLA2G12A]] (-0.63, fdr 3e-05), [[ELP1]] (-0.62, fdr 5e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.62×** | +65.0 | 0e+00 | 48/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.71×** | +39.4 | 0e+00 | 48/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +31.8 | 0e+00 | 46/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +18.9 | 0e+00 | 45/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +18.7 | 0e+00 | 46/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +17.9 | 0e+00 | 45/50 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +16.7 | 0e+00 | 41/49 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +14.9 | 0e+00 | 40/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +11.7 | 7e-30 | 40/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +11.6 | 2e-29 | 39/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +8.3 | 5e-15 | 27/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +7.6 | 1e-12 | 31/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +7.2 | 3e-11 | 35/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +5.6 | 9e-07 | 24/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +5.3 | 4e-06 | 24/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +5.1 | 1e-05 | 25/48 (A-172, C-33 A, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.3 | 6e-04 | 19/48 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.007 | 22/48 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.010 | 14/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.016 | 14/47 (NCI-H2030, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.680×** | -10.2 | 9e-22 | 35/48 (BT-474, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.751×** | -7.6 | 1e-11 | 34/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.601×** | -7.1 | 3e-10 | 37/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.802×** | -5.8 | 8e-07 | 26/48 (NCI-H2347, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.860× | -5.6 | 2e-06 | 17/48 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.822×** | -5.2 | 2e-05 | 25/48 (RKO, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.819×** | -5.0 | 5e-05 | 23/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.841× | -4.6 | 3e-04 | 19/48 (SW1417, LoVo, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.861× | -4.0 | 0.005 | 17/49 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.865× | -3.7 | 0.013 | 19/47 (SNU-423, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.909× | -3.6 | 0.020 | 16/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.876× | -3.5 | 0.023 | 14/48 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.877× | -3.5 | 0.023 | 13/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.785×** | -3.4 | 0.030 | 18/48 (SW 900, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.914× | -3.3 | 0.030 | 3/48 (Panc 03.27, A-172, …) | rises with dose |  |
| [[Lopinavir (drug)]] 5 µM |  | 0.882× | -3.3 | 0.030 | 7/47 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.050 | 20/49 (BT-474, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.873× | -3.1 | 0.061 | 11/49 (BT-474, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 488 | 7 (4 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +31.7) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -21.4) |
| [[NCI-H460 (line)]] | wt | 154 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +40.1) | — |
| [[SNU-1 (line)]] | wt | 161 | 10 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +24.5) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 85.5 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +27.9) | — |
| [[LoVo (line)]] | wt | 153 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +30.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 216 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +31.7) | — |
| [[NCI-H2347 (line)]] | alt | 300 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +38.1) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -20.1) |
| [[HOP62 (line)]] | alt | 108 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +42.8) | — |
| [[SW 900 (line)]] | alt | 143 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +27.0) | — |
| [[SW48 (line)]] | wt | 241 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 136 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.5) | [[Panobinostat (drug)]] 0.5 µM 0.502× (z -11.5) |
| [[A498 (line)]] | wt | 157 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +44.9) | — |
| [[HS-578T (line)]] | alt | 79.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +30.1) | — |
| [[LS 180 (line)]] | wt | 116 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +20.5) | — |
| [[Panc 03.27 (line)]] | alt | 308 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +44.9) | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -13.0) |
| [[PANC-1 (line)]] | alt | 117 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +59.3) | — |
| [[C32 (line)]] | wt | 90.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +32.8) | — |
| [[H4 (line)]] | wt | 148 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +30.2) | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 153 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +41.5) | — |
| [[J82 (line)]] | alt | 209 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +44.0) | — |
| [[LOX-IMVI (line)]] | wt | 225 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 185 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +36.3) | [[Selinexor (drug)]] 5 µM 0.471× (z -12.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H1792 (line)]] | alt | 217 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +44.8) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 248 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +52.4) | — |
| [[Hs 766T (line)]] | wt | 109 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +31.0) | — |
| [[hTERT-HPNE (line)]] | wt | 176 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +30.5) | — |
| [[NCI-H23 (line)]] | alt | 106 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +21.2) | — |
| [[RKO (line)]] | wt | 272 | 1 | 5 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 124 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +30.2) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +28.1) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 142 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +40.3) | — |
| [[A-427 (line)]] | wt | 78.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +22.1) | — |
| [[A549 (line)]] | wt | 210 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +45.4) | — |
| [[AsPC-1 (line)]] | alt | 156 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +35.0) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.4) |
| [[C-33 A (line)]] | alt | 142 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 115 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +30.7) | — |
| [[NCI-H2030 (line)]] | alt | 178 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +35.5) | — |
| [[SHP-77 (line)]] | alt | 136 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.417× (z -10.0) |
| [[SW 1088 (line)]] | alt | 100 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +10.7) | [[Voriconazole (drug)]] 0.05 µM 0.0734× (z -9.3) |
| [[COLO 205 (line)]] | alt | 208 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +23.2) | — |
| [[HT-29 (line)]] | alt | 150 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +28.5) | — |
| [[KATO III (line)]] | alt | 133 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.4) | — |
| [[SW1417 (line)]] | alt | 165 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +21.9) | — |
| [[AN3 CA (line)]] | alt | 222 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.5) | — |
| [[NCI-H661 (line)]] | alt | 554 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.7) |
| [[SW 1271 (line)]] | alt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +13.7) | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | +0.67 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[HIVEP1]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PLSCR2]] | +0.65 | +0.65 / +0.37 | both halves | 7e-05 |  |
| [[DGKH]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.63 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[MED13]] | +0.63 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[NEK8]] | +0.63 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[CREBBP]] | +0.63 | +0.50 / +0.45 | both halves | 3e-05 | same gene group |
| [[PATL2]] | +0.62 | +0.62 / +0.36 | both halves | 9e-05 |  |
| [[CTSS]] | +0.62 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.70 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.63 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ELP1]] | -0.62 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[PIK3R2]] | -0.62 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TBCE]] | -0.61 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HACE1]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[SKIC3]] | -0.60 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[OSBPL7]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[STARD3NL]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[MAST3]] | -0.59 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.59 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[AKTIP]] | -0.59 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BAZ1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | BAZ1A's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | BAZ1A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.455 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, -5.5); signed map (16.6, -8.0). **Vector** length 141, 48.5% of its response variance represented; |z| ≥ 3 in 1,605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.9 | +18.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +39.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +18.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.2 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.3 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.4 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.3 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.2 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.8 | -7.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.2 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain adjacent to zinc finger domain 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1-q13.2 — chr14:34,752,731-34,875,647 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hACF1, ACF1, WALp1, WCRF180 |
| Gene groups (HGNC) | PHD finger proteins; Bromodomain containing; Chromatin accessibility complex; ACF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRL2](https://www.uniprot.org/uniprotkb/Q9NRL2) (Bromodomain adjacent to zinc finger domain protein 1A):

> Regulatory subunit of the ATP-dependent ACF-1 and ACF-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on chromatin and slide edge- and center-positioned histone octamers away from their original location on the DNA template to facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. Both complexes regulate the spacing of nucleosomes along the chromatin and have the ability to slide mononucleosomes to the center of a …

**Summary**, from NCBI Gene [11177](https://www.ncbi.nlm.nih.gov/gene/11177):

> The BAZ1A gene encodes the accessory subunit of the ATP-dependent chromatin assembly factor (ACF), a member of the ISWI ('imitation switch') family of chromatin remodeling complexes (summarized by Racki et al., 2009 [PubMed 20033039]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:960) · Entrez [11177](https://www.ncbi.nlm.nih.gov/gene/11177) · UniProt [Q9NRL2](https://www.uniprot.org/uniprotkb/Q9NRL2) · Ensembl [ENSG00000198604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198604)

## Data

Gene col 12627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12627); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12627]; `tensor/DDL_lfc|DDL_z.npy` [12627]; `embed/gene_vectors.npy` [12627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12627 or target_col == 12627). Every well: [[BAZ1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAZ1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
