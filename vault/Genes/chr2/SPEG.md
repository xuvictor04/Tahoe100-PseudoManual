---
symbol: "SPEG"
type: "gene"
col: 1011
ensembl_id: "ENSG00000072195"
name: "striated muscle enriched protein kinase"
location: "2q35"
module: 132
arm: "+"
pooled_cpm: 6.34
n_lines_expressing: 34
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SPEG

*striated muscle enriched protein kinase* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.84× (z +6.7, q 9e-09, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +5.0, q 1e-04, up in 8 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.462× (z -12.5, q 5e-33, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAYN]] (+0.58, fdr 2e-05), [[ANXA6]] (+0.57, fdr 3e-05), [[LINC02377]] (+0.53, fdr 5e-05); moves opposite to [[THRB]] (-0.47, fdr 1e-04), [[POU5F1B]] (-0.44, fdr 2e-04), [[PHC2-AS1]] (-0.43, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC01615]] → it (grade B ⚠); 14 go from it, the strongest it → [[SLC4A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.7 | 9e-09 | 3/9 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 1e-04 | 8/31 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 2e-04 | 9/29 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.4 | 0.002 | 3/10 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.011 | 10/29 (LoVo, NCI-H23, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.7 | 0.018 | 4/16 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.025 | 6/30 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.025 | 6/26 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.31× | +3.1 | 0.11 | 7/32 (A-172, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.462×** | -12.5 | 5e-33 | 21/26 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.363×** | -11.6 | 2e-28 | 27/32 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.431×** | -9.6 | 1e-19 | 20/29 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.463×** | -8.8 | 2e-16 | 20/26 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.498×** | -7.9 | 2e-13 | 22/29 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.533×** | -7.2 | 6e-11 | 17/29 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.9 | 4e-10 | 14/27 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.661×** | -6.7 | 2e-09 | 16/27 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -6.0 | 2e-07 | 16/26 (H4, SW 900, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.590×** | -5.8 | 4e-07 | 13/30 (Panc 03.27, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.611×** | -5.6 | 1e-06 | 14/31 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -5.2 | 8e-06 | 11/24 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -5.1 | 2e-05 | 10/30 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -4.8 | 6e-05 | 15/29 (LOX-IMVI, RPMI-7951, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.667×** | -4.6 | 1e-04 | 9/29 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -4.4 | 3e-04 | 12/30 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.007 | 7/26 (SHP-77, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.664×** | -3.3 | 0.023 | 5/31 (LOX-IMVI, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.592×** | -3.1 | 0.044 | 5/29 (SW 900, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.052 | 10/31 (SNU-423, A-172, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.757×** | -3.0 | 0.053 | 4/31 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (drug)]] 0.05 µM |  | **0.772×** | -2.9 | 0.069 | 7/31 (SW1417, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 51.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.4) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -12.9) |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.3) |
| [[H4 (line)]] | wt | 17.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0512× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.5) |
| [[SW480 (line)]] | alt | 4.43 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0947× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.9) |
| [[A-427 (line)]] | wt | 5.27 | 0 | 1 | — | [[MK-8353 (drug)]] 0.05 µM 0.0646× (z -9.7) |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 5.04 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0872× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0665× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 4.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -9.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAYN]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[ANXA6]] | +0.57 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[LINC02377]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[NSFL1C]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[KIF3C]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[USP35]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SNPH]] | +0.52 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SHKBP1]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RASSF2]] | +0.52 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[ZBTB17]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SLC4A3]] | +0.51 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PTPRN]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THRB]] | -0.47 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[POU5F1B]] | -0.44 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PHC2-AS1]] | -0.43 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[PCAT1]] | -0.42 | -0.29 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01615]] | B | LINC01615 activity raises SPEG's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 3.18× lower at baseline in the lines without LINC01615 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[FAM167A]] | B | FAM167A activity raises SPEG's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.86× lower at baseline in the lines without FAM167A | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SOGA3]] | B | SOGA3 activity raises SPEG's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without SOGA3 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[TOP2A]] | B | TOP2A activity raises SPEG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SARDH]] | B | SARDH activity raises SPEG's level | lines that do not express SARDH (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without SARDH | 0.057 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[ADAMTS12]] | B | ADAMTS12 activity raises SPEG's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.92× lower at baseline in the lines without ADAMTS12 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[APBB1IP]] | B | APBB1IP activity raises SPEG's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without APBB1IP | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[COL6A2]] | C | COL6A2 activity raises SPEG's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without COL6A2 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; co-absent with the target |
| [[KIAA0408]] | C | KIAA0408 activity raises SPEG's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 3.09× lower at baseline in the lines without KIAA0408 | 0.023 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises SPEG's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.01× lower at baseline in the lines without MAP1A | 0.045 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[MGAT5B]] | C | MGAT5B activity raises SPEG's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 3.20× lower at baseline in the lines without MGAT5B | 0.060 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SPEG activity raises SLC4A3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without SPEG | 0.019 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[SEPTIN5]] | B | SPEG activity raises SEPTIN5's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without SPEG | 0.042 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[KIF3C]] | B | SPEG activity raises KIF3C's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without SPEG | 0.053 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[L1CAM]] | B | SPEG activity raises L1CAM's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without SPEG | 0.053 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[SOGA3]] | B | SPEG activity raises SOGA3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.86× lower at baseline in the lines without SPEG | 0.059 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[ANXA6]] | B | SPEG activity raises ANXA6's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without SPEG | 0.065 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[MAPRE3]] | B | SPEG activity raises MAPRE3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without SPEG | 0.069 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[FAM167A]] | B | SPEG activity raises FAM167A's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without SPEG | 0.074 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[ARMCX2]] | B | SPEG activity raises ARMCX2's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without SPEG | 0.076 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[CCDC136]] | C | SPEG activity raises CCDC136's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without SPEG | 0.055 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1; co-absent with the target |
| [[COL6A2]] | C | SPEG activity raises COL6A2's level | lines that do not express SPEG (16) vs lines expressing it (34) | 5.31× lower at baseline in the lines without SPEG | 0.064 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1; co-absent with the target |
| [[MGAT5B]] | C | SPEG activity raises MGAT5B's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without SPEG | 0.065 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.9, 42.4); signed map (-7.1, 22.8). **Vector** length 52.1, 9.13% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +0.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -9.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.8 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | striated muscle enriched protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,434,843-219,493,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12676, KIAA1297, SPEGalpha, SPEGbeta, BPEG, MYLK6; previously APEG1 |
| Gene groups (HGNC) | I-set domain containing; Myosin light chain kinase family |
| Hallmark sets | MYOGENESIS, APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15772](https://www.uniprot.org/uniprotkb/Q15772) (Striated muscle preferentially expressed protein kinase):

> Isoform 3 may have a role in regulating the growth and differentiation of arterial smooth muscle cells.

**Summary**, from NCBI Gene [10290](https://www.ncbi.nlm.nih.gov/gene/10290):

> This gene encodes a protein with similarity to members of the myosin light chain kinase family. This protein family is required for myocyte cytoskeletal development. Along with the desmin gene, expression of this gene may be controlled by the desmin locus control region. Mutations in this gene are associated with centronuclear myopathy 5. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:16901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16901) · Entrez [10290](https://www.ncbi.nlm.nih.gov/gene/10290) · UniProt [Q15772](https://www.uniprot.org/uniprotkb/Q15772) · Ensembl [ENSG00000072195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072195)

## Data

Gene col 1011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1011); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1011]; `tensor/DDL_lfc|DDL_z.npy` [1011]; `embed/gene_vectors.npy` [1011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1011 or target_col == 1011). Every well: [[SPEG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPEG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
