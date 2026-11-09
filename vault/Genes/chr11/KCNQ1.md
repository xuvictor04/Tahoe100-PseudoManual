---
symbol: "KCNQ1"
type: "gene"
col: 599
ensembl_id: "ENSG00000053918"
name: "potassium voltage-gated channel subfamily Q member 1"
location: "11p15.5-p15.4"
module: 44
arm: "+"
pooled_cpm: 27.29
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# KCNQ1

*potassium voltage-gated channel subfamily Q member 1* — 11p15.5-p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +19.3, q 0e+00, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.586× (z -10.7, q 5e-24, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AATK]] (+0.73, fdr 7e-06), [[LINC02580]] (+0.62, fdr 7e-06), [[CFAP92]] (+0.61, fdr 7e-06); moves opposite to [[CNRIP1]] (-0.49, fdr 3e-04), [[ZNF287]] (-0.48, fdr 1e-04), [[EIF2B4]] (-0.48, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +19.3 | 0e+00 | 31/48 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.1 | 2e-26 | 24/42 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +10.6 | 7e-24 | 27/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +10.0 | 3e-21 | 27/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.9 | 4e-17 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.4 | 6e-15 | 17/33 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +8.1 | 5e-14 | 24/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +7.9 | 2e-13 | 23/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +6.3 | 2e-08 | 16/37 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.3 | 2e-08 | 22/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 4e-06 | 19/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +3.5 | 0.019 | 14/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.029 | 4/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.1 | 0.080 | 15/47 (SNU-423, AsPC-1, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -10.7 | 5e-24 | 31/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -7.0 | 6e-10 | 24/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.734×** | -6.2 | 1e-07 | 24/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.766×** | -5.4 | 1e-05 | 23/47 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -5.1 | 3e-05 | 18/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -5.1 | 3e-05 | 16/47 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.782×** | -4.9 | 7e-05 | 19/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.787×** | -4.8 | 1e-04 | 18/47 (KATO III, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.006 | 20/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.825×** | -3.9 | 0.006 | 14/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.875× | -3.8 | 0.008 | 11/48 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -3.8 | 0.008 | 15/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -3.7 | 0.009 | 3/48 (C-33 A, SW 1088, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.029 | 13/46 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.857× | -3.1 | 0.069 | 11/47 (LS 180, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 57.7 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.192× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -13.4) |
| [[PANC-1 (line)]] | alt | 15.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +13.8) | — |
| [[SW480 (line)]] | alt | 30.6 | 5 | 1 | [[Auranofin (drug)]] 5 µM 3.14× (z +12.8) | [[Harringtonine (drug)]] 5 µM 0.395× (z -9.9) |
| [[RKO (line)]] | wt | 55.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 16.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +17.5) | — |
| [[A-172 (line)]] | wt | 22.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +30.7) | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.9) |
| [[A498 (line)]] | wt | 17.4 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +14.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 68.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -10.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.5) |
| [[KATO III (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -16.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.9) |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 2 | — | [[Hesperidin (drug)]] 5 µM 0.0662× (z -12.5) |
| [[C32 (line)]] | wt | 10.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.4) |
| [[LS 180 (line)]] | wt | 145 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 10.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 13.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +18.1) | — |
| [[HS-578T (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +13.9) | — |
| [[J82 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 9.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +17.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +25.0) | — |
| [[NCI-H2347 (line)]] | alt | 9.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.60× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.4) | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AATK]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LINC02580]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CFAP92]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PDE4C]] | +0.60 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[ASS1]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[BCL2L14]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EPHA1-AS1]] | +0.57 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC11B]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[VIPR1]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[LINC02331]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNRIP1]] | -0.49 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[ZNF287]] | -0.48 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[EIF2B4]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCN1]] | B | HCN1 activity raises KCNQ1's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without HCN1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |
| [[FGFR2]] | B | FGFR2 activity raises KCNQ1's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 3.30× lower at baseline in the lines without FGFR2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2 |
| [[HCN1]] | B | HCN1 activity weakens KCNQ1's drug response | lines that do not express HCN1 (37) vs lines expressing it (11) | the lines without HCN1 respond 4.07× as strongly (z diff -1.68); strongest at Homoharringtonine 5 µM: 2.33x vs 0.97x (z diff -6.7) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ITGA7]] | B | ITGA7 activity lowers KCNQ1's level | lines that do not express ITGA7 (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without ITGA7 | 0.079 | ⚠ within organs, on part of the lines; also absent: NXPE3, SLC22A4, TTC23L; maybe low, not absent; its own permutation p |
| [[IQGAP2]] | B | IQGAP2 activity raises KCNQ1's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without IQGAP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity weakens KCNQ1's drug response | lines that do not express MCF2L (14) vs lines expressing it (34) | the lines without MCF2L respond 2.28× as strongly (z diff -1.97); strongest at Homoharringtonine 5 µM: 4.72x vs 1.31x (z diff -7.5) | 0.088 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 37.1); signed map (55.0, -2.2). **Vector** length 90.5, 18.7% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | -0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily Q member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5-p15.4 — chr11:2,444,654-2,849,105 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv7.1, KCNA8, KVLQT1, JLNS1, LQT1; previously LQT, KCNA9 |
| Gene groups (HGNC) | Potassium voltage-gated channels |
| Reactome | 7 pathways, smallest: Phase 3 - rapid repolarisation; Phase 2 - plateau phase; Voltage gated Potassium channels |
| Matched by | ensembl_id |

**Function**, from UniProt [P51787](https://www.uniprot.org/uniprotkb/P51787) (Potassium voltage-gated channel subfamily KQT member 1):

> Pore-forming subunit of the voltage-gated potassium (Kv) channel involved in the regulation of cardiomyocyte excitability and important in normal development and functions of myocardium, inner ear, stomach and colon. Associates with KCNE beta subunits that modulates current kinetics. Induces a voltage-dependent current by rapidly activating and slowly deactivating potassium-selective outward current. Also promotes a delayed voltage activated potassium current showing outward rectification …

**Summary**, from NCBI Gene [3784](https://www.ncbi.nlm.nih.gov/gene/3784):

> This gene encodes a voltage-gated potassium channel required for repolarization phase of the cardiac action potential. This protein can form heteromultimers with two other potassium channel proteins, KCNE1 and KCNE3. Mutations in this gene are associated with hereditary long QT syndrome 1 (also known as Romano-Ward syndrome), Jervell and Lange-Nielsen syndrome, and familial atrial fibrillation. This gene exhibits tissue-specific imprinting, with preferential expression from the maternal allele …

**Accessions** — [HGNC:6294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6294) · Entrez [3784](https://www.ncbi.nlm.nih.gov/gene/3784) · UniProt [P51787](https://www.uniprot.org/uniprotkb/P51787) · Ensembl [ENSG00000053918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053918)

## Data

Gene col 599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 599); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 599]; `tensor/DDL_lfc|DDL_z.npy` [599]; `embed/gene_vectors.npy` [599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 599 or target_col == 599). Every well: [[KCNQ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
