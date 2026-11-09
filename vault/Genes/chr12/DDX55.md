---
symbol: "DDX55"
type: "gene"
col: 3228
ensembl_id: "ENSG00000111364"
name: "DEAD-box helicase 55"
location: "12q24.31"
module: 33
arm: "+"
pooled_cpm: 36.7
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DDX55

*DEAD-box helicase 55* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.22× (z +15.0, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.877× (z -8.9, q 4e-16, down in 9 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.782× (z -6.9, q 2e-09, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (Hs 766T 0.302×, MIA PaCa-2 0.411×, SNU-1 0.346×, LoVo 0.550×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.280×, SW48 0.256×, NCI-H460 0.405×, PANC-1 0.500×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.118×, A-427 0.205×, AsPC-1 0.284×; ⚠ toxic; transcription drop); [[AZD1390 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0904×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PELP1]] (+0.75, fdr 7e-06), [[ORC5]] (+0.75, fdr 7e-06), [[TAMM41]] (+0.73, fdr 7e-06); moves opposite to [[YPEL5]] (-0.65, fdr 1e-05), [[CTNNA1]] (-0.60, fdr 1e-05), [[UBE2A]] (-0.59, fdr 9e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.22×** | +15.0 | 0e+00 | 46/49 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +13.9 | 2e-41 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +13.4 | 1e-38 | 39/48 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +12.0 | 3e-31 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.73×** | +10.9 | 8e-26 | 42/48 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +10.8 | 2e-25 | 36/47 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +9.7 | 3e-20 | 42/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.8 | 5e-13 | 33/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +6.4 | 1e-08 | 29/47 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.24×** | +6.2 | 3e-08 | 22/47 (J82, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.31×** | +5.4 | 3e-06 | 23/48 (J82, SW480, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +5.1 | 1e-05 | 19/47 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +5.1 | 1e-05 | 25/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.29×** | +5.1 | 2e-05 | 24/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.57×** | +4.7 | 1e-04 | 17/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 20/48 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 4e-04 | 19/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.3 | 4e-04 | 19/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 4e-04 | 16/48 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.3 | 4e-04 | 22/48 (NCI-H460, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 6e-04 | 17/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.003 | 14/47 (A498, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (Hs 766T 0.302×, MIA PaCa-2 0.411×, SNU-1 0.346×, LoVo 0.550×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 0.280×, SW48 0.256×, NCI-H460 0.405×, PANC-1 0.500×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.118×, A-427 0.205×, AsPC-1 0.284×; ⚠ toxic; transcription drop); [[AZD1390 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0904×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -8.9 | 4e-16 | 9/48 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -6.9 | 2e-09 | 24/48 (Hs 766T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.740×** | -5.8 | 2e-06 | 22/40 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.770×** | -5.2 | 3e-05 | 25/46 (SHP-77, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.819×** | -4.0 | 0.008 | 18/47 (LoVo, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.0 | 0.22 | 15/47 (SK-MEL-2, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 43.8 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.93× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.3) |
| [[SW480 (line)]] | alt | 44.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.13× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 49.0 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 64.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0835× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +9.8) | — |
| [[KATO III (line)]] | alt | 29.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.07× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 38.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.15× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 70.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -20.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.9 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.75× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 30.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 18.1× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 26.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.2) |
| [[HT-29 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 45.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.8 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.16× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.0) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 23.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 1 | — | [[AZD1390 (drug)]] 0.05 µM 0.0904× (z -8.6) |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) |
| [[SW1417 (line)]] | alt | 52.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +8.9) | — |
| [[A-172 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELP1]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ORC5]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.73 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NLE1]] | +0.72 | +0.57 / +0.74 | both halves | 1e-05 | STRING 571 |
| [[NUDCD3]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 | STRING 489 |
| [[DHX57]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | STRING 409 |
| [[ZNF692]] | +0.72 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[GTF3C2]] | +0.72 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[CTU1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[DHODH]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.65 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[CTNNA1]] | -0.60 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[UBE2A]] | -0.59 | -0.37 / -0.62 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-32.2, -7.7); signed map (-16.2, -21.7). **Vector** length 100, 25.1% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +13.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +12.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.9 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +2.5 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 55 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,602,077-123,620,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1595 |
| Gene groups (HGNC) | DEAD-box helicases; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHQ9](https://www.uniprot.org/uniprotkb/Q8NHQ9) (ATP-dependent RNA helicase DDX55):

> Probable ATP-binding RNA helicase. Has ATPase activity and is involved in the maturation of precursor large subunit rRNAs.

**Summary**, from NCBI Gene [57696](https://www.ncbi.nlm.nih.gov/gene/57696):

> This gene encodes a member of protein family containing a characteristic Asp-Glu-Ala-Asp (DEAD) motif. These proteins are putative RNA helicases, and may be involved in a range of nuclear processes including translational initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Multiple alternatively spliced transcript variants have been found for this gene. Pseudogenes have been identified on chromosomes 1 and 12. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:20085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20085) · Entrez [57696](https://www.ncbi.nlm.nih.gov/gene/57696) · UniProt [Q8NHQ9](https://www.uniprot.org/uniprotkb/Q8NHQ9) · Ensembl [ENSG00000111364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111364)

## Data

Gene col 3228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3228); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3228]; `tensor/DDL_lfc|DDL_z.npy` [3228]; `embed/gene_vectors.npy` [3228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3228 or target_col == 3228). Every well: [[DDX55 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX55.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
