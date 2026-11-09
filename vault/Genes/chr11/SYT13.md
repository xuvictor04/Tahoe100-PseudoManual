---
symbol: "SYT13"
type: "gene"
col: 313
ensembl_id: "ENSG00000019505"
name: "synaptotagmin 13"
location: "11p11.2"
module: 34
arm: "+"
pooled_cpm: 8.99
n_lines_expressing: 17
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 19
direction_downstream: 35
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SYT13

*synaptotagmin 13* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.15× (z +13.3, q 8e-38, up in 5 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +5.3, q 1e-05, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.572× (z -5.2, q 9e-05, down in 5 of 15 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WSCD1]] (+0.64, fdr 1e-05), [[WNT7B]] (+0.58, fdr 1e-05), [[PTGS1]] (+0.56, fdr 2e-04); moves opposite to [[CEBPD]] (-0.47, fdr 9e-05), [[PIP5K1A]] (-0.44, fdr 4e-04), [[COBLL1]] (-0.44, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[PRAG1]] → it (grade B ⚠); 35 go from it, the strongest it → [[PLS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +13.3 | 8e-38 | 5/11 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +11.0 | 1e-25 | 5/8 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.4 | 8e-19 | 2/9 (KATO III, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.3 | 1e-05 | 4/15 (SW48, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.56×** | +4.1 | 0.004 | 2/11 (SW1417, COLO 205) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +4.1 | 0.004 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.84×** | +4.1 | 0.004 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.0 | 0.004 | 4/14 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.8 | 0.008 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.036 | 5/15 (HT-29, COLO 205, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.057 | 3/15 (SW1417, LS 180, …) | all doses, flat | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.057 | 3/13 (CFPAC-1, A549, …) | all doses, flat | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.070 | 2/13 (LS 180, COLO 205) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.080 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.093 | 4/15 (AsPC-1, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.572×** | -5.2 | 9e-05 | 5/15 (A549, SW1417, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.604×** | -4.7 | 6e-04 | 4/15 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.619×** | -4.2 | 0.006 | 4/15 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | **0.666×** | -3.8 | 0.018 | 1/15 (LS 180) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.487×** | -3.5 | 0.041 | 2/15 (HEC-1-A, A549) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.673×** | -3.5 | 0.041 | 1/15 (SW48) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.2 | 0.097 | 2/15 (SHP-77, NCI-H1573) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.789× | -3.2 | 0.11 | 7/15 (A549, Hs 766T, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.718× | -3.1 | 0.11 | 8/14 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.727× | -3.0 | 0.14 | 3/15 (A549, NCI-H1573, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 24.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0922× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 75.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.9) |
| [[KATO III (line)]] | alt | 44.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.1) |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.7) |
| [[SHP-77 (line)]] | alt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.7) |
| [[SW1417 (line)]] | alt | 3.55 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0677× (z -8.9) |
| [[A-172 (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WSCD1]] | +0.64 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PTGS1]] | +0.56 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[SLC35F3]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CCDC68]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[LAMC2]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TESC]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[CAPN14]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TINAGL1]] | +0.53 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[GTF2IP7]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SPNS2]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[WNT7A]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPD]] | -0.47 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[PIP5K1A]] | -0.44 | -0.34 / -0.25 | both halves | 4e-04 |  |
| [[COBLL1]] | -0.44 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[FSTL3]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ACOT2]] | -0.44 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[PTPN2]] | -0.44 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[RPP38]] | -0.43 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[CUX2]] | -0.43 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[ZCCHC10]] | -0.42 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[KIF9-AS1]] | -0.42 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[RCAN1]] | -0.42 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ZNF302]] | -0.42 | -0.44 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAG1]] | B | PRAG1 activity raises SYT13's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without PRAG1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[FAM3C2P]] | B | FAM3C2P activity lowers SYT13's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.91× higher at baseline in the lines without FAM3C2P | 0.062 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[ZNF860]] | B | ZNF860 activity raises SYT13's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without ZNF860 | 0.089 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises SYT13's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without GTF2IP7 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[HS3ST1]] | C | HS3ST1 activity raises SYT13's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without HS3ST1 | 0.006 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises SYT13's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without SPNS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[TFF1]] | C | TFF1 activity raises SYT13's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without TFF1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises SYT13's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.00× lower at baseline in the lines without ATP2C2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises SYT13's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without BSPRY | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises SYT13's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.18× lower at baseline in the lines without SULT2B1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[CNTN1]] | C | CNTN1 activity raises SYT13's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without CNTN1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[PTGS1]] | C | PTGS1 activity raises SYT13's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without PTGS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 15, C 20. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | SYT13 activity raises PLS1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 3.80× lower at baseline in the lines without SYT13 | 0.012 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[CEMIP]] | B | SYT13 activity raises CEMIP's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 3.50× lower at baseline in the lines without SYT13 | 0.025 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[CARD10]] | B | SYT13 activity raises CARD10's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without SYT13 | 0.027 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[MGAT4A]] | B | SYT13 activity raises MGAT4A's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without SYT13 | 0.037 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[PLEK2]] | B | SYT13 activity raises PLEK2's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 3.82× lower at baseline in the lines without SYT13 | 0.042 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[KIF9-AS1]] | B | SYT13 activity lowers KIF9-AS1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.36× higher at baseline in the lines without SYT13 | 0.043 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[COBLL1]] | B | SYT13 activity raises COBLL1's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without SYT13 | 0.050 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[HAS3]] | B | SYT13 activity raises HAS3's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without SYT13 | 0.051 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | SYT13 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express SYT13 (33) vs lines expressing it (15) | the lines without SYT13: 1.20× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[ITGA6]] | B | SYT13 activity raises ITGA6's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without SYT13 | 0.068 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[WNT7B]] | B | SYT13 activity raises WNT7B's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.89× lower at baseline in the lines without SYT13 | 0.068 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[FAM107B]] | B | SYT13 activity raises FAM107B's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 1.75× lower at baseline in the lines without SYT13 | 0.072 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.3, 16.7); signed map (1.3, 45.8). **Vector** length 49.6, 14.2% of its response variance represented; |z| ≥ 3 in 412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:45,240,302-45,286,341 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1427 |
| Gene groups (HGNC) | Synaptotagmins |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L8C5](https://www.uniprot.org/uniprotkb/Q7L8C5) (Synaptotagmin-13):

> May be involved in transport vesicle docking to the plasma membrane.

**Summary**, from NCBI Gene [57586](https://www.ncbi.nlm.nih.gov/gene/57586):

> This gene encodes a member of the large synaptotagmin protein family. Family members have an extracellular N-terminal transmembrane domain and a cytoplasmic C terminus with two tandem C2 domains (C2A and C2B). Synaptotogmin family members can form homo- and heteromeric complexes with each other. They also have different biochemical properties and developmental profiles, and patterns of tissue distribution. Synaptotagmins function as membrane traffickers in multicellular organisms. Two …

**Accessions** — [HGNC:14962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14962) · Entrez [57586](https://www.ncbi.nlm.nih.gov/gene/57586) · UniProt [Q7L8C5](https://www.uniprot.org/uniprotkb/Q7L8C5) · Ensembl [ENSG00000019505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019505)

## Data

Gene col 313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 313); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 313]; `tensor/DDL_lfc|DDL_z.npy` [313]; `embed/gene_vectors.npy` [313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 313 or target_col == 313). Every well: [[SYT13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
