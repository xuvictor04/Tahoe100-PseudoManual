---
symbol: "LRRIQ1"
type: "gene"
col: 5461
ensembl_id: "ENSG00000133640"
name: "leucine rich repeats and IQ motif containing 1"
location: "12q21.31"
module: 9
arm: "+"
pooled_cpm: 4.62
n_lines_expressing: 29
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LRRIQ1

*leucine rich repeats and IQ motif containing 1* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.07× (z +18.2, q 0e+00, up in 27 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0494×, NCI-H460 0.109×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0988×; ⚠ cell-cycle shift, explains ~66% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0391×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0669×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYDIN]] (+0.58, fdr 1e-05), [[CFAP299]] (+0.55, fdr 1e-04), [[DNAAF4]] (+0.55, fdr 1e-05); moves opposite to [[EEF1AKMT3]] (-0.49, fdr 4e-05), [[CRLS1]] (-0.46, fdr 3e-05), [[CCDC168]] (-0.45, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CSRNP3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAP9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.07×** | +18.2 | 0e+00 | 27/27 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.40×** | +15.9 | 0e+00 | 26/27 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **5.88×** | +14.7 | 0e+00 | 26/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +11.5 | 2e-28 | 20/24 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.7 | 5e-20 | 6/8 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.0 | 3e-17 | 10/17 (A549, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.73×** | +8.3 | 8e-15 | 25/27 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.62×** | +7.7 | 1e-12 | 19/26 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +7.6 | 3e-12 | 3/12 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.9 | 3e-10 | 8/24 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.26×** | +6.5 | 4e-09 | 21/23 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +5.8 | 3e-07 | 10/25 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.2 | 9e-06 | 10/24 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.29×** | +5.1 | 1e-05 | 19/27 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.002 | 14/27 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.098 | 8/25 (NCI-H23, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5461.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0494×, NCI-H460 0.109×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0988×; ⚠ cell-cycle shift, explains ~66% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0391×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0669×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.656× | -3.5 | 0.12 | 11/27 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.448× | -3.5 | 0.12 | 11/26 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.662× | -3.4 | 0.12 | 9/26 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.90 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 21.3× (z +12.4) | [[Digitoxin (drug)]] 0.05 µM 0.0391× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 30.2 | 2 (1 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.4) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 4.52× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -13.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H1573 (line)]] | alt | 3.73 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 21.1× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0494× (z -9.4) |
| [[A498 (line)]] | wt | 2.80 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 38.9× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.72× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 1.80 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 33.1× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 7.12 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.6× (z +10.9) | — |
| [[C32 (line)]] | wt | 2.52 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 57.3× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 5.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +8.5) | — |
| [[J82 (line)]] | alt | 11.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 1.93 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 19.3× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 4.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYDIN]] | +0.58 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CFAP299]] | +0.55 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[DNAAF4]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAP9]] | +0.53 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[TBC1D19]] | +0.51 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[SCN2A]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[FMN2]] | +0.51 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[FGF14]] | +0.50 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[NFASC]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SRRM3]] | +0.49 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[SYT1]] | +0.49 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[IGSF1]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT3]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CRLS1]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.45 | -0.24 / -0.42 | both halves | 4e-04 |  |
| [[TSNAX-DISC1]] | -0.44 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[PCGF2]] | -0.44 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TMEM68]] | -0.43 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[NEU3]] | -0.43 | -0.20 / -0.36 | ⚠ not reproduced | 8e-04 |  |
| [[EEF1AKMT4]] | -0.42 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[PRSS53]] | -0.41 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RCC1]] | -0.41 | -0.03 / -0.33 | ⚠ not reproduced | 0.006 |  |
| [[PHC2-AS1]] | -0.40 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[SLC19A2]] | -0.40 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[MAN2C1]] | -0.40 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[TMEM165]] | -0.40 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSRNP3]] | B | CSRNP3 activity raises LRRIQ1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without CSRNP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[CDH12]] | B | CDH12 activity weakens LRRIQ1's drug response | lines that do not express CDH12 (16) vs lines expressing it (11) | the lines without CDH12 respond 1.27× as strongly (z diff -0.46); strongest at Dinaciclib 0.05 µM: 1.60x vs 0.62x (z diff -4.0) | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CDH12]] | B | CDH12 activity raises LRRIQ1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without CDH12 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[LGSN]] | C | LGSN activity raises LRRIQ1's level | lines that do not express LGSN (36) vs lines expressing it (14) | 3.42× lower at baseline in the lines without LGSN | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, LINC03046, RNF212; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP9]] | C | LRRIQ1 activity raises MAP9's level | lines that do not express LRRIQ1 (21) vs lines expressing it (29) | 6.17× lower at baseline in the lines without LRRIQ1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP9, GNB4, ECHDC3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.7, 32.0); signed map (40.2, 32.7). **Vector** length 52.9, 10.2% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and IQ motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:85,036,314-85,264,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12303, KIAA1801 |
| Matched by | ensembl_id |

UniProt [Q96JM4](https://www.uniprot.org/uniprotkb/Q96JM4) carries no function annotation.

**Summary**, from NCBI Gene [84125](https://www.ncbi.nlm.nih.gov/gene/84125):

> Predicted to be involved in regulation of signal transduction. Predicted to act upstream of or within apoptotic process; gene expression; and single fertilization. Predicted to be active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25708) · Entrez [84125](https://www.ncbi.nlm.nih.gov/gene/84125) · UniProt [Q96JM4](https://www.uniprot.org/uniprotkb/Q96JM4) · Ensembl [ENSG00000133640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133640)

## Data

Gene col 5461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5461); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5461]; `tensor/DDL_lfc|DDL_z.npy` [5461]; `embed/gene_vectors.npy` [5461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5461 or target_col == 5461). Every well: [[LRRIQ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRIQ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
