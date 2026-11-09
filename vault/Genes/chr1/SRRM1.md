---
symbol: "SRRM1"
type: "gene"
col: 5431
ensembl_id: "ENSG00000133226"
name: "serine and arginine repetitive matrix 1"
location: "1p36.11"
module: 184
arm: "-"
pooled_cpm: 199.0
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# SRRM1

*serine and arginine repetitive matrix 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +19.8, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.91× (z +11.9, q 5e-30, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B2]] (+0.64, fdr 7e-06), [[PPIL4]] (+0.63, fdr 1e-05), [[DHX29]] (+0.63, fdr 1e-05); moves opposite to [[PNP]] (-0.55, fdr 2e-05), [[LINC01128]] (-0.54, fdr 4e-05), [[IRGQ]] (-0.50, fdr 3e-05).
> It sits in the **-** arm of [[Module 184]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.32×** | +19.8 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.91×** | +11.9 | 5e-30 | 48/49 (COLO 205, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +11.7 | 3e-29 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.76×** | +9.1 | 2e-17 | 47/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +8.5 | 1e-15 | 47/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.56×** | +7.4 | 1e-11 | 45/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.58×** | +7.4 | 1e-11 | 40/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.52×** | +7.0 | 2e-10 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.48×** | +6.3 | 2e-08 | 33/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.45×** | +6.0 | 1e-07 | 42/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.9 | 2e-07 | 39/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.6 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.4 | 5e-04 | 30/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.29×** | +4.2 | 9e-04 | 31/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.001 | 35/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 11/49 (KATO III, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.085 | 23/49 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.818× | -3.3 | 0.48 | 27/48 (RKO, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 219 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.65× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 196 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +28.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +16.7) | — |
| [[NCI-H1573 (line)]] | alt | 176 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +21.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 149 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +13.1) | — |
| [[A549 (line)]] | wt | 121 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +20.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 190 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.2× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 178 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +17.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 177 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 169 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.7) | — |
| [[H4 (line)]] | wt | 144 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +17.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.12× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 231 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +17.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 231 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +16.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +9.0) | — |
| [[KATO III (line)]] | alt | 187 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +17.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +10.4) | — |
| [[LoVo (line)]] | wt | 233 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.51× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 278 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 127 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 278 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +9.8) | — |
| [[RKO (line)]] | wt | 239 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.97× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 175 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.97× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 348 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +8.8) | — |
| [[C32 (line)]] | wt | 155 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 224 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.72× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[Panc 03.27 (line)]] | alt | 163 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.65× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 146 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +16.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.04× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 207 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.54× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 93.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 271 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +8.9) | — |
| [[A498 (line)]] | wt | 174 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 210 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 342 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HepG2_C3A (line)]] | wt | 315 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[J82 (line)]] | alt | 247 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 236 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RPMI-7951 (line)]] | alt | 193 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 218 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW48 (line)]] | wt | 266 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 227 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B2]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 917 |
| [[PPIL4]] | +0.63 | +0.70 / +0.49 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[DHX29]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PPIG]] | +0.60 | +0.71 / +0.44 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 896 |
| [[PRPF4B]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 893 |
| [[MATR3]] | +0.57 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TPR]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 681 |
| [[ZC3H15]] | +0.55 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[SAFB]] | +0.54 | +0.59 / +0.57 | both halves | 1e-05 | STRING 484 |
| [[WBP11]] | +0.54 | +0.47 / +0.63 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions; STRING 977 |
| [[RNF214]] | +0.53 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[SREK1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 | STRING 497 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNP]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LINC01128]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[IRGQ]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MIR222HG]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MOAP1]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[NAXE]] | -0.49 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[GATAD2A]] | -0.48 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[S100A11]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PTRH1]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[KLHL29]] | -0.46 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[HSBP1]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[C3orf52]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-36.4, -11.0); signed map (-15.0, -10.3). **Vector** length 80.5, 27.7% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.2 | +19.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.1 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +3.6 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +11.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +8.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | -0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +0.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -5.8 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.3 | +7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -4.3 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.0 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | +0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine repetitive matrix 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,631,716-24,673,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRM160, POP101, MGC39488 |
| Reactome | 16 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYB3](https://www.uniprot.org/uniprotkb/Q8IYB3) (Serine/arginine repetitive matrix protein 1):

> Part of pre- and post-splicing multiprotein mRNP complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Involved in numerous pre-mRNA processing events. Promotes constitutive and exonic splicing enhancer (ESE)-dependent splicing activation by bridging together sequence-specific (SR family proteins, SFRS4, SFRS5 and TRA2B/SFRS10) and basal snRNP (SNRP70 and SNRPA1) factors of the spliceosome. Stimulates mRNA 3'-end cleavage …

**Summary**, from NCBI Gene [10250](https://www.ncbi.nlm.nih.gov/gene/10250):

> Enables RNA binding activity. Predicted to be involved in regulation of mRNA splicing, via spliceosome. Located in nuclear speck. Part of catalytic step 2 spliceosome. Biomarker of gestational diabetes. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16638) · Entrez [10250](https://www.ncbi.nlm.nih.gov/gene/10250) · UniProt [Q8IYB3](https://www.uniprot.org/uniprotkb/Q8IYB3) · Ensembl [ENSG00000133226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133226)

## Data

Gene col 5431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5431); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5431]; `tensor/DDL_lfc|DDL_z.npy` [5431]; `embed/gene_vectors.npy` [5431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5431 or target_col == 5431). Every well: [[SRRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
