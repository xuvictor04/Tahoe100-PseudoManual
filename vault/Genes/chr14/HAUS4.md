---
symbol: "HAUS4"
type: "gene"
col: 1685
ensembl_id: "ENSG00000092036"
name: "HAUS augmin like complex subunit 4"
location: "14q11.2"
module: 45
arm: "+"
pooled_cpm: 10.25
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# HAUS4

*HAUS augmin like complex subunit 4* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.72× (z +7.9, q 2e-12, up in 12 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.45× (z +3.9, q 0.012, up in 6 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.518× (z -10.2, q 7e-22, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2]] (+0.65, fdr 1e-05), [[CEP192]] (+0.64, fdr 1e-05), [[ALDH7A1]] (+0.64, fdr 2e-05); moves opposite to [[HCG18]] (-0.60, fdr 3e-05), [[AVEN]] (-0.60, fdr 3e-05), [[EXOSC3]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.9 | 2e-12 | 12/17 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.1 | 5e-10 | 21/33 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.33×** | +4.4 | 0.002 | 15/40 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +4.1 | 0.005 | 6/48 (A-427, Panc 03.27, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.012 | 6/40 (SHP-77, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.059 | 10/43 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.059 | 10/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.3 | 0.079 | 4/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -10.2 | 7e-22 | 32/47 (BT-474, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -7.9 | 1e-12 | 26/45 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -6.7 | 4e-09 | 28/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.638×** | -6.5 | 1e-08 | 21/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.675×** | -6.1 | 1e-07 | 25/47 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -5.5 | 4e-06 | 22/45 (NCI-H2030, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -5.1 | 3e-05 | 20/45 (C-33 A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -4.8 | 1e-04 | 20/47 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -4.7 | 2e-04 | 14/46 (BT-474, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -4.7 | 2e-04 | 20/47 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -4.3 | 0.001 | 13/42 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.004 | 11/47 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.762×** | -3.9 | 0.004 | 16/39 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -3.8 | 0.006 | 10/48 (H4, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.788×** | -3.7 | 0.008 | 12/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.785×** | -3.5 | 0.014 | 11/47 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.5 | 0.015 | 12/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.021 | 14/46 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 3 (1 ⚠) | — | [[XRK3F2 (drug)]] 0.5 µM 0.0955× (z -9.2) |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[DT-061 (drug)]] 0.05 µM 0.155× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 7.62 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0953× (z -8.9) |
| [[LoVo (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.6) |
| [[A-172 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2]] | +0.65 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CEP192]] | +0.64 | +0.53 / +0.49 | both halves | 1e-05 | pathway: AURKA Activation by TPX2; STRING 526 |
| [[ALDH7A1]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MNS1]] | +0.64 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[THRA]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[KANTR]] | +0.63 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[HACE1]] | +0.63 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TTK]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CHEK2]] | +0.62 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SLC25A40]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[RFC1]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[THYN1]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG18]] | -0.60 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[AVEN]] | -0.60 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[EXOSC3]] | -0.59 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[LTO1]] | -0.58 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[LINC01829]] | -0.58 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[S100A11]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.54 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[TBILA]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[NEK10]] | -0.53 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[MIR31HG]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises HAUS4's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without PBK | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.2, -50.4); signed map (-45.1, -36.7). **Vector** length 54.7, 7.54% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,946,228-22,957,161 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20424; previously C14orf94 |
| Gene groups (HGNC) | HAUS augmin like complex ; MicroRNA protein coding host genes |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6D7](https://www.uniprot.org/uniprotkb/Q9H6D7) (HAUS augmin-like complex subunit 4):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [54930](https://www.ncbi.nlm.nih.gov/gene/54930):

> This gene encodes a subunit of the centrosome complex termed the human augmin complex. The encoded protein localizes to the spindle microtubules and may play a role in mitotic spindle assembly and maintenance of centrosome integrity during cell division. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 1. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20163) · Entrez [54930](https://www.ncbi.nlm.nih.gov/gene/54930) · UniProt [Q9H6D7](https://www.uniprot.org/uniprotkb/Q9H6D7) · Ensembl [ENSG00000092036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092036)

## Data

Gene col 1685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1685); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1685]; `tensor/DDL_lfc|DDL_z.npy` [1685]; `embed/gene_vectors.npy` [1685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1685 or target_col == 1685). Every well: [[HAUS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
