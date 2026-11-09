---
symbol: "SAMD10"
type: "gene"
col: 5087
ensembl_id: "ENSG00000130590"
name: "sterile alpha motif domain containing 10"
location: "20q13.33"
module: 54
arm: "-"
pooled_cpm: 2.62
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SAMD10

*sterile alpha motif domain containing 10* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.15× (z +7.5, q 3e-11, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Erythromycin (drug)]] 5 µM: 1.42× (z +3.6, q 0.039, up in 4 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.308× (z -12.1, q 6e-31, down in 28 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC23]] (+0.66, fdr 1e-05), [[DPY19L2P2-1]] (+0.57, fdr 2e-05), [[SEPTIN8]] (+0.56, fdr 2e-05); moves opposite to [[SNX6]] (-0.53, fdr 6e-05), [[ACAP2]] (-0.50, fdr 5e-05), [[TAOK3]] (-0.50, fdr 4e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTP4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.5 | 3e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.9 | 1e-09 | 6/13 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.9 | 6e-07 | 3/5 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.3 | 0.002 | 3/15 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Erythromycin (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.039 | 4/36 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.045 | 5/32 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.047 | 3/24 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.15 | 3/27 (PANC-1, HCT15, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.308×** | -12.1 | 6e-31 | 28/38 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.356×** | -10.6 | 6e-24 | 27/37 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.411×** | -9.1 | 1e-17 | 24/36 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -8.1 | 6e-14 | 23/37 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.450×** | -7.8 | 1e-12 | 20/33 (KATO III, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -7.5 | 6e-12 | 16/34 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.543×** | -6.3 | 3e-08 | 18/37 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -5.8 | 6e-07 | 15/28 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -5.5 | 2e-06 | 19/39 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.366×** | -5.4 | 4e-06 | 11/33 (LS 180, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.607×** | -5.1 | 1e-05 | 12/37 (SW48, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -4.6 | 2e-04 | 15/37 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.637×** | -4.6 | 2e-04 | 12/34 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.001 | 12/30 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -3.7 | 0.007 | 9/37 (LOX-IMVI, C-33 A, …) | two highest doses | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.03 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -11.1) |
| [[KATO III (line)]] | alt | 4.02 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0463× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 5.23 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -9.0) |
| [[J82 (line)]] | alt | 2.71 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0505× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 1.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -12.0) |
| [[SHP-77 (line)]] | alt | 5.22 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0751× (z -9.0) |
| [[A-172 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.125 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC23]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[DPY19L2P2-1]] | +0.57 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[SEPTIN8]] | +0.56 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[FOXP4-AS1]] | +0.51 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[ESRP2]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[DPY19L2P1]] | +0.51 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[HOTAIR]] | +0.51 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[DHRS4L2]] | +0.51 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[PRKAR1B]] | +0.50 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[PRXL2B]] | +0.50 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RNF207]] | +0.49 | +0.37 / +0.35 | both halves | 1e-04 |  |
| [[TMEM147-AS1]] | +0.48 | +0.38 / +0.40 | both halves | 6e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX6]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[ACAP2]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TAOK3]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CALCOCO2]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZNF235]] | -0.48 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[FTL]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[EXOC6B]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[VRK3]] | -0.46 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[RPS6KC1]] | -0.46 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[TALAM1]] | -0.46 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[SAMD4B]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 | same gene group |
| [[PCYT1A]] | -0.45 | -0.54 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTP4A3]] | B | PTP4A3 activity raises SAMD10's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without PTP4A3 | 0.065 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[ESRP2]] | B | ESRP2 activity raises SAMD10's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.74× lower at baseline in the lines without ESRP2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.205). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.7, 34.2); signed map (31.2, -34.2). **Vector** length 46.1, 6.20% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.2 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -9.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,974,116-63,980,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C20orf136 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q9BYL1](https://www.uniprot.org/uniprotkb/Q9BYL1) carries no function annotation.

**Summary**, from NCBI Gene [140700](https://www.ncbi.nlm.nih.gov/gene/140700):

> Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to be active in cytoplasmic side of plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16129) · Entrez [140700](https://www.ncbi.nlm.nih.gov/gene/140700) · UniProt [Q9BYL1](https://www.uniprot.org/uniprotkb/Q9BYL1) · Ensembl [ENSG00000130590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130590)

## Data

Gene col 5087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5087); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5087]; `tensor/DDL_lfc|DDL_z.npy` [5087]; `embed/gene_vectors.npy` [5087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5087 or target_col == 5087). Every well: [[SAMD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
