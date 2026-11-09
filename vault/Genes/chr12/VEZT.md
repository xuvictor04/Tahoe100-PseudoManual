---
symbol: "VEZT"
type: "gene"
col: 383
ensembl_id: "ENSG00000028203"
name: "vezatin, adherens junctions transmembrane protein"
location: "12q22"
module: 126
arm: "+"
pooled_cpm: 218.39
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# VEZT

*vezatin, adherens junctions transmembrane protein* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.00× (z +14.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.501× (z -20.8, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBS5]] (+0.63, fdr 3e-05), [[FAM133B]] (+0.61, fdr 1e-05), [[CYB5R1]] (+0.61, fdr 6e-05); moves opposite to [[HCFC1]] (-0.62, fdr 4e-05), [[PHF8]] (-0.60, fdr 2e-05), [[CERS2]] (-0.60, fdr 9e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +14.8 | 0e+00 | 47/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.98×** | +13.8 | 7e-41 | 43/48 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +13.2 | 2e-37 | 44/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +12.0 | 4e-31 | 46/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.42×** | +10.5 | 7e-24 | 31/48 (A498, HT-29, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +6.7 | 2e-09 | 37/49 (NCI-H460, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +6.2 | 5e-08 | 30/48 (A498, NCI-H460, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 9e-04 | 24/49 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 27/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.2 | 0.082 | 13/48 (A498, LS 180, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.095 | 16/49 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.1 | 0.095 | 20/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.095 | 4/48 (A-172, SNU-1, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.15× | +3.0 | 0.095 | 15/48 (A549, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.501×** | -20.8 | 0e+00 | 45/49 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.478×** | -14.4 | 2e-44 | 40/44 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -10.2 | 3e-22 | 44/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -9.5 | 4e-19 | 41/49 (HEC-1-A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -8.8 | 1e-16 | 42/48 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -7.8 | 6e-13 | 36/50 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -7.4 | 1e-11 | 32/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -6.9 | 4e-10 | 37/45 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -5.9 | 2e-07 | 31/48 (SW 1271, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -5.3 | 7e-06 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.783×** | -4.8 | 1e-04 | 29/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.801×** | -4.7 | 1e-04 | 28/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.826×** | -4.1 | 0.002 | 25/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.828×** | -4.0 | 0.002 | 24/48 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.821×** | -3.7 | 0.007 | 25/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.857× | -3.3 | 0.034 | 18/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.905× | -3.0 | 0.084 | 7/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 187 | 12 (8 ⚠) | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 284 | 1 | 9 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.03× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 273 | 2 | 8 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.95× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -23.0) |
| [[NCI-H2347 (line)]] | alt | 418 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.77× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -23.5) |
| [[A-427 (line)]] | wt | 193 | 7 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.544× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 496 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -25.6) |
| [[NCI-H2030 (line)]] | alt | 418 | 3 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.94× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -19.8) |
| [[SW48 (line)]] | wt | 185 | 5 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.7) | [[Auranofin (drug)]] 5 µM 0.305× (z -12.5) |
| [[SW480 (line)]] | alt | 158 | 6 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.48× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -13.3) |
| [[LoVo (line)]] | wt | 194 | 4 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 307 | 1 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -18.9) |
| [[LS 180 (line)]] | wt | 154 | 5 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 249 | 3 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -22.1) |
| [[PANC-1 (line)]] | alt | 203 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -11.9) |
| [[SW 900 (line)]] | alt | 238 | 3 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.62× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -16.5) |
| [[A-172 (line)]] | wt | 144 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.3) ⚠ cell-cycle shift, explains ~32% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.500× (z -12.6) |
| [[H4 (line)]] | wt | 188 | 4 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.2) |
| [[HOP62 (line)]] | alt | 131 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 5.32× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.368× (z -12.0) |
| [[HT-29 (line)]] | alt | 119 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.60× (z +15.6) | — |
| [[KATO III (line)]] | alt | 101 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 248 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.04× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -15.3) |
| [[SW1417 (line)]] | alt | 205 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.58× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.5) |
| [[A498 (line)]] | wt | 155 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +19.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -15.4) |
| [[A549 (line)]] | wt | 511 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -28.0) |
| [[BT-474 (line)]] | alt | 209 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.8) |
| [[C32 (line)]] | wt | 133 | 2 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.9) |
| [[HCT15 (line)]] | alt | 214 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 220 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -26.7) |
| [[RPMI-7951 (line)]] | alt | 114 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 141 | 1 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -10.2) |
| [[COLO 205 (line)]] | alt | 115 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.29× (z +14.9) | — |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 89.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.79× (z +11.0) | — |
| [[J82 (line)]] | alt | 140 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 223 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.75× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.6) |
| [[SHP-77 (line)]] | alt | 153 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 157 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.352× (z -12.8) |
| [[AN3 CA (line)]] | alt | 247 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 512 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.6) |
| [[RKO (line)]] | wt | 152 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.0) |
| [[SW 1271 (line)]] | alt | 243 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.270× (z -8.6) |
| [[CHP-212 (line)]] | wt | 203 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -13.7) |
| [[Hs 766T (line)]] | wt | 73.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 113 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 163 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS5]] | +0.63 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[FAM133B]] | +0.61 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.61 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[IFI27L2]] | +0.60 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[CEP290]] | +0.60 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FAM13B]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[POLR2I]] | +0.59 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[REX1BD]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[JOSD2]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BIK]] | +0.56 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[TBC1D19]] | +0.56 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SERPINB1]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.62 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PHF8]] | -0.60 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[CERS2]] | -0.60 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[SSU72]] | -0.59 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[RCC2]] | -0.59 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[MOB1A]] | -0.57 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MTA2]] | -0.57 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[LAMTOR5-AS1]] | -0.57 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FAM53B]] ⚠ | -0.56 | -0.52 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LY6G5B]] | -0.56 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[MSANTD2]] | -0.56 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NAF1]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[U2AF2]] | -0.55 | -0.21 / -0.53 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VEZT's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FGD6]] | B | FGD6 activity raises VEZT's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without FGD6 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers VEZT's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM241B]] | C | FAM241B activity raises VEZT's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction -0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.3, -15.1); signed map (-19.7, -6.5). **Vector** length 139, 52.1% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.9 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +13.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.6 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.2 | -10.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.6 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.6 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -20.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -7.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -4.1 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | vezatin, adherens junctions transmembrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:95,217,746-95,302,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761C241 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBM0](https://www.uniprot.org/uniprotkb/Q9HBM0) (Vezatin):

> Plays a pivotal role in the establishment of adherens junctions and their maintenance in adult life. Required for morphogenesis of the preimplantation embryo, and for the implantation process.; (Microbial infection) In case of Listeria infection, promotes bacterial internalization by participating in myosin VIIa recruitment to the entry site.

**Summary**, from NCBI Gene [55591](https://www.ncbi.nlm.nih.gov/gene/55591):

> This gene encodes a transmembrane protein which has been localized to adherens junctions and shown to bind to myosin VIIA. Examination of expression of this gene in gastric cancer tissues have shown that expression is decreased which appears to be related to hypermethylation of the promoter. Expression of this gene may also be inhibited by binding of a specific microRNA to a target sequence in the 3' UTR of the transcripts. A pseudogene of this gene is located on the X chromosome. Alternative …

**Accessions** — [HGNC:18258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18258) · Entrez [55591](https://www.ncbi.nlm.nih.gov/gene/55591) · UniProt [Q9HBM0](https://www.uniprot.org/uniprotkb/Q9HBM0) · Ensembl [ENSG00000028203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028203)

## Data

Gene col 383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 383); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 383]; `tensor/DDL_lfc|DDL_z.npy` [383]; `embed/gene_vectors.npy` [383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 383 or target_col == 383). Every well: [[VEZT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEZT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
