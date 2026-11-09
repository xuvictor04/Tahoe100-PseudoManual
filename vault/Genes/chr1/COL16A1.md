---
symbol: "COL16A1"
type: "gene"
col: 1403
ensembl_id: "ENSG00000084636"
name: "collagen type XVI alpha 1 chain"
location: "1p35.2"
module: 14
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 32
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# COL16A1

*collagen type XVI alpha 1 chain* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.88× (z +9.8, q 7e-20, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +9.2, q 2e-17, up in 15 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.568× (z -5.4, q 3e-05, down in 13 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRG1]] (+0.71, fdr 7e-06), [[ANO9]] (+0.68, fdr 7e-06), [[TNFAIP2]] (+0.62, fdr 1e-05); moves opposite to [[CLPP]] (-0.52, fdr 3e-05), [[PGP]] (-0.50, fdr 4e-05), [[MAP2K1]] (-0.48, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); 13 go from it, the strongest it → [[NOD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +9.8 | 7e-20 | 5/10 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +9.2 | 2e-17 | 15/29 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.1 | 2e-17 | 11/21 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.1 | 8e-14 | 20/30 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.3 | 3e-11 | 6/10 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.5 | 1e-08 | 17/29 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +4.9 | 9e-05 | 8/24 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.3 | 0.001 | 7/30 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.0 | 0.004 | 6/29 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.008 | 7/30 (LS 180, LoVo, …) | all doses, flat |  |
| [[Bergenin (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.010 | 5/27 (LoVo, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.010 | 7/30 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.013 | 4/29 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.013 | 5/23 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.3 | 0.037 | 3/19 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.059 | 3/20 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.059 | 7/26 (LoVo, HT-29, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.059 | 12/28 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -5.4 | 3e-05 | 13/29 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.612×** | -4.7 | 7e-04 | 15/30 (LoVo, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.668×** | -3.9 | 0.016 | 12/27 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.669×** | -3.9 | 0.016 | 9/28 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.729× | -3.0 | 0.23 | 6/29 (LoVo, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.730× | -3.0 | 0.23 | 13/30 (LoVo, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 37.5 | 0 | 11 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0584× (z -17.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.164× (z -11.1) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 9 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.139× (z -12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.140× (z -12.6) |
| [[HT-29 (line)]] | alt | 32.3 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.0) |
| [[A-172 (line)]] | wt | 7.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[A-427 (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.853 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRG1]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ANO9]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF14]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[DDR1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[STAT5A]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[BCL3]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ELF3-AS1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NDRG2]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DIP2C-AS1]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ZNF385C]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TNFRSF14-AS1]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPP]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PGP]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MAP2K1]] | -0.48 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ITGB1BP1]] | -0.47 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises COL16A1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without LINC03040 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[LINC00457]] | B | LINC00457 activity raises COL16A1's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without LINC00457 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[EPS8L3]] | B | EPS8L3 activity raises COL16A1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without EPS8L3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[SLC44A3]] | B | SLC44A3 activity raises COL16A1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without SLC44A3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[STAT5A]] | B | STAT5A activity raises COL16A1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without STAT5A | 0.095 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOD2]] | B | COL16A1 activity raises NOD2's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without COL16A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[TRIM29]] | B | COL16A1 activity raises TRIM29's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without COL16A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[COL22A1]] | B | COL16A1 activity raises COL22A1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without COL16A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[KRT80]] | B | COL16A1 activity raises KRT80's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without COL16A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[TMPRSS3]] | B | COL16A1 activity raises TMPRSS3's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without COL16A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[PLCD3]] | B | COL16A1 activity raises PLCD3's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without COL16A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[PRKCH-AS1]] | B | COL16A1 activity raises PRKCH-AS1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without COL16A1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[ADGRG1]] | B | COL16A1 activity raises ADGRG1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without COL16A1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | COL16A1 activity raises TNFRSF14-AS1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without COL16A1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[LINC03040]] | B | COL16A1 activity raises LINC03040's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without COL16A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[ARHGEF16]] | B | COL16A1 activity raises ARHGEF16's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without COL16A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[EFNA1]] | B | COL16A1 activity raises EFNA1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without COL16A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 3.4); signed map (46.1, 7.6). **Vector** length 63.3, 13.0% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -4.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XVI alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,652,263-31,704,319 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibril associated collagens with interrupted triple helices |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 7 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07092](https://www.uniprot.org/uniprotkb/Q07092) (Collagen alpha-1(XVI) chain):

> Involved in mediating cell attachment and inducing integrin-mediated cellular reactions, such as cell spreading and alterations in cell morphology.

**Summary**, from NCBI Gene [1307](https://www.ncbi.nlm.nih.gov/gene/1307):

> This gene encodes the alpha chain of type XVI collagen, a member of the FACIT collagen family (fibril-associated collagens with interrupted helices). Members of this collagen family are found in association with fibril-forming collagens such as type I and II, and serve to maintain the integrity of the extracellular matrix. High levels of type XVI collagen have been found in fibroblasts and keratinocytes, and in smooth muscle and amnion. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2193) · Entrez [1307](https://www.ncbi.nlm.nih.gov/gene/1307) · UniProt [Q07092](https://www.uniprot.org/uniprotkb/Q07092) · Ensembl [ENSG00000084636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084636)

## Data

Gene col 1403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1403); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1403]; `tensor/DDL_lfc|DDL_z.npy` [1403]; `embed/gene_vectors.npy` [1403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1403 or target_col == 1403). Every well: [[COL16A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL16A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
