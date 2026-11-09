---
symbol: "PITX1"
type: "gene"
col: 908
ensembl_id: "ENSG00000069011"
name: "paired like homeodomain 1"
location: "5q31.1"
module: 46
arm: "+"
pooled_cpm: 8.43
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PITX1

*paired like homeodomain 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +9.7, q 2e-19, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.472× (z -7.9, q 1e-12, down in 26 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (AsPC-1 0.0658×, KATO III 0.147×, LS 180 0.167×, SW480 0.236×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.0597×, AN3 CA 0.0448×); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.0884×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Belinostat (drug)]] 5 µM in 1 line (AsPC-1 0.239×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD1B]] (+0.55, fdr 2e-05), [[TFAP2A]] (+0.54, fdr 4e-05), [[GATA2-AS1]] (+0.53, fdr 5e-05); moves opposite to [[TLE6]] (-0.43, fdr 2e-04), [[HEMK1]] (-0.42, fdr 4e-04), [[HIF1AN]] (-0.42, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C4BPB]] → it (grade B ⚠); 3 go from it, the strongest it → [[AK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +9.7 | 2e-19 | 24/34 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +6.4 | 5e-08 | 15/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +6.1 | 2e-07 | 17/30 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.60×** | +5.0 | 1e-04 | 14/28 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.56×** | +4.5 | 7e-04 | 6/15 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.006 | 14/36 (J82, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.45×** | +4.0 | 0.006 | 12/31 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.41×** | +3.6 | 0.019 | 11/35 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.5 | 0.032 | 5/36 (HEC-1-A, HCT15, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.049 | 11/37 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | 1.42× | +3.0 | 0.12 | 6/21 (HS-578T, HT-29, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 908.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (AsPC-1 0.0658×, KATO III 0.147×, LS 180 0.167×, SW480 0.236×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.0597×, AN3 CA 0.0448×); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.0884×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Belinostat (drug)]] 5 µM in 1 line (AsPC-1 0.239×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.472×** | -7.9 | 1e-12 | 26/36 (AsPC-1, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.503×** | -7.3 | 1e-10 | 24/37 (AsPC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.559× | -3.2 | 0.23 | 10/37 (SNU-1, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.566× | -3.2 | 0.23 | 3/38 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 35.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0597× (z -17.8) |
| [[A498 (line)]] | wt | 6.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[A549 (line)]] | wt | 3.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0448× (z -9.4) |
| [[COLO 205 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -9.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[KATO III (line)]] | alt | 16.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -10.5) |
| [[LS 180 (line)]] | wt | 22.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 4.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.2) | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -9.5) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.939 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD1B]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TFAP2A]] | +0.54 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[GATA2-AS1]] | +0.53 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[MIER3]] | +0.52 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[ABHD15]] | +0.52 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[SLCO3A1]] | +0.51 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[ZFTA]] | +0.51 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[SMAD1]] | +0.51 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[SLC37A1]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[MYD88]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[FOXC1]] | +0.51 | +0.38 / +0.44 | both halves | 6e-05 | STRING 482 |
| [[SIX1]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 | STRING 477 |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE6]] | -0.43 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[HEMK1]] | -0.42 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[HIF1AN]] | -0.42 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[CFDP1]] | -0.42 | -0.47 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[INTS4]] | -0.41 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[MTG1]] | -0.41 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.41 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[LZTFL1]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[WDR59]] | -0.39 | -0.38 / -0.25 | both halves | 4e-04 |  |
| [[ADSL]] | -0.39 | -0.38 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4BPB]] | B | C4BPB activity raises PITX1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without C4BPB | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[SULF2]] | B | SULF2 activity raises PITX1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.89× lower at baseline in the lines without SULF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[LINC01133]] | B | LINC01133 activity raises PITX1's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without LINC01133 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1 |
| [[DSC2]] | B | DSC2 activity raises PITX1's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without DSC2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[MRAS]] | B | MRAS activity lowers PITX1's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.00× higher at baseline in the lines without MRAS | 0.061 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[MUC17]] | B | MUC17 activity raises PITX1's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.73× lower at baseline in the lines without MUC17 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[HOXA10-AS]] | B | HOXA10-AS activity raises PITX1's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without HOXA10-AS | 0.086 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AK3]] | B | PITX1 activity raises AK3's level | lines that do not express PITX1 (10) vs lines expressing it (40) | 1.62× lower at baseline in the lines without PITX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: MNX1 |
| [[USP6NL]] | B | PITX1 activity raises USP6NL's level | lines that do not express PITX1 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without PITX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: MNX1 |
| [[HEMK1]] | B | PITX1 activity lowers HEMK1's level | lines that do not express PITX1 (10) vs lines expressing it (40) | 1.30× higher at baseline in the lines without PITX1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: MNX1 |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.5, 11.6); signed map (18.1, -10.5). **Vector** length 59.9, 11.7% of its response variance represented; |z| ≥ 3 in 581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.1 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.3 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.3 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | paired like homeodomain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:135,027,734-135,034,813 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTX1, POTX; previously BFT |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78337](https://www.uniprot.org/uniprotkb/P78337) (Pituitary homeobox 1):

> Sequence-specific DNA-binding transcriptional activator of the bicoid class that controls regional morphogenesis and organ-specific gene programs; binds bicoid/TAAT-type elements (consensus TAATCC) via its homeodomain, whose bicoid-class specificity determinant directs target selection, and acts combinatorially by directly contacting partner transcription factors. Specifies hindlimb identity and drives hindlimb outgrowth through direct activation of the hindlimb enhancers of the T-box factor …

**Summary**, from NCBI Gene [5307](https://www.ncbi.nlm.nih.gov/gene/5307):

> This gene encodes a member of the RIEG/PITX homeobox family, which is in the bicoid class of homeodomain proteins. Members of this family are involved in organ development and left-right asymmetry. This protein acts as a transcriptional regulator involved in basal and hormone-regulated activity of prolactin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9004) · Entrez [5307](https://www.ncbi.nlm.nih.gov/gene/5307) · UniProt [P78337](https://www.uniprot.org/uniprotkb/P78337) · Ensembl [ENSG00000069011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069011)

## Data

Gene col 908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 908); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 908]; `tensor/DDL_lfc|DDL_z.npy` [908]; `embed/gene_vectors.npy` [908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 908 or target_col == 908). Every well: [[PITX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
