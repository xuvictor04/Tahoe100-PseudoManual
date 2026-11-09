---
symbol: "KLK6"
type: "gene"
col: 9532
ensembl_id: "ENSG00000167755"
name: "kallikrein related peptidase 6"
location: "19q13.41"
module: 55
arm: "+"
pooled_cpm: 11.93
n_lines_expressing: 16
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 46
direction_downstream: 59
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# KLK6

*kallikrein related peptidase 6* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.06× (z +16.2, q 0e+00, up in 12 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +7.5, q 9e-12, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.378× (z -4.2, q 0.008, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK7]] (+0.79, fdr 7e-06, ⚠ same locus), [[GPX2]] (+0.73, fdr 1e-05), [[GJB1]] (+0.72, fdr 1e-05), [[LYZ]] (+0.70, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[VILL]] → it (grade B ⚠); 59 go from it, the strongest it → [[ADAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.06×** | +16.2 | 0e+00 | 12/12 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.15×** | +15.7 | 0e+00 | 6/9 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.47×** | +9.6 | 2e-19 | 9/10 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.77×** | +7.6 | 4e-12 | 3/5 (HT-29, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.5 | 9e-12 | 2/14 (CFPAC-1, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +5.3 | 1e-05 | 2/13 (KATO III, MIA PaCa-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.2 | 0.002 | 5/13 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 3/14 (HCT15, SW480, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.9 | 0.006 | 1/13 (CFPAC-1) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.006 | 2/14 (HEC-1-A, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.4 | 0.041 | 3/13 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.091 | 5/14 (HEC-1-A, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.378×** | -4.2 | 0.008 | 10/14 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -4.2 | 0.008 | 13/14 (COLO 205, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.591×** | -4.0 | 0.011 | 7/14 (SW480, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -4.0 | 0.011 | 10/14 (SW48, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | **0.421×** | -3.7 | 0.021 | 2/14 (HT-29, SW480) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.448×** | -3.5 | 0.048 | 7/14 (HCT15, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.677× | -3.1 | 0.16 | 1/14 (CFPAC-1) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -20.7) |
| [[SW48 (line)]] | wt | 62.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.2) |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0685× (z -19.2) |
| [[KATO III (line)]] | alt | 69.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -21.2) |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0693× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -18.2) |
| [[SW1417 (line)]] | alt | 145 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.0) |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.2) |
| [[A-172 (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.956 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK7]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; STRING 669; ⚠ same locus (6.8 kb, same strand: neighbours can correlate without regulation) |
| [[GPX2]] | +0.73 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[GJB1]] | +0.72 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[LYZ]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.68 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[C9orf152]] | +0.68 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[LINC01559]] | +0.68 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.68 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[LAD1]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TFF3]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[LCK]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[BMP4]] | +0.66 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[MPZL2]] | +0.66 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 1, C 45. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VILL]] | B | VILL activity raises KLK6's level | lines that do not express VILL (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without VILL | 0.087 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[KLK7]] | C | KLK7 activity raises KLK6's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 10.83× lower at baseline in the lines without KLK7 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises KLK6's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 7.94× lower at baseline in the lines without AZGP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises KLK6's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 4.61× lower at baseline in the lines without EPCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises KLK6's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 6.96× lower at baseline in the lines without SKAP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises KLK6's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 5.56× lower at baseline in the lines without RAB25 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[KCNE3]] | C | KCNE3 activity raises KLK6's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 7.22× lower at baseline in the lines without KCNE3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[LEMD1]] | C | LEMD1 activity raises KLK6's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 4.25× lower at baseline in the lines without LEMD1 | 0.007 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises KLK6's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 5.70× lower at baseline in the lines without LAD1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises KLK6's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 6.81× lower at baseline in the lines without VWA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[BLACAT1]] | C | BLACAT1 activity raises KLK6's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 4.02× lower at baseline in the lines without BLACAT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises KLK6's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 5.31× lower at baseline in the lines without TNNT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 6, C 53. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAP1]] | B | KLK6 activity raises ADAP1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without KLK6 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[TMC6]] | B | KLK6 activity raises TMC6's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 4.07× lower at baseline in the lines without KLK6 | 0.009 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[EPS8L1]] | B | KLK6 activity raises EPS8L1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 3.86× lower at baseline in the lines without KLK6 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[USP6NL]] | B | KLK6 activity raises USP6NL's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 2.22× lower at baseline in the lines without KLK6 | 0.014 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[KRT8]] | B | KLK6 activity raises KRT8's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 4.16× lower at baseline in the lines without KLK6 | 0.037 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[SLC30A10]] | B | KLK6 activity raises SLC30A10's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without KLK6 | 0.097 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15 |
| [[BLACAT1]] | C | KLK6 activity raises BLACAT1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 4.27× lower at baseline in the lines without KLK6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[LEMD1]] | C | KLK6 activity raises LEMD1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 6.57× lower at baseline in the lines without KLK6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[AZGP1]] | C | KLK6 activity raises AZGP1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 4.91× lower at baseline in the lines without KLK6 | 0.002 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[EPS8L3]] | C | KLK6 activity raises EPS8L3's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 6.75× lower at baseline in the lines without KLK6 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[B3GNT3]] | C | KLK6 activity raises B3GNT3's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 7.61× lower at baseline in the lines without KLK6 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[LAD1]] | C | KLK6 activity raises LAD1's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 8.20× lower at baseline in the lines without KLK6 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 48.4); signed map (65.2, 10.9). **Vector** length 54.5, 19.7% of its response variance represented; |z| ≥ 3 in 361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | kallikrein related peptidase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:50,958,631-50,969,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Bssp, Klk7, neurosin; previously PRSS9, PRSS18 |
| Gene groups (HGNC) | Kallikreins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92876](https://www.uniprot.org/uniprotkb/Q92876) (Kallikrein-6):

> Serine protease which exhibits a preference for Arg over Lys in the substrate P1 position and for Ser or Pro in the P2 position. Shows activity against amyloid precursor protein, myelin basic protein, gelatin, casein and extracellular matrix proteins such as fibronectin, laminin, vitronectin and collagen. Degrades alpha-synuclein and prevents its polymerization, indicating that it may be involved in the pathogenesis of Parkinson disease and other synucleinopathies. May be involved in regulation …

**Summary**, from NCBI Gene [5653](https://www.ncbi.nlm.nih.gov/gene/5653):

> This gene encodes a member of the kallikrein subfamily of the peptidase S1 family of serine proteases. Growing evidence suggests that many kallikreins are implicated in carcinogenesis and some have potential as novel cancer and other disease biomarkers. The encoded preproprotein is proteolytically processed to generate the mature protease. Expression of this protease is regulated by steroid hormones and may be elevated in multiple human cancers and in serum from psoriasis patients. The encoded …

**Accessions** — [HGNC:6367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6367) · Entrez [5653](https://www.ncbi.nlm.nih.gov/gene/5653) · UniProt [Q92876](https://www.uniprot.org/uniprotkb/Q92876) · Ensembl [ENSG00000167755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167755)

## Data

Gene col 9532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9532); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9532]; `tensor/DDL_lfc|DDL_z.npy` [9532]; `embed/gene_vectors.npy` [9532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9532 or target_col == 9532). Every well: [[KLK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
