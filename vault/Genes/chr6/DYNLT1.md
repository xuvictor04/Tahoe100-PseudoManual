---
symbol: "DYNLT1"
type: "gene"
col: 7094
ensembl_id: "ENSG00000146425"
name: "dynein light chain Tctex-type 1"
location: "6q25.3"
module: 184
arm: "+"
pooled_cpm: 34.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# DYNLT1

*dynein light chain Tctex-type 1* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +7.1, q 7e-10, up in 32 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.41× (z +3.4, q 0.068, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.10×, CFPAC-1 3.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 4.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.570× (z -8.2, q 2e-13, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOC]] (+0.56, fdr 1e-05), [[EHD4]] (+0.55, fdr 5e-05), [[VPS25]] (+0.55, fdr 1e-05); moves opposite to [[ZNF362]] (-0.52, fdr 2e-04), [[HDGF]] (-0.52, fdr 4e-04), [[SLC43A1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7094.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 3.10×, CFPAC-1 3.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 4.55×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.98×** | +7.1 | 7e-10 | 32/44 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.03×** | +7.0 | 7e-10 | 29/38 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.58×** | +4.7 | 5e-04 | 23/45 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.63×** | +4.6 | 6e-04 | 27/42 (NCI-H2030, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +4.5 | 8e-04 | 29/48 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.068 | 22/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +3.2 | 0.096 | 21/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.36× | +3.2 | 0.10 | 22/47 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.12 | 16/48 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.35× | +3.1 | 0.12 | 20/48 (PANC-1, KATO III, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.86× | +3.0 | 0.14 | 21/47 (LoVo, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -8.2 | 2e-13 | 36/47 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -4.9 | 2e-04 | 33/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.338×** | -4.8 | 3e-04 | 33/47 (HS-578T, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -4.7 | 4e-04 | 27/46 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.671×** | -4.1 | 0.005 | 30/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -3.9 | 0.010 | 27/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 28.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Digitoxin (drug)]] 5 µM 0.207× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.1) |
| [[A-172 (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.2) |
| [[A-427 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 39.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.4) |
| [[HOP62 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.2) |
| [[J82 (line)]] | alt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.8) |
| [[LoVo (line)]] | wt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.5) |
| [[PANC-1 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOC]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[EHD4]] | +0.55 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[VPS25]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TUBB6]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ORMDL2]] | +0.52 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CLTCL1]] | +0.51 | +0.31 / +0.34 | both halves | 2e-04 |  |
| [[PLIN3]] | +0.51 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[CENPX]] | +0.51 | +0.36 / +0.38 | both halves | 9e-05 |  |
| [[GPRIN1]] | +0.51 | +0.33 / +0.32 | both halves | 2e-04 |  |
| [[DLGAP4]] | +0.50 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[MRTFA]] | +0.50 | +0.27 / +0.47 | both halves | 3e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | -0.52 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[HDGF]] | -0.52 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[SLC43A1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[HOTAIR]] | -0.51 | -0.30 / -0.29 | both halves | 2e-04 |  |
| [[MATR3]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ITPKB]] | -0.51 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[CDH26]] | -0.49 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[HOXB7]] | -0.49 | -0.41 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[UFC1]] | -0.49 | -0.36 / -0.23 | both halves | 5e-04 |  |
| [[USF2]] | -0.48 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[U2AF2]] | -0.47 | -0.27 / -0.34 | both halves | 3e-04 | pathway: Dengue Virus-Host Interactions |
| [[LAMTOR5-AS1]] | -0.47 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[METTL25]] | -0.47 | -0.39 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DYNLT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-1.3, 15.8); signed map (-16.2, 19.4). **Vector** length 76.3, 20.3% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.7 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | dynein light chain Tctex-type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,636,474-158,644,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tctex-1, TCTEX1; previously TCTEL1 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein 2 complex subunits; Dyneins, axonemal outer arm complex subunits; Dynein light chain Tctex-type family |
| Reactome | 5 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P63172](https://www.uniprot.org/uniprotkb/P63172) (Dynein light chain Tctex-type 1):

> Component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Required for structural and functional integrity of cilia (By similarity). Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles …

**Summary**, from NCBI Gene [6993](https://www.ncbi.nlm.nih.gov/gene/6993):

> This gene encodes a component of the motor complex, cytoplasmic dynein, which transports cellular cargo along microtubules in the cell. The encoded protein regulates the length of primary cilia which are sensory organelles found on the surface of cells. The protein encoded by this gene interacts with viral proteins, like the minor capsid protein L2 of human papillomavirus, and is required for dynein-mediated delivery of the viral nucleic acid to the host nucleus. This protein interacts with …

**Accessions** — [HGNC:11697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11697) · Entrez [6993](https://www.ncbi.nlm.nih.gov/gene/6993) · UniProt [P63172](https://www.uniprot.org/uniprotkb/P63172) · Ensembl [ENSG00000146425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146425)

## Data

Gene col 7094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7094); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7094]; `tensor/DDL_lfc|DDL_z.npy` [7094]; `embed/gene_vectors.npy` [7094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7094 or target_col == 7094). Every well: [[DYNLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
