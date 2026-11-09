---
symbol: "CSRNP3"
type: "gene"
col: 10944
ensembl_id: "ENSG00000178662"
name: "cysteine and serine rich nuclear protein 3"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 5.88
n_lines_expressing: 26
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CSRNP3

*cysteine and serine rich nuclear protein 3* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.95× (z +9.6, q 6e-19, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.76× (z +7.3, q 5e-11, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -6.1, q 5e-07, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH12]] (+0.71, fdr 7e-06), [[RUNX1T1]] (+0.70, fdr 1e-05), [[RMST]] (+0.69, fdr 7e-06); moves opposite to [[WNT9A]] (-0.50, fdr 4e-05), [[LINC01128]] (-0.48, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 12 go from it, the strongest it → [[LRRIQ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.6 | 6e-19 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +7.3 | 5e-11 | 15/23 (A-172, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.3 | 5e-11 | 2/21 (HEC-1-A, NCI-H1792) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +6.9 | 6e-10 | 10/23 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.2 | 8e-08 | 1/15 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.6 | 2e-06 | 1/10 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.3 | 0.002 | 13/23 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.002 | 6/21 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.58×** | +4.2 | 0.002 | 10/23 (A498, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.002 | 11/22 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.004 | 9/22 (SW480, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.004 | 8/22 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.005 | 15/23 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.021 | 9/23 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.43×** | +3.3 | 0.034 | 8/22 (A498, A-172, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +3.0 | 0.081 | 8/22 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.083 | 4/23 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.095 | 7/23 (SW480, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -6.1 | 5e-07 | 14/23 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.641×** | -4.1 | 0.013 | 10/23 (A-427, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.648×** | -4.0 | 0.014 | 16/23 (SW 900, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -3.9 | 0.015 | 15/23 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.019 | 9/23 (SW 900, NCI-H23, …) | top dose only |  |
| [[Malotilate (drug)]] 5 µM |  | **0.694×** | -3.3 | 0.061 | 3/23 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -3.3 | 0.061 | 9/23 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.772×** | -3.3 | 0.061 | 8/23 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.700×** | -3.3 | 0.070 | 5/23 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.713× | -3.1 | 0.11 | 12/22 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.714× | -3.1 | 0.11 | 11/23 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 57.2 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0998× (z -12.8) |
| [[SW480 (line)]] | alt | 9.64 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0250× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0407× (z -16.1) |
| [[H4 (line)]] | wt | 14.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0691× (z -8.9) |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.208× (z -9.2) |
| [[A-172 (line)]] | wt | 2.83 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +9.3) | — |
| [[A498 (line)]] | wt | 14.4 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 6.15× (z +9.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.9) |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0465× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 8.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0658× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH12]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[RMST]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BMP5]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CRISPLD1]] | +0.66 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[BCHE]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CDH10]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYT4]] | +0.61 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MIR2052HG]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[KCNB2]] | +0.60 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT9A]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CSRNP3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[AGMO]] | B | AGMO activity raises CSRNP3's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without AGMO | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[ADGRL3]] | B | ADGRL3 activity raises CSRNP3's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without ADGRL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[BCHE]] | C | BCHE activity raises CSRNP3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.49× lower at baseline in the lines without BCHE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises CSRNP3's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.40× lower at baseline in the lines without SRRM4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises CSRNP3's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.42× lower at baseline in the lines without GABRG2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CSRNP3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.48× lower at baseline in the lines without KCNH5 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises CSRNP3's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.54× lower at baseline in the lines without RUNX1T1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises CSRNP3's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without CDH18 | 0.076 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises CSRNP3's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.17× lower at baseline in the lines without SNTG1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises CSRNP3's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without LINC02197 | 0.087 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises CSRNP3's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without JAKMIP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRIQ1]] | B | CSRNP3 activity raises LRRIQ1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without CSRNP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[NCAM2]] | B | CSRNP3 activity raises NCAM2's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.71× lower at baseline in the lines without CSRNP3 | 0.024 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[PLCB1]] | B | CSRNP3 activity raises PLCB1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CSRNP3 | 0.032 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[PKHD1]] | B | CSRNP3 activity raises PKHD1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without CSRNP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[MID1]] | B | CSRNP3 activity raises MID1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CSRNP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[SYT1]] | B | CSRNP3 activity raises SYT1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without CSRNP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[LINC01876]] | C | CSRNP3 activity raises LINC01876's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 3.20× lower at baseline in the lines without CSRNP3 | 0.005 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[MAP2K6]] | C | CSRNP3 activity raises MAP2K6's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.99× lower at baseline in the lines without CSRNP3 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[MARCHF1]] | C | CSRNP3 activity raises MARCHF1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without CSRNP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[BCHE]] | C | CSRNP3 activity raises BCHE's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without CSRNP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[EPHA3]] | C | CSRNP3 activity raises EPHA3's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.35× lower at baseline in the lines without CSRNP3 | 0.056 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |
| [[PEX5L]] | C | CSRNP3 activity raises PEX5L's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without CSRNP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.3, 37.5); signed map (46.1, 34.8). **Vector** length 49.1, 9.93% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and serine rich nuclear protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:165,469,647-165,689,407 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32093, TAIP-2, PPP1R73; previously FAM130A2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYN3](https://www.uniprot.org/uniprotkb/Q8WYN3) (Cysteine/serine-rich nuclear protein 3):

> Binds to the consensus sequence 5'-AGAGTG-3' and has transcriptional activator activity. Plays a role in apoptosis (By similarity).

**Summary**, from NCBI Gene [80034](https://www.ncbi.nlm.nih.gov/gene/80034):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and sequence-specific DNA binding activity. Predicted to be involved in positive regulation of apoptotic process and positive regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30729) · Entrez [80034](https://www.ncbi.nlm.nih.gov/gene/80034) · UniProt [Q8WYN3](https://www.uniprot.org/uniprotkb/Q8WYN3) · Ensembl [ENSG00000178662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178662)

## Data

Gene col 10944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10944); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10944]; `tensor/DDL_lfc|DDL_z.npy` [10944]; `embed/gene_vectors.npy` [10944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10944 or target_col == 10944). Every well: [[CSRNP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRNP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
