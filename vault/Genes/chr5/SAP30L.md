---
symbol: "SAP30L"
type: "gene"
col: 8964
ensembl_id: "ENSG00000164576"
name: "SAP30 like"
location: "5q33.2"
module: 145
arm: "+"
pooled_cpm: 11.04
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# SAP30L

*SAP30 like* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +7.2, q 3e-10, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -12.4, q 1e-32, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPI2]] (+0.72, fdr 1e-05), [[GID4]] (+0.67, fdr 1e-05), [[SLC35D2]] (+0.66, fdr 1e-05); moves opposite to [[HNRNPC]] (-0.56, fdr 6e-05), [[LINC00460]] (-0.54, fdr 1e-05), [[THOC6]] (-0.50, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53I13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.2 | 3e-10 | 32/45 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +6.4 | 4e-08 | 27/44 (HEC-1-A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.8 | 1e-06 | 10/21 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.7 | 2e-06 | 21/40 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.6 | 2e-06 | 23/47 (HEC-1-A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.3 | 1e-05 | 18/36 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 20/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 6e-04 | 16/47 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.3 | 0.001 | 13/45 (A-172, Hs 766T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 17/41 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.003 | 14/46 (LoVo, PANC-1, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.010 | 7/46 (SW1417, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.011 | 11/45 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.021 | 6/47 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.022 | 18/45 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.032 | 11/45 (SW48, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.043 | 7/44 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.059 | 9/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.059 | 4/47 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -12.4 | 1e-32 | 36/44 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.575×** | -7.2 | 1e-10 | 28/47 (SW1417, A-172, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -7.1 | 2e-10 | 29/46 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -7.1 | 2e-10 | 30/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -6.2 | 5e-08 | 22/42 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -6.2 | 5e-08 | 25/47 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.468×** | -5.2 | 2e-05 | 19/43 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 6e-04 | 24/47 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -4.4 | 8e-04 | 21/45 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -3.9 | 0.005 | 13/47 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.669×** | -3.8 | 0.009 | 7/48 (NCI-H661, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.741×** | -3.6 | 0.014 | 7/47 (BT-474, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.600×** | -3.5 | 0.021 | 12/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.030 | 13/43 (SHP-77, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.038 | 8/48 (KATO III, C-33 A, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.785×** | -3.0 | 0.080 | 16/46 (AN3 CA, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.8) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0664× (z -16.1) |
| [[BT-474 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 9.27 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.104× (z -8.6) |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.1) |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 9.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 5.42 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0478× (z -9.4) |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPI2]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[GID4]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SLC35D2]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.65 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[HAGH]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[ULK1]] | +0.65 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[ARL8A]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RNF38]] | +0.64 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[PINK1]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MXD4]] | +0.61 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[DENND10]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPC]] | -0.56 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[LINC00460]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[THOC6]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53I13]] | C | TP53I13 activity lowers SAP30L's level | lines that do not express TP53I13 (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without TP53I13 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC25A37; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -43.1); signed map (-22.3, 7.0). **Vector** length 70.7, 12.7% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SAP30 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,445,997-154,461,053 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11526, NS4ATP2 |
| Gene groups (HGNC) | SIN3 histone deacetylase complex subunits |
| Reactome | 9 pathways, smallest: HDACs deacetylate histones; NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAJ7](https://www.uniprot.org/uniprotkb/Q9HAJ7) (Histone deacetylase complex subunit SAP30L):

> [Isoform 1]: Functions as a transcription repressor, probably via its interaction with histone deacetylase complexes. Involved in the functional recruitment of the class 1 Sin3-histone deacetylase complex (HDAC) to the nucleolus. Binds DNA, apparently without sequence-specificity, and bends bound double-stranded DNA. Binds phosphoinositol phosphates (phosphoinositol 3-phosphate, phosphoinositol 4-phosphate and phosphoinositol 5-phosphate) via the same basic sequence motif that mediates DNA …

**Summary**, from NCBI Gene [79685](https://www.ncbi.nlm.nih.gov/gene/79685):

> Enables several functions, including non-sequence-specific DNA binding activity, bending; phosphatidylinositol phosphate binding activity; and zinc ion binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in fibrillar center and nucleoplasm. Part of histone deacetylase complex. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:25663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25663) · Entrez [79685](https://www.ncbi.nlm.nih.gov/gene/79685) · UniProt [Q9HAJ7](https://www.uniprot.org/uniprotkb/Q9HAJ7) · Ensembl [ENSG00000164576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164576)

## Data

Gene col 8964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8964); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8964]; `tensor/DDL_lfc|DDL_z.npy` [8964]; `embed/gene_vectors.npy` [8964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8964 or target_col == 8964). Every well: [[SAP30L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP30L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
