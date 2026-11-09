---
symbol: "NADK"
type: "gene"
col: 161
ensembl_id: "ENSG00000008130"
name: "NAD kinase"
location: "1p36.33"
module: 5
arm: "+"
pooled_cpm: 16.02
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NADK

*NAD kinase* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.69× (z +8.7, q 3e-15, up in 29 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.48× (z +7.0, q 4e-10, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.846× (z -4.3, q 0.011, down in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.267×; ⚠ cell-cycle shift, explains ~93% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LETM1]] (+0.75, fdr 7e-06), [[SENP3]] (+0.73, fdr 7e-06), [[WDR4]] (+0.68, fdr 7e-06); moves opposite to [[BTG1]] (-0.66, fdr 7e-06), [[KDM5B]] (-0.61, fdr 7e-06), [[CTR9]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.7 | 3e-15 | 29/43 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.1 | 1e-13 | 20/26 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.1 | 1e-13 | 20/38 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +7.9 | 6e-13 | 29/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.0 | 4e-10 | 25/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +6.4 | 1e-08 | 28/45 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.4 | 1e-08 | 13/22 (C-33 A, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +6.3 | 2e-08 | 26/47 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.44×** | +6.2 | 4e-08 | 20/46 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.1 | 7e-08 | 23/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +6.0 | 9e-08 | 23/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 7e-07 | 17/46 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.4 | 2e-06 | 19/44 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 1e-05 | 22/47 (A498, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +4.7 | 8e-05 | 15/46 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 5e-04 | 14/46 (H4, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.2 | 1e-03 | 7/44 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 12/46 (H4, C-33 A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.018 | 6/45 (C-33 A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.088 | 3/45 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.097 | 5/47 (CFPAC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.267×; ⚠ cell-cycle shift, explains ~93% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.3 | 0.011 | 11/48 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.811×** | -3.8 | 0.046 | 13/45 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.872× | -3.5 | 0.088 | 19/47 (SNU-1, J82, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0654× (z -13.4) |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.217× (z -8.5) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.136× (z -8.7) |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM1]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[SENP3]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[DHX33]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[CAD]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[URB2]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[UTP4]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[PEX26]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.64 | +0.68 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[KDM5B]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[CTR9]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[TCEAL8]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[PJA2]] | -0.58 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[LGALS1]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[GIHCG]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[LYSMD3]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[METTL23]] | -0.57 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[AKAP9]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ING1]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises NADK's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without NUP210 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.7, -30.1); signed map (-8.9, -42.4). **Vector** length 79.7, 14.4% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.4 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -4.2 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NAD kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,751,232-1,780,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13052, NADK1 |
| Gene groups (HGNC) | NAD kinases |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

UniProt [O95544](https://www.uniprot.org/uniprotkb/O95544) carries no function annotation.

**Summary**, from NCBI Gene [65220](https://www.ncbi.nlm.nih.gov/gene/65220):

> NADK catalyzes the transfer of a phosphate group from ATP to NAD to generate NADP, which in its reduced form acts as an electron donor for biosynthetic reactions (Lerner et al., 2001 [PubMed 11594753]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29831) · Entrez [65220](https://www.ncbi.nlm.nih.gov/gene/65220) · UniProt [O95544](https://www.uniprot.org/uniprotkb/O95544) · Ensembl [ENSG00000008130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008130)

## Data

Gene col 161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 161); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 161]; `tensor/DDL_lfc|DDL_z.npy` [161]; `embed/gene_vectors.npy` [161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 161 or target_col == 161). Every well: [[NADK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NADK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
