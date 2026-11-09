---
symbol: "FXR1"
type: "gene"
col: 3551
ensembl_id: "ENSG00000114416"
name: "FMR1 autosomal homolog 1"
location: "3q26.33"
module: 60
arm: "+"
pooled_cpm: 285.18
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# FXR1

*FMR1 autosomal homolog 1* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.62× (z +17.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.619× (z -8.5, q 1e-14, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.713× (z -6.2, q 1e-07, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST13]] (+0.72, fdr 7e-06), [[TXNL1]] (+0.68, fdr 7e-06), [[SUGT1]] (+0.65, fdr 7e-06); moves opposite to [[TLNRD1]] (-0.59, fdr 1e-05), [[OPA3]] (-0.58, fdr 1e-05), [[ACTR3B]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.62×** | +17.7 | 0e+00 | 48/48 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.50×** | +16.9 | 0e+00 | 48/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.21×** | +13.8 | 8e-41 | 48/48 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +12.8 | 4e-35 | 44/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +11.1 | 1e-26 | 43/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +11.0 | 3e-26 | 40/48 (C32, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +9.3 | 1e-18 | 47/49 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.62×** | +9.3 | 1e-18 | 43/45 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.5 | 1e-15 | 34/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +8.3 | 8e-15 | 43/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.35×** | +7.9 | 2e-13 | 35/48 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.79×** | +7.7 | 9e-13 | 46/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.15×** | +7.4 | 8e-12 | 45/47 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.42×** | +6.4 | 5e-09 | 33/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 3e-06 | 31/48 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.6 | 1e-04 | 31/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.001 | 14/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.002 | 30/49 (A-172, PANC-1, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 24/48 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.023 | 19/49 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.023 | 28/48 (KATO III, SNU-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -8.5 | 1e-14 | 42/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -6.2 | 1e-07 | 47/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.741×** | -4.0 | 0.014 | 31/48 (SNU-423, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.032 | 25/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.4 | 0.062 | 0/50 | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.062 | 22/48 (LS 180, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.074 | 18/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.839× | -3.2 | 0.078 | 20/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.884× | -3.2 | 0.078 | 18/49 (LoVo, HCT15, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.085 | 21/48 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.085 | 23/49 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 323 | 13 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +20.6) | — |
| [[NCI-H460 (line)]] | wt | 182 | 11 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +22.5) | — |
| [[COLO 205 (line)]] | alt | 128 | 9 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.31× (z +22.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +13.6) | — |
| [[KATO III (line)]] | alt | 206 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.96× (z +23.3) | — |
| [[LoVo (line)]] | wt | 228 | 8 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.40× (z +17.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -12.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H1573 (line)]] | alt | 215 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 274 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.516× (z -10.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 307 | 7 (4 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.83× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -8.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 169 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.65× (z +16.1) | — |
| [[NCI-H23 (line)]] | alt | 341 | 8 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +13.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +11.5) | — |
| [[A-427 (line)]] | wt | 642 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -12.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 343 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +16.5) | — |
| [[A-172 (line)]] | wt | 288 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.60× (z +14.3) | — |
| [[C32 (line)]] | wt | 194 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +14.8) | — |
| [[J82 (line)]] | alt | 338 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 284 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +17.0) | — |
| [[LS 180 (line)]] | wt | 116 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.51× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 368 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +12.8) | — |
| [[RKO (line)]] | wt | 221 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.39× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 342 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 265 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 263 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +13.4) | — |
| [[SW48 (line)]] | wt | 266 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.9) | — |
| [[A498 (line)]] | wt | 315 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 195 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.05× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 224 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 199 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +13.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 298 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.47× (z +16.1) | — |
| [[SW1417 (line)]] | alt | 370 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +12.3) | — |
| [[A549 (line)]] | wt | 196 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 320 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 347 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.96× (z +15.0) | — |
| [[H4 (line)]] | wt | 316 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.61× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 296 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HOP62 (line)]] | alt | 278 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.85× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 344 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.50× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 259 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 238 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 338 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.05× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 461 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -8.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 183 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +9.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 360 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 339 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 306 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST13]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TXNL1]] | +0.68 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[SUGT1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HBS1L]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[HSP90AB1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CYB5R4]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HSP90AB2P]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CDC40]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TCP1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PSMC6]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[HSP90AB3P]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[OPA3]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ACTR3B]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[AEN]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ENTR1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[LINS1]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.52 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[PYCR2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SLC20A2]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.5, -7.0); signed map (-27.3, -20.3). **Vector** length 114, 49.4% of its response variance represented; |z| ≥ 3 in 1,394 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +16.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +13.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.8 | +9.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +7.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | -1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -8.6 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.6 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.5 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.2 | +11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | +8.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.9 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | FMR1 autosomal homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:180,868,141-180,982,753 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | FMR1 family |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [P51114](https://www.uniprot.org/uniprotkb/P51114) (RNA-binding protein FXR1):

> mRNA-binding protein that acts as a regulator of mRNAs translation and/or stability, and which is required for various processes, such as neurogenesis, muscle development and spermatogenesis. Specifically binds to AU-rich elements (AREs) in the 3'-UTR of target mRNAs. Promotes formation of some phase-separated membraneless compartment by undergoing liquid-liquid phase separation upon binding to AREs-containing mRNAs, leading to assemble mRNAs into cytoplasmic ribonucleoprotein granules that …

**Summary**, from NCBI Gene [8087](https://www.ncbi.nlm.nih.gov/gene/8087):

> The protein encoded by this gene is an RNA binding protein that interacts with the functionally-similar proteins FMR1 and FXR2. These proteins shuttle between the nucleus and cytoplasm and associate with polyribosomes, predominantly with the 60S ribosomal subunit. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4023) · Entrez [8087](https://www.ncbi.nlm.nih.gov/gene/8087) · UniProt [P51114](https://www.uniprot.org/uniprotkb/P51114) · Ensembl [ENSG00000114416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114416)

## Data

Gene col 3551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3551); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3551]; `tensor/DDL_lfc|DDL_z.npy` [3551]; `embed/gene_vectors.npy` [3551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3551 or target_col == 3551). Every well: [[FXR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
