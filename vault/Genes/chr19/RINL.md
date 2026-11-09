---
symbol: "RINL"
type: "gene"
col: 11964
ensembl_id: "ENSG00000187994"
name: "Ras and Rab interactor like"
location: "19q13.2"
module: 47
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# RINL

*Ras and Rab interactor like* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +10.8, q 3e-24, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.508× (z -6.8, q 7e-09, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP30]] (+0.70, fdr 7e-06), [[TMC4]] (+0.64, fdr 1e-05), [[ADCY4]] (+0.64, fdr 1e-05); moves opposite to [[ELAC2]] (-0.55, fdr 1e-05), [[MACROH2A1]] (-0.49, fdr 3e-05), [[L3HYPDH]] (-0.48, fdr 6e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[RORC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.8 | 3e-24 | 17/30 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +9.8 | 4e-20 | 4/6 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +9.6 | 2e-19 | 13/17 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +9.2 | 4e-18 | 27/44 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +8.1 | 9e-14 | 6/9 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.2 | 4e-11 | 10/16 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +7.1 | 1e-10 | 11/31 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.6 | 4e-09 | 6/24 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +5.5 | 3e-06 | 19/41 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.003 | 7/41 (A549, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.0 | 0.004 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.5 | 0.019 | 5/16 (NCI-H2347, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.024 | 2/46 (NCI-H2030, HOP62) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.067 | 4/23 (A498, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +3.1 | 0.072 | 8/43 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.074 | 5/35 (A-172, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.091 | 7/41 (Hs 766T, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.094 | 6/37 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.094 | 4/29 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.095 | 1/24 (A-172) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.095 | 2/24 (A-172, A-427) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -6.8 | 7e-09 | 22/39 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.644×** | -4.4 | 0.003 | 10/34 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -3.9 | 0.016 | 13/37 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.698×** | -3.6 | 0.044 | 9/44 (A-427, A549, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.705×** | -3.5 | 0.052 | 16/35 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 7.39 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.148× (z -9.3) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 4.18 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0808× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 4.26 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0734× (z -8.7) ⚠ cell-cycle shift, explains ~2% of this change |
| [[PANC-1 (line)]] | alt | 2.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +10.8) | — |
| [[A-172 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP30]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TMC4]] | +0.64 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.64 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GP6]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MROH3P]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FAM177B]] | +0.56 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[MOGAT3]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[HPN]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[PDE4C]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RAP1GAP]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[STARD10]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAC2]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MACROH2A1]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[L3HYPDH]] | -0.48 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[MTOR]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CAPRIN1]] | -0.48 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[R3HDM1]] | -0.47 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORC]] | B | RORC activity weakens RINL's drug response | lines that do not express RORC (27) vs lines expressing it (17) | the lines without RORC respond 3.17× as strongly (z diff -1.72); strongest at Idarubicin (hydrochloride) 5 µM: 3.10x vs 0.70x (z diff -6.4) | 0.005 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; target measured in part of the lines; artifact flags |
| [[RORC]] | B | RORC activity raises RINL's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without RORC | 0.009 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[ADRA2C]] | B | ADRA2C activity lowers RINL's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.48× higher at baseline in the lines without ADRA2C | 0.009 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[LINC03040]] | B | LINC03040 activity raises RINL's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without LINC03040 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[CLDN3]] | B | CLDN3 activity weakens RINL's drug response | lines that do not express CLDN3 (24) vs lines expressing it (20) | the lines without CLDN3 respond 2.16× as strongly (z diff -1.21); strongest at Idarubicin (hydrochloride) 5 µM: 3.11x vs 0.87x (z diff -5.5) | 0.014 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; target measured in part of the lines; the reference differs; artifact flags |
| [[RNF183]] | B | RNF183 activity raises RINL's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without RNF183 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[MROH3P]] | B | MROH3P activity raises RINL's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without MROH3P | 0.028 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[LINC03040]] | B | LINC03040 activity weakens RINL's drug response | lines that do not express LINC03040 (28) vs lines expressing it (16) | the lines without LINC03040 respond 4.58× as strongly (z diff -2.03); strongest at Idarubicin (hydrochloride) 5 µM: 3.04x vs 0.81x (z diff -5.7) | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; target measured in part of the lines; artifact flags |
| [[TMEM45B]] | B | TMEM45B activity raises RINL's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 1.71× lower at baseline in the lines without TMEM45B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[HSH2D]] | B | HSH2D activity raises RINL's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without HSH2D | 0.038 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[ADRA2C]] | B | ADRA2C activity strengthens RINL's drug response | lines that do not express ADRA2C (17) vs lines expressing it (27) | the lines without ADRA2C respond 0.57× as strongly (z diff +0.93); strongest at Homoharringtonine 5 µM: 0.95x vs 1.67x (z diff +2.8) | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B; target measured in part of the lines; both ways; artifact flags |
| [[FUT3]] | B | FUT3 activity weakens RINL's drug response | lines that do not express FUT3 (26) vs lines expressing it (18) | the lines without FUT3 respond 2.39× as strongly (z diff -1.41); strongest at Idarubicin (hydrochloride) 5 µM: 2.63x vs 0.90x (z diff -4.8) | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.367). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 55.7); signed map (57.6, 6.2). **Vector** length 50.5, 6.58% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -6.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Ras and Rab interactor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,867,830-38,878,275 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45909 |
| Gene groups (HGNC) | VPS9 domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZS11](https://www.uniprot.org/uniprotkb/Q6ZS11) (Ras and Rab interactor-like protein):

> Guanine nucleotide exchange factor (GEF) for RAB5A and RAB22A that activates RAB5A and RAB22A by exchanging bound GDP for free GTP. Plays a role in endocytosis via its role in activating Rab family members (By similarity).

**Summary**, from NCBI Gene [126432](https://www.ncbi.nlm.nih.gov/gene/126432):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in endocytosis. Predicted to be located in ruffle. Predicted to be active in cytosol and endocytic vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24795) · Entrez [126432](https://www.ncbi.nlm.nih.gov/gene/126432) · UniProt [Q6ZS11](https://www.uniprot.org/uniprotkb/Q6ZS11) · Ensembl [ENSG00000187994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187994)

## Data

Gene col 11964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11964); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11964]; `tensor/DDL_lfc|DDL_z.npy` [11964]; `embed/gene_vectors.npy` [11964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11964 or target_col == 11964). Every well: [[RINL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RINL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
