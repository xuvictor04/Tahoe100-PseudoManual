---
symbol: "ATRAID"
type: "gene"
col: 6123
ensembl_id: "ENSG00000138085"
name: "all-trans retinoic acid induced differentiation factor"
location: "2p23.3"
module: 29
arm: "+"
pooled_cpm: 17.8
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ATRAID

*all-trans retinoic acid induced differentiation factor* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +14.7, q 0e+00, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.26× (z +3.7, q 0.028, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.94×, A549 5.69×, NCI-H460 4.28×, NCI-H2030 3.74×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 4.97×, A549 5.11×, MIA PaCa-2 5.79×, A498 3.38×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 6.97×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.537× (z -9.8, q 9e-20, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN6]] (+0.71, fdr 7e-06), [[SCARB2]] (+0.68, fdr 1e-05), [[SH3BGRL]] (+0.67, fdr 7e-06); moves opposite to [[ZDHHC18]] (-0.62, fdr 1e-05), [[ZNF83]] (-0.61, fdr 7e-06), [[GPSM1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUSP19]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.94×, A549 5.69×, NCI-H460 4.28×, NCI-H2030 3.74×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (KATO III 4.97×, A549 5.11×, MIA PaCa-2 5.79×, A498 3.38×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 6.97×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +14.7 | 0e+00 | 36/37 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +13.0 | 4e-36 | 27/31 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +9.7 | 8e-20 | 31/34 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.73×** | +6.1 | 2e-07 | 32/44 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.028 | 20/48 (SK-MEL-2, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.071 | 20/48 (NCI-H1573, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.537×** | -9.8 | 9e-20 | 40/47 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -9.6 | 2e-19 | 39/46 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.462×** | -7.9 | 6e-13 | 37/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.509×** | -7.5 | 8e-12 | 32/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -7.0 | 3e-10 | 27/46 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -6.2 | 4e-08 | 34/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.588×** | -5.9 | 3e-07 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -5.8 | 5e-07 | 37/48 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -5.6 | 2e-06 | 29/47 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -5.5 | 3e-06 | 31/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -4.9 | 5e-05 | 29/48 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -4.9 | 5e-05 | 32/48 (LoVo, LS 180, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.696×** | -3.9 | 0.005 | 21/47 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -3.8 | 0.007 | 24/48 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.720×** | -3.7 | 0.010 | 18/48 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.550×** | -3.5 | 0.018 | 18/46 (HCT15, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.553×** | -3.4 | 0.019 | 17/46 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -14.4) |
| [[KATO III (line)]] | alt | 28.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +10.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 20.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.9) |
| [[PANC-1 (line)]] | alt | 21.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +13.0) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.309× (z -8.7) |
| [[A498 (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.97× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 18.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.8) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -9.1) |
| [[LoVo (line)]] | wt | 11.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.5) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.169× (z -10.8) |
| [[A-172 (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0693× (z -11.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.6) |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.4) |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -8.6) |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.2) |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN6]] | +0.71 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[COX11]] | +0.67 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ITM2B]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CNOT1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[G6PC3]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.62 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[GPAA1]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MFSD14A]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC18]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZNF83]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[GPSM1]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MPP3]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TM4SF19-DYNLT2B]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ARAP3]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RRP7BP-1]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[LRRC8E]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[GOLGA6L9]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[FPGS]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LINC02804]] | -0.51 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[EIF5B]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP19]] | C | DUSP19 activity raises ATRAID's level | lines that do not express DUSP19 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without DUSP19 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.9, -19.7); signed map (-21.7, -40.1). **Vector** length 72.8, 15.4% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | all-trans retinoic acid induced differentiation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,212,041-27,217,178 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC013, p18, APR3; previously C2orf28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW56](https://www.uniprot.org/uniprotkb/Q6UW56) (All-trans retinoic acid-induced differentiation factor):

> Promotes osteoblast cell differentiation and terminal mineralization. Plays a role in inducing the cell cycle arrest via inhibiting CCND1 expression in all-trans-retinoic acid (ATRA) signal pathway. In osteoclasts, forms a transporter complex with ATRAID for nitrogen-containing-bisphosphonates (N-BPs) required for releasing N-BP molecules that have trafficked to lysosomes through fluid-phase endocytosis into the cytosol.

**Summary**, from NCBI Gene [51374](https://www.ncbi.nlm.nih.gov/gene/51374):

> This gene is thought to be involved in apoptosis, and may also be involved in hematopoietic development and differentiation. The use of alternative splice sites and promotors result in multiple transcript variants encoding different isoforms.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:24090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24090) · Entrez [51374](https://www.ncbi.nlm.nih.gov/gene/51374) · UniProt [Q6UW56](https://www.uniprot.org/uniprotkb/Q6UW56) · Ensembl [ENSG00000138085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138085)

## Data

Gene col 6123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6123); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6123]; `tensor/DDL_lfc|DDL_z.npy` [6123]; `embed/gene_vectors.npy` [6123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6123 or target_col == 6123). Every well: [[ATRAID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATRAID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
