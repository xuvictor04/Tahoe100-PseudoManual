---
symbol: "DNAJC15"
type: "gene"
col: 4201
ensembl_id: "ENSG00000120675"
name: "DnaJ heat shock protein family (Hsp40) member C15"
location: "13q14.11"
module: 55
arm: "+"
pooled_cpm: 58.43
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 18
direction_downstream: 6
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# DNAJC15

*DnaJ heat shock protein family (Hsp40) member C15* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +11.2, q 3e-26, up in 24 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.77× (z +5.2, q 2e-05, up in 17 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.775× (z -7.3, q 2e-10, down in 23 of 38 measured lines) ⚠ cell-cycle shift, explains ~16% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.725× (z -6.5, q 2e-08, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDAR]] (+0.63, fdr 1e-05), [[VILL]] (+0.62, fdr 2e-05), [[LINC01819]] (+0.60, fdr 1e-05); moves opposite to [[TOB2]] (-0.48, fdr 3e-05), [[METTL21A]] (-0.46, fdr 3e-05), [[DGKE]] (-0.46, fdr 6e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[LINC02474]] → it (grade B ⚠); 6 go from it, the strongest it → [[TNFRSF14-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.2 | 3e-26 | 24/37 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.1 | 2e-13 | 17/30 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +6.4 | 3e-08 | 19/34 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +5.2 | 2e-05 | 17/38 (Panc 03.27, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.6 | 4e-04 | 9/37 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.5 | 5e-04 | 11/37 (Hs 766T, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +4.3 | 0.001 | 14/38 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.004 | 8/37 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.7 | 0.012 | 10/37 (HEC-1-A, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.013 | 11/37 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.027 | 14/37 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.036 | 9/36 (NCI-H23, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.042 | 6/37 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.052 | 9/36 (AsPC-1, SNU-1, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.081 | 4/36 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.082 | 5/37 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -7.3 | 2e-10 | 23/38 (LS 180, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.719×** | -6.6 | 1e-08 | 21/37 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.725×** | -6.5 | 2e-08 | 21/37 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.727×** | -6.4 | 2e-08 | 21/37 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.733×** | -6.2 | 6e-08 | 21/37 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.739×** | -6.0 | 1e-07 | 21/37 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.755×** | -5.5 | 4e-06 | 21/37 (LS 180, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -5.3 | 9e-06 | 19/37 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.787×** | -4.8 | 9e-05 | 18/37 (SNU-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.829×** | -3.8 | 0.010 | 19/37 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.7 | 0.010 | 18/36 (COLO 205, LS 180, …) | top dose only | composition shift |
| [[Gefitinib (drug)]] 5 µM |  | 0.840× | -3.5 | 0.025 | 8/37 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.844× | -3.4 | 0.028 | 14/37 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.890× | -3.3 | 0.035 | 9/38 (LS 180, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.848× | -3.3 | 0.035 | 8/37 (SW 1088, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.850× | -3.2 | 0.038 | 11/37 (LS 180, HT-29, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.059 | 3/37 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.852× | -3.1 | 0.059 | 8/37 (AsPC-1, LoVo, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.082 | 1/37 (H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 241 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 1,260 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0639× (z -28.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 88.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -10.5) |
| [[SW480 (line)]] | alt | 161 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -16.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 59.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.13× (z +10.3) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 5 µM 0.378× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 29.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0757× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 54.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[Hs 766T (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDAR]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[VILL]] | +0.62 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LINC01819]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[GAREM1]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RNF43]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.57 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[EPS8]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[LINC00511]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LINC02331]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[KCTD14]] | +0.56 | +0.60 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOB2]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[METTL21A]] | -0.46 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[DGKE]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[NOG]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[CCSAP]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02474]] | B | LINC02474 activity raises DNAJC15's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.35× lower at baseline in the lines without LINC02474 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[LINC01559]] | B | LINC01559 activity raises DNAJC15's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 3.43× lower at baseline in the lines without LINC01559 | 0.018 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[NPSR1-AS1]] | B | NPSR1-AS1 activity raises DNAJC15's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without NPSR1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[PLCH1]] | B | PLCH1 activity strengthens DNAJC15's drug response | lines that do not express PLCH1 (10) vs lines expressing it (28) | the lines without PLCH1 respond 0.78× as strongly (z diff +0.77); strongest at Idarubicin (hydrochloride) 5 µM: 0.95x vs 0.65x (z diff +3.3) | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[PCK1]] | B | PCK1 activity strengthens DNAJC15's drug response | lines that do not express PCK1 (30) vs lines expressing it (8) | the lines without PCK1 respond 0.46× as strongly (z diff +2.57); strongest at Panobinostat 5 µM: 0.74x vs 0.29x (z diff +5.6) | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; target measured in part of the lines; artifact flags |
| [[SULT1C2]] | B | SULT1C2 activity raises DNAJC15's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without SULT1C2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[TMEM139]] | B | TMEM139 activity raises DNAJC15's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without TMEM139 | 0.054 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[LINC02331]] | B | LINC02331 activity raises DNAJC15's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without LINC02331 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises DNAJC15's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without TSPOAP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[FOXQ1]] | B | FOXQ1 activity strengthens DNAJC15's drug response | lines that do not express FOXQ1 (22) vs lines expressing it (16) | the lines without FOXQ1 respond 0.52× as strongly (z diff +1.86); strongest at Belinostat 5 µM: 0.80x vs 0.43x (z diff +3.8) | 0.063 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; target measured in part of the lines; artifact flags |
| [[CLRN3]] | B | CLRN3 activity raises DNAJC15's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.40× lower at baseline in the lines without CLRN3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[RASSF6]] | B | RASSF6 activity strengthens DNAJC15's drug response | lines that do not express RASSF6 (21) vs lines expressing it (17) | the lines without RASSF6 respond 0.54× as strongly (z diff +1.58); strongest at Idarubicin (hydrochloride) 5 µM: 0.90x vs 0.54x (z diff +4.1) | 0.069 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; target measured in part of the lines; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | B | DNAJC15 activity raises TNFRSF14-AS1's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without DNAJC15 | 0.029 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[PELI1]] | B | DNAJC15 activity raises PELI1's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without DNAJC15 | 0.044 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[FUT2]] | B | DNAJC15 activity raises FUT2's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without DNAJC15 | 0.055 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[PLAC8]] | B | DNAJC15 activity raises PLAC8's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without DNAJC15 | 0.060 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[TMPRSS2]] | B | DNAJC15 activity raises TMPRSS2's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without DNAJC15 | 0.091 | ⚠ within organs, on part of the lines; also absent: VILL |
| [[B3GNT3]] | B | DNAJC15 activity raises B3GNT3's level | lines that do not express DNAJC15 (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without DNAJC15 | 0.094 | ⚠ within organs, on part of the lines; also absent: VILL |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.9, 44.4); signed map (62.5, 10.0). **Vector** length 84.3, 19.4% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -6.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.1 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:43,023,203-43,114,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCJ; previously DNAJD1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5T4](https://www.uniprot.org/uniprotkb/Q9Y5T4) (DnaJ homolog subfamily C member 15):

> Negative regulator of the mitochondrial respiratory chain. Prevents mitochondrial hyperpolarization state and restricts mitochondrial generation of ATP (By similarity). Acts as an import component of the TIM23 translocase complex. Stimulates the ATPase activity of HSPA9.

**Summary**, from NCBI Gene [29103](https://www.ncbi.nlm.nih.gov/gene/29103):

> Predicted to enable ATPase activator activity. Predicted to be involved in protein import into mitochondrial matrix. Predicted to act upstream of or within several processes, including cellular response to starvation; negative regulation of mitochondrial electron transport, NADH to ubiquinone; and negative regulation of protein-containing complex assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20325) · Entrez [29103](https://www.ncbi.nlm.nih.gov/gene/29103) · UniProt [Q9Y5T4](https://www.uniprot.org/uniprotkb/Q9Y5T4) · Ensembl [ENSG00000120675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120675)

## Data

Gene col 4201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4201); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4201]; `tensor/DDL_lfc|DDL_z.npy` [4201]; `embed/gene_vectors.npy` [4201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4201 or target_col == 4201). Every well: [[DNAJC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
