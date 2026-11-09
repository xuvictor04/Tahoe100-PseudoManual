---
symbol: "PIMREG"
type: "gene"
col: 4954
ensembl_id: "ENSG00000129195"
name: "PICALM interacting mitotic regulator"
location: "17p13.2"
module: 22
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 97
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PIMREG

*PICALM interacting mitotic regulator* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.00× (z +18.8, q 0e+00, up in 32 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (SW480 6.25×, A549 18.1×, J82 5.00×, NCI-H460 7.94×, …); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 4.81×; ⚠ cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.461× (z -6.4, q 9e-08, down in 26 of 41 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.499× (z -5.7, q 2e-06, down in 17 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.85, fdr 7e-06), [[CDCA3]] (+0.85, fdr 7e-06), [[TACC3]] (+0.85, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 97 go from it, the strongest it → [[PTTG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4954.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (SW480 6.25×, A549 18.1×, J82 5.00×, NCI-H460 7.94×, …); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 4.81×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.00×** | +18.8 | 0e+00 | 32/33 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.23×** | +9.7 | 8e-20 | 32/41 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.91×** | +8.8 | 2e-16 | 32/41 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.00×** | +8.7 | 3e-16 | 8/11 (J82, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.54×** | +7.7 | 2e-12 | 29/41 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **2.41×** | +7.3 | 3e-11 | 17/24 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **2.17×** | +6.4 | 1e-08 | 18/29 (HOP62, J82, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.94×** | +4.9 | 6e-05 | 7/16 (NCI-H2030, J82, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.38×** | +3.8 | 0.011 | 14/42 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.033 | 8/42 (HT-29, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.461×** | -6.4 | 9e-08 | 26/41 (A-172, C32, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.480×** | -6.1 | 4e-07 | 26/38 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -5.7 | 2e-06 | 17/31 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.423×** | -5.3 | 2e-05 | 23/38 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -5.1 | 3e-05 | 20/38 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.554×** | -4.9 | 1e-04 | 17/40 (LS 180, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.716×** | -3.9 | 0.008 | 20/40 (A-172, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.631×** | -3.6 | 0.019 | 18/39 (C32, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.022 | 15/42 (LoVo, NCI-H460, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.665×** | -3.4 | 0.044 | 15/42 (SW480, RPMI-7951, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.670×** | -3.3 | 0.050 | 18/39 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.684×** | -3.1 | 0.083 | 14/41 (A-172, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.98 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.41 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.3) |
| [[A-172 (line)]] | wt | 8.28 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.137× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.225× (z -9.0) |
| [[LS 180 (line)]] | wt | 4.17 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0446× (z -9.6) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0463× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.28 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +9.1) | [[Homoharringtonine (drug)]] 0.05 µM 0.0741× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 4.46 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.94× (z +11.8) | [[Selinexor (drug)]] 0.5 µM 0.0248× (z -14.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[Panc 03.27 (line)]] | alt | 2.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.12× (z +8.9) | [[Pentamidine (isethionate) (drug)]] 0.5 µM 0.0492× (z -8.6) |
| [[A-427 (line)]] | wt | 9.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.115× (z -9.0) |
| [[A498 (line)]] | wt | 7.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.173× (z -8.9) |
| [[A549 (line)]] | wt | 5.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +14.1) | — |
| [[BT-474 (line)]] | alt | 3.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.92× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 8.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0396× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +13.2) | — |
| [[KATO III (line)]] | alt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.4) | — |
| [[LoVo (line)]] | wt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 9.58 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0667× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 5.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 9.81 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0467× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.85 | +0.88 / +0.84 | both halves | 7e-06 | STRING 676 |
| [[CDCA3]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | STRING 834 |
| [[TACC3]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | STRING 484 |
| [[TROAP]] | +0.84 | +0.86 / +0.80 | both halves | 7e-06 | STRING 623 |
| [[CDCA8]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | STRING 679 |
| [[CDCA2]] | +0.82 | +0.75 / +0.82 | both halves | 7e-06 | STRING 629 |
| [[HJURP]] | +0.82 | +0.83 / +0.81 | both halves | 7e-06 | STRING 710 |
| [[DEPDC1B]] | +0.82 | +0.85 / +0.78 | both halves | 7e-06 |  |
| [[FAM83D]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | STRING 510 |
| [[GTSE1]] | +0.81 | +0.79 / +0.83 | both halves | 7e-06 | STRING 623 |
| [[KIF22]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | STRING 451 |
| [[KIFC1]] | +0.80 | +0.85 / +0.74 | both halves | 7e-06 | STRING 589 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PIMREG's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PIMREG's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NEURL1B]] | C | NEURL1B activity raises PIMREG's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.88× lower at baseline in the lines without NEURL1B | 0.005 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises PIMREG's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises PIMREG's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.95× lower at baseline in the lines without PBK | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[C21orf58]] | C | C21orf58 activity raises PIMREG's level | lines that do not express C21orf58 (3) vs lines expressing it (47) | 2.91× lower at baseline in the lines without C21orf58 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises PIMREG's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises PIMREG's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises PIMREG's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without FAM72D | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises PIMREG's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.92× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 91, C 6. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTTG1]] | B | PIMREG activity raises PTTG1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without PIMREG | 0.001 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[CENPF]] | B | PIMREG activity raises CENPF's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.97× lower at baseline in the lines without PIMREG | 0.001 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[CDKN3]] | B | PIMREG activity raises CDKN3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without PIMREG | 0.003 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NCAPG]] | B | PIMREG activity raises NCAPG's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without PIMREG | 0.004 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[MAD2L1]] | B | PIMREG activity raises MAD2L1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.50× lower at baseline in the lines without PIMREG | 0.004 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[DBF4]] | B | PIMREG activity raises DBF4's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without PIMREG | 0.005 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PSRC1]] | B | PIMREG activity raises PSRC1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[GTSE1]] | B | PIMREG activity raises GTSE1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[CCNB2]] | B | PIMREG activity raises CCNB2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[KIF20A]] | B | PIMREG activity raises KIF20A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[UBE2T]] | B | PIMREG activity raises UBE2T's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[BIRC5]] | B | PIMREG activity raises BIRC5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.4, -56.9); signed map (-51.5, -40.8). **Vector** length 89.9, 22.1% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.71 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +18.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | +4.6 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.6 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.4 | +7.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.7 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.7 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | PICALM interacting mitotic regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:6,444,441-6,451,469 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10156, FLJ10491, CATS, RCS1; previously FAM64A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSJ6](https://www.uniprot.org/uniprotkb/Q9BSJ6) (Protein PIMREG):

> During mitosis, may play a role in the control of metaphase-to-anaphase transition.

**Summary**, from NCBI Gene [54478](https://www.ncbi.nlm.nih.gov/gene/54478):

> Predicted to be involved in cell division. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25483) · Entrez [54478](https://www.ncbi.nlm.nih.gov/gene/54478) · UniProt [Q9BSJ6](https://www.uniprot.org/uniprotkb/Q9BSJ6) · Ensembl [ENSG00000129195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129195)

## Data

Gene col 4954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4954); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4954]; `tensor/DDL_lfc|DDL_z.npy` [4954]; `embed/gene_vectors.npy` [4954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4954 or target_col == 4954). Every well: [[PIMREG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIMREG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
