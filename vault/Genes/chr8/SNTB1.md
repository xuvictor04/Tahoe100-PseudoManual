---
symbol: "SNTB1"
type: "gene"
col: 10217
ensembl_id: "ENSG00000172164"
name: "syntrophin beta 1"
location: "8q24.12"
module: 55
arm: "+"
pooled_cpm: 116.05
n_lines_expressing: 31
n_dd_up: 3
n_dd_down: 48
n_dd_up_clean: 3
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 43
direction_downstream: 24
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SNTB1

*syntrophin beta 1* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.35× (z +4.7, q 8e-04, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.249× (z -30.6, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF43]] (+0.61, fdr 1e-05), [[PROM1]] (+0.58, fdr 1e-05), [[IL20RA]] (+0.54, fdr 3e-05); moves opposite to [[CYS1]] (-0.43, fdr 2e-04), [[ULK2]] (-0.43, fdr 4e-05), [[ITGB1BP1]] (-0.41, fdr 2e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[FAAH2]] → it (grade B ⚠); 24 go from it, the strongest it → [[TMC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.7 | 8e-04 | 16/29 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 8e-04 | 15/29 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.060 | 11/29 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.086 | 11/30 (NCI-H2347, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.249×** | -30.6 | 0e+00 | 29/29 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.221×** | -23.5 | 0e+00 | 29/29 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.247×** | -21.8 | 0e+00 | 29/29 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.250×** | -21.6 | 0e+00 | 28/29 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.254×** | -20.6 | 0e+00 | 28/29 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.286×** | -19.5 | 0e+00 | 28/29 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.418×** | -13.6 | 4e-40 | 28/29 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.431×** | -13.1 | 2e-37 | 28/29 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.431×** | -13.1 | 2e-37 | 28/29 (COLO 205, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.519×** | -10.2 | 1e-22 | 23/29 (SW 900, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.522×** | -10.1 | 2e-22 | 25/29 (HT-29, HepG2/C3A, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.541×** | -9.5 | 7e-20 | 22/29 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -9.0 | 8e-18 | 24/29 (HepG2/C3A, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.564×** | -8.9 | 2e-17 | 24/29 (SW48, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -8.0 | 6e-14 | 22/28 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.635×** | -7.0 | 6e-11 | 21/29 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -6.8 | 2e-10 | 22/29 (SW480, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.650×** | -6.4 | 3e-09 | 21/29 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.670×** | -6.2 | 1e-08 | 23/29 (COLO 205, HT-29, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.490×** | -5.8 | 2e-07 | 22/30 (HepG2/C3A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 431 | 0 | 23 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0603× (z -32.5) |
| [[SW480 (line)]] | alt | 473 | 0 | 23 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0312× (z -26.5) |
| [[HT-29 (line)]] | alt | 531 | 0 | 20 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0426× (z -24.8) |
| [[COLO 205 (line)]] | alt | 911 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0111× (z -54.5) |
| [[HepG2_C3A (line)]] | wt | 478 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0681× (z -31.1) |
| [[NCI-H1792 (line)]] | alt | 169 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -30.7) |
| [[SW 900 (line)]] | alt | 128 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -19.9) |
| [[SW48 (line)]] | wt | 212 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -26.7) |
| [[KATO III (line)]] | alt | 82.4 | 1 | 14 (5 ⚠) | [[Ponatinib (drug)]] 5 µM 2.60× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0842× (z -22.6) |
| [[LS 180 (line)]] | wt | 305 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0617× (z -27.7) |
| [[SW1417 (line)]] | alt | 296 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0970× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0814× (z -29.6) |
| [[LoVo (line)]] | wt | 116 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -25.0) |
| [[CFPAC-1 (line)]] | alt | 111 | 1 | 9 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 3.18× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -27.2) |
| [[SK-MEL-2 (line)]] | alt | 67.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -24.5) |
| [[H4 (line)]] | wt | 72.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 70.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -21.8) |
| [[J82 (line)]] | alt | 31.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 92.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -28.7) |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0942× (z -14.8) |
| [[HCT15 (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -11.1) |
| [[A498 (line)]] | wt | 38.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.0) |
| [[HS-578T (line)]] | alt | 40.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.9) |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.0) |
| [[A-172 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 25.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 28.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF43]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PROM1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IL20RA]] | +0.54 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[VSNL1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RNF128]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CADPS]] | +0.52 | +0.42 / +0.48 | both halves | 4e-05 | same gene group |
| [[TSPOAP1]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[PIP5K1B]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ARHGAP6]] | +0.51 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[GJB1]] | +0.51 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[KCNE3]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[FKBP9P1]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYS1]] | -0.43 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ULK2]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ITGB1BP1]] | -0.41 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[CROCCP3-1]] | -0.41 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[TTC7B]] | -0.41 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[IAH1]] | -0.40 | -0.26 / -0.30 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 27, C 16. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAAH2]] | B | FAAH2 activity raises SNTB1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without FAAH2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[VSNL1]] | B | VSNL1 activity raises SNTB1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 4.40× lower at baseline in the lines without VSNL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[RNF128]] | B | RNF128 activity raises SNTB1's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 3.10× lower at baseline in the lines without RNF128 | 0.018 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[RASSF6]] | B | RASSF6 activity raises SNTB1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.99× lower at baseline in the lines without RASSF6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TRIM2]] | B | TRIM2 activity raises SNTB1's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 3.65× lower at baseline in the lines without TRIM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[IL20RA]] | B | IL20RA activity raises SNTB1's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 3.72× lower at baseline in the lines without IL20RA | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises SNTB1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without HNF1A-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[GPX2]] | B | GPX2 activity raises SNTB1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.19× lower at baseline in the lines without GPX2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[MGAM2]] | B | MGAM2 activity raises SNTB1's level | lines that do not express MGAM2 (33) vs lines expressing it (17) | 3.56× lower at baseline in the lines without MGAM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[RAB17]] | B | RAB17 activity raises SNTB1's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.82× lower at baseline in the lines without RAB17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[LINC00299]] | B | LINC00299 activity raises SNTB1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 3.22× lower at baseline in the lines without LINC00299 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[BMP4]] | B | BMP4 activity raises SNTB1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without BMP4 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC4]] | B | SNTB1 activity raises TMC4's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without SNTB1 | 0.025 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[RNF43]] | B | SNTB1 activity raises RNF43's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 3.27× lower at baseline in the lines without SNTB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[BCL2L15]] | B | SNTB1 activity raises BCL2L15's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without SNTB1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[FKBP9P1-1]] | B | SNTB1 activity raises FKBP9P1-1's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SNTB1 | 0.044 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[SLC1A5]] | B | SNTB1 activity raises SLC1A5's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without SNTB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | SNTB1 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express SNTB1 (19) vs lines expressing it (29) | the lines without SNTB1: 0.77× the cells of the other lines | 0.049 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[TRIM2]] | B | SNTB1 activity raises TRIM2's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without SNTB1 | 0.055 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[RAB17]] | B | SNTB1 activity raises RAB17's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without SNTB1 | 0.057 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[TSPOAP1-AS1]] | B | SNTB1 activity raises TSPOAP1-AS1's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without SNTB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[RASSF6]] | B | SNTB1 activity raises RASSF6's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without SNTB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[FKBP9P1]] | B | SNTB1 activity raises FKBP9P1's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 1.89× lower at baseline in the lines without SNTB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[HGD]] | B | SNTB1 activity raises HGD's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without SNTB1 | 0.078 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 48.3); signed map (62.6, 11.3). **Vector** length 111, 35.6% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.3 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.1 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.8 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +0.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -8.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | syntrophin beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:120,535,745-120,813,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 59-DAP, A1B, BSYN2, TIP-43, SNT2; previously SNT2B1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; PDZ domain containing; Syntrophin family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13884](https://www.uniprot.org/uniprotkb/Q13884) (Beta-1-syntrophin):

> Adapter protein that binds to and probably organizes the subcellular localization of a variety of membrane proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex.

**Summary**, from NCBI Gene [6641](https://www.ncbi.nlm.nih.gov/gene/6641):

> Dystrophin is a large, rod-like cytoskeletal protein found at the inner surface of muscle fibers. Dystrophin is missing in Duchenne Muscular Dystrophy patients and is present in reduced amounts in Becker Muscular Dystrophy patients. The protein encoded by this gene is a peripheral membrane protein found associated with dystrophin and dystrophin-related proteins. This gene is a member of the syntrophin gene family, which contains at least two other structurally-related genes. [provided by …

**Accessions** — [HGNC:11168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11168) · Entrez [6641](https://www.ncbi.nlm.nih.gov/gene/6641) · UniProt [Q13884](https://www.uniprot.org/uniprotkb/Q13884) · Ensembl [ENSG00000172164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172164)

## Data

Gene col 10217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10217); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10217]; `tensor/DDL_lfc|DDL_z.npy` [10217]; `embed/gene_vectors.npy` [10217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10217 or target_col == 10217). Every well: [[SNTB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNTB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
