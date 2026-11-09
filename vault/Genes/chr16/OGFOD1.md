---
symbol: "OGFOD1"
type: "gene"
col: 1494
ensembl_id: "ENSG00000087263"
name: "2-oxoglutarate and iron dependent oxygenase domain containing 1"
location: "16q13"
module: 5
arm: "+"
pooled_cpm: 34.13
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# OGFOD1

*2-oxoglutarate and iron dependent oxygenase domain containing 1* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.41× (z +27.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.904× (z -5.3, q 8e-05, down in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.855× (z -3.5, q 0.060, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.162×, SW1417 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.680×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.255×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM27]] (+0.61, fdr 1e-05), [[TXNDC9]] (+0.60, fdr 1e-05), [[ZNF142]] (+0.58, fdr 3e-05); moves opposite to [[PER3]] (-0.54, fdr 3e-05), [[TUFT1]] (-0.50, fdr 3e-05), [[PPFIBP2]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +27.6 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.42×** | +13.5 | 3e-39 | 42/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.28×** | +12.6 | 3e-34 | 39/48 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.16×** | +12.3 | 2e-32 | 44/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.35×** | +12.2 | 3e-32 | 40/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.53×** | +10.5 | 1e-23 | 39/48 (LS 180, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.56×** | +10.0 | 2e-21 | 34/48 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.86×** | +9.9 | 5e-21 | 42/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +9.7 | 1e-20 | 44/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.80×** | +9.3 | 5e-19 | 42/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.83×** | +9.2 | 1e-18 | 37/48 (NCI-H1792, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +9.1 | 3e-18 | 37/47 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +8.9 | 3e-17 | 42/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +8.4 | 2e-15 | 41/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.69×** | +8.1 | 3e-14 | 39/46 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +7.9 | 8e-14 | 41/48 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +7.5 | 2e-12 | 38/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.3 | 8e-12 | 34/48 (NCI-H460, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.2 | 1e-11 | 30/48 (BT-474, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 2e-05 | 24/48 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.2 | 6e-04 | 19/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 1e-03 | 18/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.017 | 17/48 (NCI-H2030, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1494.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.162×, SW1417 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.680×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.207×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.255×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -5.3 | 8e-05 | 7/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.740×** | -4.8 | 6e-04 | 25/48 (SW48, CHP-212, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.778×** | -3.6 | 0.060 | 15/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.855× | -3.5 | 0.060 | 19/48 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.060 | 16/48 (CHP-212, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.0 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 34.1 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +16.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +17.8) | — |
| [[LoVo (line)]] | wt | 27.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 23.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +21.5) | — |
| [[NCI-H2030 (line)]] | alt | 53.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 41.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +19.1) | — |
| [[BT-474 (line)]] | alt | 31.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.8) | — |
| [[C32 (line)]] | wt | 22.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 34.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 17.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +12.3) | — |
| [[RKO (line)]] | wt | 53.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.41× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 20.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +14.4) | — |
| [[SW1417 (line)]] | alt | 39.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.8) | — |
| [[A549 (line)]] | wt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +15.4) | — |
| [[C-33 A (line)]] | alt | 26.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +11.6) | — |
| [[H4 (line)]] | wt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.255× (z -8.7) |
| [[Hs 766T (line)]] | wt | 35.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 31.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.8) | — |
| [[J82 (line)]] | alt | 51.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +14.4) | — |
| [[KATO III (line)]] | alt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +15.2) | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.9) | — |
| [[SNU-1 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.9) | — |
| [[A-427 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM27]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TXNDC9]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF142]] | +0.58 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ICE1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TIMM21]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 | STRING 630 |
| [[AGAP6]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PARG]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MRPS11]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[C1orf109]] | +0.52 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[TOP3A]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TMEM11]] | +0.51 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[MRPL18]] | +0.51 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER3]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TUFT1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PPFIBP2]] | -0.48 | -0.39 / -0.36 | both halves | 1e-04 | STRING 415 |
| [[LUC7L3]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[CA8]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[GEM]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[LINC01273]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SHF]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[GDF11]] | -0.46 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[NDRG4]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TBL1XR1]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MAFK]] | -0.46 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OGFOD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-48.0, 2.6); signed map (-8.7, -26.9). **Vector** length 80.3, 20.7% of its response variance represented; |z| ≥ 3 in 1,333 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +27.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.5 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.2 | +12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +7.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.8 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -3.1 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | 2-oxoglutarate and iron dependent oxygenase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,451,521-56,479,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1612, FLJ10826, TPA1 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Reactome | 2 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N543](https://www.uniprot.org/uniprotkb/Q8N543) (Prolyl 3-hydroxylase OGFOD1):

> Prolyl 3-hydroxylase that catalyzes 3-hydroxylation of 'Pro-62' of small ribosomal subunit uS12 (RPS23), thereby regulating protein translation termination efficiency. Involved in stress granule formation.

**Summary**, from NCBI Gene [55239](https://www.ncbi.nlm.nih.gov/gene/55239):

> Enables peptidyl-proline 3-dioxygenase activity. Involved in several processes, including peptidyl-proline hydroxylation; regulation of translational termination; and stress granule assembly. Located in cytoplasmic stress granule; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25585) · Entrez [55239](https://www.ncbi.nlm.nih.gov/gene/55239) · UniProt [Q8N543](https://www.uniprot.org/uniprotkb/Q8N543) · Ensembl [ENSG00000087263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087263)

## Data

Gene col 1494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1494); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1494]; `tensor/DDL_lfc|DDL_z.npy` [1494]; `embed/gene_vectors.npy` [1494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1494 or target_col == 1494). Every well: [[OGFOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGFOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
