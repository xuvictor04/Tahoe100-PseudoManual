---
symbol: "SCN8A"
type: "gene"
col: 12298
ensembl_id: "ENSG00000196876"
name: "sodium voltage-gated channel alpha subunit 8"
location: "12q13.13"
module: 82
arm: "+"
pooled_cpm: 40.58
n_lines_expressing: 32
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 13
direction_downstream: 11
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# SCN8A

*sodium voltage-gated channel alpha subunit 8* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.29× (z +21.5, q 0e+00, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.758× (z -7.2, q 4e-10, down in 20 of 30 measured lines) ⚠ cell-cycle shift, explains ~87% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.617× (z -4.6, q 3e-04, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STOX2]] (+0.60, fdr 1e-05), [[ADGRB1]] (+0.59, fdr 2e-05), [[CCDC136]] (+0.58, fdr 2e-05); moves opposite to [[DYNC2I1]] (-0.43, fdr 1e-04), [[MPV17]] (-0.42, fdr 3e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SLC4A8]] → it (grade B ⚠); 11 go from it, the strongest it → [[TMEM150C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +21.5 | 0e+00 | 23/30 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +15.5 | 0e+00 | 25/29 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +11.3 | 4e-27 | 19/30 (A-172, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +8.9 | 6e-17 | 14/29 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +8.5 | 1e-15 | 11/30 (C32, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.5 | 9e-12 | 12/29 (C32, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +5.7 | 1e-06 | 18/30 (SW480, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 2e-04 | 8/30 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.7 | 2e-04 | 11/30 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +4.6 | 2e-04 | 8/30 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.024 | 2/30 (SW480, A-172) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.029 | 6/29 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.036 | 13/29 (SW480, A498, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.19× | +3.1 | 0.067 | 6/29 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.067 | 9/29 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.067 | 6/29 (NCI-H2030, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.758×** | -7.2 | 4e-10 | 20/30 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.738×** | -5.6 | 6e-06 | 15/30 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.740×** | -5.5 | 6e-06 | 18/29 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.737×** | -5.4 | 1e-05 | 17/29 (SW480, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.768×** | -4.9 | 1e-04 | 14/29 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -4.6 | 3e-04 | 18/30 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.5 | 5e-04 | 19/30 (J82, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -4.5 | 6e-04 | 10/29 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.791×** | -4.3 | 0.001 | 14/29 (NCI-H1573, A498, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.799×** | -4.1 | 0.002 | 13/30 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.004 | 12/29 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.807×** | -3.8 | 0.007 | 13/29 (PANC-1, A549, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.815×** | -3.8 | 0.007 | 16/30 (NCI-H1573, PANC-1, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.023 | 10/30 (PANC-1, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.025 | 14/29 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 54.7 | 0 | 12 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -20.6) ⚠ cell-cycle shift, explains ~87% of this change |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 57.9 | 1 | 8 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -19.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -31.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.5) |
| [[A-427 (line)]] | wt | 186 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0524× (z -35.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.9) |
| [[SW480 (line)]] | alt | 62.5 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.335× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 49.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.3) ⚠ cell-cycle shift, explains ~87% of this change |
| [[LoVo (line)]] | wt | 35.1 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.67× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW1417 (line)]] | alt | 58.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HCT15 (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 32.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.3) |
| [[A498 (line)]] | wt | 50.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.352× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 13.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 98.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.88× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.4) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[SHP-77 (line)]] | alt | 95.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STOX2]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ADGRB1]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[CCDC136]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LINC00937]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MTMR8]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[NFASC]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 | pathway: Interaction between L1 and Ankyrins; STRING 888 |
| [[PLEKHA5]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CHMP1B2P]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TMEM150C]] | +0.53 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[CHST10]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[DOCK3]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 | STRING 519 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2I1]] | -0.43 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MPV17]] | -0.42 | -0.36 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A8]] | B | SLC4A8 activity raises SCN8A's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 3.61× lower at baseline in the lines without SLC4A8 | 0.019 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[FAM184A]] | B | FAM184A activity raises SCN8A's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.90× lower at baseline in the lines without FAM184A | 0.035 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[TRIM58]] | B | TRIM58 activity raises SCN8A's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without TRIM58 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[GNAO1]] | B | GNAO1 activity raises SCN8A's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without GNAO1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[RGS7]] | B | RGS7 activity raises SCN8A's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without RGS7 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[LMX1B]] | B | LMX1B activity raises SCN8A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without LMX1B | 0.069 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[ARHGEF25]] | B | ARHGEF25 activity raises SCN8A's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without ARHGEF25 | 0.075 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SCN8A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SCN8A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EMID1]] | B | EMID1 activity raises SCN8A's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without EMID1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[SLC6A17]] | C | SLC6A17 activity raises SCN8A's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.41× lower at baseline in the lines without SLC6A17 | 0.003 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises SCN8A's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 3.31× lower at baseline in the lines without JPH3 | 0.009 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM150C]] | B | SCN8A activity raises TMEM150C's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without SCN8A | 0.022 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[GNAO1]] | B | SCN8A activity raises GNAO1's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without SCN8A | 0.041 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[SYT9-AS1]] | B | SCN8A activity raises SYT9-AS1's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without SCN8A | 0.042 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[RAB6B]] | B | SCN8A activity raises RAB6B's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.10× lower at baseline in the lines without SCN8A | 0.054 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[SPTB]] | B | SCN8A activity raises SPTB's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without SCN8A | 0.055 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[FAM184A]] | B | SCN8A activity raises FAM184A's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without SCN8A | 0.071 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[SEPTIN3]] | B | SCN8A activity raises SEPTIN3's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without SCN8A | 0.076 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[ATP6V1E2]] | B | SCN8A activity raises ATP6V1E2's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without SCN8A | 0.089 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[NFASC]] | C | SCN8A activity raises NFASC's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.95× lower at baseline in the lines without SCN8A | 0.024 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |
| [[DPYSL5]] | C | SCN8A activity raises DPYSL5's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without SCN8A | 0.053 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |
| [[HAGLR]] | C | SCN8A activity raises HAGLR's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without SCN8A | 0.096 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, 37.4); signed map (28.7, 27.6). **Vector** length 81.8, 21.8% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +21.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +3.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.0 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -1.7 | -7.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel alpha subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,590,266-51,812,864 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nav1.6, NaCh6, PN4, CerIII, CIAT; previously MED |
| Gene groups (HGNC) | Sodium voltage-gated channel alpha subunits |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 7 pathways, smallest: Interaction between L1 and Ankyrins; Phase 0 - rapid depolarisation; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQD0](https://www.uniprot.org/uniprotkb/Q9UQD0) (Sodium channel protein type 8 subunit alpha):

> Pore-forming subunit of a voltage-gated sodium channel complex assuming opened or closed conformations in response to the voltage difference across membranes and through which sodium ions selectively pass along their electrochemical gradient. Contributes to neuronal excitability by regulating action potential threshold and propagation.; [Isoform 5]: More specifically expressed in non-neuronal cells, could play a role in sodium release from intracellular compartments and participate in the …

**Summary**, from NCBI Gene [6334](https://www.ncbi.nlm.nih.gov/gene/6334):

> This gene encodes a member of the sodium channel alpha subunit gene family. The encoded protein forms the ion pore region of the voltage-gated sodium channel. This protein is essential for the rapid membrane depolarization that occurs during the formation of the action potential in excitable neurons. Mutations in this gene are associated with cognitive disability, pancerebellar atrophy and ataxia. Alternate splicing results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:10596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10596) · Entrez [6334](https://www.ncbi.nlm.nih.gov/gene/6334) · UniProt [Q9UQD0](https://www.uniprot.org/uniprotkb/Q9UQD0) · Ensembl [ENSG00000196876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196876)

## Data

Gene col 12298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12298); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12298]; `tensor/DDL_lfc|DDL_z.npy` [12298]; `embed/gene_vectors.npy` [12298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12298 or target_col == 12298). Every well: [[SCN8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
