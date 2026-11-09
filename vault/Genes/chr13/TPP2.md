---
symbol: "TPP2"
type: "gene"
col: 5623
ensembl_id: "ENSG00000134900"
name: "tripeptidyl peptidase 2"
location: "13q33.1"
module: 42
arm: "+"
pooled_cpm: 116.97
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TPP2

*tripeptidyl peptidase 2* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.96× (z +14.2, q 9e-43, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.942× (z -4.4, q 0.005, down in 3 of 50 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.261×, KATO III 0.500×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.404×, COLO 205 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L3]] (+0.67, fdr 7e-06), [[RECQL]] (+0.65, fdr 7e-06), [[GDI2]] (+0.64, fdr 7e-06); moves opposite to [[NSMCE3]] (-0.63, fdr 1e-05), [[URGCP]] (-0.59, fdr 1e-05), [[ERCC4]] (-0.59, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +14.2 | 9e-43 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +13.7 | 5e-40 | 41/49 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +13.1 | 1e-36 | 45/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +12.9 | 4e-36 | 46/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.6 | 7e-20 | 32/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.8 | 2e-16 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +8.3 | 8e-15 | 37/48 (HOP62, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.3 | 2e-11 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +6.9 | 3e-10 | 35/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +6.9 | 4e-10 | 34/48 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.7 | 1e-09 | 36/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +6.2 | 3e-08 | 33/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +6.1 | 5e-08 | 33/50 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 4e-07 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +5.7 | 5e-07 | 38/49 (C32, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 2e-06 | 28/48 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 4e-04 | 24/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.005 | 22/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.005 | 15/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5623.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.261×, KATO III 0.500×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.404×, COLO 205 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.4 | 0.005 | 3/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.829×** | -3.8 | 0.036 | 22/44 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.834× | -3.7 | 0.041 | 19/48 (HOP62, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.13 | 17/49 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.861× | -3.2 | 0.15 | 16/49 (SHP-77, SNU-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.858× | -3.1 | 0.15 | 20/47 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.15 | 18/47 (NCI-H23, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.9 | 15 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +15.4) | — |
| [[SW480 (line)]] | alt | 248 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 91.9 | 7 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 199 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 129 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 113 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 159 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +12.6) | — |
| [[C32 (line)]] | wt | 92.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.3) | — |
| [[LoVo (line)]] | wt | 106 | 5 | 0 | [[Belinostat (drug)]] 5 µM 2.25× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 5 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.73× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 106 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 92.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 132 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.39× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 111 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 132 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 64.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +11.6) | — |
| [[A549 (line)]] | wt | 72.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 66.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 191 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.13× (z +9.8) | — |
| [[KATO III (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 72.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 82.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 260 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.3) | — |
| [[A-427 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 69.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.4) | — |
| [[RKO (line)]] | wt | 183 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 149 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[A-172 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L3]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RECQL]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GDI2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PPIP5K2]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SENP5]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[P3H1]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZFC3H1]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RARS2]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MLEC]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ODF2]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DDB1]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[SFXN2]] | +0.56 | +0.38 / +0.54 | both halves | 6e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE3]] | -0.63 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[URGCP]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PPP4R2]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ZNF260]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[COIL]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[TAB2]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF592]] | -0.52 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TRAPPC3]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ZSWIM1]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.51 | -0.37 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -27.9); signed map (-53.2, 4.4). **Vector** length 78.5, 20.8% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.8 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | -3.8 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tripeptidyl peptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,596,958-102,679,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TPPII |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P29144](https://www.uniprot.org/uniprotkb/P29144) (Tripeptidyl-peptidase 2):

> Cytosolic tripeptidyl-peptidase that releases N-terminal tripeptides from polypeptides and is a component of the proteolytic cascade acting downstream of the 26S proteasome in the ubiquitin-proteasome pathway. It plays an important role in intracellular amino acid homeostasis. Stimulates adipogenesis (By similarity).

**Summary**, from NCBI Gene [7174](https://www.ncbi.nlm.nih.gov/gene/7174):

> This gene encodes a mammalian peptidase that, at neutral pH, removes tripeptides from the N terminus of longer peptides. The protein has a specialized function that is essential for some MHC class I antigen presentation. The protein is a high molecular mass serine exopeptidase; the amino acid sequence surrounding the serine residue at the active site is similar to the peptidases of the subtilisin class rather than the trypsin class. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12016) · Entrez [7174](https://www.ncbi.nlm.nih.gov/gene/7174) · UniProt [P29144](https://www.uniprot.org/uniprotkb/P29144) · Ensembl [ENSG00000134900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134900)

## Data

Gene col 5623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5623); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5623]; `tensor/DDL_lfc|DDL_z.npy` [5623]; `embed/gene_vectors.npy` [5623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5623 or target_col == 5623). Every well: [[TPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
