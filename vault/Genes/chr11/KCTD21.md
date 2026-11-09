---
symbol: "KCTD21"
type: "gene"
col: 12075
ensembl_id: "ENSG00000188997"
name: "potassium channel tetramerization domain containing 21"
location: "11q14.1"
module: 2
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KCTD21

*potassium channel tetramerization domain containing 21* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.64× (z +5.3, q 7e-05, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.364× (z -15.2, q 0e+00, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP35]] (+0.71, fdr 7e-06, ⚠ same locus), [[TANGO2]] (+0.67, fdr 7e-06), [[RBAK-RBAKDN]] (+0.65, fdr 1e-05), [[TRIP4]] (+0.65, fdr 7e-06); moves opposite to [[MBNL3]] (-0.65, fdr 1e-05), [[ZNF827]] (-0.62, fdr 4e-05), [[MEIS2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.64×** | +5.3 | 7e-05 | 21/44 (NCI-H23, RPMI-7951, …) | two highest doses | low cells (technical?); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +3.7 | 0.051 | 17/44 (NCI-H460, RPMI-7951, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.052 | 13/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.36× | +3.3 | 0.16 | 15/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.33× | +3.0 | 0.28 | 7/46 (PANC-1, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.364×** | -15.2 | 0e+00 | 36/40 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.385×** | -14.4 | 3e-44 | 33/39 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.268×** | -14.0 | 2e-42 | 42/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.298×** | -12.9 | 8e-36 | 33/41 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.385×** | -10.2 | 3e-22 | 37/45 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.406×** | -9.6 | 9e-20 | 33/45 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.382×** | -9.2 | 4e-18 | 33/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.234×** | -8.1 | 4e-14 | 32/43 (Hs 766T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.428×** | -8.1 | 4e-14 | 26/38 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.461×** | -7.4 | 1e-11 | 27/39 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.576×** | -5.9 | 2e-07 | 23/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.585×** | -5.7 | 6e-07 | 23/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -5.6 | 1e-06 | 25/46 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.622×** | -4.5 | 2e-04 | 18/36 (NCI-H1573, HCT15, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.445×** | -4.5 | 2e-04 | 19/41 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.660×** | -4.4 | 4e-04 | 20/45 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.002 | 17/47 (RPMI-7951, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -3.8 | 0.005 | 15/46 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.541×** | -3.4 | 0.019 | 10/43 (J82, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 15.2 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -13.5) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -17.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 5.58 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -11.7) |
| [[PANC-1 (line)]] | alt | 7.07 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0903× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 6.87 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0730× (z -11.1) |
| [[Hs 766T (line)]] | wt | 8.39 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -14.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ritonavir (drug)]] 0.5 µM 0.0796× (z -10.6) |
| [[J82 (line)]] | alt | 5.52 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0607× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 5.25 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0965× (z -13.0) |
| [[A549 (line)]] | wt | 8.78 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0718× (z -11.2) |
| [[SW480 (line)]] | alt | 6.69 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0301× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 7.33 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.5) |
| [[HT-29 (line)]] | alt | 7.56 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 6.53 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0827× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 5.36 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0993× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 8.20 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0497× (z -12.1) |
| [[SNU-423 (line)]] | alt | 7.23 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 9.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 6.50 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0575× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 7.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0386× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 6.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0842× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 8.33 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -9.6) |
| [[SW1417 (line)]] | alt | 5.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP35]] | +0.71 | +0.68 / +0.58 | both halves | 7e-06 | STRING 516; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[TANGO2]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RBAK-RBAKDN]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TRIP4]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TECPR1]] | +0.64 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[YKT6]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PCYT1A]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RPS6KC1]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[PSMD9]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PSMD3]] | +0.61 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[FCHSD1]] | +0.61 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL3]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ZNF827]] | -0.62 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MEIS2]] | -0.62 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PARP8]] | -0.60 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[YAP1]] | -0.60 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[CASD1]] | -0.60 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[LRRC37A4P]] | -0.59 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TBC1D5]] | -0.59 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LINC00869-1]] | -0.57 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ARID2]] | -0.57 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SLC16A9]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KCTD21's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises KCTD21's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without TMEM92-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[CYP2R1]] | C | CYP2R1 activity lowers KCTD21's level | lines that do not express CYP2R1 (3) vs lines expressing it (47) | 1.74× higher at baseline in the lines without CYP2R1 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: PIM2, CDCA7, NMRAL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.3, 1.1); signed map (-33.7, 0.2). **Vector** length 76.1, 14.3% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -15.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.8 | -14.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,171,249-78,188,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCASH2 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0X4](https://www.uniprot.org/uniprotkb/Q4G0X4) (BTB/POZ domain-containing protein KCTD21):

> Probable substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex mediating the ubiquitination and subsequent proteasomal degradation of target proteins. Promotes the ubiquitination of HDAC1. Can function as antagonist of the Hedgehog pathway by affecting the nuclear transfer of transcription factor GLI1; the function probably occurs via HDAC1 down-regulation, keeping GLI1 acetylated and inactive. Inhibits cell growth and tumorigenicity of medulloblastoma (MDB).

**Summary**, from NCBI Gene [283219](https://www.ncbi.nlm.nih.gov/gene/283219):

> Enables cullin family protein binding activity; histone deacetylase binding activity; and identical protein binding activity. Involved in negative regulation of smoothened signaling pathway and ubiquitin-dependent protein catabolic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27452) · Entrez [283219](https://www.ncbi.nlm.nih.gov/gene/283219) · UniProt [Q4G0X4](https://www.uniprot.org/uniprotkb/Q4G0X4) · Ensembl [ENSG00000188997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188997)

## Data

Gene col 12075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12075); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12075]; `tensor/DDL_lfc|DDL_z.npy` [12075]; `embed/gene_vectors.npy` [12075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12075 or target_col == 12075). Every well: [[KCTD21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
