---
symbol: "KCP"
type: "gene"
col: 5672
ensembl_id: "ENSG00000135253"
name: "kielin cysteine rich BMP regulator"
location: "7q32.1"
module: 125
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# KCP

*kielin cysteine rich BMP regulator* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.53× (z +11.1, q 8e-26, up in 4 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +10.9, q 2e-25, up in 14 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.609× (z -4.7, q 0.001, down in 15 of 36 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.227×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.230×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.120×; ⚠ cell-cycle shift, explains ~33% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC39A]] (+0.69, fdr 7e-06), [[FER1L6]] (+0.64, fdr 1e-05), [[CELF6]] (+0.64, fdr 9e-06); moves opposite to [[ACTL6A]] (-0.54, fdr 2e-05), [[CNOT10]] (-0.53, fdr 3e-05), [[NCAPD3]] (-0.51, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[UNC13D]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +11.1 | 8e-26 | 4/10 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +10.9 | 2e-25 | 14/29 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +10.0 | 3e-21 | 3/6 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +8.1 | 6e-14 | 3/12 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +7.7 | 2e-12 | 14/32 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +7.4 | 2e-11 | 15/35 (SW480, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +5.1 | 3e-05 | 18/39 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.4 | 6e-04 | 11/39 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +4.3 | 9e-04 | 12/39 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.8 | 0.007 | 1/21 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.009 | 8/28 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.47×** | +3.7 | 0.012 | 5/39 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.016 | 9/37 (HEC-1-A, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.4 | 0.023 | 2/15 (KATO III, AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.023 | 4/30 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.023 | 2/28 (SW1417, MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.031 | 1/34 (HOP62) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.035 | 5/34 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.050 | 9/33 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5672.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.227×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.230×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.120×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.609×** | -4.7 | 0.001 | 15/36 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.660×** | -4.0 | 0.022 | 16/41 (AsPC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.503× | -3.4 | 0.12 | 5/25 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.701× | -3.3 | 0.15 | 6/39 (J82, C32, …) | top dose only |  |
| [[Ivabradine (hydrochloride) (drug)]] 0.5 µM | ⚠ transcription drop; unreliable plate only | 0.714× | -3.2 | 0.15 | 4/30 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 8.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.30 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.67× (z +9.6) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC39A]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[FER1L6]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CELF6]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[MIR4300HG]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SPINK1]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD30B]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LINC00520]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MYO16]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[FAM149A]] | +0.60 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LY96]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CLIC2]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CNOT10]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NCAPD3]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC13D]] | B | UNC13D activity raises KCP's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without UNC13D | 0.033 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises KCP's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without PLEKHG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[MIR4307HG]] | B | MIR4307HG activity raises KCP's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.48× lower at baseline in the lines without MIR4307HG | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | KCP activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCP (5) vs lines expressing it (43) | the lines without KCP: 0.65× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: RILP, EPB41L1; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 5 µM | C | KCP activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express KCP (5) vs lines expressing it (43) | the lines without KCP: 0.65× the cells of the other lines | 0.094 | ⚠ tissue-confounded; across organs; also absent: RILP, EPB41L1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.3, 23.8); signed map (36.9, 22.6). **Vector** length 57.6, 9.06% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | kielin cysteine rich BMP regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,862,042-128,910,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33365, NET67; previously CRIM2 |
| Gene groups (HGNC) | Cysteine rich transmembrane BMP regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWJ8](https://www.uniprot.org/uniprotkb/Q6ZWJ8) (Kielin/chordin-like protein):

> Enhances bone morphogenetic protein (BMP) signaling in a paracrine manner. In contrast, it inhibits both the activin-A and TGFB1-mediated signaling pathways (By similarity).

**Summary**, from NCBI Gene [375616](https://www.ncbi.nlm.nih.gov/gene/375616):

> Predicted to be involved in positive regulation of BMP signaling pathway. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be located in obsolete extracellular space. Predicted to be active in extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17585) · Entrez [375616](https://www.ncbi.nlm.nih.gov/gene/375616) · UniProt [Q6ZWJ8](https://www.uniprot.org/uniprotkb/Q6ZWJ8) · Ensembl [ENSG00000135253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135253)

## Data

Gene col 5672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5672); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5672]; `tensor/DDL_lfc|DDL_z.npy` [5672]; `embed/gene_vectors.npy` [5672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5672 or target_col == 5672). Every well: [[KCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
