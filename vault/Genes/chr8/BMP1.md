---
symbol: "BMP1"
type: "gene"
col: 9657
ensembl_id: "ENSG00000168487"
name: "bone morphogenetic protein 1"
location: "8p21.3"
module: 62
arm: "+"
pooled_cpm: 28.25
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# BMP1

*bone morphogenetic protein 1* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.39× (z +6.6, q 2e-08, up in 15 of 33 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 3.39×, KATO III 4.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.87×; ⚠ cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.68×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.396× (z -19.5, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL7A1]] (+0.59, fdr 1e-05), [[GPC1]] (+0.57, fdr 1e-05), [[ST6GALNAC2]] (+0.49, fdr 6e-05); moves opposite to [[UBE3D]] (-0.43, fdr 3e-04), [[NOB1]] (-0.41, fdr 3e-04), [[SYCP2L]] (-0.39, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[COL1A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ACAP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9657.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 3.39×, KATO III 4.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.87×; ⚠ cell-cycle shift, explains ~9% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 2.36×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.68×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.6 | 2e-08 | 15/33 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.4 | 0.003 | 8/35 (HS-578T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +3.9 | 0.020 | 11/34 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.020 | 15/43 (hTERT-HPNE, H4, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +3.7 | 0.020 | 19/42 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.046 | 10/43 (SHP-77, H4, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.046 | 8/44 (RKO, A-172, …) | top dose only |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.097 | 6/44 (C32, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.396×** | -19.5 | 0e+00 | 37/45 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.422×** | -18.1 | 0e+00 | 38/45 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.503×** | -14.4 | 7e-45 | 35/45 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -9.9 | 7e-21 | 25/42 (Panc 03.27, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -6.7 | 2e-09 | 22/45 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.748×** | -6.1 | 1e-07 | 21/45 (A-172, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -6.1 | 1e-07 | 17/45 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.818×** | -6.0 | 2e-07 | 20/44 (BT-474, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -5.3 | 8e-06 | 18/45 (HOP62, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.792×** | -4.6 | 2e-04 | 15/43 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.808×** | -4.5 | 4e-04 | 14/45 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.810×** | -4.4 | 5e-04 | 15/45 (RPMI-7951, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.805×** | -4.4 | 5e-04 | 18/43 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.815×** | -4.3 | 8e-04 | 18/43 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -4.2 | 0.001 | 17/45 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -4.0 | 0.002 | 15/45 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.828×** | -3.8 | 0.005 | 12/42 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.012 | 8/43 (HS-578T, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.735×** | -3.4 | 0.019 | 12/43 (Hs 766T, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.758×** | -3.0 | 0.057 | 7/43 (SW 1088, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.057 | 2/45 (A-172, HEC-1-A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.8 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.9) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 5 µM 0.340× (z -13.4) |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 5 | — | [[Bortezomib (drug)]] 0.05 µM 0.292× (z -10.3) |
| [[A-172 (line)]] | wt | 124 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 77.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 66.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -13.7) |
| [[HS-578T (line)]] | alt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -16.8) |
| [[LoVo (line)]] | wt | 23.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.302× (z -10.6) |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 2 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0682× (z -9.1) |
| [[A549 (line)]] | wt | 28.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -8.6) |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[KATO III (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.180× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -13.7) |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0610× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.8) |
| [[SW48 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 12.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -8.7) |
| [[A-427 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL7A1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 589 |
| [[GPC1]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ST6GALNAC2]] | +0.49 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[EML1]] | +0.48 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FBN1]] | +0.48 | +0.40 / +0.46 | both halves | 4e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[RBMS1]] | +0.47 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[ADGRA2]] | +0.47 | +0.37 / +0.36 | both halves | 9e-05 |  |
| [[BCL9L]] | +0.46 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[SUSD6]] | +0.46 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GAS6]] | +0.46 | +0.31 / +0.41 | both halves | 2e-04 |  |
| [[PLXNB2]] | +0.46 | +0.37 / +0.42 | both halves | 9e-05 |  |
| [[IPO9-AS1]] | +0.45 | +0.33 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE3D]] | -0.43 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[NOB1]] | -0.41 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[SYCP2L]] | -0.39 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[ANK3]] | -0.38 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NMNAT3]] | -0.38 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[INTS9]] | -0.37 | -0.26 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL1A1]] | B | COL1A1 activity strengthens BMP1's drug response | lines that do not express COL1A1 (32) vs lines expressing it (13) | the lines without COL1A1 respond 0.62× as strongly (z diff +1.72); strongest at Idarubicin (hydrochloride) 5 µM: 0.90x vs 0.48x (z diff +6.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; target measured in part of the lines; artifact flags |
| [[ZNF469]] | B | ZNF469 activity raises BMP1's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 1.88× lower at baseline in the lines without ZNF469 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[COL1A1]] | B | COL1A1 activity raises BMP1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without COL1A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[PDGFRB]] | B | PDGFRB activity raises BMP1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.28× lower at baseline in the lines without PDGFRB | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[COL5A1]] | B | COL5A1 activity strengthens BMP1's drug response | lines that do not express COL5A1 (28) vs lines expressing it (17) | the lines without COL5A1 respond 0.61× as strongly (z diff +1.65); strongest at Idarubicin (hydrochloride) 5 µM: 0.97x vs 0.51x (z diff +5.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; target measured in part of the lines; artifact flags |
| [[PHLDA3]] | B | PHLDA3 activity raises BMP1's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.95× lower at baseline in the lines without PHLDA3 | 0.088 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |
| [[COL6A1]] | B | COL6A1 activity raises BMP1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without COL6A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[COL5A1]] | B | COL5A1 activity raises BMP1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without COL5A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[LIMS2]] | B | LIMS2 activity raises BMP1's level | lines that do not express LIMS2 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without LIMS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PALM, FHL1, ZNF469 |
| [[PLXNA2]] | B | PLXNA2 activity raises BMP1's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without PLXNA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACAP3]] | C | BMP1 activity raises ACAP3's level | lines that do not express BMP1 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without BMP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPEPPSP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.360). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, -6.8); signed map (43.9, -11.7). **Vector** length 82.7, 15.9% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.1 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +6.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -1.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.5 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,165,140-22,212,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BMP-1; previously PCOLC |
| Gene groups (HGNC) | Bone morphogenetic proteins; Astacins |
| Hallmark sets | COAGULATION, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: HDL assembly; Plasma lipoprotein assembly; Anchoring fibril formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13497](https://www.uniprot.org/uniprotkb/P13497) (Bone morphogenetic protein 1):

> Metalloprotease that plays key roles in regulating the formation of the extracellular matrix (ECM) via processing of various precursor proteins into mature functional enzymes or structural proteins. Thereby participates in several developmental and physiological processes such as cartilage and bone formation, muscle growth and homeostasis, wound healing and tissue repair. Roles in ECM formation include cleavage of the C-terminal propeptides from procollagens such as procollagen I, II and III or …

**Summary**, from NCBI Gene [649](https://www.ncbi.nlm.nih.gov/gene/649):

> This gene encodes a protein that is capable of inducing formation of cartilage in vivo. Although other bone morphogenetic proteins are members of the TGF-beta superfamily, this gene encodes a protein that is not closely related to other known growth factors. This gene is expressed as alternatively spliced variants that share an N-terminal protease domain but differ in their C-terminal region. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:1067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1067) · Entrez [649](https://www.ncbi.nlm.nih.gov/gene/649) · UniProt [P13497](https://www.uniprot.org/uniprotkb/P13497) · Ensembl [ENSG00000168487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168487)

## Data

Gene col 9657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9657); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9657]; `tensor/DDL_lfc|DDL_z.npy` [9657]; `embed/gene_vectors.npy` [9657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9657 or target_col == 9657). Every well: [[BMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
