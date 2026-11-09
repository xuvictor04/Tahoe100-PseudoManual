---
symbol: "ANK3"
type: "gene"
col: 7491
ensembl_id: "ENSG00000151150"
name: "ankyrin 3"
location: "10q21.2"
module: 8
arm: "+"
pooled_cpm: 118.19
n_lines_expressing: 27
n_dd_up: 27
n_dd_down: 32
n_dd_up_clean: 25
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 48
direction_downstream: 64
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ANK3

*ankyrin 3* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +10.1, q 4e-21, up in 4 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +8.3, q 2e-14, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.467× (z -13.7, q 7e-40, down in 22 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF38]] (+0.72, fdr 7e-06), [[PLCH1]] (+0.71, fdr 7e-06), [[LINC02253]] (+0.71, fdr 7e-06); moves opposite to [[SNX21]] (-0.55, fdr 3e-05), [[ITGB1BP1]] (-0.53, fdr 2e-05), [[LOXL2]] (-0.51, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 48 arrows point to it, the strongest [[MIR4713HG]] → it (grade B ⚠); 64 go from it, the strongest it → [[EXPH5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +10.1 | 4e-21 | 4/25 (A-172, NCI-H2122, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.3 | 2e-14 | 8/25 (SW 900, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +7.9 | 4e-13 | 9/26 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.6 | 4e-12 | 4/26 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 6e-09 | 15/25 (NCI-H460, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +6.2 | 5e-08 | 19/24 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +6.0 | 2e-07 | 14/25 (NCI-H460, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +5.7 | 8e-07 | 12/26 (NCI-H460, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +5.1 | 2e-05 | 12/26 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 15/24 (NCI-H460, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 9e-04 | 9/24 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 13/25 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 9/24 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 13/25 (SW 900, LoVo, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 6/24 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.003 | 12/24 (LoVo, HEC-1-A, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -13.7 | 7e-40 | 22/25 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -11.6 | 1e-28 | 21/25 (COLO 205, LS 180, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -9.8 | 2e-20 | 21/25 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -9.4 | 6e-19 | 21/25 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -9.4 | 7e-19 | 21/24 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.612×** | -8.8 | 1e-16 | 20/25 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -7.2 | 4e-11 | 22/24 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -7.2 | 4e-11 | 17/25 (C32, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -6.0 | 1e-07 | 8/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -5.9 | 2e-07 | 17/24 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -5.9 | 2e-07 | 19/25 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -5.9 | 2e-07 | 20/26 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -5.9 | 2e-07 | 18/25 (HT-29, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -5.7 | 5e-07 | 17/25 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.744×** | -5.1 | 1e-05 | 13/25 (SW480, HCT15, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.559×** | -5.0 | 2e-05 | 18/25 (A-427, LOX-IMVI, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.782×** | -4.4 | 3e-04 | 17/25 (SW48, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 129 | 0 | 23 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0583× (z -16.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0778× (z -15.5) |
| [[COLO 205 (line)]] | alt | 184 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -29.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.117× (z -22.1) |
| [[SW480 (line)]] | alt | 189 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.164× (z -19.7) |
| [[HCT15 (line)]] | alt | 358 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -18.8) |
| [[KATO III (line)]] | alt | 244 | 0 | 14 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.178× (z -20.4) |
| [[LoVo (line)]] | wt | 265 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -18.4) |
| [[A-427 (line)]] | wt | 95.3 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -16.7) |
| [[HT-29 (line)]] | alt | 307 | 0 | 13 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.169× (z -20.1) |
| [[LS 180 (line)]] | wt | 392 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -20.9) |
| [[NCI-H1573 (line)]] | alt | 216 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -26.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0833× (z -22.5) |
| [[SW48 (line)]] | wt | 350 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 294 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -19.0) |
| [[Panc 03.27 (line)]] | alt | 220 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 253 | 4 | 5 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.94× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.178× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 341 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -15.9) |
| [[SW1417 (line)]] | alt | 258 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -15.0) |
| [[CHP-212 (line)]] | wt | 188 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.84× (z +19.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.166× (z -10.6) |
| [[A-172 (line)]] | wt | 36.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +22.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.85× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 337 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.1) |
| [[H4 (line)]] | wt | 34.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF38]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[LINC02253]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[FAAH2]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[GRHL2]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PROM1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[POF1B]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[SAMD12]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SYK]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 | STRING 559 |
| [[ATP10B]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LINC02331]] | +0.62 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[LINC01814]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX21]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ITGB1BP1]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[LOXL2]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ADAMTS10]] | -0.50 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[EPOR]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 6, C 42. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4713HG]] | B | MIR4713HG activity raises ANK3's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without MIR4713HG | 0.024 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[SPTLC3]] | B | SPTLC3 activity raises ANK3's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 1.95× lower at baseline in the lines without SPTLC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[LINC02343]] | B | LINC02343 activity raises ANK3's level | lines that do not express LINC02343 (7) vs lines expressing it (43) | 3.55× lower at baseline in the lines without LINC02343 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRAF2; maybe low, not absent |
| [[MYO5C]] | B | MYO5C activity raises ANK3's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 3.44× lower at baseline in the lines without MYO5C | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[EXPH5]] | B | EXPH5 activity raises ANK3's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without EXPH5 | 0.073 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[ARHGEF6]] | B | ARHGEF6 activity lowers ANK3's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.32× higher at baseline in the lines without ARHGEF6 | 0.076 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[MACC1]] | C | MACC1 activity raises ANK3's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 8.69× lower at baseline in the lines without MACC1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ANK3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 7.99× lower at baseline in the lines without TMEM125 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises ANK3's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 7.56× lower at baseline in the lines without GRHL2 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[PRR15]] | C | PRR15 activity raises ANK3's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 6.05× lower at baseline in the lines without PRR15 | 6e-04 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[CATSPERB]] | C | CATSPERB activity raises ANK3's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 5.37× lower at baseline in the lines without CATSPERB | 0.002 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises ANK3's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 6.94× lower at baseline in the lines without ARHGEF38 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |

### Downstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 23, C 41. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXPH5]] | B | ANK3 activity raises EXPH5's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.82× lower at baseline in the lines without ANK3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[C4orf19]] | B | ANK3 activity raises C4orf19's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.29× lower at baseline in the lines without ANK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[MYO5C]] | B | ANK3 activity raises MYO5C's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without ANK3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[SLC44A3]] | B | ANK3 activity raises SLC44A3's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without ANK3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[TNFRSF14-AS1]] | B | ANK3 activity raises TNFRSF14-AS1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 1.82× lower at baseline in the lines without ANK3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[CCSER1]] | B | ANK3 activity raises CCSER1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.13× lower at baseline in the lines without ANK3 | 0.020 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[SORL1]] | B | ANK3 activity raises SORL1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.01× lower at baseline in the lines without ANK3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[ITGB8]] | B | ANK3 activity raises ITGB8's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.62× lower at baseline in the lines without ANK3 | 0.023 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[STARD9]] | B | ANK3 activity lowers STARD9's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.04× higher at baseline in the lines without ANK3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[BCL2L15]] | B | ANK3 activity raises BCL2L15's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without ANK3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[MANSC1]] | B | ANK3 activity raises MANSC1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without ANK3 | 0.034 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[NAALADL2]] | B | ANK3 activity raises NAALADL2's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.78× lower at baseline in the lines without ANK3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, 49.9); signed map (57.9, 2.2). **Vector** length 117, 38.8% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -11.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -5.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:60,026,298-60,733,490 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ZU5 domain containing ; Ankyrin family |
| Reactome | 18 pathways, smallest: Interaction between L1 and Ankyrins; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12955](https://www.uniprot.org/uniprotkb/Q12955) (Ankyrin-3):

> Required for the organization of specialized membrane domains by linking the membrane to the cytoskeleton. In neurons, participates in the maintenance/targeting of ion channels and cell adhesion molecules at the nodes of Ranvier and axonal initial segments. In skeletal muscle, required for the localization of dystrophin (DMD) and beta-dystroglycan (betaDAG1) to costameres (By similarity). In rod photoreceptors, required for the transport of cyclic nucleotide-gated (CNG) channel subunits from …

**Summary**, from NCBI Gene [288](https://www.ncbi.nlm.nih.gov/gene/288):

> Ankyrins are a family of proteins that are believed to link the integral membrane proteins to the underlying spectrin-actin cytoskeleton and play key roles in activities such as cell motility, activation, proliferation, contact, and the maintenance of specialized membrane domains. Multiple isoforms of ankyrin with different affinities for various target proteins are expressed in a tissue-specific, developmentally regulated manner. Most ankyrins are typically composed of three structural …

**Accessions** — [HGNC:494](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:494) · Entrez [288](https://www.ncbi.nlm.nih.gov/gene/288) · UniProt [Q12955](https://www.uniprot.org/uniprotkb/Q12955) · Ensembl [ENSG00000151150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151150)

## Data

Gene col 7491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7491); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7491]; `tensor/DDL_lfc|DDL_z.npy` [7491]; `embed/gene_vectors.npy` [7491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7491 or target_col == 7491). Every well: [[ANK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
