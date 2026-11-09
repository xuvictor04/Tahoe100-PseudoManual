---
symbol: "EFNA2"
type: "gene"
col: 1804
ensembl_id: "ENSG00000099617"
name: "ephrin A2"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# EFNA2

*ephrin A2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.23× (z +14.7, q 0e+00, up in 20 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (A-172 0.155×, HT-29 0.145×, MIA PaCa-2 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.157×); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.172×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELAVL3]] (+0.73, fdr 7e-06), [[PRX]] (+0.69, fdr 7e-06), [[IRX5]] (+0.67, fdr 7e-06); moves opposite to [[RPE]] (-0.61, fdr 1e-05), [[LANCL1]] (-0.59, fdr 1e-05), [[AP3M1]] (-0.55, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDGFA]] → it (grade B ⚠); 7 go from it, the strongest it → [[ADRA2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.23×** | +14.7 | 0e+00 | 20/33 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.4 | 6e-23 | 24/31 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.0 | 4e-10 | 5/8 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +6.4 | 3e-08 | 17/34 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +6.1 | 2e-07 | 15/30 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.09×** | +5.3 | 1e-05 | 3/15 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +5.0 | 6e-05 | 5/18 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.86×** | +4.2 | 0.002 | 6/19 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.72×** | +3.6 | 0.020 | 1/11 (A498) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.022 | 7/36 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.027 | 9/33 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.35× | +3.0 | 0.12 | 7/37 (LS 180, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (A-172 0.155×, HT-29 0.145×, MIA PaCa-2 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.157×); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.172×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.157× (z -9.1) |
| [[C32 (line)]] | wt | 3.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.3× (z +11.1) | — |
| [[A498 (line)]] | wt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 1.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +11.2) | — |
| [[SW480 (line)]] | alt | 6.22 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.36× (z +8.8) | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAVL3]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PRX]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[IRX5]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CCNP]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[EPHA1-AS1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[ZBTB7A]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[CATSPERD]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[TGIF2-RAB5IF]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PDE4C]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[AP3M1]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[TMTC3]] | -0.52 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[EIF2B1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFA]] | B | PDGFA activity raises EFNA2's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without PDGFA | 0.033 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA2C]] | B | EFNA2 activity raises ADRA2C's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without EFNA2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[SPSB2]] | B | EFNA2 activity raises SPSB2's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without EFNA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[KCNQ4]] | B | EFNA2 activity raises KCNQ4's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without EFNA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[MFSD2B]] | B | EFNA2 activity raises MFSD2B's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without EFNA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[AZU1]] | B | EFNA2 activity raises AZU1's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without EFNA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[RELA-DT]] | B | EFNA2 activity raises RELA-DT's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without EFNA2 | 0.090 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[MMP25]] | B | EFNA2 activity raises MMP25's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without EFNA2 | 0.097 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, -15.9); signed map (17.6, 14.3). **Vector** length 62.4, 11.3% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ephrin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,285,873-1,301,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ELF-1, LERK6; previously EPLG6 |
| Gene groups (HGNC) | Ephrins |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43921](https://www.uniprot.org/uniprotkb/O43921) (Ephrin-A2):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as …

**Summary**, from NCBI Gene [1943](https://www.ncbi.nlm.nih.gov/gene/1943):

> This gene encodes a member of the ephrin family. The protein is composed of a signal sequence, a receptor-binding region, a spacer region, and a hydrophobic region. The EPH and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the …

**Accessions** — [HGNC:3222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3222) · Entrez [1943](https://www.ncbi.nlm.nih.gov/gene/1943) · UniProt [O43921](https://www.uniprot.org/uniprotkb/O43921) · Ensembl [ENSG00000099617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099617)

## Data

Gene col 1804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1804); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1804]; `tensor/DDL_lfc|DDL_z.npy` [1804]; `embed/gene_vectors.npy` [1804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1804 or target_col == 1804). Every well: [[EFNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
