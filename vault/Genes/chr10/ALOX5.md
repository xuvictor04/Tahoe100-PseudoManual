---
symbol: "ALOX5"
type: "gene"
col: 259
ensembl_id: "ENSG00000012779"
name: "arachidonate 5-lipoxygenase"
location: "10q11.21"
module: 8
arm: "+"
pooled_cpm: 9.39
n_lines_expressing: 22
n_dd_up: 35
n_dd_down: 14
n_dd_up_clean: 29
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 81
direction_downstream: 101
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ALOX5

*arachidonate 5-lipoxygenase* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.17× (z +23.2, q 0e+00, up in 19 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.592× (z -5.8, q 3e-06, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.77, fdr 7e-06), [[MUC4]] (+0.75, fdr 7e-06), [[ADGRF1]] (+0.75, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); 101 go from it, the strongest it → [[LINC01504]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.17×** | +23.2 | 0e+00 | 19/20 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.37×** | +14.0 | 7e-42 | 17/18 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.14×** | +13.1 | 4e-37 | 15/20 (A549, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +11.8 | 9e-30 | 1/14 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +11.5 | 1e-28 | 2/9 (HT-29, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +10.2 | 2e-22 | 10/20 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +10.1 | 4e-22 | 13/20 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +9.6 | 4e-20 | 11/20 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +8.0 | 6e-14 | 2/10 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +6.0 | 1e-07 | 11/20 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.70×** | +5.8 | 3e-07 | 11/20 (AsPC-1, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +5.3 | 7e-06 | 10/20 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 7e-06 | 11/20 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 7e-06 | 2/18 (LS 180, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +5.2 | 9e-06 | 8/19 (LS 180, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 5e-05 | 10/20 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.6 | 1e-04 | 10/20 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.52×** | +4.6 | 2e-04 | 11/19 (AsPC-1, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.592×** | -5.8 | 3e-06 | 13/18 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -5.5 | 1e-05 | 10/20 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -4.9 | 2e-04 | 13/18 (Panc 03.27, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.653×** | -4.7 | 3e-04 | 8/20 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.688×** | -4.3 | 0.002 | 0/20 | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -4.0 | 0.005 | 6/20 (LoVo, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -3.7 | 0.017 | 7/20 (Panc 03.27, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.018 | 11/20 (LoVo, SW1417, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.6 | 0.020 | 4/20 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | **0.563×** | -3.5 | 0.030 | 1/20 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.751×** | -3.3 | 0.044 | 13/20 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.044 | 5/20 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.827×** | -3.1 | 0.075 | 1/20 (NCI-H2347) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -3.1 | 0.075 | 8/18 (Panc 03.27, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Cilostazol (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.081 | 1/20 (H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 61.7 | 7 | 5 (2 ⚠) | [[Elimusertib hydrochloride (drug)]] 0.05 µM 6.02× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.134× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 69.3 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -26.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0769× (z -26.3) |
| [[LoVo (line)]] | wt | 69.1 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -25.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -12.3) |
| [[HT-29 (line)]] | alt | 44.9 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0939× (z -23.6) |
| [[LS 180 (line)]] | wt | 24.3 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.84× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.170× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.2) |
| [[A498 (line)]] | wt | 4.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.78× (z +8.9) | — |
| [[A549 (line)]] | wt | 7.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 5.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 9.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 5.06 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.33× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 5.95 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -15.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HHLA2]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TMC5]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MYH14]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MMP7]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 6, C 75. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises ALOX5's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without CGN | 0.045 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ALOX5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without ELF3-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[BICDL2]] | B | BICDL2 activity raises ALOX5's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without BICDL2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[SCIN]] | B | SCIN activity raises ALOX5's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without SCIN | 0.056 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[ATP8B1]] | B | ATP8B1 activity raises ALOX5's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without ATP8B1 | 0.070 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[P2RY6]] | B | P2RY6 activity raises ALOX5's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without P2RY6 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[SYNPR-AS1]] | C | SYNPR-AS1 activity raises ALOX5's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.90× lower at baseline in the lines without SYNPR-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises ALOX5's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.00× lower at baseline in the lines without SLC44A4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises ALOX5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.51× lower at baseline in the lines without ADGRF1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises ALOX5's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.34× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises ALOX5's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.89× lower at baseline in the lines without MUC13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises ALOX5's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.01× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |

### Downstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 26, C 75. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01504]] | B | ALOX5 activity raises LINC01504's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.08× lower at baseline in the lines without ALOX5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[FUT2]] | B | ALOX5 activity raises FUT2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without ALOX5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[CD2AP]] | B | ALOX5 activity raises CD2AP's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without ALOX5 | 0.002 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[MUC20]] | B | ALOX5 activity raises MUC20's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without ALOX5 | 0.003 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ELF3-AS1]] | B | ALOX5 activity raises ELF3-AS1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without ALOX5 | 0.003 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[LGALS9]] | B | ALOX5 activity raises LGALS9's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.67× lower at baseline in the lines without ALOX5 | 0.004 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[CARD14]] | B | ALOX5 activity raises CARD14's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without ALOX5 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[SCIN]] | B | ALOX5 activity raises SCIN's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without ALOX5 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ASS1]] | B | ALOX5 activity raises ASS1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without ALOX5 | 0.007 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[FZD5]] | B | ALOX5 activity raises FZD5's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without ALOX5 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[TSPAN3]] | B | ALOX5 activity raises TSPAN3's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.59× lower at baseline in the lines without ALOX5 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[CGN]] | B | ALOX5 activity raises CGN's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.29× lower at baseline in the lines without ALOX5 | 0.010 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 55.0); signed map (59.7, 4.0). **Vector** length 82.4, 27.3% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.56 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +23.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +5.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -5.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -4.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | arachidonate 5-lipoxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:45,374,176-45,446,119 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 5-LOX |
| Gene groups (HGNC) | Arachidonate lipoxygenases |
| Reactome | 21 pathways, smallest: Biosynthesis of E-series 18(R)-resolvins; Biosynthesis of Lipoxins (LX); Biosynthesis of aspirin-triggered D-series resolvins |
| Matched by | ensembl_id |

**Function**, from UniProt [P09917](https://www.uniprot.org/uniprotkb/P09917) (Polyunsaturated fatty acid 5-lipoxygenase):

> Catalyzes the oxygenation of arachidonate ((5Z,8Z,11Z,14Z)-eicosatetraenoate) to 5-hydroperoxyeicosatetraenoate (5-HPETE) followed by the dehydration to 5,6- epoxyeicosatetraenoate (Leukotriene A4/LTA4), the first two steps in the biosynthesis of leukotrienes, which are potent mediators of inflammation. Also catalyzes the oxygenation of arachidonate into 8-hydroperoxyicosatetraenoate (8-HPETE) and 12-hydroperoxyicosatetraenoate (12-HPETE). Displays lipoxin synthase activity being able to …

**Summary**, from NCBI Gene [240](https://www.ncbi.nlm.nih.gov/gene/240):

> This gene encodes a member of the lipoxygenase gene family and plays a dual role in the synthesis of leukotrienes from arachidonic acid. The encoded protein, which is expressed specifically in bone marrow-derived cells, catalyzes the conversion of arachidonic acid to 5(S)-hydroperoxy-6-trans-8,11,14-cis-eicosatetraenoic acid, and further to the allylic epoxide 5(S)-trans-7,9-trans-11,14-cis-eicosatetrenoic acid (leukotriene A4). Leukotrienes are important mediators of a number of inflammatory …

**Accessions** — [HGNC:435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:435) · Entrez [240](https://www.ncbi.nlm.nih.gov/gene/240) · UniProt [P09917](https://www.uniprot.org/uniprotkb/P09917) · Ensembl [ENSG00000012779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012779)

## Data

Gene col 259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 259); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 259]; `tensor/DDL_lfc|DDL_z.npy` [259]; `embed/gene_vectors.npy` [259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 259 or target_col == 259). Every well: [[ALOX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALOX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
