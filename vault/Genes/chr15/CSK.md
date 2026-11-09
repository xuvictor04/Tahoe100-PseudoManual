---
symbol: "CSK"
type: "gene"
col: 2389
ensembl_id: "ENSG00000103653"
name: "C-terminal Src kinase"
location: "15q24.1"
module: 2
arm: "+"
pooled_cpm: 14.01
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CSK

*C-terminal Src kinase* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.37× (z +5.7, q 5e-06, up in 16 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 1.28× (z +4.2, q 0.003, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.565× (z -14.6, q 3e-45, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.67, fdr 8e-06), [[GFOD2]] (+0.67, fdr 1e-05), [[ZNF496]] (+0.65, fdr 7e-06); moves opposite to [[THAP9]] (-0.57, fdr 1e-05), [[SGO1-AS1]] (-0.57, fdr 1e-05), [[NUCKS1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BRAT1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.7 | 5e-06 | 16/47 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.6 | 5e-06 | 19/42 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +4.6 | 0.001 | 16/43 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 0.003 | 15/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.011 | 13/46 (NCI-H2347, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erythromycin (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.031 | 4/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.033 | 8/31 (C-33 A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.079 | 8/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.079 | 2/47 (LoVo, SW1417) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.13 | 10/44 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.565×** | -14.6 | 3e-45 | 34/47 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -8.8 | 3e-16 | 25/46 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -8.7 | 8e-16 | 28/46 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -6.1 | 2e-07 | 21/47 (BT-474, A-427, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -6.0 | 2e-07 | 21/45 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -5.6 | 2e-06 | 18/48 (SW1417, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.4 | 6e-06 | 19/46 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -5.1 | 2e-05 | 21/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.755×** | -5.1 | 3e-05 | 17/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -4.0 | 0.003 | 16/47 (SK-MEL-2, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.805×** | -3.9 | 0.005 | 15/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.029 | 15/46 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.058 | 9/46 (NCI-H460, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.721×** | -3.1 | 0.083 | 8/48 (J82, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.844× | -3.1 | 0.084 | 11/47 (NCI-H460, SW 1271, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.9 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0854× (z -9.9) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.1) |
| [[RKO (line)]] | wt | 25.2 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0727× (z -16.9) |
| [[A-172 (line)]] | wt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.0) |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.6) |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.5) |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -9.9) |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.67 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[GFOD2]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[STK25]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MTMR12]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[TELO2]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[STARD3]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[UBE2F]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.63 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PPM1F]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[GBA2]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP9]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NUCKS1]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[STAG2]] | -0.54 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[HHLA3]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[CHD2]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRAT1]] | C | BRAT1's natural level weakens CSK's drug response | BRAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.07; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.7, -25.8); signed map (-45.1, -13.4). **Vector** length 70.2, 11.4% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | C-terminal Src kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,782,080-74,803,197 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; Csk family tyrosine kinases; SH3 domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 32 pathways, smallest: Phosphorylation of CD3 and TCR zeta chains; Negative regulation of FLT3; GAB1 signalosome |
| Matched by | ensembl_id |

**Function**, from UniProt [P41240](https://www.uniprot.org/uniprotkb/P41240) (Tyrosine-protein kinase CSK):

> Non-receptor tyrosine-protein kinase that plays an important role in the regulation of cell growth, differentiation, migration and immune response. Phosphorylates tyrosine residues located in the C-terminal tails of Src-family kinases (SFKs) including LCK, SRC, HCK, FYN, LYN, CSK or YES1. Upon tail phosphorylation, Src-family members engage in intramolecular interactions between the phosphotyrosine tail and the SH2 domain that result in an inactive conformation. To inhibit SFKs, CSK is …

**Summary**, from NCBI Gene [1445](https://www.ncbi.nlm.nih.gov/gene/1445):

> The protein encoded by this gene is involved in multiple pathways, including the regulation of Src family kinases. It plays an important role in T-cell activation through its association with the protein encoded by the protein tyrosine phosphatase, non-receptor type 22 (PTPN22) gene. This protein also phosphorylates C-terminal tyrosine residues on multiple substrates, including the protein encoded by the SRC proto-oncogene, non-receptor tyrosine kinase gene. Phosphorylation suppresses the …

**Accessions** — [HGNC:2444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2444) · Entrez [1445](https://www.ncbi.nlm.nih.gov/gene/1445) · UniProt [P41240](https://www.uniprot.org/uniprotkb/P41240) · Ensembl [ENSG00000103653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103653)

## Data

Gene col 2389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2389); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2389]; `tensor/DDL_lfc|DDL_z.npy` [2389]; `embed/gene_vectors.npy` [2389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2389 or target_col == 2389). Every well: [[CSK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
