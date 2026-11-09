---
symbol: "SCEL"
type: "gene"
col: 5824
ensembl_id: "ENSG00000136155"
name: "sciellin"
location: "13q22.3"
module: 34
arm: "+"
pooled_cpm: 23.94
n_lines_expressing: 15
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 32
direction_downstream: 67
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SCEL

*sciellin* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.08× (z +13.4, q 3e-38, up in 8 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.63× (z +6.6, q 8e-09, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.615× (z -6.6, q 3e-08, down in 12 of 13 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.592× (z -4.6, q 0.001, down in 5 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA3]] (+0.70, fdr 7e-06), [[GJB3]] (+0.67, fdr 1e-05), [[TNS4]] (+0.66, fdr 1e-05); moves opposite to [[B9D2]] (-0.47, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 67 go from it, the strongest it → [[LMO7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +13.4 | 3e-38 | 8/13 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.12×** | +13.0 | 4e-36 | 6/9 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +10.1 | 1e-21 | 5/11 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.63×** | +6.6 | 8e-09 | 8/14 (HT-29, LS 180, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.55×** | +6.4 | 2e-08 | 7/13 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.1 | 8e-08 | 9/13 (LS 180, KATO III, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.77×** | +5.4 | 4e-06 | 7/13 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.74×** | +5.3 | 8e-06 | 9/13 (HT-29, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.73×** | +5.2 | 1e-05 | 9/13 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.71×** | +5.1 | 2e-05 | 0/12 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.6 | 2e-04 | 3/12 (NCI-H2347, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.61×** | +4.6 | 2e-04 | 2/13 (Panc 03.27, NCI-H1573) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **2.48×** | +4.5 | 3e-04 | 7/12 (HT-29, KATO III, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +4.5 | 3e-04 | 6/9 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.001 | 7/13 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.005 | 1/14 (NCI-H2347) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.020 | 3/14 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.022 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.025 | 1/14 (NCI-H2347) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.041 | 10/13 (HT-29, SHP-77, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.099 | 5/13 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.615×** | -6.6 | 3e-08 | 12/13 (HT-29, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.592×** | -4.6 | 0.001 | 5/13 (SHP-77, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.652×** | -3.9 | 0.017 | 7/14 (SHP-77, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Pimozide (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.017 | 0/13 | top dose only |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.659×** | -3.8 | 0.017 | 0/13 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.676×** | -3.7 | 0.017 | 5/13 (SHP-77, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.761×** | -3.6 | 0.024 | 4/13 (SHP-77, HEC-1-A, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.494×** | -3.5 | 0.028 | 8/14 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.028 | 12/13 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.685×** | -3.5 | 0.028 | 8/13 (SHP-77, SW48, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.706×** | -3.3 | 0.046 | 0/13 | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.538×** | -3.1 | 0.092 | 0/13 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.727× | -3.0 | 0.10 | 4/14 (NCI-H2030, SHP-77, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 43.4 | 2 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.94× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -11.0) |
| [[KATO III (line)]] | alt | 52.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -15.1) |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0595× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.123× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 422 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA3]] | +0.70 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[TNS4]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[KRT6A]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | STRING 441 |
| [[MPRIP]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LINC00707]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ANO1]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[IL1R2]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LINC02582]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MST1R]] | +0.60 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[CAPN8]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B9D2]] | -0.47 | -0.37 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 1, C 31. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises SCEL's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without ZNF860 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[TMPRSS4]] | C | TMPRSS4 activity raises SCEL's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.24× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises SCEL's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 5.02× lower at baseline in the lines without HS3ST1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[KIAA0040]] | C | KIAA0040 activity raises SCEL's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 3.85× lower at baseline in the lines without KIAA0040 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises SCEL's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.36× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises SCEL's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.25× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises SCEL's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.67× lower at baseline in the lines without P2RY2 | 0.001 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises SCEL's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.14× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises SCEL's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.21× lower at baseline in the lines without GJB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises SCEL's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 5.15× lower at baseline in the lines without CEACAM6 | 0.003 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises SCEL's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without KLK10 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises SCEL's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 4.59× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |

### Downstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 32, C 35. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | SCEL activity raises LMO7's level | lines that do not express SCEL (35) vs lines expressing it (15) | 4.20× lower at baseline in the lines without SCEL | 0.004 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[DIAPH1]] | B | SCEL activity raises DIAPH1's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.58× lower at baseline in the lines without SCEL | 0.008 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[NOSTRIN]] | B | SCEL activity raises NOSTRIN's level | lines that do not express SCEL (35) vs lines expressing it (15) | 3.10× lower at baseline in the lines without SCEL | 0.012 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[SNRK]] | B | SCEL activity raises SNRK's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without SCEL | 0.012 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[LYPD3]] | B | SCEL activity raises LYPD3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.09× lower at baseline in the lines without SCEL | 0.016 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[MET]] | B | SCEL activity raises MET's level | lines that do not express SCEL (35) vs lines expressing it (15) | 3.23× lower at baseline in the lines without SCEL | 0.022 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[PLEK2]] | B | SCEL activity raises PLEK2's level | lines that do not express SCEL (35) vs lines expressing it (15) | 4.08× lower at baseline in the lines without SCEL | 0.022 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[PKP2]] | B | SCEL activity raises PKP2's level | lines that do not express SCEL (35) vs lines expressing it (15) | 3.46× lower at baseline in the lines without SCEL | 0.022 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[PTK2B]] | B | SCEL activity raises PTK2B's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without SCEL | 0.031 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[KRT8]] | B | SCEL activity raises KRT8's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.94× lower at baseline in the lines without SCEL | 0.033 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[ATG16L1]] | B | SCEL activity raises ATG16L1's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.54× lower at baseline in the lines without SCEL | 0.034 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[RAPGEF3]] | B | SCEL activity raises RAPGEF3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.94× lower at baseline in the lines without SCEL | 0.035 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.2, 51.6); signed map (3.2, 37.1). **Vector** length 55.8, 19.1% of its response variance represented; |z| ≥ 3 in 439 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +6.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +3.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.9 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | sciellin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:77,535,674-77,645,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21667, MGC22531 |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95171](https://www.uniprot.org/uniprotkb/O95171) (Sciellin):

> May function in the assembly or regulation of proteins in the cornified envelope. The LIM domain may be involved in homotypic or heterotypic associations and may function to localize sciellin to the cornified envelope.

**Summary**, from NCBI Gene [8796](https://www.ncbi.nlm.nih.gov/gene/8796):

> The protein encoded by this gene is a precursor to the cornified envelope of terminally differentiated keratinocytes. This protein localizes to the periphery of cells and may function in the assembly or regulation of proteins in the cornified envelope. Transcript variants encoding different isoforms exist. A transcript variant utilizing an alternative polyA signal has been described in the literature, but its full-length nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10573) · Entrez [8796](https://www.ncbi.nlm.nih.gov/gene/8796) · UniProt [O95171](https://www.uniprot.org/uniprotkb/O95171) · Ensembl [ENSG00000136155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136155)

## Data

Gene col 5824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5824); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5824]; `tensor/DDL_lfc|DDL_z.npy` [5824]; `embed/gene_vectors.npy` [5824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5824 or target_col == 5824). Every well: [[SCEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
