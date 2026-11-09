---
symbol: "TINAGL1"
type: "gene"
col: 6664
ensembl_id: "ENSG00000142910"
name: "tubulointerstitial nephritis antigen like 1"
location: "1p35.2"
module: 34
arm: "+"
pooled_cpm: 50.7
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 65
direction_downstream: 109
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TINAGL1

*tubulointerstitial nephritis antigen like 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.47× (z +8.5, q 1e-14, up in 8 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 5 µM: 1.55× (z +6.1, q 2e-07, up in 22 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.500× (z -6.3, q 2e-07, down in 19 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PADI1]] (+0.75, fdr 7e-06), [[PLEK2]] (+0.70, fdr 7e-06), [[TGFA]] (+0.67, fdr 7e-06); moves opposite to [[PAIP1]] (-0.56, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 65 arrows point to it, the strongest [[TGFA]] → it (grade B ⚠); 109 go from it, the strongest it → [[TGFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +8.5 | 1e-14 | 8/20 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.1 | 1e-13 | 9/22 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.55×** | +6.1 | 2e-07 | 22/22 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.65×** | +4.9 | 2e-04 | 20/22 (HEC-1-A, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +4.7 | 3e-04 | 5/21 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.003 | 9/22 (A-172, HCT15, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.010 | 16/22 (LS 180, KATO III, …) | all doses, flat | position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.010 | 19/22 (LS 180, SW480, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.42×** | +3.4 | 0.035 | 11/22 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.035 | 7/22 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.42×** | +3.4 | 0.037 | 7/22 (SNU-423, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.044 | 16/22 (LS 180, KATO III, …) | all doses, flat | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.054 | 16/22 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.069 | 8/22 (HEC-1-A, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.66× | +3.0 | 0.10 | 5/22 (LS 180, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.500×** | -6.3 | 2e-07 | 19/22 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.554×** | -5.6 | 8e-06 | 21/22 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.684×** | -5.2 | 4e-05 | 15/22 (SW480, SW48, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.616×** | -4.6 | 7e-04 | 18/22 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.727×** | -4.4 | 0.001 | 18/22 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.668×** | -4.0 | 0.007 | 18/22 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.702×** | -3.9 | 0.007 | 18/22 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.009 | 17/22 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.760×** | -3.7 | 0.012 | 14/22 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.768×** | -3.7 | 0.013 | 13/22 (A-172, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.705×** | -3.4 | 0.030 | 12/22 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.766×** | -3.4 | 0.030 | 17/22 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.698×** | -3.4 | 0.030 | 20/22 (A-172, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.031 | 20/22 (SW480, HCT15, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.718×** | -3.3 | 0.041 | 16/22 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.699×** | -3.2 | 0.041 | 4/22 (HepG2/C3A, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 120 | 1 | 4 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.18× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.8) |
| [[J82 (line)]] | alt | 86.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.6) |
| [[LS 180 (line)]] | wt | 76.4 | 1 | 2 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.54× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 92.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -22.4) |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.5) |
| [[HOP62 (line)]] | alt | 155 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.4) |
| [[KATO III (line)]] | alt | 139 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.6) |
| [[LoVo (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 89.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[SW1417 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 253 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PADI1]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TGFA]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TMC7]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[LAMA3]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LCK]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.56 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 25, C 40. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | TGFA activity raises TINAGL1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 4.29× lower at baseline in the lines without TGFA | 0.005 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PTPRE]] | B | PTPRE activity raises TINAGL1's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 4.88× lower at baseline in the lines without PTPRE | 0.008 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[LYPD3]] | B | LYPD3 activity raises TINAGL1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.94× lower at baseline in the lines without LYPD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LANCL3]] | B | LANCL3 activity raises TINAGL1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.83× lower at baseline in the lines without LANCL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[MYEOV]] | B | MYEOV activity raises TINAGL1's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 3.21× lower at baseline in the lines without MYEOV | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[PTK2B]] | B | PTK2B activity raises TINAGL1's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 4.36× lower at baseline in the lines without PTK2B | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises TINAGL1's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without ADAM19 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[GPRC5A]] | B | GPRC5A activity raises TINAGL1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 4.05× lower at baseline in the lines without GPRC5A | 0.034 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ITGA3]] | B | ITGA3 activity raises TINAGL1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.06× lower at baseline in the lines without ITGA3 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SERPINB1]] | B | SERPINB1 activity raises TINAGL1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 5.29× lower at baseline in the lines without SERPINB1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[ATG9B]] | B | ATG9B activity raises TINAGL1's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 3.62× lower at baseline in the lines without ATG9B | 0.041 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[CCDC120]] | B | CCDC120 activity raises TINAGL1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 4.26× lower at baseline in the lines without CCDC120 | 0.042 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |

### Downstream of this gene

*109 arrows, 109 of them with an alert ⚠; grade A 0, B 64, C 45. Shown: the 12 strongest; 97 more arrows (97 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | TINAGL1 activity raises TGFA's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 4.48× lower at baseline in the lines without TINAGL1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PTPRE]] | B | TINAGL1 activity raises PTPRE's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[JUP]] | B | TINAGL1 activity raises JUP's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 4.10× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PTK2B]] | B | TINAGL1 activity raises PTK2B's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.56× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[TNIK]] | B | TINAGL1 activity raises TNIK's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.27× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[SERINC2]] | B | TINAGL1 activity raises SERINC2's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.96× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[SOX13]] | B | TINAGL1 activity raises SOX13's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without TINAGL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PLEKHM1P1]] | B | TINAGL1 activity raises PLEKHM1P1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without TINAGL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ALS2CL]] | B | TINAGL1 activity raises ALS2CL's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.30× lower at baseline in the lines without TINAGL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[OSBPL3]] | B | TINAGL1 activity raises OSBPL3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without TINAGL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ADAM19]] | B | TINAGL1 activity raises ADAM19's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.66× lower at baseline in the lines without TINAGL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CD58]] | B | TINAGL1 activity raises CD58's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TINAGL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 52.3); signed map (2.6, 40.6). **Vector** length 88.4, 29.8% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | -0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | tubulointerstitial nephritis antigen like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,576,485-31,587,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P3ECSL, LIECG3, ARG1, TINAGRP; previously LCN7 |
| Gene groups (HGNC) | Peptidase family C1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZM7](https://www.uniprot.org/uniprotkb/Q9GZM7) (Tubulointerstitial nephritis antigen-like):

> May be implicated in the adrenocortical zonation and in mechanisms for repressing the CYP11B1 gene expression in adrenocortical cells. This is a non catalytic peptidase C1 family protein (By similarity).

**Summary**, from NCBI Gene [64129](https://www.ncbi.nlm.nih.gov/gene/64129):

> The protein encoded by this gene is similar in sequence to tubulointerstitial nephritis antigen, a secreted glycoprotein that is recognized by antibodies in some types of immune-related tubulointerstitial nephritis. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:19168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19168) · Entrez [64129](https://www.ncbi.nlm.nih.gov/gene/64129) · UniProt [Q9GZM7](https://www.uniprot.org/uniprotkb/Q9GZM7) · Ensembl [ENSG00000142910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142910)

## Data

Gene col 6664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6664); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6664]; `tensor/DDL_lfc|DDL_z.npy` [6664]; `embed/gene_vectors.npy` [6664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6664 or target_col == 6664). Every well: [[TINAGL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TINAGL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
