---
symbol: "STAP2"
type: "gene"
col: 10895
ensembl_id: "ENSG00000178078"
name: "signal transducing adaptor family member 2"
location: "19p13.3"
module: 14
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 38
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 17
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# STAP2

*signal transducing adaptor family member 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.72× (z +26.2, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.326× (z -13.4, q 3e-38, down in 28 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAT5A]] (+0.76, fdr 7e-06), [[LTB]] (+0.74, fdr 7e-06), [[TAPBPL]] (+0.73, fdr 7e-06); moves opposite to [[RSU1]] (-0.65, fdr 1e-05), [[FBXW2]] (-0.65, fdr 1e-05), [[BLTP2]] (-0.65, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); 4 go from it, the strongest it → [[ANO9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.72×** | +26.2 | 0e+00 | 33/33 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.61×** | +17.5 | 0e+00 | 30/34 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.4 | 5e-28 | 25/33 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +8.0 | 2e-13 | 25/35 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.5 | 1e-08 | 18/35 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 3e-05 | 16/34 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +5.1 | 3e-05 | 18/33 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.50×** | +4.8 | 1e-04 | 14/32 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +4.6 | 2e-04 | 15/33 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.009 | 11/34 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +3.7 | 0.011 | 8/36 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.5 | 0.025 | 9/26 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.028 | 11/35 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.326×** | -13.4 | 3e-38 | 28/34 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.357×** | -12.3 | 2e-32 | 32/35 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -11.4 | 1e-27 | 29/35 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.543×** | -7.3 | 4e-11 | 28/35 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.431×** | -5.3 | 2e-05 | 20/34 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.646×** | -5.2 | 2e-05 | 19/33 (SW48, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -5.1 | 3e-05 | 17/35 (LoVo, SNU-423, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.013 | 15/35 (SW480, SNU-423, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.744×** | -3.5 | 0.024 | 9/34 (SNU-423, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.749×** | -3.5 | 0.029 | 10/35 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.043 | 14/35 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.053 | 8/35 (HT-29, SW480, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.073 | 9/35 (AsPC-1, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.6 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 39.0 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +18.9) | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.8) |
| [[PANC-1 (line)]] | alt | 8.05 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +23.3) | — |
| [[SNU-423 (line)]] | alt | 16.9 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.117× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 14.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +19.8) | — |
| [[BT-474 (line)]] | alt | 18.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0986× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 27.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -11.7) |
| [[J82 (line)]] | alt | 6.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +14.2) | — |
| [[LoVo (line)]] | wt | 12.4 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 6.63× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +10.3) | — |
| [[SW48 (line)]] | wt | 11.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +11.5) | [[Belinostat (drug)]] 0.5 µM 0.0867× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 9.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -9.1) |
| [[HOP62 (line)]] | alt | 2.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 8.19× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0454× (z -10.4) |
| [[SW1417 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +14.2) | — |
| [[SW480 (line)]] | alt | 8.98 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.265× (z -8.7) |
| [[A-427 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT5A]] | +0.76 | +0.68 / +0.70 | both halves | 7e-06 | STRING 647 |
| [[LTB]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[TAPBPL]] | +0.73 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[IL32]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[BTN2A1]] | +0.69 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LGALSL-DT]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[UNK]] | +0.68 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PATL2]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CX3CL1]] | +0.67 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ZNF827]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | -0.65 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.65 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PAFAH1B2]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NAPG]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[CAP1]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[HERC2]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[STK25]] | -0.60 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[STRAP]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[KIF21B]] | -0.60 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[TBC1D24]] | -0.59 | -0.58 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises STAP2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.15× lower at baseline in the lines without ANO9 | 0.001 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[LRRN1]] | B | LRRN1 activity raises STAP2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without LRRN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises STAP2's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.33× lower at baseline in the lines without MTUS1-DT | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[HCP5]] | B | HCP5 activity raises STAP2's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without HCP5 | 0.021 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[ANO9]] | B | ANO9 activity strengthens STAP2's drug response | lines that do not express ANO9 (12) vs lines expressing it (24) | the lines without ANO9 respond 0.45× as strongly (z diff +2.43); rises at some drug-doses, falls at others (30% from rises): Panobinostat 0.5 µM: 0.60x vs 0.29x (z diff +4.8); Belinostat 5 µM: 0.52x vs 0.31x (z diff +3.7); Digitoxin 5 µM: 1.90x vs 2.67x (z diff +2.8) | 0.033 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[STAT5A]] | B | STAT5A activity raises STAP2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without STAT5A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[MARVELD3]] | B | MARVELD3 activity raises STAP2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without MARVELD3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[PSTPIP2]] | B | PSTPIP2 activity raises STAP2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without PSTPIP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises STAP2's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without TNFAIP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[LGALS3]] | B | LGALS3 activity strengthens STAP2's drug response | lines that do not express LGALS3 (6) vs lines expressing it (30) | the lines without LGALS3 respond 0.30× as strongly (z diff +2.53); rises at some drug-doses, falls at others (40% from rises): Panobinostat 0.5 µM: 0.70x vs 0.32x (z diff +4.5); Belinostat 5 µM: 0.68x vs 0.32x (z diff +3.8); Digitoxin 5 µM: 1.45x vs 2.67x (z diff +3.5) | 0.073 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[LGALS3]] | B | LGALS3 activity raises STAP2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without LGALS3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[CGNL1]] | B | CGNL1 activity raises STAP2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without CGNL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | STAP2 activity raises ANO9's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 3.46× lower at baseline in the lines without STAP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[DDX43]] | B | STAP2 activity raises DDX43's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without STAP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[CGNL1]] | B | STAP2 activity raises CGNL1's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without STAP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[RTN4]] | B | STAP2 activity lowers RTN4's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without STAP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 3.6); signed map (42.7, 9.4). **Vector** length 91.3, 23.5% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +26.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +17.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.3 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -13.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -11.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | signal transducing adaptor family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,324,043-4,342,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAP-2, BKS |
| Reactome | 7 pathways, smallest: PTK6 Activates STAT3; Cytoprotection by HMOX1; Signaling by Non-Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGK3](https://www.uniprot.org/uniprotkb/Q9UGK3) (Signal-transducing adaptor protein 2):

> Substrate of protein kinase PTK6. May play a regulatory role in the acute-phase response in systemic inflammation and may modulate STAT3 activity.

**Summary**, from NCBI Gene [55620](https://www.ncbi.nlm.nih.gov/gene/55620):

> This gene encodes the substrate of breast tumor kinase, an Src-type non-receptor tyrosine kinase. The encoded protein possesses domains and several tyrosine phosphorylation sites characteristic of adaptor proteins that mediate the interactions linking proteins involved in signal transduction pathways. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30430) · Entrez [55620](https://www.ncbi.nlm.nih.gov/gene/55620) · UniProt [Q9UGK3](https://www.uniprot.org/uniprotkb/Q9UGK3) · Ensembl [ENSG00000178078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178078)

## Data

Gene col 10895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10895); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10895]; `tensor/DDL_lfc|DDL_z.npy` [10895]; `embed/gene_vectors.npy` [10895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10895 or target_col == 10895). Every well: [[STAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
