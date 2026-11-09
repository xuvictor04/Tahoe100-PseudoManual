---
symbol: "ARL8B"
type: "gene"
col: 5511
ensembl_id: "ENSG00000134108"
name: "ARF like GTPase 8B"
location: "3p26.1"
module: 30
arm: "+"
pooled_cpm: 121.55
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 5
n_dd_up_clean: 29
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ARL8B

*ARF like GTPase 8B* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.38× (z +17.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.700× (z -5.0, q 4e-04, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Diphenhydramine (drug)]] 0.5 µM: 0.789× (z -3.4, q 0.085, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1B2]] (+0.61, fdr 1e-05), [[CYB5R4]] (+0.61, fdr 1e-05), [[VPS41]] (+0.59, fdr 3e-05); moves opposite to [[PPRC1]] (-0.50, fdr 3e-05), [[NOP2]] (-0.48, fdr 3e-05), [[PRR7-AS1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.38×** | +17.5 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +14.7 | 0e+00 | 46/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +14.2 | 1e-43 | 47/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.36×** | +12.3 | 1e-32 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.34×** | +12.2 | 6e-32 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.31×** | +11.0 | 6e-26 | 47/49 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +7.5 | 6e-12 | 39/48 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.51×** | +6.9 | 4e-10 | 41/48 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +6.6 | 2e-09 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 6e-09 | 40/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.4 | 6e-09 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.0 | 1e-07 | 36/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.5 | 2e-06 | 42/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 2e-05 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 3e-05 | 32/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 3e-04 | 31/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 5e-04 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5511.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -5.0 | 4e-04 | 27/44 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.5 | 0.085 | 23/49 (RKO, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.789×** | -3.4 | 0.085 | 23/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.085 | 27/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.094 | 25/47 (LS 180, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.094 | 27/48 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.802× | -3.2 | 0.11 | 19/48 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.805× | -3.2 | 0.11 | 28/48 (HOP62, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 93.9 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +18.6) | — |
| [[SW480 (line)]] | alt | 86.1 | 11 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 97.4 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.64× (z +23.9) | — |
| [[NCI-H23 (line)]] | alt | 87.8 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +16.9) | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.43× (z +16.9) | — |
| [[LoVo (line)]] | wt | 93.8 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +14.8) | — |
| [[H4 (line)]] | wt | 83.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.03× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 77.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +14.0) | — |
| [[J82 (line)]] | alt | 169 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +14.7) | — |
| [[KATO III (line)]] | alt | 83.4 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.99× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 104 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 191 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 93.7 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.63× (z +16.0) | — |
| [[HOP62 (line)]] | alt | 113 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 116 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.1) | — |
| [[RKO (line)]] | wt | 140 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -14.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 196 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 138 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 123 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 125 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.90× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 141 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.28× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 172 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.01× (z +19.2) | — |
| [[SW1417 (line)]] | alt | 199 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +12.6) | — |
| [[A-427 (line)]] | wt | 112 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 142 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 125 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.55× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 130 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 88.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +8.6) | — |
| [[A-172 (line)]] | wt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.6) | — |
| [[CFPAC-1 (line)]] | alt | 85.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 139 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 96.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 262 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.535× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 100 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +10.1) | — |
| [[A498 (line)]] | wt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1B2]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CYB5R4]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[VPS41]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 | STRING 699 |
| [[WDFY1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[STX7]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 | STRING 529 |
| [[VPS26A]] | +0.54 | +0.51 / +0.63 | both halves | 1e-05 | STRING 400 |
| [[ABRAXAS1]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TMEM38B]] | +0.54 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[VAT1]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[FIG4]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SPAG9]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SNN]] | +0.52 | +0.44 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPRC1]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NOP2]] | -0.48 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PRR7-AS1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF850]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TOE1]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ZC3H18]] | -0.46 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[RIC8B]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[HSPA14]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[LRR1]] | -0.45 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[DNAAF10]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ZNF689]] | -0.45 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CENPL]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.7, -10.4); signed map (-33.7, -14.7). **Vector** length 73.9, 25.3% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | +14.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | +0.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 8B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:5,122,249-5,180,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10702, Gie1; previously ARL10C |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVJ2](https://www.uniprot.org/uniprotkb/Q9NVJ2) (ADP-ribosylation factor-like protein 8B):

> Small GTPase which cycles between active GTP-bound and inactive GDP-bound states. In its active state, binds to a variety of effector proteins playing a key role in the regulation of lysosomal positioning which is important for nutrient sensing, natural killer cell-mediated cytotoxicity and antigen presentation. Along with its effectors, orchestrates lysosomal transport and fusion. Localizes specifically to lysosomal membranes and mediates anterograde lysosomal motility by recruiting PLEKHM2, …

**Summary**, from NCBI Gene [55207](https://www.ncbi.nlm.nih.gov/gene/55207):

> Enables G protein activity; guanyl ribonucleotide binding activity; and tubulin binding activity. Involved in several processes, including antigen processing and presentation following phagocytosis; cytosolic transport; and vesicle fusion. Located in cytolytic granule membrane; midbody; and spindle midzone. Is active in early endosome membrane and lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25564) · Entrez [55207](https://www.ncbi.nlm.nih.gov/gene/55207) · UniProt [Q9NVJ2](https://www.uniprot.org/uniprotkb/Q9NVJ2) · Ensembl [ENSG00000134108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134108)

## Data

Gene col 5511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5511); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5511]; `tensor/DDL_lfc|DDL_z.npy` [5511]; `embed/gene_vectors.npy` [5511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5511 or target_col == 5511). Every well: [[ARL8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
