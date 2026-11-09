---
symbol: "CLEC11A"
type: "gene"
col: 2608
ensembl_id: "ENSG00000105472"
name: "C-type lectin domain containing 11A"
location: "19q13.33"
module: 3
arm: "+"
pooled_cpm: 6.89
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CLEC11A

*C-type lectin domain containing 11A* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.23× (z +9.1, q 4e-17, up in 6 of 6 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 1.73× (z +3.5, q 0.041, up in 6 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.526× (z -3.9, q 0.041, down in 6 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JARID2]] (+0.59, fdr 1e-05), [[IGFBP2]] (+0.59, fdr 2e-05), [[AP2S1]] (+0.57, fdr 1e-05); moves opposite to [[RNF6]] (-0.57, fdr 2e-05), [[CLIP1]] (-0.56, fdr 3e-05), [[ZXDB]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PDGFRB]] → it (grade B ⚠); 4 go from it, the strongest it → [[MHENCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.23×** | +9.1 | 4e-17 | 6/6 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.46×** | +8.2 | 1e-13 | 11/13 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +5.4 | 1e-05 | 4/16 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.99×** | +4.5 | 8e-04 | 13/24 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.89×** | +4.2 | 0.003 | 6/20 (NCI-H460, HEC-1-A, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.74×** | +3.7 | 0.023 | 5/17 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.041 | 6/22 (A-172, SW1417, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +3.4 | 0.051 | 0/7 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.526×** | -3.9 | 0.041 | 6/24 (SW480, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.537×** | -3.8 | 0.041 | 6/25 (AN3 CA, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.547×** | -3.7 | 0.041 | 7/25 (HOP62, SW480, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.041 | 14/22 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.371×** | -3.4 | 0.074 | 10/22 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.0) |
| [[RKO (line)]] | wt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 68.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.4) |
| [[SW480 (line)]] | alt | 5.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.8) |
| [[A-172 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JARID2]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[IGFBP2]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[AP2S1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 | STRING 538 |
| [[METRN]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RNF24]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SERPINE1]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[MHENCR]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SH3GL1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.53 | +0.56 / +0.54 | both halves | 1e-05 | ⚠ same locus (3.6 kb: neighbours can correlate without regulation) |
| [[B3GAT3]] | +0.52 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[NFYA]] | +0.52 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[C1QL1]] | +0.52 | +0.38 / +0.54 | both halves | 6e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CLIP1]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[IDE]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZXDA]] | -0.50 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[HTATIP2]] | -0.49 | -0.55 / -0.24 | both halves | 4e-04 |  |
| [[GCLM]] | -0.48 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[LURAP1L-AS1]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[DCTN2]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[AIFM2]] | -0.47 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[BCL2L13]] | -0.47 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[ZFR]] | -0.47 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRB]] | B | PDGFRB activity raises CLEC11A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without PDGFRB | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[DIRAS3]] | B | DIRAS3 activity raises CLEC11A's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without DIRAS3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[SHANK1]] | B | SHANK1 activity weakens CLEC11A's drug response | lines that do not express SHANK1 (6) vs lines expressing it (19) | the lines without SHANK1 respond 1.26× as strongly (z diff -0.20); rises at some drug-doses, falls at others (70% from rises): Topotecan (hydrochloride) 5 µM: 2.65x vs 0.97x (z diff -3.2); Panobinostat 0.5 µM: 2.96x vs 1.43x (z diff -2.4); Rutin (trihydrate) 0.05 µM: 0.46x vs 0.77x (z diff -1.5) | 0.054 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[SGIP1]] | B | SGIP1 activity weakens CLEC11A's drug response | lines that do not express SGIP1 (16) vs lines expressing it (9) | the lines without SGIP1 respond 1.18× as strongly (z diff -0.26); rises at some drug-doses, falls at others (51% from rises): Panobinostat 0.5 µM: 2.18x vs 1.07x (z diff -2.5); Topotecan (hydrochloride) 5 µM: 1.64x vs 0.88x (z diff -2.3); Rutin (trihydrate) 0.05 µM: 0.59x vs 0.89x (z diff -1.3) | 0.090 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[SHANK1]] | C | SHANK1 activity raises CLEC11A's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.91× lower at baseline in the lines without SHANK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MHENCR]] | B | CLEC11A activity raises MHENCR's level | lines that do not express CLEC11A (21) vs lines expressing it (29) | 1.34× lower at baseline in the lines without CLEC11A | 0.044 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | B | CLEC11A activity lowers the cells' numbers under Vinblastine (sulfate) 0.5 µM (makes them more sensitive) | lines that do not express CLEC11A (21) vs lines expressing it (27) | the lines without CLEC11A: 1.20× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1 |
| [[PDGFRB]] | B | CLEC11A activity raises PDGFRB's level | lines that do not express CLEC11A (21) vs lines expressing it (29) | 1.77× lower at baseline in the lines without CLEC11A | 0.079 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1 |
| [[SHANK1]] | C | CLEC11A activity raises SHANK1's level | lines that do not express CLEC11A (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without CLEC11A | 0.089 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.352). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.1, -8.5); signed map (-38.3, 16.7). **Vector** length 41.5, 8.86% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.9 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +1.4 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +0.7 | +0.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.7 | +0.9 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.7 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | C-type lectin domain containing 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,723,364-50,725,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P47, LSLCL, CLECSF3; previously SCGF |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y240](https://www.uniprot.org/uniprotkb/Q9Y240) (C-type lectin domain family 11 member A):

> Promotes osteogenesis by stimulating the differentiation of mesenchymal progenitors into mature osteoblasts. Important for repair and maintenance of adult bone (By similarity).

**Summary**, from NCBI Gene [6320](https://www.ncbi.nlm.nih.gov/gene/6320):

> This gene encodes a member of the C-type lectin superfamily. The encoded protein is a secreted sulfated glycoprotein and functions as a growth factor for primitive hematopoietic progenitor cells. An alternative splice variant has been described but its biological nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10576) · Entrez [6320](https://www.ncbi.nlm.nih.gov/gene/6320) · UniProt [Q9Y240](https://www.uniprot.org/uniprotkb/Q9Y240) · Ensembl [ENSG00000105472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105472)

## Data

Gene col 2608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2608); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2608]; `tensor/DDL_lfc|DDL_z.npy` [2608]; `embed/gene_vectors.npy` [2608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2608 or target_col == 2608). Every well: [[CLEC11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLEC11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
