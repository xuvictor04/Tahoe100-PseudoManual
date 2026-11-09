---
symbol: "RIN3"
type: "gene"
col: 1996
ensembl_id: "ENSG00000100599"
name: "Ras and Rab interactor 3"
location: "14q32.12"
module: 5
arm: "+"
pooled_cpm: 29.63
n_lines_expressing: 43
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RIN3

*Ras and Rab interactor 3* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Sapanisertib (drug)]] 0.05 µM: 1.34× (z +4.0, q 0.020, up in 16 of 41 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 1.68× (z +4.0, q 0.020, up in 16 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.123× (z -30.8, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRK1]] (+0.63, fdr 6e-05), [[WNT5B]] (+0.51, fdr 4e-05), [[DHX37]] (+0.50, fdr 2e-04); moves opposite to [[PJA2]] (-0.49, fdr 4e-04), [[KLHL32]] (-0.45, fdr 1e-04), [[LINC00482]] (-0.45, fdr 3e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PARVA]] → it (grade B ⚠); 4 go from it, the strongest it → [[DOCK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.34×** | +4.0 | 0.020 | 16/41 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.020 | 16/41 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.123×** | -30.8 | 0e+00 | 41/41 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.136×** | -29.3 | 0e+00 | 40/41 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.147×** | -28.1 | 0e+00 | 40/41 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.274×** | -26.8 | 0e+00 | 37/40 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.267×** | -18.6 | 0e+00 | 38/41 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.327×** | -16.4 | 0e+00 | 39/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.359×** | -15.0 | 0e+00 | 37/40 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.409×** | -13.1 | 2e-37 | 34/41 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.428×** | -12.5 | 7e-34 | 32/41 (NCI-H23, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.474×** | -10.9 | 4e-26 | 32/41 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -10.8 | 1e-25 | 30/40 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -10.5 | 6e-24 | 30/41 (SW 900, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.262×** | -10.3 | 4e-23 | 37/42 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.510×** | -9.5 | 1e-19 | 27/39 (LoVo, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.520×** | -9.2 | 1e-18 | 19/27 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.540×** | -7.8 | 2e-13 | 27/41 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.364×** | -7.8 | 3e-13 | 34/41 (CHP-212, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.701×** | -7.4 | 4e-12 | 33/41 (SK-MEL-2, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.617×** | -7.1 | 4e-11 | 27/41 (HEC-1-A, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 38.5 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.4) |
| [[NCI-H1792 (line)]] | alt | 74.0 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.5) |
| [[SW 900 (line)]] | alt | 55.3 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0578× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0835× (z -22.1) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -22.8) |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0755× (z -22.5) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -18.8) |
| [[SW48 (line)]] | wt | 61.2 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0269× (z -22.9) |
| [[LOX-IMVI (line)]] | wt | 35.6 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0572× (z -23.9) |
| [[HEC-1-A (line)]] | alt | 38.2 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.9) |
| [[RKO (line)]] | wt | 55.6 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -19.4) |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.3) |
| [[A549 (line)]] | wt | 61.6 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0721× (z -23.5) |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.123× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 53.3 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0714× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 77.4 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0879× (z -18.5) |
| [[A-172 (line)]] | wt | 24.5 | 0 | 8 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0459× (z -19.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.100× (z -14.9) |
| [[J82 (line)]] | alt | 47.4 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.2) |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 8 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0881× (z -13.9) |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0646× (z -18.7) |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -23.9) |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -18.0) |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.1) |
| [[C32 (line)]] | wt | 50.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -17.7) |
| [[H4 (line)]] | wt | 42.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0354× (z -20.2) |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0728× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0877× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0633× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.101× (z -13.2) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.0) |
| [[CHP-212 (line)]] | wt | 35.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0465× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.4) |
| [[A498 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 13 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRK1]] | +0.63 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[WNT5B]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[DHX37]] | +0.50 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[AVEN]] | +0.49 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[MVB12B]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SETMAR]] | +0.48 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[ZNF195]] | +0.48 | +0.31 / +0.37 | both halves | 2e-04 |  |
| [[ZNF124]] | +0.48 | +0.29 / +0.27 | both halves | 3e-04 |  |
| [[METTL8]] | +0.48 | +0.29 / +0.41 | both halves | 2e-04 |  |
| [[NOL9]] | +0.47 | +0.34 / +0.36 | both halves | 1e-04 |  |
| [[SETD6]] | +0.46 | +0.37 / +0.34 | both halves | 1e-04 |  |
| [[SLFNL1-AS1]] | +0.46 | +0.27 / +0.35 | both halves | 3e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.49 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[KLHL32]] | -0.45 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[LINC00482]] | -0.45 | -0.26 / -0.45 | both halves | 3e-04 |  |
| [[FRY]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PIP4P2]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[FAM13A]] | -0.43 | -0.22 / -0.37 | both halves | 6e-04 | STRING 623 |
| [[SNAP25]] | -0.42 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CPE]] | -0.42 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[GABRA2]] | -0.42 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ARHGAP12]] | -0.42 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[RADX]] | -0.41 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[PTP4A2]] | -0.41 | -0.21 / -0.29 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVA]] | B | PARVA activity raises RIN3's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without PARVA | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK1]] | B | RIN3 activity raises DOCK1's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.87× lower at baseline in the lines without RIN3 | 0.051 | ⚠ within organs, on part of the lines |
| [[PACRGL]] | B | RIN3 activity raises PACRGL's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.44× lower at baseline in the lines without RIN3 | 0.070 | ⚠ within organs, on part of the lines |
| [[SUCLG2]] | B | RIN3 activity raises SUCLG2's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RIN3 | 0.074 | ⚠ within organs, on part of the lines |
| [[GABRA2]] | B | RIN3 activity lowers GABRA2's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.77× higher at baseline in the lines without RIN3 | 0.088 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.4, -31.5); signed map (4.4, -48.3). **Vector** length 69.3, 16.2% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +2.9 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.3 | -10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -12.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | Ras and Rab interactor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,513,781-92,688,994 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22439 |
| Gene groups (HGNC) | VPS9 domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB24](https://www.uniprot.org/uniprotkb/Q8TB24) (Ras and Rab interactor 3):

> Ras effector protein that functions as a guanine nucleotide exchange (GEF) for RAB5B and RAB31, by exchanging bound GDP for free GTP. Required for normal RAB31 function.

**Summary**, from NCBI Gene [79890](https://www.ncbi.nlm.nih.gov/gene/79890):

> Summary: This protein encoded by this gene is a member of the RIN family of Ras interaction-interference proteins, which are binding partners to the RAB5 small GTPases. The protein functions as a guanine nucleotide exchange for RAB5B and RAB31. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:18751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18751) · Entrez [79890](https://www.ncbi.nlm.nih.gov/gene/79890) · UniProt [Q8TB24](https://www.uniprot.org/uniprotkb/Q8TB24) · Ensembl [ENSG00000100599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100599)

## Data

Gene col 1996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1996); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1996]; `tensor/DDL_lfc|DDL_z.npy` [1996]; `embed/gene_vectors.npy` [1996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1996 or target_col == 1996). Every well: [[RIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
