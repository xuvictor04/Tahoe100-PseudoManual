---
symbol: "GET1-SH3BGR"
type: "gene"
col: 16151
ensembl_id: "ENSG00000285815"
name: "GET1-SH3BGR readthrough"
location: "21q22.2"
module: 37
arm: "+"
pooled_cpm: 3.69
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# GET1-SH3BGR

*GET1-SH3BGR readthrough* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +6.1, q 7e-07, up in 16 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.390× (z -15.3, q 0e+00, down in 30 of 37 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.274× (z -14.3, q 3e-44, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECT2L]] (+0.74, fdr 7e-06), [[LINC02680]] (+0.70, fdr 7e-06), [[GET1]] (+0.68, fdr 7e-06, ⚠ same locus), [[SDHAP4-1]] (+0.68, fdr 7e-06); moves opposite to [[CSTF2T]] (-0.65, fdr 9e-06), [[TIGD2]] (-0.63, fdr 1e-05), [[SLC35A4]] (-0.62, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.1 | 7e-07 | 16/34 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 7e-07 | 12/36 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.9 | 9e-07 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +5.4 | 1e-05 | 13/46 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.5 | 9e-04 | 7/43 (SW48, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.28×** | +4.1 | 0.004 | 9/45 (A498, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.004 | 11/43 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.8 | 0.011 | 12/41 (SW 900, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.012 | 8/40 (COLO 205, HT-29, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.021 | 5/34 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.033 | 4/47 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.070 | 5/32 (A-172, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.084 | 6/45 (KATO III, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.390×** | -15.3 | 0e+00 | 30/37 (A-172, CFPAC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.274×** | -14.3 | 3e-44 | 33/42 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.397×** | -10.7 | 3e-24 | 29/45 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.398×** | -10.6 | 3e-24 | 31/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.402×** | -10.5 | 9e-24 | 28/42 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.409×** | -10.3 | 7e-23 | 23/34 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.489×** | -8.2 | 1e-14 | 27/42 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.506×** | -7.9 | 3e-13 | 20/44 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.517×** | -7.6 | 2e-12 | 22/33 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.287×** | -7.5 | 3e-12 | 24/39 (NCI-H2030, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.682×** | -4.4 | 6e-04 | 10/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -4.3 | 7e-04 | 13/34 (A-172, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.010 | 11/41 (HS-578T, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.548×** | -3.6 | 0.012 | 7/32 (HOP62, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.016 | 11/44 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.569×** | -3.4 | 0.025 | 6/28 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.576×** | -3.3 | 0.028 | 7/38 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0550× (z -13.1) |
| [[A-172 (line)]] | wt | 5.24 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0297× (z -19.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0479× (z -11.7) |
| [[H4 (line)]] | wt | 9.98 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0544× (z -9.4) |
| [[HOP62 (line)]] | alt | 5.44 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0725× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.102× (z -9.5) |
| [[A498 (line)]] | wt | 4.61 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0964× (z -9.8) |
| [[A549 (line)]] | wt | 3.33 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0251× (z -11.4) |
| [[C32 (line)]] | wt | 5.96 | 0 | 2 | — | [[Roxadustat (drug)]] 5 µM 0.0719× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 8.16 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0702× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.10 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0503× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 3.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 4.87 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0260× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 7.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0687× (z -8.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Hs 766T (line)]] | wt | 5.71 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0708× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 5.41 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0799× (z -9.1) |
| [[PANC-1 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 2.40 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0779× (z -10.5) |
| [[A-427 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECT2L]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.70 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[GET1]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SDHAP4-1]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[RBM44]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[WDR49]] | +0.67 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[DRD4]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[METTL21EP-1]] | +0.67 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.67 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[GNRH1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MAX]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[TSNAX-DISC1]] | +0.66 | +0.55 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | -0.65 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[TIGD2]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[FAT1]] | -0.61 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.61 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[SLX4IP]] | -0.60 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[DCLRE1A]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[COA7]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[RTL6]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[LIG4]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GET1-SH3BGR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SYCP2L]] | B | SYCP2L activity raises GET1-SH3BGR's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SYCP2L | 0.099 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, -21.0); signed map (9.2, 6.0). **Vector** length 61.6, 8.74% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | -0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -15.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -10.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | GET1-SH3BGR readthrough |
| Locus type | readthrough (other) |
| Location | 21q22.2 — chr21:39,380,332-39,515,506 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [106865373](https://www.ncbi.nlm.nih.gov/gene/106865373):

> This locus represents naturally occurring readthrough transcription between the neighboring WRB (tryptophan rich basic protein) and SH3BGR (SH3 domain binding glutamate-rich protein) genes on chromosome 21. Readthrough transcripts may encode fusion proteins that shares sequence identity with each individual gene product. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:54635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54635) · Entrez [106865373](https://www.ncbi.nlm.nih.gov/gene/106865373) · Ensembl [ENSG00000285815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285815)

## Data

Gene col 16151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16151); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16151]; `tensor/DDL_lfc|DDL_z.npy` [16151]; `embed/gene_vectors.npy` [16151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16151 or target_col == 16151). Every well: [[GET1-SH3BGR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GET1-SH3BGR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
