---
symbol: "MPG"
type: "gene"
col: 2326
ensembl_id: "ENSG00000103152"
name: "N-methylpurine DNA glycosylase"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 17.38
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MPG

*N-methylpurine DNA glycosylase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.71× (z +5.5, q 3e-05, up in 29 of 44 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.204× (z -22.9, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPT1]] (+0.80, fdr 7e-06), [[MRPL55]] (+0.80, fdr 1e-05), [[LCMT1]] (+0.77, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.75, fdr 2e-05), [[HNRNPL]] (-0.72, fdr 3e-05), [[RIPK2-DT]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FGF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.5 | 3e-05 | 29/44 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 1.40× | +3.4 | 0.19 | 15/38 (A549, A498, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.204×** | -22.9 | 0e+00 | 45/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.284×** | -12.8 | 6e-35 | 45/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.399×** | -9.0 | 6e-17 | 43/47 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -8.4 | 6e-15 | 41/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.237×** | -7.4 | 2e-11 | 43/48 (NCI-H460, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.244×** | -7.2 | 4e-11 | 41/44 (SW480, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -6.6 | 3e-09 | 36/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.534×** | -6.0 | 1e-07 | 30/47 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -5.7 | 9e-07 | 27/47 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -5.4 | 3e-06 | 31/46 (C-33 A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.502×** | -3.5 | 0.020 | 20/46 (NCI-H460, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.020 | 20/47 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.053 | 18/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.059 | 17/47 (A549, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.5) |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.9) |
| [[LoVo (line)]] | wt | 19.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.1) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -14.1) |
| [[A-427 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -10.6) |
| [[A549 (line)]] | wt | 16.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -19.0) |
| [[H4 (line)]] | wt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.7) |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.4) |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -20.4) |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.4) |
| [[J82 (line)]] | alt | 19.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -18.5) |
| [[KATO III (line)]] | alt | 20.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0531× (z -24.5) |
| [[NCI-H460 (line)]] | wt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.3) |
| [[PANC-1 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0310× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.7) |
| [[SW48 (line)]] | wt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.7) |
| [[SW480 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -17.8) |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -10.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.0) |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.8) |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.8) |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0819× (z -20.2) |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 8.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0989× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -20.4) |
| [[NCI-H2347 (line)]] | alt | 9.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -14.8) |
| [[RKO (line)]] | wt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.9) |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -10.6) |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.1) |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -14.7) |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.9) |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPT1]] | +0.80 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.80 | +0.55 / +0.79 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.77 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.77 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[NUDT22]] | +0.76 | +0.49 / +0.83 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC5]] | +0.74 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[HEBP1]] | +0.74 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.74 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[BBLN]] | +0.73 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[QPCTL]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.73 | +0.69 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.75 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[HNRNPL]] | -0.72 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.72 | -0.76 / -0.52 | both halves | 1e-05 |  |
| [[ACADM]] | -0.72 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.72 | -0.39 / -0.80 | both halves | 5e-05 |  |
| [[HNRNPH3]] | -0.72 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | -0.71 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[YWHAE]] | -0.71 | -0.42 / -0.74 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.70 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.70 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[BCLAF1]] | -0.70 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.70 | -0.64 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF2]] | B | FGF2 activity raises MPG's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.17× lower at baseline in the lines without FGF2 | 0.040 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[GUCY1B2]] | B | GUCY1B2 activity lowers MPG's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 1.24× higher at baseline in the lines without GUCY1B2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[PMP22]] | B | PMP22 activity raises MPG's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without PMP22 | 0.085 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[CXCL2]] | B | CXCL2 activity lowers MPG's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.19× higher at baseline in the lines without CXCL2 | 0.091 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.868). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.4, -15.4); signed map (-31.3, 13.5). **Vector** length 75.8, 17.4% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -0.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -22.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.9 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | N-methylpurine DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:77,007-85,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDG |
| Gene groups (HGNC) | DNA glycosylases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 8 pathways, smallest: Displacement of DNA glycosylase by APEX1; Cleavage of the damaged purine; Depurination |
| Matched by | ensembl_id |

**Function**, from UniProt [P29372](https://www.uniprot.org/uniprotkb/P29372) (DNA-3-methyladenine glycosylase):

> Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine, and 7-methylguanine from the damaged DNA polymer formed by alkylation lesions.

**Summary**, from NCBI Gene [4350](https://www.ncbi.nlm.nih.gov/gene/4350):

> Enables DNA binding activity. Predicted to be involved in base-excision repair. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7211) · Entrez [4350](https://www.ncbi.nlm.nih.gov/gene/4350) · UniProt [P29372](https://www.uniprot.org/uniprotkb/P29372) · Ensembl [ENSG00000103152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103152)

## Data

Gene col 2326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2326); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2326]; `tensor/DDL_lfc|DDL_z.npy` [2326]; `embed/gene_vectors.npy` [2326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2326 or target_col == 2326). Every well: [[MPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
