---
symbol: "LARP4B"
type: "gene"
col: 2898
ensembl_id: "ENSG00000107929"
name: "La ribonucleoprotein 4B"
location: "10p15.3"
module: 45
arm: "-"
pooled_cpm: 189.86
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# LARP4B

*La ribonucleoprotein 4B* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 3.27× (z +9.2, q 9e-18, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.495× (z -10.2, q 1e-21, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.799× (z -4.8, q 3e-04, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SNU-1 0.117×, KATO III 0.283×, SW480 0.309×, NCI-H460 0.363×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.280×, A549 0.299×, SHP-77 0.332×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.192×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF407]] (+0.62, fdr 4e-05), [[KANSL1L-AS1]] (+0.61, fdr 1e-05), [[HCFC1]] (+0.59, fdr 3e-05); moves opposite to [[HPF1]] (-0.61, fdr 1e-05), [[COMMD3]] (-0.60, fdr 1e-05), [[KBTBD3]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.27×** | +9.2 | 9e-18 | 47/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.25×** | +9.2 | 9e-18 | 46/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +7.1 | 3e-10 | 42/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.8 | 1e-06 | 37/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.1 | 5e-05 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 8e-05 | 42/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 1e-03 | 34/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.004 | 29/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.015 | 28/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.033 | 31/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.068 | 22/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.095 | 26/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.12 | 29/48 (RKO, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2898.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SNU-1 0.117×, KATO III 0.283×, SW480 0.309×, NCI-H460 0.363×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.280×, A549 0.299×, SHP-77 0.332×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.192×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -10.2 | 1e-21 | 39/44 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.605×** | -7.6 | 1e-11 | 46/49 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -4.8 | 3e-04 | 34/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -4.3 | 0.002 | 34/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.703×** | -4.2 | 0.003 | 33/45 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.058 | 33/48 (HepG2/C3A, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.867× | -3.1 | 0.17 | 15/48 (CFPAC-1, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 143 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 105 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 262 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.19× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -12.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 227 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 235 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -10.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 135 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.8) | — |
| [[LoVo (line)]] | wt | 214 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 145 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.7) | — |
| [[A-172 (line)]] | wt | 180 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.22× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.445× (z -9.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -15.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -14.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 223 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 268 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 212 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 252 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 187 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.77× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 245 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 297 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.96× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 94.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 114 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.54× (z +8.7) | — |
| [[KATO III (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 261 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 118 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.03× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -19.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | +0.62 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[KANSL1L-AS1]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.59 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[PRR5L]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[MFN2]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PSME3]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[HCG18]] | +0.58 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ATP2A2]] | +0.57 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PPIA]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ZNF876P]] | +0.56 | +0.32 / +0.59 | both halves | 1e-04 |  |
| [[ABCF2]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.61 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.60 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TCAF1]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PIP4P2]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[FAM229B]] | -0.57 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PRKAB2]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[WDSUB1]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CYRIA]] | -0.55 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.55 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[LINC00888-1]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.3, 19.1); signed map (-9.9, -38.3). **Vector** length 110, 40.3% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.1 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.3 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +9.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:806,933-931,821 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0217, LARP5 |
| Gene groups (HGNC) | La ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92615](https://www.uniprot.org/uniprotkb/Q92615) (La-related protein 4B):

> Stimulates mRNA translation.

**Summary**, from NCBI Gene [23185](https://www.ncbi.nlm.nih.gov/gene/23185):

> This gene encodes a member of an evolutionarily conserved protein family implicated in RNA metabolism and translation. Members of this family are characterized by the presence of an La motif, which is often located adjacent to one or more RNA recognition motifs (RRM). Together, the two motifs constitute the functional region of the protein and enable its interaction with the RNA substrate. This protein family is divided into five sub-families: the genuine La proteins and four La-related protein …

**Accessions** — [HGNC:28987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28987) · Entrez [23185](https://www.ncbi.nlm.nih.gov/gene/23185) · UniProt [Q92615](https://www.uniprot.org/uniprotkb/Q92615) · Ensembl [ENSG00000107929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107929)

## Data

Gene col 2898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2898); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2898]; `tensor/DDL_lfc|DDL_z.npy` [2898]; `embed/gene_vectors.npy` [2898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2898 or target_col == 2898). Every well: [[LARP4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
