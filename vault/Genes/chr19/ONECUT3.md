---
symbol: "ONECUT3"
type: "gene"
col: 13023
ensembl_id: "ENSG00000205922"
name: "one cut homeobox 3"
location: "19p13.3"
module: 31
arm: "+"
pooled_cpm: 36.58
n_lines_expressing: 13
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 23
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ONECUT3

*one cut homeobox 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.37× (z +10.3, q 5e-22, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.13× (z +9.0, q 3e-17, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.545× (z -4.9, q 4e-04, down in 10 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.72, fdr 7e-06), [[LINC00659]] (+0.71, fdr 1e-05), [[TMC6]] (+0.71, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 23 go from it, the strongest it → [[IQANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +10.3 | 5e-22 | 3/9 (HCT15, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +9.4 | 1e-18 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +9.0 | 3e-17 | 1/11 (SW480) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.46×** | +5.4 | 7e-06 | 4/11 (SW1417, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +5.1 | 3e-05 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.029 | 1/11 (SW48) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.041 | 0/11 | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.041 | 1/11 (SW1417) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.078 | 1/11 (HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -4.9 | 4e-04 | 10/11 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -4.7 | 8e-04 | 9/10 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.571×** | -4.4 | 0.002 | 8/11 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.691×** | -4.3 | 0.002 | 5/11 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.617×** | -3.8 | 0.018 | 0/11 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -3.7 | 0.018 | 6/11 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.766× | -3.2 | 0.11 | 6/11 (LS 180, Panc 03.27, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.631× | -3.2 | 0.11 | 9/11 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 742 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -13.0) |
| [[PANC-1 (line)]] | alt | 120 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -27.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0812× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 56.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -12.0) |
| [[SW480 (line)]] | alt | 13.5 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.95× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -9.4) |
| [[KATO III (line)]] | alt | 177 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -13.5) |
| [[A-427 (line)]] | wt | 15.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0822× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 120 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.9) |
| [[HCT15 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LINC00659]] | +0.71 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TMC6]] | +0.71 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GPR35]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[SLC5A1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ITGB4]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PADI1]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PIWIL1]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises ONECUT3's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.45× lower at baseline in the lines without ZNF860 | 0.073 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[CBLC]] | C | CBLC activity raises ONECUT3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 4.64× lower at baseline in the lines without CBLC | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; co-absent with the target |
| [[SLC52A3]] | C | SLC52A3 activity raises ONECUT3's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 3.81× lower at baseline in the lines without SLC52A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises ONECUT3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without NKD1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[MOGAT3]] | C | MOGAT3 activity raises ONECUT3's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without MOGAT3 | 0.080 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises ONECUT3's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without IGFL4 | 0.086 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises ONECUT3's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 4.52× lower at baseline in the lines without VWA2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises ONECUT3's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.47× lower at baseline in the lines without ATP2C2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 11, C 12. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQANK1]] | B | ONECUT3 activity raises IQANK1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without ONECUT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[OSBPL10]] | B | ONECUT3 activity raises OSBPL10's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without ONECUT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[ZNF860]] | B | ONECUT3 activity raises ZNF860's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.23× lower at baseline in the lines without ONECUT3 | 0.017 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[ADAP1]] | B | ONECUT3 activity raises ADAP1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.77× lower at baseline in the lines without ONECUT3 | 0.038 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[EEPD1]] | B | ONECUT3 activity raises EEPD1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.11× lower at baseline in the lines without ONECUT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[KRT8]] | B | ONECUT3 activity raises KRT8's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.48× lower at baseline in the lines without ONECUT3 | 0.064 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[ACOT11]] | B | ONECUT3 activity raises ACOT11's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.58× lower at baseline in the lines without ONECUT3 | 0.067 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[ARHGEF16]] | B | ONECUT3 activity raises ARHGEF16's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.44× lower at baseline in the lines without ONECUT3 | 0.070 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[BLACAT1]] | B | ONECUT3 activity raises BLACAT1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.48× lower at baseline in the lines without ONECUT3 | 0.082 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[TMC6]] | B | ONECUT3 activity raises TMC6's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.88× lower at baseline in the lines without ONECUT3 | 0.082 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[EPHA2-AS1]] | B | ONECUT3 activity raises EPHA2-AS1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without ONECUT3 | 0.095 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[MST1R]] | C | ONECUT3 activity raises MST1R's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 4.92× lower at baseline in the lines without ONECUT3 | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 51.7); signed map (4.2, 38.3). **Vector** length 54.5, 21.2% of its response variance represented; |z| ≥ 3 in 318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +1.8 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | one cut homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,753,506-1,780,988 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes |
| Reactome | 3 pathways, smallest: Regulation of gene expression in early pancreatic precursor cells; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells; Regulation of beta-cell development |
| Matched by | ensembl_id |

**Function**, from UniProt [O60422](https://www.uniprot.org/uniprotkb/O60422) (One cut domain family member 3):

> Transcriptional activator. Binds the consensus DNA sequence 5'-DHWATTGAYTWWD-3' on a variety of gene promoters such as those of HNF3B and TTR (By similarity).

**Summary**, from NCBI Gene [390874](https://www.ncbi.nlm.nih.gov/gene/390874):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13399) · Entrez [390874](https://www.ncbi.nlm.nih.gov/gene/390874) · UniProt [O60422](https://www.uniprot.org/uniprotkb/O60422) · Ensembl [ENSG00000205922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205922)

## Data

Gene col 13023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13023); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13023]; `tensor/DDL_lfc|DDL_z.npy` [13023]; `embed/gene_vectors.npy` [13023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13023 or target_col == 13023). Every well: [[ONECUT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ONECUT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
