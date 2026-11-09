---
symbol: "DEPDC7"
type: "gene"
col: 4287
ensembl_id: "ENSG00000121690"
name: "DEP domain containing 7"
location: "11p13"
module: 72
arm: "+"
pooled_cpm: 8.76
n_lines_expressing: 37
n_dd_up: 35
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# DEPDC7

*DEP domain containing 7* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.48× (z +20.3, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.695× (z -4.9, q 4e-04, down in 15 of 33 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFAP2C]] (+0.49, fdr 3e-05), [[POU3F2]] (+0.48, fdr 5e-04), [[MAP3K1]] (+0.48, fdr 5e-05); moves opposite to [[VTI1A]] (-0.52, fdr 2e-05), [[ZC3H3]] (-0.51, fdr 3e-05), [[SARM1]] (-0.49, fdr 1e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[AAK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.48×** | +20.3 | 0e+00 | 32/34 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +19.3 | 0e+00 | 27/30 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +18.6 | 0e+00 | 23/27 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.61×** | +17.3 | 0e+00 | 32/34 (PANC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.53×** | +17.1 | 0e+00 | 31/34 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +14.2 | 9e-44 | 26/34 (LoVo, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.61×** | +13.0 | 2e-36 | 27/34 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.28×** | +11.1 | 7e-27 | 21/29 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.25×** | +10.9 | 5e-26 | 22/34 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +10.8 | 2e-25 | 25/32 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +10.6 | 1e-24 | 15/24 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +10.6 | 1e-24 | 18/28 (LS 180, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.01×** | +9.0 | 6e-18 | 14/29 (A498, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.93×** | +8.5 | 6e-16 | 15/26 (SNU-423, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +7.7 | 5e-13 | 17/30 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +7.2 | 2e-11 | 20/33 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.9 | 2e-10 | 15/33 (A498, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 8e-10 | 15/33 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.40×** | +6.2 | 2e-08 | 10/33 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.8 | 2e-07 | 9/35 (A-172, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 1e-05 | 8/33 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.695×** | -4.9 | 4e-04 | 15/33 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -4.7 | 6e-04 | 10/33 (SW1417, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.703×** | -4.6 | 8e-04 | 10/30 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.808×** | -4.1 | 0.006 | 9/35 (SW 1271, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.803×** | -4.0 | 0.006 | 6/34 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.048 | 9/34 (SNU-423, LoVo, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.080 | 4/29 (NCI-H1792, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 34.9 | 2 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.175× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.411× (z -10.4) |
| [[A498 (line)]] | wt | 28.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 14.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.99 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0605× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 7.84 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.5) | — |
| [[A-172 (line)]] | wt | 6.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +9.3) | — |
| [[A549 (line)]] | wt | 6.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 7.65 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0723× (z -10.1) |
| [[C32 (line)]] | wt | 3.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 4.69 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0756× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0682× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 3.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 56.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.992 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAP2C]] | +0.49 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[POU3F2]] | +0.48 | +0.24 / +0.48 | both halves | 5e-04 |  |
| [[MAP3K1]] | +0.48 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[POLH]] | +0.48 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[POLR2L]] | +0.46 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CDC14A]] | +0.45 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[ZNF217]] | +0.44 | +0.29 / +0.46 | both halves | 3e-04 |  |
| [[SERTAD4]] | +0.44 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[LYPD1]] | +0.44 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[PCNA]] | +0.44 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[CLEC11A]] | +0.43 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[FBXL5]] | +0.42 | +0.45 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTI1A]] | -0.52 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ZC3H3]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SARM1]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[GTPBP2]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PCYT1A]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CUL4A]] | -0.47 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[HSPA9]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ATP9B]] | -0.46 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[TANGO2]] | -0.45 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GCLM]] | -0.45 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[ZNF771]] | -0.45 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SLC38A7]] | -0.45 | -0.24 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DEPDC7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HTATIP2]] | B | HTATIP2 activity lowers DEPDC7's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without HTATIP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AAK1]] | B | DEPDC7 activity raises AAK1's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.45× lower at baseline in the lines without DEPDC7 | 0.048 | ⚠ within organs, on part of the lines |
| [[SERTAD4]] | B | DEPDC7 activity lowers SERTAD4's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.65× higher at baseline in the lines without DEPDC7 | 0.053 | ⚠ within organs, on part of the lines |
| [[FBXL5]] | B | DEPDC7 activity lowers FBXL5's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.29× higher at baseline in the lines without DEPDC7 | 0.059 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction -0.396). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 40.6); signed map (44.7, -2.0). **Vector** length 58.6, 10.1% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +19.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +1.9 | +11.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,015,876-33,033,582 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DEP domain containing |
| Matched by | ensembl_id |

UniProt [Q96QD5](https://www.uniprot.org/uniprotkb/Q96QD5) carries no function annotation.

**Summary**, from NCBI Gene [91614](https://www.ncbi.nlm.nih.gov/gene/91614):

> Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29899) · Entrez [91614](https://www.ncbi.nlm.nih.gov/gene/91614) · UniProt [Q96QD5](https://www.uniprot.org/uniprotkb/Q96QD5) · Ensembl [ENSG00000121690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121690)

## Data

Gene col 4287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4287); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4287]; `tensor/DDL_lfc|DDL_z.npy` [4287]; `embed/gene_vectors.npy` [4287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4287 or target_col == 4287). Every well: [[DEPDC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPDC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
