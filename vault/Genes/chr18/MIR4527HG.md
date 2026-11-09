---
symbol: "MIR4527HG"
type: "gene"
col: 15576
ensembl_id: "ENSG00000267761"
name: "MIR4527 host gene"
location: "18q21.1"
module: 61
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 14
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# MIR4527HG

*MIR4527 host gene* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 8.34× (z +26.4, q 0e+00, up in 10 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.741× (z -3.8, q 0.096, down in 0 of 12 measured lines) ⚠ cell-cycle shift, explains ~20% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0589×, LOX-IMVI 0.165×, hTERT-HPNE 0.0883×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.181×, SK-MEL-2 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.128×, HOP62 0.113×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.353×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNQ3]] (+0.66, fdr 2e-05), [[SNTG2]] (+0.56, fdr 3e-05), [[ERC2]] (+0.55, fdr 1e-05); moves opposite to [[FAM227A]] (-0.45, fdr 2e-04), [[FBXL8]] (-0.44, fdr 8e-04, ⚠ not reproduced), [[LRRC27]] (-0.43, fdr 1e-04), [[HDAC6]] (-0.42, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAGEA1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[KCNN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **8.34×** | +26.4 | 0e+00 | 10/12 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **8.05×** | +26.0 | 0e+00 | 7/11 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **18.3×** | +25.6 | 0e+00 | 10/12 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **10.7×** | +20.9 | 0e+00 | 11/12 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **10.6×** | +20.8 | 0e+00 | 9/11 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.84×** | +15.5 | 0e+00 | 10/12 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.97×** | +15.1 | 0e+00 | 9/12 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +14.9 | 0e+00 | 4/11 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.02×** | +12.2 | 1e-32 | 9/11 (hTERT-HPNE, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.92×** | +12.0 | 1e-31 | 8/11 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +10.0 | 5e-22 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.95×** | +9.5 | 9e-20 | 9/12 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +8.5 | 9e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.46×** | +7.9 | 9e-14 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.28×** | +7.3 | 1e-11 | 2/12 (NCI-H460, A549) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.13×** | +6.5 | 2e-09 | 8/12 (A549, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +6.1 | 3e-08 | 3/11 (A549, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.94×** | +5.9 | 2e-07 | 3/11 (hTERT-HPNE, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.0589×, LOX-IMVI 0.165×, hTERT-HPNE 0.0883×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LOX-IMVI 0.181×, SK-MEL-2 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.128×, HOP62 0.113×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.353×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.741×** | -3.8 | 0.096 | 0/12 | rises with dose |  |
| [[Entrectinib (drug)]] 0.05 µM |  | 0.711× | -3.0 | 0.43 | 1/11 (A549) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.712× | -3.0 | 0.43 | 1/12 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 2.55 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 153× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 32.7× (z +14.0) | — |
| [[A-427 (line)]] | wt | 3.06 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 55.6× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 131× (z +12.6) | — |
| [[H4 (line)]] | wt | 55.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0589× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0883× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.818 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNQ3]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[SNTG2]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ERC2]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[COLEC12]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC02476]] | +0.53 | +0.20 / +0.59 | both halves | 7e-04 |  |
| [[KCNH1]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[LPAR3]] | +0.51 | +0.26 / +0.54 | both halves | 3e-04 |  |
| [[VAT1L]] | +0.51 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[BNC1]] | +0.51 | +0.32 / +0.46 | both halves | 2e-04 |  |
| [[SNAP91]] | +0.50 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[HS6ST3]] | +0.50 | +0.42 / +0.39 | both halves | 6e-05 |  |
| [[PCSK2]] | +0.49 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM227A]] | -0.45 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[FBXL8]] | -0.44 | -0.20 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[LRRC27]] | -0.43 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[HDAC6]] | -0.42 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RSPO3]] | -0.42 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA1]] | C | MAGEA1 activity raises MIR4527HG's level | lines that do not express MAGEA1 (37) vs lines expressing it (13) | 3.72× lower at baseline in the lines without MAGEA1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises MIR4527HG's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without LNCOG | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[COL5A3]] | C | COL5A3 activity raises MIR4527HG's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without COL5A3 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises MIR4527HG's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without MIR646HG | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[LINC02220]] | C | LINC02220 activity raises MIR4527HG's level | lines that do not express LINC02220 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without LINC02220 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent; co-absent with the target |
| [[OR4F15]] | C | OR4F15 activity raises MIR4527HG's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 3.20× lower at baseline in the lines without OR4F15 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4; co-absent with the target |
| [[LRFN5]] | C | LRFN5 activity raises MIR4527HG's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 2.11× lower at baseline in the lines without LRFN5 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN2]] | B | MIR4527HG activity raises KCNN2's level | lines that do not express MIR4527HG (36) vs lines expressing it (14) | 2.11× lower at baseline in the lines without MIR4527HG | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADGRG7, UNC5D, ENSG00000287474 |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 31.3); signed map (32.2, 24.1). **Vector** length 31.4, 7.24% of its response variance represented; |z| ≥ 3 in 331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +26.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.2 | +7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.5 | +5.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +0.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.6 | -0.7 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | MIR4527 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q21.1 — chr18:47,285,725-47,594,550 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31724) · Entrez [110175910](https://www.ncbi.nlm.nih.gov/gene/110175910) · Ensembl [ENSG00000267761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267761)

## Data

Gene col 15576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15576); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15576]; `tensor/DDL_lfc|DDL_z.npy` [15576]; `embed/gene_vectors.npy` [15576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15576 or target_col == 15576). Every well: [[MIR4527HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4527HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
