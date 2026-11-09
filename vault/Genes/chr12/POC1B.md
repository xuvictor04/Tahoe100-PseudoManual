---
symbol: "POC1B"
type: "gene"
col: 6291
ensembl_id: "ENSG00000139323"
name: "POC1 centriolar protein B"
location: "12q21.33"
module: 92
arm: "+"
pooled_cpm: 51.45
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# POC1B

*POC1 centriolar protein B* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +8.9, q 2e-16, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.23×, PANC-1 1.64×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 3.41×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.562× (z -18.7, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHSL1]] (+0.61, fdr 7e-06), [[DOCK9]] (+0.58, fdr 1e-05), [[SPRY4-AS1]] (+0.58, fdr 1e-05); moves opposite to [[RAB30]] (-0.58, fdr 1e-05), [[RAB9A]] (-0.57, fdr 1e-05), [[DHFR2]] (-0.56, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.23×, PANC-1 1.64×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 3.41×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +8.9 | 2e-16 | 23/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.1 | 1e-13 | 31/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.008 | 21/48 (LS 180, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +3.4 | 0.080 | 16/47 (HOP62, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.562×** | -18.7 | 0e+00 | 39/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -15.0 | 0e+00 | 39/47 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -14.1 | 4e-43 | 40/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -13.4 | 1e-38 | 38/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -10.8 | 6e-25 | 33/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -10.1 | 7e-22 | 39/49 (NCI-H23, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -10.0 | 2e-21 | 39/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.677×** | -9.3 | 1e-18 | 32/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.693×** | -8.8 | 1e-16 | 34/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -8.6 | 6e-16 | 35/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -8.3 | 4e-15 | 27/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -8.2 | 1e-14 | 30/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -6.3 | 2e-08 | 25/47 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.810×** | -6.1 | 3e-08 | 25/48 (Hs 766T, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.776×** | -6.0 | 6e-08 | 27/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.785×** | -5.8 | 3e-07 | 22/49 (Hs 766T, SW 900, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -5.7 | 4e-07 | 25/48 (C-33 A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -5.3 | 4e-06 | 25/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.3 | 0 | 12 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -17.8) |
| [[Hs 766T (line)]] | wt | 74.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.8) |
| [[LS 180 (line)]] | wt | 114 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.1) |
| [[SW480 (line)]] | alt | 62.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 52.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 70.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -24.1) |
| [[PANC-1 (line)]] | alt | 36.4 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.2) |
| [[SNU-1 (line)]] | wt | 78.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 58.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.9) |
| [[A-172 (line)]] | wt | 47.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.2) |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.398× (z -9.6) |
| [[J82 (line)]] | alt | 46.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.296× (z -11.6) |
| [[RKO (line)]] | wt | 58.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -10.0) |
| [[A549 (line)]] | wt | 55.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.2) |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.3) |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -8.8) |
| [[KATO III (line)]] | alt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 58.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.326× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 79.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -14.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 51.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -14.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.5) |
| [[A498 (line)]] | wt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.7) | — |
| [[C32 (line)]] | wt | 40.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -14.1) |
| [[H4 (line)]] | wt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.4) |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.614× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.0) |
| [[SW48 (line)]] | wt | 61.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHSL1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[DOCK9]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.57 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[RECQL]] | +0.54 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ACOT7]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NUP205]] | +0.53 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[TTL]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SRPK1]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[SUV39H2]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PTDSS1]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[MALT1]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[DHFR2]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NECAP1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SRSF11]] ⚠ | -0.55 | -0.50 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NFKBIA]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PIM3]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SREK1]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[XPA]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[UAP1L1]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[LIPT1]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MOSPD2]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POC1B's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, -7.0); signed map (-11.9, 44.6). **Vector** length 100, 24.4% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.9 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | POC1 centriolar protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:89,419,718-89,526,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TUWD12, FLJ14923; previously WDR51B |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC44](https://www.uniprot.org/uniprotkb/Q8TC44) (POC1 centriolar protein homolog B):

> Plays an important role in centriole assembly and/or stability and ciliogenesis. Involved in early steps of centriole duplication, as well as in the later steps of centriole length control. Acts in concert with POC1A to ensure centriole integrity and proper mitotic spindle formation. Required for primary cilia formation, ciliary length and also cell proliferation. Required for retinal integrity. Acts as a positive regulator of centriole elongation.

**Summary**, from NCBI Gene [282809](https://www.ncbi.nlm.nih.gov/gene/282809):

> POC1 proteins contain an N-terminal WD40 domain and a C-terminal coiled coil domain and are part of centrosomes. They play an important role in basal body and cilia formation. This gene encodes one of the two POC1 proteins found in humans. Mutation in this gene result in autosomal-recessive cone-rod dystrophy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:30836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30836) · Entrez [282809](https://www.ncbi.nlm.nih.gov/gene/282809) · UniProt [Q8TC44](https://www.uniprot.org/uniprotkb/Q8TC44) · Ensembl [ENSG00000139323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139323)

## Data

Gene col 6291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6291); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6291]; `tensor/DDL_lfc|DDL_z.npy` [6291]; `embed/gene_vectors.npy` [6291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6291 or target_col == 6291). Every well: [[POC1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POC1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
