---
symbol: "NIPA2"
type: "gene"
col: 6376
ensembl_id: "ENSG00000140157"
name: "NIPA magnesium transporter 2"
location: "15q11.2"
module: 36
arm: "+"
pooled_cpm: 45.72
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NIPA2

*NIPA magnesium transporter 2* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.04× (z +14.5, q 7e-45, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.00× (z +14.1, q 2e-42, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.825× (z -5.6, q 2e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (H4 0.141×; ⚠ cell-cycle shift, explains ~63% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.456×; ⚠ cell-cycle shift, explains ~44% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0754×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLTP2]] (+0.71, fdr 7e-06), [[TRAPPC10]] (+0.71, fdr 7e-06), [[TMEM248]] (+0.69, fdr 7e-06); moves opposite to [[CLK4]] (-0.69, fdr 1e-05), [[ABCA5]] (-0.67, fdr 7e-06), [[NBPF19]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.04×** | +14.5 | 7e-45 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +14.1 | 2e-42 | 46/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.99×** | +13.9 | 7e-42 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.92×** | +13.2 | 9e-38 | 46/48 (SW480, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +11.2 | 3e-27 | 38/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.85×** | +11.1 | 1e-26 | 41/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +10.7 | 6e-25 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +9.2 | 2e-18 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.59×** | +9.0 | 1e-17 | 36/46 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +8.8 | 1e-16 | 37/47 (COLO 205, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +8.3 | 5e-15 | 37/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 2e-14 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.48×** | +7.9 | 2e-13 | 29/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.44×** | +7.1 | 4e-11 | 24/39 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.40×** | +6.8 | 4e-10 | 27/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.7 | 5e-07 | 34/48 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 5e-06 | 26/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.002 | 16/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.011 | 14/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.028 | 12/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.029 | 13/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.040 | 10/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.054 | 15/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.068 | 16/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +2.8 | 0.081 | 4/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6376.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.5 µM in 1 line (H4 0.141×; ⚠ cell-cycle shift, explains ~63% of this change); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.456×; ⚠ cell-cycle shift, explains ~44% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0754×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -5.6 | 2e-05 | 25/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.821×** | -4.0 | 0.016 | 17/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.832×** | -3.8 | 0.031 | 13/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.727×** | -3.4 | 0.094 | 14/45 (SNU-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.733×** | -3.3 | 0.100 | 10/48 (LoVo, SW 1088, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.100 | 12/47 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.855× | -3.2 | 0.100 | 13/47 (KATO III, RPMI-7951, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.100 | 14/48 (KATO III, SW48, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.8 | 10 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.88× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 43.4 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 55.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.27× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 37.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 67.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Selinexor (drug)]] 5 µM 0.456× (z -11.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 41.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.70× (z +10.6) | — |
| [[A-172 (line)]] | wt | 31.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.69× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.141× (z -11.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HCT15 (line)]] | alt | 36.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.88× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 59.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.37× (z +8.8) | — |
| [[LoVo (line)]] | wt | 61.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.25× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.93× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0754× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[A-427 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.71 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[TMEM248]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZNF731P]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CHID1]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[FBXW2]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CPSF4]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[RNPS1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | -0.69 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.67 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[NBPF19]] | -0.65 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[BTN2A2]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RSF1]] | -0.64 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[PIM3]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SEC62]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[COIL]] | -0.63 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[KMT2E]] | -0.63 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[LCA5]] | -0.62 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[ANKRD12]] | -0.62 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[KMT2A]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (0.6, -28.1); signed map (-45.3, -20.7). **Vector** length 86.8, 21.5% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +14.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +3.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +3.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.6 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NIPA magnesium transporter 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:22,838,644-22,869,362 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC57A2 |
| Gene groups (HGNC) | Solute carrier family 57, NIPA-like magnesium transporters |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8Q9](https://www.uniprot.org/uniprotkb/Q8N8Q9) (Magnesium transporter NIPA2):

> Acts as a selective Mg(2+) transporter.

**Summary**, from NCBI Gene [81614](https://www.ncbi.nlm.nih.gov/gene/81614):

> This gene encodes a possible magnesium transporter. This gene is located adjacent to the imprinted domain in the Prader-Willi syndrome deletion region of chromosome 15. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 3, 7 and 21.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:17044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17044) · Entrez [81614](https://www.ncbi.nlm.nih.gov/gene/81614) · UniProt [Q8N8Q9](https://www.uniprot.org/uniprotkb/Q8N8Q9) · Ensembl [ENSG00000140157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140157)

## Data

Gene col 6376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6376); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6376]; `tensor/DDL_lfc|DDL_z.npy` [6376]; `embed/gene_vectors.npy` [6376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6376 or target_col == 6376). Every well: [[NIPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
