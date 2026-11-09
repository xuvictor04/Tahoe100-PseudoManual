---
symbol: "EPHA3"
type: "gene"
col: 501
ensembl_id: "ENSG00000044524"
name: "EPH receptor A3"
location: "3p11.1"
module: 152
arm: "+"
pooled_cpm: 15.6
n_lines_expressing: 24
n_dd_up: 17
n_dd_down: 28
n_dd_up_clean: 15
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# EPHA3

*EPH receptor A3* — 3p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.45× (z +13.7, q 9e-40, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.511× (z -7.2, q 3e-10, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC7]] (+0.71, fdr 7e-06), [[LRP2]] (+0.70, fdr 7e-06), [[PTPRD]] (+0.70, fdr 7e-06).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[FAM13C]] → it (grade B ⚠); 21 go from it, the strongest it → [[TCAF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +13.7 | 9e-40 | 17/22 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +9.0 | 6e-17 | 11/20 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +9.0 | 6e-17 | 13/21 (NCI-H23, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +8.2 | 4e-14 | 15/21 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +8.0 | 2e-13 | 15/21 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +6.3 | 3e-08 | 8/21 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +5.9 | 4e-07 | 16/20 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 3e-04 | 7/20 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.003 | 11/21 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +4.0 | 0.003 | 8/21 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.015 | 5/20 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.022 | 6/22 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.032 | 8/20 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.039 | 4/21 (NCI-H23, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.35×** | +3.2 | 0.047 | 1/16 (J82) | rises with dose | composition shift |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.099 | 0/21 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.511×** | -7.2 | 3e-10 | 17/20 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -6.7 | 5e-09 | 17/20 (C32, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.540×** | -6.6 | 7e-09 | 17/20 (C32, HCT15, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.555×** | -6.3 | 3e-08 | 17/21 (SK-MEL-2, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.665×** | -6.2 | 6e-08 | 15/20 (C32, SHP-77, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -5.7 | 1e-06 | 17/21 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -5.6 | 2e-06 | 19/20 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.599×** | -5.3 | 8e-06 | 12/20 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -4.6 | 2e-04 | 16/21 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -4.6 | 2e-04 | 11/21 (SNU-423, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -4.6 | 2e-04 | 13/21 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.641×** | -4.6 | 2e-04 | 11/21 (CFPAC-1, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.653×** | -4.6 | 2e-04 | 14/21 (C32, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -4.5 | 3e-04 | 19/21 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -4.5 | 3e-04 | 15/20 (SHP-77, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.657×** | -4.4 | 5e-04 | 8/20 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.668×** | -4.3 | 5e-04 | 13/20 (SK-MEL-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 222 | 0 | 16 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0599× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 80.5 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0590× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0826× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.234× (z -10.5) |
| [[SHP-77 (line)]] | alt | 129 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.3) |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 44.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.1) |
| [[HOP62 (line)]] | alt | 23.2 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0710× (z -13.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 15.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 181 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -8.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.188× (z -8.5) |
| [[H4 (line)]] | wt | 14.5 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0550× (z -9.9) |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0737× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 9.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 6.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0716× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 4.49 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0684× (z -9.1) |
| [[A-172 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC7]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LRP2]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PTPRD]] | +0.70 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP28]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NRN1]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LRAT]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 | **novel candidate** |
| [[EYA1]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[DPYSL4]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 | **novel candidate** |
| [[TNFRSF19]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[NREP]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[KCTD16]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 5, C 17. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM13C]] | B | FAM13C activity raises EPHA3's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without FAM13C | 0.032 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPHA3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TET1]] | B | TET1 activity raises EPHA3's level | lines that do not express TET1 (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without TET1 | 0.071 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises EPHA3's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 3.41× lower at baseline in the lines without KDM2B-DT | 0.088 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[LOXL3]] | B | LOXL3 activity raises EPHA3's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without LOXL3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[ADGRB3]] | C | ADGRB3 activity raises EPHA3's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.72× lower at baseline in the lines without ADGRB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises EPHA3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 6.28× lower at baseline in the lines without BCHE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[SMIM10]] | C | SMIM10 activity raises EPHA3's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 3.39× lower at baseline in the lines without SMIM10 | 0.011 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365; co-absent with the target |
| [[KCTD16]] | C | KCTD16 activity raises EPHA3's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.72× lower at baseline in the lines without KCTD16 | 0.022 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[PI15]] | C | PI15 activity raises EPHA3's level | lines that do not express PI15 (36) vs lines expressing it (14) | 3.89× lower at baseline in the lines without PI15 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1; co-absent with the target |
| [[LRP2]] | C | LRP2 activity raises EPHA3's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without LRP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises EPHA3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without NLGN1 | 0.050 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCAF2]] | B | EPHA3 activity raises TCAF2's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without EPHA3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[NRG4]] | B | EPHA3 activity raises NRG4's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without EPHA3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[CHRM3]] | B | EPHA3 activity raises CHRM3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without EPHA3 | 0.050 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[GPR155]] | B | EPHA3 activity raises GPR155's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without EPHA3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[PFKFB4]] | B | EPHA3 activity raises PFKFB4's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without EPHA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[BCL11A]] | B | EPHA3 activity raises BCL11A's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without EPHA3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[MLLT3]] | B | EPHA3 activity raises MLLT3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without EPHA3 | 0.095 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[ADGRB3]] | C | EPHA3 activity raises ADGRB3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 5.68× lower at baseline in the lines without EPHA3 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[KCTD16]] | C | EPHA3 activity raises KCTD16's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.49× lower at baseline in the lines without EPHA3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[PAX3]] | C | EPHA3 activity raises PAX3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.23× lower at baseline in the lines without EPHA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[NELL2]] | C | EPHA3 activity raises NELL2's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.25× lower at baseline in the lines without EPHA3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[SETBP1]] | C | EPHA3 activity raises SETBP1's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.13× lower at baseline in the lines without EPHA3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.0, 28.8); signed map (31.8, 41.5). **Vector** length 79.1, 25.3% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p11.1 — chr3:89,107,621-89,482,134 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEK, HEK4; previously ETK, ETK1, TYRO4 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P29320](https://www.uniprot.org/uniprotkb/P29320) (Ephrin type-A receptor 3):

> Receptor tyrosine kinase which binds promiscuously membrane-bound ephrin family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Highly promiscuous for ephrin-A ligands it binds preferentially EFNA5 (By similarity). Upon activation by EFNA5 regulates …

**Summary**, from NCBI Gene [2042](https://www.ncbi.nlm.nih.gov/gene/2042):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3387) · Entrez [2042](https://www.ncbi.nlm.nih.gov/gene/2042) · UniProt [P29320](https://www.uniprot.org/uniprotkb/P29320) · Ensembl [ENSG00000044524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044524)

## Data

Gene col 501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 501); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 501]; `tensor/DDL_lfc|DDL_z.npy` [501]; `embed/gene_vectors.npy` [501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 501 or target_col == 501). Every well: [[EPHA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
