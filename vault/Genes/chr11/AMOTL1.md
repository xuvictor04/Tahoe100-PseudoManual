---
symbol: "AMOTL1"
type: "gene"
col: 9227
ensembl_id: "ENSG00000166025"
name: "angiomotin like 1"
location: "11q21"
module: 151
arm: "+"
pooled_cpm: 56.08
n_lines_expressing: 34
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 23
direction_downstream: 18
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# AMOTL1

*angiomotin like 1* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +5.3, q 6e-05, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.510× (z -12.6, q 2e-33, down in 25 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02454]] (+0.64, fdr 7e-06), [[SCHIP1]] (+0.63, fdr 7e-06), [[NES]] (+0.63, fdr 9e-06); moves opposite to [[TRPM7]] (-0.55, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[UBASH3B]] → it (grade B ⚠); 18 go from it, the strongest it → [[DCBLD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 6e-05 | 19/32 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 0.003 | 21/33 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.005 | 17/32 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.059 | 15/31 (NCI-H2347, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Busulfan (drug)]] 0.05 µM |  | 1.27× | +3.2 | 0.18 | 13/33 (Hs 766T, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.510×** | -12.6 | 2e-33 | 25/32 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.0 | 4e-07 | 25/33 (CHP-212, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.650×** | -5.5 | 6e-06 | 24/32 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -5.1 | 4e-05 | 15/29 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -4.9 | 1e-04 | 20/31 (SW 1271, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -4.8 | 2e-04 | 21/31 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.697×** | -4.6 | 4e-04 | 17/32 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.752×** | -4.4 | 7e-04 | 15/33 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -4.4 | 7e-04 | 17/32 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -4.4 | 7e-04 | 16/32 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.002 | 15/32 (C32, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.007 | 17/33 (SK-MEL-2, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.008 | 15/32 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.760×** | -3.7 | 0.010 | 15/32 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.013 | 18/33 (Panc 03.27, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.035 | 16/32 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.785×** | -3.2 | 0.042 | 15/32 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.061 | 15/32 (SK-MEL-2, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 159 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0320× (z -33.8) |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -20.3) |
| [[C32 (line)]] | wt | 92.2 | 1 (1 ⚠) | 9 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.48× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (drug)]] 5 µM 0.223× (z -11.9) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.232× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 69.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -31.4) |
| [[HOP62 (line)]] | alt | 57.5 | 0 | 6 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.581× (z -14.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.353× (z -8.8) |
| [[CHP-212 (line)]] | wt | 283 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 74.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.5) |
| [[Hs 766T (line)]] | wt | 378 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.3) |
| [[J82 (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.4) |
| [[A549 (line)]] | wt | 57.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 38.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.96× (z +10.0) | — |
| [[H4 (line)]] | wt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 95.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.0) |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.6) |
| [[A-172 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02454]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[NES]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[ELK3]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NT5E]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[RGS4]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PKIA]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DNMBP]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SHC4]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPM7]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 12, C 11. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBASH3B]] | B | UBASH3B activity raises AMOTL1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without UBASH3B | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[SERPIND1]] | B | SERPIND1 activity raises AMOTL1's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without SERPIND1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[MAST4]] | B | MAST4 activity raises AMOTL1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without MAST4 | 0.022 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[COL13A1]] | B | COL13A1 activity raises AMOTL1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 4.02× lower at baseline in the lines without COL13A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AMOTL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers AMOTL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPAT3]] | B | GPAT3 activity lowers AMOTL1's level | lines that do not express GPAT3 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without GPAT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: HLA-H, ABCA5, ISG20; maybe low, not absent; its own permutation p |
| [[CDH4]] | B | CDH4 activity raises AMOTL1's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without CDH4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT |
| [[LNCOG]] | B | LNCOG activity raises AMOTL1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.69× lower at baseline in the lines without LNCOG | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[DPF3]] | B | DPF3 activity raises AMOTL1's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without DPF3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[PTPRE]] | B | PTPRE activity raises AMOTL1's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without PTPRE | 0.082 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[LINC02454]] | B | LINC02454 activity raises AMOTL1's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 3.97× lower at baseline in the lines without LINC02454 | 0.089 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCBLD2]] | B | AMOTL1 activity raises DCBLD2's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without AMOTL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[UBASH3B]] | B | AMOTL1 activity raises UBASH3B's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without AMOTL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[ADAM19]] | B | AMOTL1 activity raises ADAM19's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without AMOTL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[FXYD5]] | B | AMOTL1 activity raises FXYD5's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without AMOTL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[PTPRE]] | B | AMOTL1 activity raises PTPRE's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.37× lower at baseline in the lines without AMOTL1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[CDCP1]] | B | AMOTL1 activity raises CDCP1's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.21× lower at baseline in the lines without AMOTL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[CDK17]] | B | AMOTL1 activity raises CDK17's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without AMOTL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[DUSP5]] | B | AMOTL1 activity raises DUSP5's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without AMOTL1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[SLC35F3]] | B | AMOTL1 activity raises SLC35F3's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without AMOTL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[FAM3C2P]] | B | AMOTL1 activity raises FAM3C2P's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without AMOTL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[CDYL2]] | B | AMOTL1 activity raises CDYL2's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without AMOTL1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[COL13A1]] | B | AMOTL1 activity raises COL13A1's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 3.26× lower at baseline in the lines without AMOTL1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.4, 7.5); signed map (5.7, 48.5). **Vector** length 105, 29.5% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.4 | +1.2 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | angiomotin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,706,431-94,876,748 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JEAP |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY63](https://www.uniprot.org/uniprotkb/Q8IY63) (Angiomotin-like protein 1):

> Inhibits the Wnt/beta-catenin signaling pathway, probably by recruiting CTNNB1 to recycling endosomes and hence preventing its translocation to the nucleus.

**Summary**, from NCBI Gene [154810](https://www.ncbi.nlm.nih.gov/gene/154810):

> The protein encoded by this gene is a peripheral membrane protein that is a component of tight junctions or TJs. TJs form an apical junctional structure and act to control paracellular permeability and maintain cell polarity. This protein is related to angiomotin, an angiostatin binding protein that regulates endothelial cell migration and capillary formation. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:17811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17811) · Entrez [154810](https://www.ncbi.nlm.nih.gov/gene/154810) · UniProt [Q8IY63](https://www.uniprot.org/uniprotkb/Q8IY63) · Ensembl [ENSG00000166025](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166025)

## Data

Gene col 9227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9227); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9227]; `tensor/DDL_lfc|DDL_z.npy` [9227]; `embed/gene_vectors.npy` [9227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9227 or target_col == 9227). Every well: [[AMOTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMOTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
