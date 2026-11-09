---
symbol: "REL"
type: "gene"
col: 8599
ensembl_id: "ENSG00000162924"
name: "REL proto-oncogene, NF-kB subunit"
location: "2p16.1"
module: 14
arm: "+"
pooled_cpm: 137.08
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# REL

*REL proto-oncogene, NF-kB subunit* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.37× (z +68.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.638× (z -9.8, q 7e-20, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFNA1]] (+0.73, fdr 7e-06), [[TNFAIP2]] (+0.73, fdr 7e-06), [[IRF1]] (+0.72, fdr 7e-06); moves opposite to [[POP1]] (-0.61, fdr 9e-06), [[ACOT7]] (-0.59, fdr 1e-05), [[TPD52L2]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.37×** | +68.9 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.77×** | +40.0 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.40×** | +32.3 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.23×** | +25.6 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +21.0 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.31×** | +18.3 | 0e+00 | 38/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.01×** | +15.2 | 0e+00 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.75×** | +15.1 | 0e+00 | 48/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +14.9 | 0e+00 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +10.6 | 2e-24 | 38/47 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +6.2 | 3e-08 | 31/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.0 | 8e-08 | 31/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.33×** | +5.8 | 4e-07 | 29/45 (LoVo, PANC-1, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.3 | 7e-04 | 19/49 (J82, SW 900, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 24/48 (KATO III, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.003 | 21/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 14/49 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.008 | 19/49 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.017 | 6/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.3 | 0.026 | 6/48 (Hs 766T, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -9.8 | 7e-20 | 37/48 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -6.5 | 2e-08 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.743×** | -6.2 | 9e-08 | 28/44 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.753×** | -5.9 | 7e-07 | 31/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -5.0 | 6e-05 | 19/48 (Hs 766T, CHP-212, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.740×** | -4.7 | 3e-04 | 25/48 (SK-MEL-2, NCI-H1573, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.683×** | -4.4 | 0.001 | 26/45 (H4, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.824×** | -4.2 | 0.002 | 20/49 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.830×** | -4.1 | 0.003 | 22/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.838× | -3.9 | 0.006 | 20/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.847× | -3.6 | 0.015 | 21/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.081 | 16/46 (NCI-H1573, H4, …) | two highest doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.091 | 6/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.870× | -3.0 | 0.091 | 11/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.907× | -3.0 | 0.091 | 10/49 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 147 | 15 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +53.4) | — |
| [[NCI-H1573 (line)]] | alt | 313 | 9 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +38.1) | [[Bortezomib (drug)]] 0.05 µM 0.408× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.553× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 276 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +37.8) | — |
| [[PANC-1 (line)]] | alt | 103 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +59.6) | — |
| [[SW 900 (line)]] | alt | 166 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +33.4) | — |
| [[LoVo (line)]] | wt | 142 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +40.2) | — |
| [[A-172 (line)]] | wt | 99.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +43.2) | — |
| [[A-427 (line)]] | wt | 167 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 175 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +51.9) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 96.9 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +34.0) | — |
| [[H4 (line)]] | wt | 102 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +30.0) | [[Bortezomib (drug)]] 5 µM 0.142× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 155 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +44.5) | [[Auranofin (drug)]] 5 µM 0.513× (z -9.6) |
| [[LS 180 (line)]] | wt | 153 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +31.5) | — |
| [[NCI-H2347 (line)]] | alt | 114 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +34.7) | [[Auranofin (drug)]] 5 µM 0.461× (z -9.0) |
| [[SNU-1 (line)]] | wt | 103 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +25.8) | — |
| [[SW480 (line)]] | alt | 101 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +36.3) | — |
| [[HOP62 (line)]] | alt | 110 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +42.0) | — |
| [[HS-578T (line)]] | alt | 88.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +40.3) | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +29.9) | — |
| [[KATO III (line)]] | alt | 105 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +32.2) | — |
| [[SW1417 (line)]] | alt | 153 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +32.1) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 155 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +30.2) | — |
| [[HepG2_C3A (line)]] | wt | 154 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +33.5) | — |
| [[LOX-IMVI (line)]] | wt | 101 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +37.1) | — |
| [[SK-MEL-2 (line)]] | alt | 79.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 24.2× (z +44.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 145 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +43.3) | [[Auranofin (drug)]] 5 µM 0.489× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 213 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +42.8) | [[Auranofin (drug)]] 5 µM 0.351× (z -13.0) |
| [[HT-29 (line)]] | alt | 126 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +37.2) | — |
| [[J82 (line)]] | alt | 49.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +30.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 149 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +28.7) | [[Auranofin (drug)]] 5 µM 0.383× (z -10.8) |
| [[RKO (line)]] | wt | 109 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +22.3) | — |
| [[HCT15 (line)]] | alt | 109 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.9) | — |
| [[NCI-H23 (line)]] | alt | 243 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +25.0) | — |
| [[SNU-423 (line)]] | alt | 96.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +40.9) | — |
| [[AN3 CA (line)]] | alt | 171 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +18.3) | — |
| [[C32 (line)]] | wt | 63.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +33.5) | — |
| [[CFPAC-1 (line)]] | alt | 160 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +48.8) | — |
| [[COLO 205 (line)]] | alt | 149 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +37.7) | — |
| [[RPMI-7951 (line)]] | alt | 144 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +31.3) | — |
| [[SHP-77 (line)]] | alt | 170 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +21.9) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 124 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +17.0) | — |
| [[Hs 766T (line)]] | wt | 123 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +24.1) | [[Auranofin (drug)]] 5 µM 0.407× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +27.7) | — |
| [[NCI-H661 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.2) | — |
| [[SW 1088 (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +12.2) | — |
| [[SW 1271 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +12.5) | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA1]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFAIP2]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRF1]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 713 |
| [[CHD2]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[BCL3]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 952 |
| [[NFKBIA]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[B2M]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 | STRING 474 |
| [[KMT2E]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SIRT1]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 | STRING 622 |
| [[PER2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NFKB1]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[NFKB2]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ACOT7]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[THBD]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[THOC5]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DAP3]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[HSPA8]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 | STRING 775 |
| [[TANGO2]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RUSC2]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[STK25]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL2]] | B | CXCL2 activity raises REL's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.22× lower at baseline in the lines without CXCL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[PSMB5]] | B | PSMB5 activity raises REL's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 4.2); signed map (44.5, 6.6). **Vector** length 126, 43.3% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.54 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.52 to 4); *Toll Like Receptor 3 (TLR3) Cascade* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +7.3 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +40.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +18.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.8 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.1 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.6 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.2 | -9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -11.0 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -10.5 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.5 | -3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -6.1 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | REL proto-oncogene, NF-kB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:60,881,491-60,931,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | I-Rel, c-Rel, HIVEN86A |
| Gene groups (HGNC) | NF-kappa B complex subunits; IPT domain containing |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Activation of NF-kappaB in B cells; Downstream signaling events of B Cell Receptor (BCR); Signaling by the B Cell Receptor (BCR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04864](https://www.uniprot.org/uniprotkb/Q04864) (Proto-oncogene c-Rel):

> Proto-oncogene that may play a role in differentiation and lymphopoiesis. NF-kappa-B is a pleiotropic transcription factor which is present in almost all cell types and is involved in many biological processed such as inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis. NF-kappa-B is a homo- or heterodimeric complex formed by the Rel-like domain-containing proteins RELA/p65, RELB, NFKB1/p105, NFKB1/p50, REL and NFKB2/p52. The dimers bind at kappa-B sites in the DNA …

**Summary**, from NCBI Gene [5966](https://www.ncbi.nlm.nih.gov/gene/5966):

> This gene encodes a protein that belongs to the Rel homology domain/immunoglobulin-like fold, plexin, transcription factor (RHD/IPT) family. Members of this family regulate genes involved in apoptosis, inflammation, the immune response, and oncogenic processes. This proto-oncogene plays a role in the survival and proliferation of B lymphocytes. Mutation or amplification of this gene is associated with B-cell lymphomas, including Hodgkin's lymphoma. Single nucleotide polymorphisms in this gene …

**Accessions** — [HGNC:9954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9954) · Entrez [5966](https://www.ncbi.nlm.nih.gov/gene/5966) · UniProt [Q04864](https://www.uniprot.org/uniprotkb/Q04864) · Ensembl [ENSG00000162924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162924)

## Data

Gene col 8599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8599); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8599]; `tensor/DDL_lfc|DDL_z.npy` [8599]; `embed/gene_vectors.npy` [8599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8599 or target_col == 8599). Every well: [[REL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
