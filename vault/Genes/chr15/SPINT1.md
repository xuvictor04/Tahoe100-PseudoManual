---
symbol: "SPINT1"
type: "gene"
col: 9245
ensembl_id: "ENSG00000166145"
name: "serine peptidase inhibitor, Kunitz type 1"
location: "15q15.1"
module: 8
arm: "+"
pooled_cpm: 33.3
n_lines_expressing: 25
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 117
direction_downstream: 107
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SPINT1

*serine peptidase inhibitor, Kunitz type 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.13× (z +6.2, q 4e-07, up in 3 of 24 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +4.8, q 5e-04, up in 7 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -13.0, q 1e-35, down in 19 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.75, fdr 7e-06), [[TACSTD2]] (+0.72, fdr 9e-06), [[INAVA]] (+0.72, fdr 7e-06); moves opposite to [[ST3GAL3]] (-0.54, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 117 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 107 go from it, the strongest it → [[TMC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.2 | 4e-07 | 3/24 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-04 | 7/23 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.29×** | +3.9 | 0.019 | 4/23 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.048 | 4/23 (HOP62, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.3 | 0.093 | 7/23 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib (drug)]] 5 µM |  | 1.51× | +3.3 | 0.10 | 9/23 (SW1417, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.14 | 9/23 (KATO III, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -13.0 | 1e-35 | 19/23 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -12.4 | 1e-32 | 20/22 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -7.7 | 3e-12 | 19/23 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.640×** | -6.5 | 1e-08 | 17/23 (COLO 205, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.708×** | -5.2 | 2e-05 | 15/23 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.760×** | -4.1 | 0.003 | 15/23 (HT-29, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.780×** | -3.8 | 0.014 | 16/23 (HT-29, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.772×** | -3.7 | 0.016 | 17/23 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.032 | 20/24 (HT-29, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.813× | -3.1 | 0.10 | 12/23 (SW1417, COLO 205, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.815× | -3.1 | 0.10 | 7/23 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 179 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -24.9) |
| [[HT-29 (line)]] | alt | 153 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -18.5) |
| [[LoVo (line)]] | wt | 65.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -22.8) |
| [[LS 180 (line)]] | wt | 68.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 87.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -21.7) |
| [[SW1417 (line)]] | alt | 67.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.0) |
| [[SW480 (line)]] | alt | 23.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.9) |
| [[KATO III (line)]] | alt | 82.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -18.9) |
| [[RKO (line)]] | wt | 23.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -12.8) |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0671× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0945× (z -9.8) |
| [[HCT15 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 84.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) |
| [[A-172 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 | STRING 998 |
| [[TACSTD2]] | +0.72 | +0.75 / +0.57 | both halves | 9e-06 | STRING 458 |
| [[INAVA]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | STRING 500 |
| [[TMEM45B]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[TMC4]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TC2N]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ADCY4]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.54 | -0.61 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*117 arrows, 117 of them with an alert ⚠; grade A 0, B 23, C 94. Shown: the 12 strongest; 105 more arrows (105 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises SPINT1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 4.18× lower at baseline in the lines without EPS8L1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity raises SPINT1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.93× lower at baseline in the lines without SLC28A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[PCDH1]] | B | PCDH1 activity raises SPINT1's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without PCDH1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[SPATA6L]] | B | SPATA6L activity raises SPINT1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 5.30× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity strengthens SPINT1's drug response | lines that do not express SLC28A3 (15) vs lines expressing it (9) | the lines without SLC28A3 respond 0.64× as strongly (z diff +2.15); strongest at Panobinostat 0.5 µM: 0.82x vs 0.44x (z diff +5.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; target measured in part of the lines; artifact flags |
| [[LRATD2]] | B | LRATD2 activity raises SPINT1's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 4.89× lower at baseline in the lines without LRATD2 | 0.037 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[ANKRD22]] | B | ANKRD22 activity strengthens SPINT1's drug response | lines that do not express ANKRD22 (10) vs lines expressing it (14) | the lines without ANKRD22 respond 0.53× as strongly (z diff +2.57); strongest at Homoharringtonine 5 µM: 0.56x vs 0.34x (z diff +5.2) | 0.039 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; target measured in part of the lines; artifact flags |
| [[PROM2]] | B | PROM2 activity raises SPINT1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 3.54× lower at baseline in the lines without PROM2 | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[MAL2]] | B | MAL2 activity strengthens SPINT1's drug response | lines that do not express MAL2 (7) vs lines expressing it (17) | the lines without MAL2 respond 0.50× as strongly (z diff +2.40); strongest at Panobinostat 5 µM: 0.94x vs 0.48x (z diff +6.2) | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; target measured in part of the lines; artifact flags |
| [[TMC6]] | B | TMC6 activity raises SPINT1's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 5.49× lower at baseline in the lines without TMC6 | 0.048 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[FAM83E]] | B | FAM83E activity raises SPINT1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 4.54× lower at baseline in the lines without FAM83E | 0.054 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[RAB25]] | B | RAB25 activity strengthens SPINT1's drug response | lines that do not express RAB25 (8) vs lines expressing it (16) | the lines without RAB25 respond 0.59× as strongly (z diff +2.12); strongest at Panobinostat 5 µM: 0.88x vs 0.48x (z diff +5.6) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; target measured in part of the lines; artifact flags |

### Downstream of this gene

*107 arrows, 107 of them with an alert ⚠; grade A 0, B 22, C 85. Shown: the 12 strongest; 95 more arrows (95 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | SPINT1 activity raises TMC6's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 4.53× lower at baseline in the lines without SPINT1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[EPS8L1]] | B | SPINT1 activity raises EPS8L1's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 3.44× lower at baseline in the lines without SPINT1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[ELMO3]] | B | SPINT1 activity raises ELMO3's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.50× lower at baseline in the lines without SPINT1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[SPATA6L]] | B | SPINT1 activity raises SPATA6L's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 3.80× lower at baseline in the lines without SPINT1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[ST3GAL3]] | B | SPINT1 activity lowers ST3GAL3's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.28× higher at baseline in the lines without SPINT1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[FAM83E]] | B | SPINT1 activity raises FAM83E's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 3.35× lower at baseline in the lines without SPINT1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[TNFRSF21]] | B | SPINT1 activity raises TNFRSF21's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 3.60× lower at baseline in the lines without SPINT1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[KIAA1522]] | B | SPINT1 activity raises KIAA1522's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.70× lower at baseline in the lines without SPINT1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[LRATD2]] | B | SPINT1 activity raises LRATD2's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.86× lower at baseline in the lines without SPINT1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[USP6NL]] | B | SPINT1 activity raises USP6NL's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without SPINT1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[MYRF]] | B | SPINT1 activity raises MYRF's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.97× lower at baseline in the lines without SPINT1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[GPRC5C]] | B | SPINT1 activity raises GPRC5C's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without SPINT1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.6, 57.2); signed map (57.6, 7.6). **Vector** length 80.0, 26.7% of its response variance represented; |z| ≥ 3 in 514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +4.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | serine peptidase inhibitor, Kunitz type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,844,018-40,858,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAI, HAI-1, MANSC2 |
| Reactome | 4 pathways, smallest: Signaling by MST1; MET Receptor Activation; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [O43278](https://www.uniprot.org/uniprotkb/O43278) (Kunitz-type protease inhibitor 1):

> Inhibitor of HGFAC. Inhibits serine protease activity of ST14/matriptase in vitro. Inhibits serine protease activity of TMPRSS13, via the BPTI/Kunitz inhibitor 1 domain.

**Summary**, from NCBI Gene [6692](https://www.ncbi.nlm.nih.gov/gene/6692):

> The protein encoded by this gene is a member of the Kunitz family of serine protease inhibitors. The protein is a potent inhibitor specific for HGF activator and is thought to be involved in the regulation of the proteolytic activation of HGF in injured tissues. Alternative splicing results in multiple variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11246) · Entrez [6692](https://www.ncbi.nlm.nih.gov/gene/6692) · UniProt [O43278](https://www.uniprot.org/uniprotkb/O43278) · Ensembl [ENSG00000166145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166145)

## Data

Gene col 9245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9245); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9245]; `tensor/DDL_lfc|DDL_z.npy` [9245]; `embed/gene_vectors.npy` [9245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9245 or target_col == 9245). Every well: [[SPINT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
