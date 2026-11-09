---
symbol: "SAMD4B"
type: "gene"
col: 11003
ensembl_id: "ENSG00000179134"
name: "sterile alpha motif domain containing 4B"
location: "19q13.2"
module: 2
arm: "+"
pooled_cpm: 165.45
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SAMD4B

*sterile alpha motif domain containing 4B* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.05× (z +20.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.791× (z -9.7, q 2e-19, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VRK3]] (+0.71, fdr 7e-06), [[PWWP3A]] (+0.68, fdr 1e-05), [[TANGO2]] (+0.67, fdr 7e-06); moves opposite to [[MBNL3]] (-0.64, fdr 1e-05), [[RWDD2B]] (-0.60, fdr 1e-05), [[YAP1]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +20.9 | 0e+00 | 45/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.05×** | +19.9 | 0e+00 | 47/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +17.9 | 0e+00 | 45/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +10.0 | 2e-21 | 37/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +10.0 | 2e-21 | 31/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +9.4 | 5e-19 | 36/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +9.0 | 2e-17 | 45/49 (PANC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +8.7 | 2e-16 | 33/49 (NCI-H23, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +8.6 | 7e-16 | 35/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +6.7 | 1e-09 | 28/45 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +6.3 | 2e-08 | 27/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +6.0 | 1e-07 | 24/44 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +5.7 | 4e-07 | 26/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +5.2 | 6e-06 | 20/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.19× | +4.9 | 3e-05 | 22/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +4.2 | 9e-04 | 13/48 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.004 | 16/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.8 | 0.004 | 6/49 (HT-29, RKO, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.005 | 7/48 (RKO, SW1417, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.009 | 15/48 (HOP62, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.009 | 17/47 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -9.7 | 2e-19 | 33/49 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -9.5 | 4e-19 | 35/48 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.770×** | -7.7 | 4e-12 | 28/48 (A549, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -6.0 | 2e-07 | 27/48 (A549, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.874× | -5.6 | 2e-06 | 19/48 (BT-474, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.834× | -5.3 | 9e-06 | 22/48 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.828×** | -5.3 | 9e-06 | 21/48 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.864× | -4.1 | 0.003 | 17/50 (SW480, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.913× | -3.8 | 0.010 | 10/48 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.880× | -3.6 | 0.016 | 20/48 (HEC-1-A, NCI-H23, …) | two highest doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.965× | -3.5 | 0.020 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.923× | -3.3 | 0.039 | 5/48 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.923× | -3.3 | 0.039 | 7/48 (AsPC-1, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.894× | -3.3 | 0.041 | 3/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.070 | 13/48 (C32, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.902× | -3.0 | 0.081 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 91.8 | 8 (2 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +17.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 138 | 4 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -14.2) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.544× (z -10.0) |
| [[HOP62 (line)]] | alt | 173 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.40× (z +15.7) | — |
| [[NCI-H23 (line)]] | alt | 106 | 3 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.475× (z -10.2) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -8.8) |
| [[PANC-1 (line)]] | alt | 1,057 | 6 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.12× (z +26.1) | — |
| [[A549 (line)]] | wt | 206 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +12.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.494× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 89.4 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +11.6) | — |
| [[A-172 (line)]] | wt | 124 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.01× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.518× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[BT-474 (line)]] | alt | 97.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 88.5 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.94× (z +13.9) | — |
| [[H4 (line)]] | wt | 160 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +10.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -17.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HT-29 (line)]] | alt | 179 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.25× (z +22.7) | — |
| [[LoVo (line)]] | wt | 109 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 90.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 116 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 77.2 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.538× (z -9.1) |
| [[SW1417 (line)]] | alt | 95.9 | 2 (1 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -10.4) |
| [[SW48 (line)]] | wt | 125 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 124 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 81.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.08× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 132 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.9) ⚠ cell-cycle shift, explains ~4% of this change |
| [[KATO III (line)]] | alt | 120 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 103 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 98.8 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.467× (z -9.9) |
| [[SHP-77 (line)]] | alt | 119 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[A-427 (line)]] | wt | 107 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.88× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.0) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.4) | — |
| [[C32 (line)]] | wt | 74.0 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.49× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 91.1 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -10.9) |
| [[HCT15 (line)]] | alt | 109 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 118 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 99.5 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.3) |
| [[SNU-423 (line)]] | alt | 82.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 144 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 1.97× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 101 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PRKCZ]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.65 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[PSMD3]] | +0.65 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ABAT]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[KCTD21]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[UFD1]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PLD3]] | +0.61 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[EXOC6B]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RPS6KC1]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL3]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[RWDD2B]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[YAP1]] | -0.59 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[LINC01145-1]] | -0.58 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ISOC1]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[FAS]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SLC16A9]] | -0.57 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[LHFPL6]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TIFA]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | -0.56 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[BMI1]] | -0.56 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K1]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.5, -7.9); signed map (-28.4, -1.1). **Vector** length 134, 39.5% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +13.4 | +20.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +13.0 | +19.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.0 | +17.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.9 | +9.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -10.6 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -6.7 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,342,421-39,385,710 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10211, MGC99832, SMGB, hSmaug2 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5PRF9](https://www.uniprot.org/uniprotkb/Q5PRF9) (Protein Smaug homolog 2):

> Has transcriptional repressor activity. Overexpression inhibits the transcriptional activities of AP-1, p53/TP53 and CDKN1A.

**Summary**, from NCBI Gene [55095](https://www.ncbi.nlm.nih.gov/gene/55095):

> Enables RNA binding activity. Predicted to be involved in nuclear-transcribed mRNA poly(A) tail shortening. Predicted to act upstream of or within cerebellar neuron development. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25492) · Entrez [55095](https://www.ncbi.nlm.nih.gov/gene/55095) · UniProt [Q5PRF9](https://www.uniprot.org/uniprotkb/Q5PRF9) · Ensembl [ENSG00000179134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179134)

## Data

Gene col 11003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11003); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11003]; `tensor/DDL_lfc|DDL_z.npy` [11003]; `embed/gene_vectors.npy` [11003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11003 or target_col == 11003). Every well: [[SAMD4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
