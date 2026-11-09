---
symbol: "RASSF6"
type: "gene"
col: 9807
ensembl_id: "ENSG00000169435"
name: "Ras association domain family member 6"
location: "4q13.3"
module: 8
arm: "+"
pooled_cpm: 30.05
n_lines_expressing: 22
n_dd_up: 24
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 86
direction_downstream: 114
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RASSF6

*Ras association domain family member 6* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +11.0, q 3e-25, up in 14 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.617× (z -6.0, q 1e-06, down in 12 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A1CF]] (+0.78, fdr 7e-06), [[TOX3]] (+0.77, fdr 7e-06), [[ELF3-AS1]] (+0.76, fdr 7e-06); moves opposite to [[CROCCP3-1]] (-0.57, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 86 arrows point to it, the strongest [[HGD]] → it (grade B ⚠); 114 go from it, the strongest it → [[EPS8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +11.0 | 3e-25 | 14/20 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +9.6 | 1e-19 | 14/20 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.8 | 2e-16 | 6/20 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +7.6 | 3e-12 | 13/20 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.0 | 3e-10 | 3/14 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 1e-06 | 14/20 (AsPC-1, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +5.5 | 3e-06 | 14/20 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 7e-06 | 12/20 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.1 | 2e-05 | 4/16 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 4e-04 | 13/21 (AsPC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.5 | 4e-04 | 11/20 (AsPC-1, A549, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **2.11×** | +4.3 | 9e-04 | 7/20 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.001 | 8/20 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 4/20 (KATO III, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.009 | 13/20 (AsPC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.013 | 13/20 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.84×** | +3.5 | 0.015 | 8/20 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.017 | 12/20 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -6.0 | 1e-06 | 12/20 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.670×** | -4.8 | 5e-04 | 11/20 (SW480, AsPC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.690×** | -4.6 | 8e-04 | 9/20 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.009 | 10/20 (SW480, HT-29, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.019 | 3/20 (Panc 03.27, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -3.7 | 0.019 | 9/21 (LS 180, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.663×** | -3.6 | 0.023 | 0/20 | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.024 | 11/20 (COLO 205, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.750×** | -3.6 | 0.024 | 9/20 (HEC-1-A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.028 | 9/20 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -3.5 | 0.028 | 16/20 (SW480, SW1417, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -3.4 | 0.030 | 12/20 (LS 180, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.038 | 10/20 (SHP-77, SW480, …) | rises with dose |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.760×** | -3.1 | 0.069 | 1/20 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 185 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0943× (z -23.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.181× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 37.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.0) | — |
| [[COLO 205 (line)]] | alt | 167 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -18.3) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 96.2 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -18.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 118 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 92.1 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 30.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.1) | — |
| [[LoVo (line)]] | wt | 91.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.11× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 8.76 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.148× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A1CF]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.77 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ELF3-AS1]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[ARHGEF38]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[STX19]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[LINC02253]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[RNF43]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[FRK]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 13, C 73. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | HGD activity raises RASSF6's level | lines that do not express HGD (15) vs lines expressing it (35) | 3.44× lower at baseline in the lines without HGD | 0.010 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[AKR1C3]] | B | AKR1C3 activity raises RASSF6's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.87× lower at baseline in the lines without AKR1C3 | 0.012 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[PPARGC1A]] | B | PPARGC1A activity raises RASSF6's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without PPARGC1A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SPATA6L]] | B | SPATA6L activity raises RASSF6's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without SPATA6L | 0.046 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[CHN2]] | B | CHN2 activity raises RASSF6's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without CHN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[SNTB1]] | B | SNTB1 activity raises RASSF6's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without SNTB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[ETS2]] | B | ETS2 activity raises RASSF6's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.94× lower at baseline in the lines without ETS2 | 0.063 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[PLCH1]] | B | PLCH1 activity raises RASSF6's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.66× lower at baseline in the lines without PLCH1 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF703]] | B | ZNF703 activity raises RASSF6's level | lines that do not express ZNF703 (12) vs lines expressing it (38) | 2.50× lower at baseline in the lines without ZNF703 | 0.089 | ⚠ within organs, on part of the lines; also absent: HOXA10; maybe low, not absent |
| [[MAN1A1]] | B | MAN1A1 activity raises RASSF6's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without MAN1A1 | 0.090 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises RASSF6's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without TNFRSF14-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[MAP2K1]] | B | MAP2K1 activity lowers RASSF6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*114 arrows, 114 of them with an alert ⚠; grade A 0, B 41, C 73. Shown: the 12 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8]] | B | RASSF6 activity raises EPS8's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without RASSF6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[SLC44A3]] | B | RASSF6 activity raises SLC44A3's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TMEM184A]] | B | RASSF6 activity raises TMEM184A's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TNFRSF14-AS1]] | B | RASSF6 activity raises TNFRSF14-AS1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[NUDT4]] | B | RASSF6 activity raises NUDT4's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without RASSF6 | 0.004 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[CHN2]] | B | RASSF6 activity raises CHN2's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without RASSF6 | 0.005 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[ZNF703]] | B | RASSF6 activity raises ZNF703's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without RASSF6 | 0.006 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[HGD]] | B | RASSF6 activity raises HGD's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.20× lower at baseline in the lines without RASSF6 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[C4orf19]] | B | RASSF6 activity raises C4orf19's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without RASSF6 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[RHOU]] | B | RASSF6 activity raises RHOU's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without RASSF6 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[EFNA1]] | B | RASSF6 activity raises EFNA1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without RASSF6 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[ETS2]] | B | RASSF6 activity raises ETS2's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without RASSF6 | 0.010 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 50.5); signed map (58.1, 3.5). **Vector** length 83.7, 28.7% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +11.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.5 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,571,550-73,620,631 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ras association domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZTQ3](https://www.uniprot.org/uniprotkb/Q6ZTQ3) (Ras association domain-containing protein 6):

> Involved in the induction of apoptosis, through both caspase-dependent and caspase-independent pathways. May act as a Ras effector protein. May suppress the serum-induced basal levels of NF-kappa-B (By similarity).

**Summary**, from NCBI Gene [166824](https://www.ncbi.nlm.nih.gov/gene/166824):

> This gene encodes a member of the Ras-association domain family (RASSF). Members of this family form the core of a highly conserved tumor suppressor network, the Salvador-Warts-Hippo (SWH) pathway. The protein encoded by this gene is a Ras effector protein that induces apoptosis. A genomic region containing this gene has been linked to susceptibility to viral bronchiolitis. Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:20796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20796) · Entrez [166824](https://www.ncbi.nlm.nih.gov/gene/166824) · UniProt [Q6ZTQ3](https://www.uniprot.org/uniprotkb/Q6ZTQ3) · Ensembl [ENSG00000169435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169435)

## Data

Gene col 9807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9807); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9807]; `tensor/DDL_lfc|DDL_z.npy` [9807]; `embed/gene_vectors.npy` [9807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9807 or target_col == 9807). Every well: [[RASSF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
