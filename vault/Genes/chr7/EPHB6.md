---
symbol: "EPHB6"
type: "gene"
col: 2725
ensembl_id: "ENSG00000106123"
name: "EPH receptor B6"
location: "7q34"
module: 34
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 23
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 17
direction_downstream: 15
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# EPHB6

*EPH receptor B6* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.09× (z +9.5, q 1e-18, up in 6 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.35× (z +8.5, q 4e-15, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.556× (z -5.9, q 3e-06, down in 16 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRBC2]] (+0.69, fdr 7e-06), [[VSIG1]] (+0.67, fdr 7e-06), [[CEMIP]] (+0.65, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CACNA2D4]] → it (grade B ⚠); 15 go from it, the strongest it → [[CD58]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.09×** | +9.5 | 1e-18 | 6/10 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.59×** | +9.0 | 7e-17 | 10/14 (SW1417, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +8.5 | 4e-15 | 11/19 (SW1417, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +6.6 | 5e-09 | 7/13 (HT-29, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +4.1 | 0.005 | 6/20 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.006 | 3/16 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +3.9 | 0.007 | 3/15 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.6 | 0.020 | 5/19 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.66×** | +3.4 | 0.037 | 1/16 (SW1417) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.60×** | +3.3 | 0.057 | 2/20 (A498, NCI-H2030) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.59×** | +3.2 | 0.061 | 7/20 (A498, HT-29, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.56×** | +3.1 | 0.091 | 3/20 (NCI-H2030, A498, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **2.29×** | +3.0 | 0.100 | 9/16 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2725.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -5.9 | 3e-06 | 16/17 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -5.5 | 1e-05 | 18/20 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -5.3 | 3e-05 | 14/18 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.522×** | -4.6 | 7e-04 | 13/19 (BT-474, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -4.2 | 0.002 | 14/17 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **0.316×** | -4.2 | 0.002 | 6/19 (SW 900, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.562×** | -4.1 | 0.003 | 10/19 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.547×** | -3.9 | 0.006 | 9/19 (HOP62, SW 900, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.674×** | -3.9 | 0.007 | 10/19 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -3.5 | 0.023 | 11/19 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -3.4 | 0.041 | 13/19 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -3.3 | 0.044 | 11/20 (A498, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.4 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -19.4) |
| [[SW 900 (line)]] | alt | 55.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -14.5) |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0413× (z -23.0) |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.5) |
| [[HOP62 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.519× (z -9.0) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 7.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -13.6) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0924× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.451× (z -11.3) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0314× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -10.5) |
| [[A-172 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRBC2]] | +0.69 | +0.76 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[VSIG1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CEMIP]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PTPRE]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ADAM19]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC02813]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TMC6]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TMEM163]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D4]] | B | CACNA2D4 activity raises EPHB6's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without CACNA2D4 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[ITGA1]] | B | ITGA1 activity raises EPHB6's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without ITGA1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[MYEOV]] | B | MYEOV activity raises EPHB6's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without MYEOV | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[TINAGL1]] | B | TINAGL1 activity raises EPHB6's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without TINAGL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[SCAT1]] | B | SCAT1 activity raises EPHB6's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SCAT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[MANCR]] | B | MANCR activity raises EPHB6's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without MANCR | 0.051 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[DUSP4]] | B | DUSP4 activity raises EPHB6's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without DUSP4 | 0.077 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[LINC02813]] | B | LINC02813 activity raises EPHB6's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without LINC02813 | 0.098 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[RAC2]] | B | RAC2 activity raises EPHB6's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without RAC2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TRBC2]] | C | TRBC2 activity raises EPHB6's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 4.20× lower at baseline in the lines without TRBC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises EPHB6's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without CARD11 | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[AFAP1L2]] | C | AFAP1L2 activity raises EPHB6's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without AFAP1L2 | 0.022 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD58]] | B | EPHB6 activity raises CD58's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without EPHB6 | 0.005 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[PTPRE]] | B | EPHB6 activity raises PTPRE's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.76× lower at baseline in the lines without EPHB6 | 0.019 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[ADAM8]] | B | EPHB6 activity raises ADAM8's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without EPHB6 | 0.032 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[EVA1A-AS]] | B | EPHB6 activity raises EVA1A-AS's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without EPHB6 | 0.051 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[LAMA3]] | B | EPHB6 activity raises LAMA3's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without EPHB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[SYNJ2]] | B | EPHB6 activity raises SYNJ2's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.35× lower at baseline in the lines without EPHB6 | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[SCAT1]] | B | EPHB6 activity raises SCAT1's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without EPHB6 | 0.088 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[ADGRE2]] | C | EPHB6 activity raises ADGRE2's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without EPHB6 | 0.005 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |
| [[TRBC2]] | C | EPHB6 activity raises TRBC2's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without EPHB6 | 0.022 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |
| [[LYPD3]] | C | EPHB6 activity raises LYPD3's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without EPHB6 | 0.025 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |
| [[ANO1]] | C | EPHB6 activity raises ANO1's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without EPHB6 | 0.050 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |
| [[LINC02432]] | C | EPHB6 activity raises LINC02432's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without EPHB6 | 0.053 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 7.4); signed map (10.7, 52.2). **Vector** length 63.8, 18.5% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.6 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor B6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:142,855,061-142,871,094 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEP |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O15197](https://www.uniprot.org/uniprotkb/O15197) (Ephrin type-B receptor 6):

> Kinase-defective receptor for members of the ephrin-B family. Binds to ephrin-B1 and ephrin-B2. Modulates cell adhesion and migration by exerting both positive and negative effects upon stimulation with ephrin-B2. Inhibits JNK activation, T-cell receptor-induced IL-2 secretion and CD25 expression upon stimulation with ephrin-B2. Can recruit SH2 domain-containing signaling adapters following phosphorylation by EPHB4.

**Summary**, from NCBI Gene [2051](https://www.ncbi.nlm.nih.gov/gene/2051):

> This gene encodes a member of a family of transmembrane proteins that function as receptors for ephrin-B family proteins. Unlike other members of this family, the encoded protein does not contain a functional kinase domain. Activity of this protein can influence cell adhesion and migration. Expression of this gene is downregulated during tumor progression, suggesting that the protein may suppress tumor invasion and metastasis. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:3396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3396) · Entrez [2051](https://www.ncbi.nlm.nih.gov/gene/2051) · UniProt [O15197](https://www.uniprot.org/uniprotkb/O15197) · Ensembl [ENSG00000106123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106123)

## Data

Gene col 2725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2725); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2725]; `tensor/DDL_lfc|DDL_z.npy` [2725]; `embed/gene_vectors.npy` [2725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2725 or target_col == 2725). Every well: [[EPHB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
