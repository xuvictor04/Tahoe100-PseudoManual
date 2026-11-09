---
symbol: "FLT1"
type: "gene"
col: 2267
ensembl_id: "ENSG00000102755"
name: "fms related receptor tyrosine kinase 1"
location: "13q12.3"
module: 84
arm: "+"
pooled_cpm: 12.19
n_lines_expressing: 22
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# FLT1

*fms related receptor tyrosine kinase 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +15.1, q 0e+00, up in 9 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.485× (z -6.6, q 1e-08, down in 11 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1549L]] (+0.66, fdr 7e-06), [[COL13A1]] (+0.64, fdr 7e-06), [[SPRY4]] (+0.62, fdr 7e-06); moves opposite to [[KIF13A]] (-0.47, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RNF152]] → it (grade B ⚠); 19 go from it, the strongest it → [[FURIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +15.1 | 0e+00 | 9/17 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +11.5 | 2e-28 | 3/14 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +11.2 | 1e-26 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +9.3 | 1e-18 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.1 | 5e-14 | 7/18 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.6 | 2e-06 | 8/18 (HCT15, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.4 | 0.001 | 3/18 (SK-MEL-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.1 | 0.003 | 0/14 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.003 | 7/18 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.9 | 0.005 | 3/10 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.11 | 3/17 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.36× | +3.0 | 0.12 | 9/19 (C32, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.485×** | -6.6 | 1e-08 | 11/18 (C32, HOP62, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.629×** | -6.6 | 1e-08 | 13/18 (C32, RPMI-7951, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.517×** | -6.3 | 4e-08 | 14/18 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.546×** | -6.3 | 6e-08 | 15/19 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.637×** | -5.7 | 2e-06 | 14/18 (A-172, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.618×** | -5.2 | 2e-05 | 14/19 (A-172, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.651×** | -4.9 | 7e-05 | 11/18 (NCI-H1573, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.623×** | -4.7 | 2e-04 | 13/19 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -4.4 | 6e-04 | 9/18 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.730×** | -4.3 | 8e-04 | 9/18 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.451×** | -4.1 | 0.003 | 8/18 (A-172, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.642×** | -4.0 | 0.004 | 9/18 (C32, A-172, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.674×** | -3.8 | 0.006 | 7/18 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.695×** | -3.6 | 0.011 | 13/18 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[crizotinib (drug)]] 5 µM |  | **0.691×** | -3.6 | 0.014 | 6/18 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.705×** | -3.5 | 0.017 | 12/18 (C32, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 140 | 0 | 11 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0584× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 26.4 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0318× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~85% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0397× (z -12.3) |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 5 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.161× (z -11.3) |
| [[C32 (line)]] | wt | 49.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.182× (z -9.0) |
| [[LoVo (line)]] | wt | 50.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0343× (z -12.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[J82 (line)]] | alt | 54.6 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.151× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.2) | — |
| [[A-427 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1549L]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SH2B3]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.58 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[HS3ST3A1]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PTPN12]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PHC2]] | +0.58 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[HTR7]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NLRP3]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.47 | -0.36 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | RNF152 activity raises FLT1's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without RNF152 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[SDC2]] | C | SDC2 activity raises FLT1's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without SDC2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[CAMK4]] | C | CAMK4 activity raises FLT1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without CAMK4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises FLT1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without COL15A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[SHC4]] | C | SHC4 activity raises FLT1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.63× lower at baseline in the lines without SHC4 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FURIN]] | B | FLT1 activity raises FURIN's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without FLT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[A3GALT2]] | B | FLT1 activity raises A3GALT2's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without FLT1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[COL13A1]] | B | FLT1 activity raises COL13A1's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without FLT1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[ARHGAP31]] | B | FLT1 activity raises ARHGAP31's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.88× lower at baseline in the lines without FLT1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[CYGB]] | B | FLT1 activity raises CYGB's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without FLT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[REP15]] | B | FLT1 activity raises REP15's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without FLT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[SH2B3]] | B | FLT1 activity raises SH2B3's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without FLT1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[PGF]] | B | FLT1 activity weakens PGF's drug response | lines that do not express FLT1 (20) vs lines expressing it (15) | the lines without FLT1 respond 5.67× as strongly (z diff -2.37); strongest at Dinaciclib 0.5 µM: 0.91x vs 0.20x (z diff -6.4) | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB; target measured in part of the lines; artifact flags |
| [[BOC]] | B | FLT1 activity raises BOC's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without FLT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[COL23A1]] | B | FLT1 activity raises COL23A1's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without FLT1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[LOXL3]] | B | FLT1 activity raises LOXL3's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without FLT1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[SDC2]] | C | FLT1 activity raises SDC2's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 5.82× lower at baseline in the lines without FLT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.9, 6.8); signed map (6.9, 50.1). **Vector** length 74.6, 24.1% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.6 | -6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | fms related receptor tyrosine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:28,300,346-28,495,145 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VEGFR1; previously FLT |
| Gene groups (HGNC) | V-set domain containing; I-set domain containing; VEGF receptor tyrosine kinase family |
| Reactome | 7 pathways, smallest: Neuropilin interactions with VEGF and VEGFR; VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P17948](https://www.uniprot.org/uniprotkb/P17948) (Vascular endothelial growth factor receptor 1):

> Tyrosine-protein kinase that acts as a cell-surface receptor for VEGFA, VEGFB and PGF, and plays an essential role in the development of embryonic vasculature, the regulation of angiogenesis, cell survival, cell migration, macrophage function, chemotaxis, and cancer cell invasion. Acts as a positive regulator of postnatal retinal hyaloid vessel regression (By similarity). May play an essential role as a negative regulator of embryonic angiogenesis by inhibiting excessive proliferation of …

**Summary**, from NCBI Gene [2321](https://www.ncbi.nlm.nih.gov/gene/2321):

> This gene encodes a member of the vascular endothelial growth factor receptor (VEGFR) family. VEGFR family members are receptor tyrosine kinases (RTKs) which contain an extracellular ligand-binding region with seven immunoglobulin (Ig)-like domains, a transmembrane segment, and a tyrosine kinase (TK) domain within the cytoplasmic domain. This protein binds to VEGFR-A, VEGFR-B and placental growth factor and plays an important role in angiogenesis and vasculogenesis. Expression of this receptor …

**Accessions** — [HGNC:3763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3763) · Entrez [2321](https://www.ncbi.nlm.nih.gov/gene/2321) · UniProt [P17948](https://www.uniprot.org/uniprotkb/P17948) · Ensembl [ENSG00000102755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102755)

## Data

Gene col 2267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2267); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2267]; `tensor/DDL_lfc|DDL_z.npy` [2267]; `embed/gene_vectors.npy` [2267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2267 or target_col == 2267). Every well: [[FLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
