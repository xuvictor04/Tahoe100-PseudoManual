---
symbol: "SFTA3-1"
type: "gene"
col: 15046
ensembl_id: "ENSG00000257520"
name: ""
location: ""
module: 9
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 15
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SFTA3-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.12× (z +14.3, q 2e-43, up in 5 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fingolimod (hydrochloride) (drug)]] 0.5 µM: 0.565× (z -4.1, q 0.019, down in 0 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SHP-77 0.188×, SW 900 0.162×; ⚠ cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.109×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.110×; ⚠ cell-cycle shift, explains ~57% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02197]] (+0.64, fdr 1e-05), [[SNTG1]] (+0.58, fdr 1e-05), [[NRXN1]] (+0.57, fdr 3e-05); moves opposite to [[HLCS]] (-0.46, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLUT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CACNB2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.12×** | +14.3 | 2e-43 | 5/9 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.62×** | +11.9 | 5e-30 | 2/4 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.96×** | +11.4 | 5e-28 | 2/4 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.75×** | +10.3 | 1e-22 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.77×** | +5.2 | 3e-05 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +5.0 | 6e-05 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 3/12 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +4.6 | 3e-04 | 2/7 (NCI-H2347, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.32×** | +4.3 | 0.001 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.003 | 1/9 (SW 900) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.19×** | +4.0 | 0.004 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **2.12×** | +3.8 | 0.007 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.75×** | +3.7 | 0.011 | 0/8 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.02×** | +3.6 | 0.015 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +3.3 | 0.032 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.078 | 1/8 (NCI-H2347) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15046.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SHP-77 0.188×, SW 900 0.162×; ⚠ cell-cycle shift, explains ~55% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.109×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.110×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | **0.565×** | -4.1 | 0.019 | 0/12 | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.583×** | -3.9 | 0.025 | 3/11 (MIA PaCa-2, NCI-H23, …) | two highest doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.646× | -3.2 | 0.22 | 1/12 (HCT15) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -3.1 | 0.22 | 3/13 (HCT15, NCI-H1573, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.639× | -3.1 | 0.22 | 0/10 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.658× | -3.0 | 0.22 | 5/12 (SHP-77, NCI-H661, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 37.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.162× (z -8.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02197]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SNTG1]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NRXN1]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SYT4]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDH10]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ESRRG]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ASCL1]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SRRM4]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RUNX1T1]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[NFATC4]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[RIT2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[RALYL]] | +0.52 | +0.40 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLCS]] | -0.46 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLUT]] | B | PLUT activity raises SFTA3-1's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without PLUT | 0.046 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[MEIS1]] | B | MEIS1 activity lowers SFTA3-1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 1.61× higher at baseline in the lines without MEIS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[RUNX1T1]] | C | RUNX1T1 activity raises SFTA3-1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without RUNX1T1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises SFTA3-1's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.58× lower at baseline in the lines without SNTG1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNB2]] | C | SFTA3-1 activity raises CACNB2's level | lines that do not express SFTA3-1 (35) vs lines expressing it (15) | 2.44× lower at baseline in the lines without SFTA3-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01035, ZNF736P9Y, ENSG00000289418; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.1, 36.2); signed map (44.4, 33.2). **Vector** length 20.5, 3.78% of its response variance represented; |z| ≥ 3 in 261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +4.0 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -2.5 |

## What is on record

> [!warning] No registry record
> SFTA3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15046); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15046]; `tensor/DDL_lfc|DDL_z.npy` [15046]; `embed/gene_vectors.npy` [15046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15046 or target_col == 15046). Every well: [[SFTA3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFTA3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
