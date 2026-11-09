---
symbol: "SEPTIN3"
type: "gene"
col: 1884
ensembl_id: "ENSG00000100167"
name: "septin 3"
location: "22q13.2"
module: 176
arm: "+"
pooled_cpm: 3.93
n_lines_expressing: 37
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 22
direction_downstream: 30
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# SEPTIN3

*septin 3* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.43× (z +11.8, q 2e-29, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.413× (z -8.5, q 1e-14, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIF1L]] (+0.74, fdr 7e-06), [[RAB6B]] (+0.68, fdr 1e-05), [[ADAM22]] (+0.67, fdr 7e-06); moves opposite to [[GPATCH2]] (-0.52, fdr 1e-04), [[BMS1P4-1]] (-0.51, fdr 2e-04), [[COMMD1]] (-0.49, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[APLP1]] → it (grade B ⚠); 30 go from it, the strongest it → [[EMID1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +11.8 | 2e-29 | 25/33 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.40×** | +11.7 | 2e-29 | 25/32 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.33×** | +11.5 | 4e-28 | 23/31 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +11.2 | 7e-27 | 2/3 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.03×** | +10.6 | 3e-24 | 22/32 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.4 | 4e-19 | 11/17 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.53×** | +8.9 | 4e-17 | 23/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.43×** | +8.5 | 1e-15 | 22/29 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +8.1 | 4e-14 | 3/5 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.28×** | +6.0 | 1e-07 | 13/30 (PANC-1, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.50×** | +5.5 | 2e-06 | 8/32 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.64×** | +4.7 | 1e-04 | 9/32 (SW480, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.7 | 1e-04 | 13/28 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +3.4 | 0.026 | 9/26 (A549, A498, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.39×** | +3.2 | 0.059 | 5/30 (SHP-77, C-33 A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.413×** | -8.5 | 1e-14 | 20/31 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -7.1 | 4e-10 | 21/33 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.484×** | -6.9 | 7e-10 | 15/22 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.498×** | -6.4 | 2e-08 | 19/31 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -5.7 | 2e-06 | 18/26 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -5.4 | 7e-06 | 18/32 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.617×** | -4.6 | 3e-04 | 14/31 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 4e-04 | 15/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.629×** | -4.4 | 6e-04 | 11/33 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.721×** | -4.4 | 6e-04 | 12/28 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -3.7 | 0.011 | 13/31 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -3.5 | 0.021 | 11/31 (LoVo, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -3.1 | 0.068 | 11/25 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 5 µM |  | **0.792×** | -3.1 | 0.068 | 3/32 (SHP-77, NCI-H661, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.712×** | -3.1 | 0.081 | 11/29 (AN3 CA, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.68 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0868× (z -10.7) |
| [[C32 (line)]] | wt | 5.23 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0561× (z -8.7) |
| [[A-172 (line)]] | wt | 7.77 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0963× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.83 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 7.95 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0848× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 1.96 | 0 | 1 | — | [[Vemurafenib (drug)]] 0.5 µM 0.152× (z -373.0) |
| [[A498 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIF1L]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[RAB6B]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[VASH1]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GNAO1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[DPYSL5]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ADCY1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; STRING 989 |
| [[ASIC1]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.61 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[GNAZ]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2]] | -0.52 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[BMS1P4-1]] | -0.51 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[COMMD1]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[CCAR1]] | -0.48 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[AMY2B]] | -0.48 | -0.35 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 18, C 4. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises SEPTIN3's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without APLP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[RET]] | B | RET activity raises SEPTIN3's level | lines that do not express RET (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without RET | 0.012 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[SEMA6B]] | B | SEMA6B activity raises SEPTIN3's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.20× lower at baseline in the lines without SEMA6B | 0.019 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[KIF1A]] | B | KIF1A activity raises SEPTIN3's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without KIF1A | 0.023 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[PAX2]] | B | PAX2 activity raises SEPTIN3's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without PAX2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[ARHGAP44]] | B | ARHGAP44 activity raises SEPTIN3's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without ARHGAP44 | 0.039 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises SEPTIN3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 2.31× lower at baseline in the lines without JAG2 | 0.041 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[CELSR2]] | B | CELSR2 activity raises SEPTIN3's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without CELSR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises SEPTIN3's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without RIMS3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises SEPTIN3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.68× lower at baseline in the lines without BRSK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises SEPTIN3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without GNAZ | 0.060 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[NPTXR]] | B | NPTXR activity raises SEPTIN3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without NPTXR | 0.060 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 26, C 4. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMID1]] | B | SEPTIN3 activity raises EMID1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without SEPTIN3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[CCAR1]] | B | SEPTIN3 activity raises CCAR1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without SEPTIN3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[ADGRL1]] | B | SEPTIN3 activity raises ADGRL1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without SEPTIN3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[ZNF483]] | B | SEPTIN3 activity raises ZNF483's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.68× lower at baseline in the lines without SEPTIN3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[MCF2L2]] | B | SEPTIN3 activity raises MCF2L2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without SEPTIN3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[LINC00937]] | B | SEPTIN3 activity raises LINC00937's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without SEPTIN3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[AIF1L]] | B | SEPTIN3 activity raises AIF1L's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without SEPTIN3 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[BRSK2]] | B | SEPTIN3 activity raises BRSK2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without SEPTIN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[GJA3]] | B | SEPTIN3 activity raises GJA3's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without SEPTIN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[HAGLR]] | B | SEPTIN3 activity raises HAGLR's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without SEPTIN3 | 0.045 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[SEMA6B]] | B | SEPTIN3 activity raises SEMA6B's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without SEPTIN3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[SHANK3]] | B | SEPTIN3 activity raises SHANK3's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without SEPTIN3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.1, 40.0); signed map (26.3, 27.6). **Vector** length 57.4, 10.4% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.4 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | septin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,969,443-41,998,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SEP3, SEPT3 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH03](https://www.uniprot.org/uniprotkb/Q9UH03) (Neuronal-specific septin-3):

> Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential).

**Summary**, from NCBI Gene [55964](https://www.ncbi.nlm.nih.gov/gene/55964):

> This gene belongs to the septin family of GTPases. Members of this family are required for cytokinesis. Expression is upregulated by retinoic acid in a human teratocarcinoma cell line. The specific function of this gene has not been determined. Alternative splicing of this gene results in several transcript variants encoding different isoforms. [provided by RefSeq, May 2018]

**Accessions** — [HGNC:10750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10750) · Entrez [55964](https://www.ncbi.nlm.nih.gov/gene/55964) · UniProt [Q9UH03](https://www.uniprot.org/uniprotkb/Q9UH03) · Ensembl [ENSG00000100167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100167)

## Data

Gene col 1884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1884); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1884]; `tensor/DDL_lfc|DDL_z.npy` [1884]; `embed/gene_vectors.npy` [1884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1884 or target_col == 1884). Every well: [[SEPTIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
