---
symbol: "TMEM33"
type: "gene"
col: 3033
ensembl_id: "ENSG00000109133"
name: "transmembrane protein 33"
location: "4p13"
module: 4
arm: "+"
pooled_cpm: 54.35
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TMEM33

*transmembrane protein 33* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +15.4, q 0e+00, up in 39 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +11.4, q 5e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.779× (z -5.4, q 5e-05, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.554×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR77]] (+0.81, fdr 7e-06), [[ATIC]] (+0.76, fdr 7e-06), [[GFM1]] (+0.75, fdr 7e-06); moves opposite to [[AAMDC]] (-0.74, fdr 7e-06), [[RSRP1]] (-0.72, fdr 7e-06), [[TTC21A]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 28 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.07×** | +15.4 | 0e+00 | 39/44 (A-427, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.95×** | +14.8 | 0e+00 | 38/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.94×** | +13.5 | 2e-39 | 36/45 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.84×** | +13.4 | 1e-38 | 43/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.75×** | +12.4 | 4e-33 | 41/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.78×** | +12.1 | 1e-31 | 44/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +11.4 | 5e-28 | 43/48 (SW480, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.67×** | +11.4 | 5e-28 | 43/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.70×** | +11.2 | 3e-27 | 37/47 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +10.6 | 2e-24 | 41/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +10.2 | 1e-22 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +9.9 | 2e-21 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.54×** | +9.6 | 5e-20 | 35/47 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +9.3 | 8e-19 | 37/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.33×** | +8.9 | 1e-17 | 29/48 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +8.4 | 2e-15 | 35/49 (J82, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 4e-15 | 35/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +8.0 | 6e-14 | 38/48 (HOP62, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +7.2 | 1e-11 | 36/48 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +6.6 | 1e-09 | 32/48 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +6.0 | 5e-08 | 23/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.7 | 3e-07 | 32/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.4 | 1e-06 | 21/48 (SW1417, A549, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.47×** | +4.4 | 2e-04 | 23/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 3e-04 | 21/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +4.1 | 7e-04 | 20/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3033.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.554×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.779×** | -5.4 | 5e-05 | 25/47 (NCI-H23, SNU-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.910× | -3.0 | 0.45 | 5/48 (CFPAC-1, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 33.9 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.62× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 39.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 57.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H460 (line)]] | wt | 53.4 | 5 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.53× (z +10.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +9.7) | — |
| [[SW480 (line)]] | alt | 64.3 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[A549 (line)]] | wt | 36.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 36.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +8.9) | — |
| [[A-172 (line)]] | wt | 41.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[A498 (line)]] | wt | 61.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.17× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 42.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 75.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2347 (line)]] | alt | 63.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 59.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 70.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 42.1 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +9.0) | — |
| [[A-427 (line)]] | wt | 90.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HOP62 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +8.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HT-29 (line)]] | alt | 79.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.41× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 73.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR77]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[ATIC]] | +0.76 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[GFM1]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[LETM1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[TMX3]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[VMA21]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CCT5]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[GOT2]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[AGPS]] | +0.72 | +0.62 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | -0.74 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.72 | -0.64 / -0.77 | both halves | 7e-06 |  |
| [[TTC21A]] | -0.71 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.71 | -0.69 / -0.72 | both halves | 7e-06 |  |
| [[TESK2]] | -0.69 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.69 | -0.55 / -0.73 | both halves | 1e-05 |  |
| [[ARID4A]] | -0.69 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[ING2]] | -0.69 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[FAM53C]] | -0.68 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.67 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[WBP1]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.857). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.9, -33.1); signed map (-10.9, -44.8). **Vector** length 90.4, 25.4% of its response variance represented; |z| ≥ 3 in 1,383 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.52 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.52 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.6 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +5.2 | +14.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.0 | +15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.4 | +8.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -2.6 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:41,935,129-41,960,803 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10525, Pom33 |
| Matched by | ensembl_id |

**Function**, from UniProt [P57088](https://www.uniprot.org/uniprotkb/P57088) (Transmembrane protein 33):

> Acts as a regulator of the tubular endoplasmic reticulum (ER) network by modulating intracellular calcium homeostasis. Mechanistically, stimulates PKD2 calcium-dependent activity (By similarity). Suppresses the RTN3/4-induced formation of the ER tubules. Positively regulates PERK-mediated and IRE1-mediated unfolded protein response signaling. Plays an essential role in VEGF-mediated release of Ca(2+) from ER stores during angiogenesis. Also plays a role in the modulation of innate immune …

**Summary**, from NCBI Gene [55161](https://www.ncbi.nlm.nih.gov/gene/55161):

> Involved in positive regulation of endoplasmic reticulum unfolded protein response; regulation of endoplasmic reticulum tubular network organization; and response to endoplasmic reticulum stress. Located in endoplasmic reticulum membrane; melanosome; and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25541) · Entrez [55161](https://www.ncbi.nlm.nih.gov/gene/55161) · UniProt [P57088](https://www.uniprot.org/uniprotkb/P57088) · Ensembl [ENSG00000109133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109133)

## Data

Gene col 3033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3033); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3033]; `tensor/DDL_lfc|DDL_z.npy` [3033]; `embed/gene_vectors.npy` [3033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3033 or target_col == 3033). Every well: [[TMEM33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
