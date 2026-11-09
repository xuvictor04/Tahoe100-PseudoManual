---
symbol: "GJB3"
type: "gene"
col: 12064
ensembl_id: "ENSG00000188910"
name: "gap junction protein beta 3"
location: "1p34.3"
module: 34
arm: "+"
pooled_cpm: 7.96
n_lines_expressing: 19
n_dd_up: 17
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 71
direction_downstream: 118
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GJB3

*gap junction protein beta 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.31× (z +10.1, q 3e-21, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 2.34× (z +5.3, q 1e-05, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.298× (z -10.7, q 1e-23, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FERMT1]] (+0.77, fdr 7e-06), [[HS3ST1]] (+0.77, fdr 7e-06), [[KLK10]] (+0.72, fdr 7e-06); moves opposite to [[SELENOP]] (-0.53, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 71 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 118 go from it, the strongest it → [[ITPKC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +10.1 | 3e-21 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.7 | 4e-09 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +6.3 | 6e-08 | 3/17 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +5.4 | 9e-06 | 2/15 (AsPC-1, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **2.34×** | +5.3 | 1e-05 | 13/17 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.64×** | +4.3 | 0.001 | 4/15 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.005 | 1/17 (Panc 03.27) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.55×** | +3.9 | 0.008 | 6/16 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.008 | 11/17 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.013 | 14/17 (HT-29, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.013 | 12/17 (HT-29, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.017 | 11/17 (HT-29, LS 180, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.76×** | +3.5 | 0.018 | 2/15 (NCI-H2347, KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.5 | 0.018 | 0/16 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +3.5 | 0.020 | 8/17 (SW1417, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.028 | 7/17 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 1 with an alert ⚠; shown: the 15 strongest. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12064.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.298×** | -10.7 | 1e-23 | 17/17 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.371×** | -8.7 | 7e-16 | 16/17 (SW48, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.466×** | -6.2 | 1e-07 | 13/17 (LS 180, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.486×** | -5.7 | 2e-06 | 14/17 (AsPC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -5.5 | 4e-06 | 14/17 (NCI-H2347, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.649×** | -5.3 | 1e-05 | 15/17 (HCT15, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.659×** | -5.2 | 2e-05 | 12/17 (AsPC-1, LoVo, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -5.1 | 3e-05 | 17/17 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.564×** | -4.8 | 8e-05 | 14/17 (AsPC-1, SW48, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.645×** | -4.8 | 8e-05 | 14/17 (AsPC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -4.5 | 3e-04 | 12/17 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.599×** | -4.5 | 3e-04 | 13/17 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.591×** | -4.5 | 4e-04 | 15/17 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.676×** | -4.4 | 5e-04 | 13/17 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.334×** | -4.3 | 6e-04 | 14/17 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 38.2 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -20.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0533× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0970× (z -15.6) |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0269× (z -19.7) |
| [[LoVo (line)]] | wt | 21.4 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0565× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0357× (z -27.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0750× (z -14.3) |
| [[SW48 (line)]] | wt | 33.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0156× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0537× (z -24.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0507× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.111× (z -11.0) |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.127× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 6.31 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0533× (z -10.7) |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 4.50 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0418× (z -9.8) |
| [[SW480 (line)]] | alt | 6.95 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -9.6) |
| [[HT-29 (line)]] | alt | 9.90 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.652 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT1]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SERPINB5]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PLEK2]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ANO1]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SH2D3A]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[EPHA2-AS1]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 410 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOP]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 9, C 62. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises GJB3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without SEMA3B | 0.009 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises GJB3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.9% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds |
| [[ABCC3]] | B | ABCC3 activity raises GJB3's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.22× lower at baseline in the lines without ABCC3 | 0.038 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[EFNB2]] | B | EFNB2 activity raises GJB3's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without EFNB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[PTK2B]] | B | PTK2B activity raises GJB3's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.90× lower at baseline in the lines without PTK2B | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises GJB3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without TJP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[PDE9A]] | B | PDE9A activity raises GJB3's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without PDE9A | 0.072 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[AHNAK2]] | B | AHNAK2 activity raises GJB3's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without AHNAK2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises GJB3's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.27× lower at baseline in the lines without ALS2CL | 0.0999 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[C1orf116]] | C | C1orf116 activity raises GJB3's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 8.85× lower at baseline in the lines without C1orf116 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises GJB3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 7.74× lower at baseline in the lines without TMPRSS4 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises GJB3's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 9.19× lower at baseline in the lines without KLK10 | 4e-05 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |

### Downstream of this gene

*118 arrows, 118 of them with an alert ⚠; grade A 0, B 58, C 60. Shown: the 12 strongest; 106 more arrows (106 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPKC]] | B | GJB3 activity raises ITPKC's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without GJB3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ARHGAP27]] | B | GJB3 activity raises ARHGAP27's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without GJB3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[PKP3]] | B | GJB3 activity raises PKP3's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.38× lower at baseline in the lines without GJB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[PTK2B]] | B | GJB3 activity raises PTK2B's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.49× lower at baseline in the lines without GJB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[EPS8L1]] | B | GJB3 activity raises EPS8L1's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.96× lower at baseline in the lines without GJB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[SEMA3B]] | B | GJB3 activity raises SEMA3B's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without GJB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[BCR]] | B | GJB3 activity raises BCR's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.18× lower at baseline in the lines without GJB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[PDE9A]] | B | GJB3 activity raises PDE9A's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.16× lower at baseline in the lines without GJB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[TMC6]] | B | GJB3 activity raises TMC6's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.98× lower at baseline in the lines without GJB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ALS2CL]] | B | GJB3 activity raises ALS2CL's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.47× lower at baseline in the lines without GJB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[TJP2]] | B | GJB3 activity raises TJP2's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without GJB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[RDH13]] | B | GJB3 activity raises RDH13's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without GJB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 52.8); signed map (2.3, 38.1). **Vector** length 95.5, 41.1% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | -10.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.7 | -5.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:34,781,214-34,786,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CX31; previously DFNA2, EKV |
| Gene groups (HGNC) | Gap junction proteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 5 pathways, smallest: Gap junction assembly; Gap junction trafficking; Gap junction trafficking and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75712](https://www.uniprot.org/uniprotkb/O75712) (Gap junction beta-3 protein):

> One gap junction consists of a cluster of closely packed pairs of transmembrane channels, the connexons, through which materials of low MW diffuse from one cell to a neighboring cell.

**Summary**, from NCBI Gene [2707](https://www.ncbi.nlm.nih.gov/gene/2707):

> This gene is a member of the connexin gene family. The encoded protein is a component of gap junctions, which are composed of arrays of intercellular channels that provide a route for the diffusion of low molecular weight materials from cell to cell. Mutations in this gene can cause non-syndromic deafness or erythrokeratodermia variabilis, a skin disorder. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4285) · Entrez [2707](https://www.ncbi.nlm.nih.gov/gene/2707) · UniProt [O75712](https://www.uniprot.org/uniprotkb/O75712) · Ensembl [ENSG00000188910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188910)

## Data

Gene col 12064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12064); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12064]; `tensor/DDL_lfc|DDL_z.npy` [12064]; `embed/gene_vectors.npy` [12064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12064 or target_col == 12064). Every well: [[GJB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
