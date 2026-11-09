---
symbol: "IGSF3"
type: "gene"
col: 6673
ensembl_id: "ENSG00000143061"
name: "immunoglobulin superfamily member 3"
location: "1p13.1"
module: 100
arm: "+"
pooled_cpm: 28.1
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# IGSF3

*immunoglobulin superfamily member 3* — 1p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.63× (z +9.8, q 6e-20, up in 35 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (LS 180 3.63×, NCI-H460 2.81×, PANC-1 2.44×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 4.66×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.08×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (NCI-H460 3.94×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.321× (z -22.8, q 0e+00, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDS1]] (+0.61, fdr 2e-05), [[TIMP2]] (+0.61, fdr 1e-05), [[NPTN]] (+0.59, fdr 1e-05); moves opposite to [[RPAP2]] (-0.56, fdr 2e-05), [[TAF1]] (-0.54, fdr 1e-05), [[PAAF1]] (-0.53, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PLEKHG1]] → it (grade B ⚠); 3 go from it, the strongest it → [[MBOAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6673.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 3 lines (LS 180 3.63×, NCI-H460 2.81×, PANC-1 2.44×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 4.66×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.08×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (NCI-H460 3.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +9.8 | 6e-20 | 35/42 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +8.4 | 1e-14 | 35/41 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.7 | 3e-12 | 14/27 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.0 | 2e-07 | 21/39 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.15 | 10/41 (SK-MEL-2, A-172, …) | two highest doses |  |
| [[DT-061 (drug)]] 5 µM |  | 1.52× | +3.1 | 0.17 | 5/38 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.321×** | -22.8 | 0e+00 | 34/41 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.241×** | -20.1 | 0e+00 | 38/40 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.403×** | -12.4 | 6e-33 | 30/41 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.429×** | -12.0 | 6e-31 | 36/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.452×** | -11.2 | 3e-27 | 33/42 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -9.3 | 1e-18 | 32/41 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -8.5 | 2e-15 | 30/41 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.552×** | -8.4 | 3e-15 | 29/42 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -8.1 | 2e-14 | 29/40 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -7.5 | 3e-12 | 30/41 (NCI-H2347, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.626×** | -6.6 | 2e-09 | 28/41 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -6.6 | 2e-09 | 26/41 (H4, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -5.9 | 1e-07 | 26/43 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.641×** | -5.9 | 1e-07 | 26/41 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -5.4 | 3e-06 | 24/38 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.016 | 18/40 (SK-MEL-2, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 33.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 45.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0473× (z -32.9) |
| [[C32 (line)]] | wt | 67.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -18.6) |
| [[SW480 (line)]] | alt | 15.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.3) |
| [[COLO 205 (line)]] | alt | 39.2 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0106× (z -27.9) |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.0) |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -14.3) |
| [[HT-29 (line)]] | alt | 84.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -23.4) |
| [[KATO III (line)]] | alt | 22.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.1) |
| [[LS 180 (line)]] | wt | 13.8 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 3.63× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0709× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 10.2 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.81× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -21.3) |
| [[A-172 (line)]] | wt | 33.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -12.5) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 34.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.9) |
| [[H4 (line)]] | wt | 27.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0370× (z -16.4) |
| [[HS-578T (line)]] | alt | 38.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.0) |
| [[LoVo (line)]] | wt | 56.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -26.0) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0846× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 32.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.342× (z -9.1) |
| [[RKO (line)]] | wt | 13.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -11.4) |
| [[A498 (line)]] | wt | 61.6 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.373× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -10.6) |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.7) |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 51.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.336× (z -9.2) |
| [[PANC-1 (line)]] | alt | 11.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.128× (z -8.9) |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDS1]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TIMP2]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NPTN]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MCAM]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 | same gene group |
| [[ADGRB2]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | +0.57 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[JUP]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ANXA11]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SPINT1]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PCOLCE]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TAF1]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PAAF1]] | -0.53 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PIGL]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MCM3AP]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ICE2]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[C8orf33]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[PPWD1]] | -0.48 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[ZNF507]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG1]] | B | PLEKHG1 activity raises IGSF3's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.67× lower at baseline in the lines without PLEKHG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[CRYBG2]] | B | CRYBG2 activity raises IGSF3's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without CRYBG2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[MYO1D]] | B | MYO1D activity raises IGSF3's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without MYO1D | 0.015 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises IGSF3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without SEMA3B | 0.020 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ST14]] | B | ST14 activity raises IGSF3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without ST14 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ATP2C2]] | B | ATP2C2 activity raises IGSF3's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 1.84× lower at baseline in the lines without ATP2C2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[CBLC]] | B | CBLC activity raises IGSF3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.45× lower at baseline in the lines without CBLC | 0.062 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[CDS1]] | B | CDS1 activity raises IGSF3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without CDS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RTN4R]] | C | RTN4R activity raises IGSF3's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 3.26× lower at baseline in the lines without RTN4R | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBOAT1]] | B | IGSF3 activity strengthens MBOAT1's drug response | lines that do not express IGSF3 (5) vs lines expressing it (40) | the lines without IGSF3 respond 0.56× as strongly (z diff +2.87); strongest at Panobinostat 0.5 µM: 0.77x vs 0.37x (z diff +5.0) | 0.046 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3; target measured in part of the lines; artifact flags |
| [[RTN4R]] | B | IGSF3 activity raises RTN4R's level | lines that do not express IGSF3 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without IGSF3 | 0.046 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3 |
| [[IGSF8]] | B | IGSF3 activity raises IGSF8's level | lines that do not express IGSF3 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without IGSF3 | 0.081 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3 |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.7, 0.3); signed map (-13.8, 36.8). **Vector** length 92.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -20.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -12.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.1 — chr1:116,574,399-116,667,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | V8, EWI-3, MGC117164 |
| Gene groups (HGNC) | V-set domain containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [O75054](https://www.uniprot.org/uniprotkb/O75054) carries no function annotation.

**Summary**, from NCBI Gene [3321](https://www.ncbi.nlm.nih.gov/gene/3321):

> The protein encoded by this gene is an immunoglobulin-like membrane protein containing several V-type Ig-like domains. A mutation in this gene has been associated with bilateral nasolacrimal duct obstruction (LCDD). [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:5950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5950) · Entrez [3321](https://www.ncbi.nlm.nih.gov/gene/3321) · UniProt [O75054](https://www.uniprot.org/uniprotkb/O75054) · Ensembl [ENSG00000143061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143061)

## Data

Gene col 6673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6673); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6673]; `tensor/DDL_lfc|DDL_z.npy` [6673]; `embed/gene_vectors.npy` [6673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6673 or target_col == 6673). Every well: [[IGSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
