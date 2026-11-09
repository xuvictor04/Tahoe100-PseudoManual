---
symbol: "RFX8"
type: "gene"
col: 12213
ensembl_id: "ENSG00000196460"
name: "regulatory factor X8"
location: "2q11.2"
module: 13
arm: "+"
pooled_cpm: 53.35
n_lines_expressing: 15
n_dd_up: 6
n_dd_down: 36
n_dd_up_clean: 3
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 56
direction_downstream: 59
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# RFX8

*regulatory factor X8* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +8.2, q 9e-14, up in 0 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +5.2, q 5e-05, up in 0 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -10.2, q 1e-21, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR68]] (+0.78, fdr 7e-06), [[SAMD3]] (+0.77, fdr 7e-06), [[SHANK1]] (+0.76, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 59 go from it, the strongest it → [[POU2F2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +8.2 | 9e-14 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.7 | 6e-09 | 1/11 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 5e-05 | 0/13 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.9 | 0.013 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.053 | 0/13 | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.095 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.14 | 1/13 (AsPC-1) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 2 with an alert ⚠; shown: the 15 strongest. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.489×** | -10.2 | 1e-21 | 13/13 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.509×** | -8.2 | 6e-14 | 12/13 (HOP62, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.420×** | -8.0 | 2e-13 | 13/13 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -7.6 | 5e-12 | 12/13 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -7.5 | 5e-12 | 11/13 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.448×** | -7.5 | 6e-12 | 12/13 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.466×** | -7.4 | 1e-11 | 13/13 (H4, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.426×** | -7.1 | 1e-10 | 13/15 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.608×** | -7.0 | 1e-10 | 10/13 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -5.8 | 3e-07 | 12/13 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.589×** | -5.3 | 5e-06 | 13/14 (H4, HOP62, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.577×** | -5.2 | 8e-06 | 13/13 (HOP62, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -5.0 | 3e-05 | 9/13 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.607×** | -4.8 | 6e-05 | 11/12 (H4, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.628×** | -4.7 | 1e-04 | 12/13 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 203 | 0 | 29 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00738× (z -26.3) |
| [[HOP62 (line)]] | alt | 833 | 0 | 27 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0182× (z -32.9) |
| [[HS-578T (line)]] | alt | 179 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -23.7) |
| [[hTERT-HPNE (line)]] | wt | 392 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0369× (z -22.3) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0314× (z -25.2) |
| [[RPMI-7951 (line)]] | alt | 237 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0279× (z -30.5) |
| [[NCI-H1792 (line)]] | alt | 26.0 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.394× (z -13.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.3) |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.105× (z -9.9) |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.1) |
| [[SW480 (line)]] | alt | 35.8 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.67× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.6) |
| [[SW 1088 (line)]] | alt | 76.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0285× (z -12.1) |
| [[A-172 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR68]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[COL6A2]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TSHZ3]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VEPH1]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[RAC2]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ARHGAP22]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 5, C 51. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RFX8's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.9% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds |
| [[RPSAP52]] | B | RPSAP52 activity raises RFX8's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 3.19× lower at baseline in the lines without RPSAP52 | 0.066 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[NTNG2]] | B | NTNG2 activity raises RFX8's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.00× lower at baseline in the lines without NTNG2 | 0.084 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8 |
| [[TM4SF19]] | B | TM4SF19 activity raises RFX8's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 2.54× lower at baseline in the lines without TM4SF19 | 0.097 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[GDNF-AS1]] | B | GDNF-AS1 activity raises RFX8's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.70× lower at baseline in the lines without GDNF-AS1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[WNT5A]] | C | WNT5A activity raises RFX8's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 5.66× lower at baseline in the lines without WNT5A | 5e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises RFX8's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 8.62× lower at baseline in the lines without LINC01411 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises RFX8's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 6.62× lower at baseline in the lines without CDH13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises RFX8's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 6.83× lower at baseline in the lines without APCDD1L | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[NLRP1]] | C | NLRP1 activity raises RFX8's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 4.11× lower at baseline in the lines without NLRP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises RFX8's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 5.74× lower at baseline in the lines without HS3ST3A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises RFX8's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 5.49× lower at baseline in the lines without ADAMTS12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 21, C 38. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU2F2]] | B | RFX8 activity raises POU2F2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.97× lower at baseline in the lines without RFX8 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[MAP4K4]] | B | RFX8 activity raises MAP4K4's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without RFX8 | 1e-03 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[TMEM92-AS1]] | B | RFX8 activity raises TMEM92-AS1's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without RFX8 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[GPR68]] | B | RFX8 activity raises GPR68's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without RFX8 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[C13orf46]] | B | RFX8 activity raises C13orf46's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.19× lower at baseline in the lines without RFX8 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[POU2F2]] | B | RFX8 activity weakens POU2F2's drug response | lines that do not express RFX8 (34) vs lines expressing it (13) | the lines without RFX8 respond 2.22× as strongly (z diff -1.91); strongest at Idarubicin (hydrochloride) 5 µM: 2.90x vs 1.14x (z diff -5.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; target measured in part of the lines; artifact flags |
| [[RASA3]] | B | RFX8 activity raises RASA3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without RFX8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[PDE4DIPP2]] | B | RFX8 activity raises PDE4DIPP2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.24× lower at baseline in the lines without RFX8 | 0.021 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[SYTL3]] | B | RFX8 activity raises SYTL3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without RFX8 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[BCL11B]] | B | RFX8 activity raises BCL11B's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without RFX8 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[RPSAP52]] | B | RFX8 activity raises RPSAP52's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without RFX8 | 0.043 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[ANTXR2]] | B | RFX8 activity raises ANTXR2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without RFX8 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 13.7); signed map (19.6, 47.6). **Vector** length 97.7, 43.8% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.52 to 11); *Collagen degradation* (reactome, mean cos +0.54 to 8); *Collagen chain trimerization* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -8.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -7.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -7.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,397,359-101,475,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42986 |
| Gene groups (HGNC) | Regulatory factor X family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZV50](https://www.uniprot.org/uniprotkb/Q6ZV50) (DNA-binding protein RFX8):

> May be a transcription factor.

**Summary**, from NCBI Gene [731220](https://www.ncbi.nlm.nih.gov/gene/731220):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37253) · Entrez [731220](https://www.ncbi.nlm.nih.gov/gene/731220) · UniProt [Q6ZV50](https://www.uniprot.org/uniprotkb/Q6ZV50) · Ensembl [ENSG00000196460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196460)

## Data

Gene col 12213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12213); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12213]; `tensor/DDL_lfc|DDL_z.npy` [12213]; `embed/gene_vectors.npy` [12213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12213 or target_col == 12213). Every well: [[RFX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
