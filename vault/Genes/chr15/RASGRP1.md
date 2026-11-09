---
symbol: "RASGRP1"
type: "gene"
col: 10270
ensembl_id: "ENSG00000172575"
name: "RAS guanyl releasing protein 1"
location: "15q14"
module: 14
arm: "+"
pooled_cpm: 5.71
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RASGRP1

*RAS guanyl releasing protein 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.20× (z +19.9, q 0e+00, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 0.05 µM: 0.708× (z -4.0, q 0.041, down in 6 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0726×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.171×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (SW48 0.0636×); [[Saquinavir (drug)]] 0.05 µM in 1 line (C-33 A 0.0772×); [[DT-061 (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.74, fdr 7e-06), [[DRAM1]] (+0.69, fdr 7e-06), [[HSD11B1-AS1]] (+0.68, fdr 7e-06); moves opposite to [[RTTN]] (-0.54, fdr 2e-04), [[RNGTT]] (-0.54, fdr 4e-05), [[TBC1D8]] (-0.52, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TLCD4]], [[TLCD4-RWDD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.20×** | +19.9 | 0e+00 | 28/37 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.12×** | +13.2 | 2e-37 | 27/43 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +11.4 | 4e-28 | 30/44 (SW1417, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.6 | 5e-24 | 22/35 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +9.3 | 1e-18 | 22/36 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +7.3 | 2e-11 | 3/10 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.9 | 4e-10 | 8/21 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.7 | 2e-09 | 17/40 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +5.8 | 3e-07 | 15/41 (BT-474, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.1 | 2e-05 | 2/6 (CFPAC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.0 | 3e-05 | 4/21 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 2e-04 | 15/44 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.1 | 0.002 | 7/23 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.009 | 5/43 (CFPAC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.012 | 5/45 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.029 | 6/43 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.70×** | +3.3 | 0.029 | 1/28 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.034 | 4/40 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.095 | 14/38 (HEC-1-A, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10270.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0726×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.171×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (SW48 0.0636×); [[Saquinavir (drug)]] 0.05 µM in 1 line (C-33 A 0.0772×); [[DT-061 (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | **0.708×** | -4.0 | 0.041 | 6/44 (SW 900, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.2 | 0.36 | 8/47 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.57 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 18.8× (z +9.4) | — |
| [[A498 (line)]] | wt | 12.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +14.2) | — |
| [[J82 (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 4.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 9.55 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0772× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 3.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.7× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0726× (z -15.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 4.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.152× (z -9.2) |
| [[SW48 (line)]] | wt | 16.0 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0636× (z -10.6) |
| [[A-427 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[DRAM1]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LGALSL-DT]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[WIPF3]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.64 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ESR1]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[STX11]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTTN]] | -0.54 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[RNGTT]] | -0.54 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[TBC1D8]] | -0.52 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4]], [[TLCD4-RWDD3]] | B | TLCD4, TLCD4-RWDD3 activity raises RASGRP1's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 2.08× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| [[NTN1]] | B | NTN1 activity raises RASGRP1's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without NTN1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[WIPF3]] | B | WIPF3 activity raises RASGRP1's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 1.39× lower at baseline in the lines without WIPF3 | 0.075 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[LRRN1]] | B | LRRN1 activity raises RASGRP1's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.34× lower at baseline in the lines without LRRN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[DENND2B]] | B | DENND2B activity lowers RASGRP1's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 2.23× higher at baseline in the lines without DENND2B | 0.099 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 3.8); signed map (41.2, 9.7). **Vector** length 68.7, 11.0% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +19.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RAS guanyl releasing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:38,488,103-38,565,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CalDAG-GEFII, RASGRP |
| Gene groups (HGNC) | EF-hand domain containing; RAS guanyl releasing proteins |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_UP, COMPLEMENT, ESTROGEN_RESPONSE_EARLY |
| Reactome | 19 pathways, smallest: Activation of RAS in B cells; Rap1 signalling; Effects of PIP2 hydrolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [O95267](https://www.uniprot.org/uniprotkb/O95267) (RAS guanyl-releasing protein 1):

> Functions as a calcium- and diacylglycerol (DAG)-regulated nucleotide exchange factor specifically activating Ras through the exchange of bound GDP for GTP. Activates the Erk/MAP kinase cascade. Regulates T-cell/B-cell development, homeostasis and differentiation by coupling T-lymphocyte/B-lymphocyte antigen receptors to Ras. Regulates NK cell cytotoxicity and ITAM-dependent cytokine production by activation of Ras-mediated ERK and JNK pathways. Functions in mast cell degranulation and cytokine …

**Summary**, from NCBI Gene [10125](https://www.ncbi.nlm.nih.gov/gene/10125):

> This gene is a member of a family of genes characterized by the presence of a Ras superfamily guanine nucleotide exchange factor (GEF) domain. It functions as a diacylglycerol (DAG)-regulated nucleotide exchange factor specifically activating Ras through the exchange of bound GDP for GTP. It activates the Erk/MAP kinase cascade and regulates T-cells and B-cells development, homeostasis and differentiation. Alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:9878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9878) · Entrez [10125](https://www.ncbi.nlm.nih.gov/gene/10125) · UniProt [O95267](https://www.uniprot.org/uniprotkb/O95267) · Ensembl [ENSG00000172575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172575)

## Data

Gene col 10270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10270); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10270]; `tensor/DDL_lfc|DDL_z.npy` [10270]; `embed/gene_vectors.npy` [10270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10270 or target_col == 10270). Every well: [[RASGRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
