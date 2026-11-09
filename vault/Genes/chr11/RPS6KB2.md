---
symbol: "RPS6KB2"
type: "gene"
col: 10634
ensembl_id: "ENSG00000175634"
name: "ribosomal protein S6 kinase B2"
location: "11q13.2"
module: 2
arm: "+"
pooled_cpm: 11.4
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RPS6KB2

*ribosomal protein S6 kinase B2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +11.7, q 5e-29, up in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +10.2, q 2e-22, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.784× (z -4.3, q 0.010, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM3A]] (+0.71, fdr 7e-06), [[RHOT2]] (+0.67, fdr 1e-05), [[MIB2]] (+0.62, fdr 1e-05); moves opposite to [[HSPD1]] (-0.55, fdr 1e-05), [[CCT4]] (-0.52, fdr 3e-05), [[LDHB]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[POTEE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.94×** | +11.7 | 5e-29 | 37/43 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.34×** | +10.6 | 6e-24 | 38/47 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.2 | 2e-22 | 38/44 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.12×** | +9.4 | 1e-18 | 41/47 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.11×** | +9.3 | 1e-18 | 30/35 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.07×** | +8.8 | 2e-16 | 15/21 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.87×** | +7.8 | 5e-13 | 33/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.86×** | +7.2 | 5e-11 | 20/28 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +6.8 | 6e-10 | 30/46 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.8 | 6e-10 | 25/43 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.72×** | +6.8 | 6e-10 | 26/41 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.72×** | +6.8 | 6e-10 | 29/47 (PANC-1, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.71×** | +6.7 | 7e-10 | 31/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.0 | 6e-08 | 26/37 (NCI-H1573, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +4.4 | 5e-04 | 18/45 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.015 | 13/46 (NCI-H23, HCT15, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.018 | 8/40 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.069 | 12/47 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -4.3 | 0.010 | 18/48 (CHP-212, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.727× | -3.3 | 0.26 | 11/45 (SNU-423, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 12.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3A]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RHOT2]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[MIB2]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[EDC4]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DGAT1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[NEURL4]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SLC2A8]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NOC4L]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RCE1]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[DMWD]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FXR2]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GSK3A]] | +0.54 | +0.47 / +0.61 | both halves | 2e-05 | pathway: Constitutive Signaling by AKT1 E17K in Cancer |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPD1]] | -0.55 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[CCT4]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[LDHB]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MREG]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TUSC3]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[MTMR8]] | -0.46 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[TXN]] | -0.46 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[GLO1]] | -0.45 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[HSP90AA1]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 | STRING 706 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POTEE]] | B | POTEE activity strengthens RPS6KB2's drug response | lines that do not express POTEE (29) vs lines expressing it (19) | the lines without POTEE respond 0.80× as strongly (z diff +0.97); strongest at Dinaciclib 5 µM: 1.60x vs 2.81x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.414). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.8, -25.3); signed map (-26.2, 1.3). **Vector** length 57.1, 9.57% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | +2.5 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +2.3 | +9.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.2 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,428,460-67,435,401 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p70S6Kb, P70-BETA, STK14B, KLS, S6KB, S6Kbeta, S6Kβ |
| Gene groups (HGNC) | Ribosomal protein S6 kinase family |
| Reactome | 6 pathways, smallest: AKT phosphorylates targets in the nucleus; Constitutive Signaling by AKT1 E17K in Cancer; PI3K/AKT Signaling in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS0](https://www.uniprot.org/uniprotkb/Q9UBS0) (Ribosomal protein S6 kinase beta-2):

> Phosphorylates specifically ribosomal protein S6. Seems to act downstream of mTOR signaling in response to growth factors and nutrients to promote cell proliferation, cell growth and cell cycle progression in an alternative pathway regulated by MEAK7.

**Summary**, from NCBI Gene [6199](https://www.ncbi.nlm.nih.gov/gene/6199):

> This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains a kinase catalytic domain and phosphorylates the S6 ribosomal protein and eukaryotic translation initiation factor 4B (eIF4B). Phosphorylation of S6 leads to an increase in protein synthesis and cell proliferation. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:10437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10437) · Entrez [6199](https://www.ncbi.nlm.nih.gov/gene/6199) · UniProt [Q9UBS0](https://www.uniprot.org/uniprotkb/Q9UBS0) · Ensembl [ENSG00000175634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175634)

## Data

Gene col 10634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10634); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10634]; `tensor/DDL_lfc|DDL_z.npy` [10634]; `embed/gene_vectors.npy` [10634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10634 or target_col == 10634). Every well: [[RPS6KB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
