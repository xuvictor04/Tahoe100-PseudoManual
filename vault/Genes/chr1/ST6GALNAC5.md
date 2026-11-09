---
symbol: "ST6GALNAC5"
type: "gene"
col: 3872
ensembl_id: "ENSG00000117069"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 5"
location: "1p31.1"
module: 8
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 19
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ST6GALNAC5

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 5* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +14.6, q 1e-45, up in 3 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (HEC-1-A 0.0477×, Panc 03.27 0.0994×, SW1417 0.165×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0543×, SW1417 0.142×, Panc 03.27 0.0990×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 0.187×, HEC-1-A 0.214×, NCI-H2347 0.147×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA3]] (+0.61, fdr 1e-05), [[MACC1]] (+0.60, fdr 8e-06), [[SLC44A3]] (+0.60, fdr 1e-05); moves opposite to [[CHD1L]] (-0.47, fdr 3e-05), [[AZIN2]] (-0.43, fdr 2e-04), [[TSHZ3]] (-0.43, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[VGLL3]] → it (grade B ⚠); 24 go from it, the strongest it → [[STS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +14.6 | 1e-45 | 3/15 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +12.0 | 1e-30 | 2/8 (HS-578T, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +11.6 | 1e-28 | 9/17 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +11.2 | 1e-26 | 8/17 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.5 | 9e-24 | 3/10 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.2 | 2e-14 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +7.4 | 1e-11 | 8/16 (C-33 A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +5.5 | 2e-06 | 2/15 (C32, HS-578T) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.6 | 2e-04 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.3 | 0.001 | 2/11 (SK-MEL-2, LS 180) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.005 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.034 | 1/14 (SW480) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.038 | 2/14 (HS-578T, SW 900) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.3 | 0.039 | 1/14 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.049 | 5/16 (SW480, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3872.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (HEC-1-A 0.0477×, Panc 03.27 0.0994×, SW1417 0.165×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0543×, SW1417 0.142×, Panc 03.27 0.0990×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 0.187×, HEC-1-A 0.214×, NCI-H2347 0.147×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.705× | -3.6 | 0.15 | 9/16 (HEC-1-A, CFPAC-1, …) | two highest doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.729× | -3.3 | 0.25 | 2/17 (SW480, SW1417) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.25 | 1/17 (CHP-212) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.25 | 2/17 (COLO 205, SW 900) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.748× | -3.0 | 0.28 | 7/16 (HEC-1-A, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 38.4 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0477× (z -18.7) |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0474× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0990× (z -12.4) |
| [[SW1417 (line)]] | alt | 59.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.2) |
| [[SW480 (line)]] | alt | 7.24 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -9.9) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.187× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 46.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.8) |
| [[A-172 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA3]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[MACC1]] | +0.60 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[SLC44A3]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CCR3]] | +0.60 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[GPR87]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SCN5A]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LASTR]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ARHGEF28]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SYK]] | +0.53 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[RAPGEF5]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[LINC02999]] | +0.52 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[PSORS1C1]] | +0.50 | +0.44 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1L]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[AZIN2]] | -0.43 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[TSHZ3]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[JARID2]] | -0.42 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[RDH11]] | -0.41 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[NHSL1-AS1]] | -0.41 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VGLL3]] | B | VGLL3 activity raises ST6GALNAC5's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 1.66× lower at baseline in the lines without VGLL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[CARD11]] | C | CARD11 activity raises ST6GALNAC5's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.99× lower at baseline in the lines without CARD11 | 0.002 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[WNT7A]] | C | WNT7A activity raises ST6GALNAC5's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 3.32× lower at baseline in the lines without WNT7A | 0.007 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises ST6GALNAC5's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 1.74× lower at baseline in the lines without VWA2 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises ST6GALNAC5's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without SKAP1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises ST6GALNAC5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without ADGRF1 | 0.025 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[SCN5A]] | C | SCN5A activity raises ST6GALNAC5's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without SCN5A | 0.033 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises ST6GALNAC5's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.40× lower at baseline in the lines without ENPP5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises ST6GALNAC5's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without LINC03040 | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[EXPH5]] | C | EXPH5 activity raises ST6GALNAC5's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 1.95× lower at baseline in the lines without EXPH5 | 0.052 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A; co-absent with the target |
| [[CCR3]] | C | CCR3 activity raises ST6GALNAC5's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without CCR3 | 0.063 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises ST6GALNAC5's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without MACC1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 9, C 15. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STS]] | B | ST6GALNAC5 activity raises STS's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without ST6GALNAC5 | 0.019 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[ADGRF4]] | B | ST6GALNAC5 activity raises ADGRF4's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without ST6GALNAC5 | 0.035 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[YWHAEP7-1]] | B | ST6GALNAC5 activity raises YWHAEP7-1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without ST6GALNAC5 | 0.045 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[LATS2]] | B | ST6GALNAC5 activity lowers LATS2's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.64× higher at baseline in the lines without ST6GALNAC5 | 0.047 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[STK33]] | B | ST6GALNAC5 activity raises STK33's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.20× lower at baseline in the lines without ST6GALNAC5 | 0.048 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[LINC02981]] | B | ST6GALNAC5 activity raises LINC02981's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without ST6GALNAC5 | 0.071 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[RAMP1]] | B | ST6GALNAC5 activity raises RAMP1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without ST6GALNAC5 | 0.071 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[TLDC2]] | B | ST6GALNAC5 activity raises TLDC2's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without ST6GALNAC5 | 0.090 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[TJP2]] | B | ST6GALNAC5 activity raises TJP2's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without ST6GALNAC5 | 0.094 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[CARD11]] | C | ST6GALNAC5 activity raises CARD11's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without ST6GALNAC5 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8; co-absent with the target |
| [[PKHD1]] | C | ST6GALNAC5 activity raises PKHD1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without ST6GALNAC5 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8; co-absent with the target |
| [[SKAP1]] | C | ST6GALNAC5 activity raises SKAP1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without ST6GALNAC5 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 45.9); signed map (55.7, 6.0). **Vector** length 52.2, 15.2% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:76,867,480-77,067,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3184, ST6GalNAcV; previously SIAT7E |
| Gene groups (HGNC) | Sialyltransferases; MicroRNA protein coding host genes |
| Reactome | 8 pathways, smallest: Glycosphingolipid biosynthesis; Sialic acid metabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVH7](https://www.uniprot.org/uniprotkb/Q9BVH7) (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 5):

> Predominantly catalyzes the biosynthesis of ganglioside GD1alpha from GM1b in the brain, by transferring the sialyl group (N-acetyl-alpha-neuraminyl or NeuAc) from CMP-NeuAc to the GalNAc residue on the NeuAc-alpha-2,3-Gal-beta-1,3-GalNAc sequence of GM1b. GD1alpha is a critical molecule in the communication and interaction between neuronal cells and their supportive cells, particularly in brain tissues, and functions as an adhesion molecule in the process of metastasis (By similarity). Also …

**Summary**, from NCBI Gene [81849](https://www.ncbi.nlm.nih.gov/gene/81849):

> The protein encoded by this gene is a Golgi type II transmembrane glycosyltransferase. The encoded protein catalyzes the transfer of sialic acid to cell surface proteins to modulate cell-cell interactions. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:19342](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19342) · Entrez [81849](https://www.ncbi.nlm.nih.gov/gene/81849) · UniProt [Q9BVH7](https://www.uniprot.org/uniprotkb/Q9BVH7) · Ensembl [ENSG00000117069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117069)

## Data

Gene col 3872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3872); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3872]; `tensor/DDL_lfc|DDL_z.npy` [3872]; `embed/gene_vectors.npy` [3872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3872 or target_col == 3872). Every well: [[ST6GALNAC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
