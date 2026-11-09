---
symbol: "ONECUT2"
type: "gene"
col: 4079
ensembl_id: "ENSG00000119547"
name: "one cut homeobox 2"
location: "18q21.31"
module: 14
arm: "+"
pooled_cpm: 19.78
n_lines_expressing: 40
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ONECUT2

*one cut homeobox 2* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.12× (z +29.4, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.789× (z -4.3, q 0.010, down in 14 of 37 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK4]] (+0.57, fdr 2e-04), [[CHGB]] (+0.50, fdr 6e-05), [[COQ2]] (+0.50, fdr 6e-05); moves opposite to [[TMPRSS5]] (-0.51, fdr 1e-04), [[NOXRED1]] (-0.51, fdr 0.001, ⚠ not reproduced), [[CCDC32]] (-0.46, fdr 2e-04), [[KCNIP2]] (-0.45, fdr 8e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STXBP6]] → it (grade B ⚠); 4 go from it, the strongest it → [[FABP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.12×** | +29.4 | 0e+00 | 34/37 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.81×** | +28.2 | 0e+00 | 34/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.69×** | +27.8 | 0e+00 | 33/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +22.5 | 0e+00 | 30/37 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.36×** | +21.8 | 0e+00 | 35/37 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.34×** | +21.6 | 0e+00 | 33/38 (J82, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +18.4 | 0e+00 | 26/38 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +14.4 | 7e-45 | 25/36 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +13.7 | 1e-40 | 27/37 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.10×** | +13.3 | 1e-38 | 29/36 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.45×** | +11.6 | 1e-29 | 32/38 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.95×** | +11.5 | 5e-29 | 11/21 (HT-29, CFPAC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.92×** | +10.8 | 9e-26 | 13/24 (HT-29, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.82×** | +10.8 | 2e-25 | 20/32 (HT-29, CFPAC-1, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.80×** | +10.1 | 1e-22 | 24/36 (A498, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.4 | 5e-09 | 18/37 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 2e-07 | 13/38 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.5 | 1e-06 | 17/38 (A549, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.8 | 4e-05 | 9/37 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.789×** | -4.3 | 0.010 | 14/37 (SNU-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.013 | 7/37 (SNU-1, KATO III, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.668×** | -3.8 | 0.025 | 3/38 (LoVo, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.688×** | -3.5 | 0.057 | 9/38 (SNU-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.1 | 0.22 | 11/37 (SNU-1, C-33 A, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.726× | -3.0 | 0.22 | 3/34 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.22 | 9/36 (SNU-1, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 205 | 0 | 10 (6 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.359× (z -14.0) |
| [[SW480 (line)]] | alt | 8.73 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.0) | — |
| [[A498 (line)]] | wt | 12.9 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 83.6 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.3) | [[Lonafarnib (drug)]] 5 µM 0.0801× (z -14.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.399× (z -9.9) |
| [[J82 (line)]] | alt | 16.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 5.46 | 6 | 0 | [[Belinostat (drug)]] 5 µM 8.16× (z +11.5) | — |
| [[A-427 (line)]] | wt | 27.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -9.1) |
| [[LoVo (line)]] | wt | 18.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 6.07 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 7.06× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.22× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 204 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 45.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) | — |
| [[A549 (line)]] | wt | 6.55 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 19.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -9.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 18.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.15× (z +10.1) | — |
| [[RKO (line)]] | wt | 20.4 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.88× (z +8.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.289× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 17.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.89× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0883× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 8.98 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.78× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +13.2) | — |
| [[A-172 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK4]] | +0.57 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[CHGB]] | +0.50 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[COQ2]] | +0.50 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[ENPP1]] | +0.50 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[BCOR]] | +0.50 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[NOL4]] | +0.49 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[STIM2]] | +0.49 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ABCG2]] | +0.49 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ASRGL1]] | +0.49 | +0.27 / +0.64 | both halves | 3e-04 |  |
| [[CAMK1D]] | +0.48 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[SSX2IP]] | +0.48 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[DOT1L]] | +0.47 | +0.12 / +0.44 | ⚠ not reproduced | 0.002 |  |
| [[TRERF1]] | +0.47 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS5]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[NOXRED1]] | -0.51 | -0.15 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[CCDC32]] | -0.46 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[KCNIP2]] | -0.45 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[VPS51]] | -0.45 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ZNF500]] | -0.44 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[GET1-SH3BGR]] | -0.44 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[VPS39]] | -0.44 | -0.20 / -0.50 | both halves | 7e-04 |  |
| [[DRD4]] | -0.44 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ACOX3]] | -0.44 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PRPF18]] | -0.44 | -0.11 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[MLYCD]] | -0.44 | -0.10 / -0.41 | ⚠ not reproduced | 0.003 |  |
| [[SLC30A6]] | -0.44 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[MKRN5P]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[PPHLN1]] | -0.43 | -0.49 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STXBP6]] | B | STXBP6 activity raises ONECUT2's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without STXBP6 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[TOP2A]] | B | TOP2A activity lowers ONECUT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FREM2]] | B | FREM2 activity raises ONECUT2's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without FREM2 | 0.072 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent |
| [[FUT9]] | B | FUT9 activity raises ONECUT2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 1.41× lower at baseline in the lines without FUT9 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FABP5]] | B | ONECUT2 activity raises FABP5's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without ONECUT2 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAPRE2]] | B | ONECUT2 activity strengthens MAPRE2's drug response | lines that do not express ONECUT2 (10) vs lines expressing it (39) | the lines without ONECUT2 respond 0.75× as strongly (z diff +1.26); strongest at Homoharringtonine 5 µM: 1.39x vs 2.01x (z diff +2.6) | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NMNAT2]] | B | ONECUT2 activity lowers NMNAT2's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 2.58× higher at baseline in the lines without ONECUT2 | 0.056 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRERF1]] | B | ONECUT2 activity lowers TRERF1's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without ONECUT2 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.346). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.0, 9.7); signed map (27.2, 33.0). **Vector** length 65.1, 10.9% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +21.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +5.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +4.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.2 | +10.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +11.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.3 | +4.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | one cut homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:57,435,374-57,491,298 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OC-2 |
| Gene groups (HGNC) | CUT class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95948](https://www.uniprot.org/uniprotkb/O95948) (One cut domain family member 2):

> Transcriptional activator. Activates the transcription of a number of liver genes such as HNF3B.

**Summary**, from NCBI Gene [9480](https://www.ncbi.nlm.nih.gov/gene/9480):

> This gene encodes a member of the onecut family of transcription factors, which are characterized by a cut domain and an atypical homeodomain. The protein binds to specific DNA sequences and stimulates expression of target genes, including genes involved in melanocyte and hepatocyte differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8139) · Entrez [9480](https://www.ncbi.nlm.nih.gov/gene/9480) · UniProt [O95948](https://www.uniprot.org/uniprotkb/O95948) · Ensembl [ENSG00000119547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119547)

## Data

Gene col 4079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4079); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4079]; `tensor/DDL_lfc|DDL_z.npy` [4079]; `embed/gene_vectors.npy` [4079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4079 or target_col == 4079). Every well: [[ONECUT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ONECUT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
