---
symbol: "CCDC57"
type: "gene"
col: 10689
ensembl_id: "ENSG00000176155"
name: "coiled-coil domain containing 57"
location: "17q25.3"
module: 4
arm: "+"
pooled_cpm: 69.41
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCDC57

*coiled-coil domain containing 57* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.96× (z +9.7, q 2e-19, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.496× (z -10.1, q 5e-21, down in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.498× (z -10.0, q 6e-21, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCA4]] (+0.65, fdr 1e-05), [[CENPB]] (+0.60, fdr 1e-05), [[IQCH]] (+0.58, fdr 3e-05); moves opposite to [[SMPDL3A]] (-0.61, fdr 1e-05), [[CIAO2A]] (-0.57, fdr 2e-05), [[FHIP2A]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +9.7 | 2e-19 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +8.9 | 1e-16 | 40/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +7.8 | 1e-12 | 39/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +7.1 | 2e-10 | 32/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.003 | 23/48 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.006 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.023 | 25/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 1.51× | +3.1 | 0.13 | 21/49 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.0 | 0.14 | 15/48 (SW480, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -10.1 | 5e-21 | 38/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -10.0 | 6e-21 | 40/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -6.9 | 1e-09 | 38/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.713×** | -6.8 | 1e-09 | 33/48 (J82, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -6.8 | 1e-09 | 38/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -6.6 | 4e-09 | 34/48 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -5.9 | 3e-07 | 33/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -5.8 | 5e-07 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -4.7 | 2e-04 | 28/48 (J82, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.549×** | -4.5 | 4e-04 | 25/45 (J82, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -4.4 | 5e-04 | 28/50 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -4.3 | 8e-04 | 25/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.616×** | -3.6 | 0.013 | 24/48 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -3.6 | 0.014 | 23/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.017 | 21/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -3.5 | 0.017 | 23/48 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.050 | 17/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 123 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.2) |
| [[BT-474 (line)]] | alt | 118 | 0 | 8 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.110× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.3) |
| [[J82 (line)]] | alt | 61.6 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -13.1) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -13.9) |
| [[SW480 (line)]] | alt | 78.5 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -12.3) |
| [[A-427 (line)]] | wt | 80.2 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -14.5) |
| [[LoVo (line)]] | wt | 55.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 70.0 | 1 | 4 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.28× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 125 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.0716× (z -12.9) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.426× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 18.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.62× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 89.7 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.9) |
| [[C32 (line)]] | wt | 77.6 | 0 | 3 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.265× (z -10.2) |
| [[COLO 205 (line)]] | alt | 68.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 60.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +20.5) | — |
| [[HT-29 (line)]] | alt | 70.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 35.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 23.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 57.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 51.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.190× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 60.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 100.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.493× (z -11.2) |
| [[HOP62 (line)]] | alt | 92.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +16.6) | — |
| [[KATO III (line)]] | alt | 72.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 67.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 77.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.321× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 53.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 62.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +14.2) | — |
| [[A-172 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | +0.65 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CENPB]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[IQCH]] | +0.58 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[FAF1]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[DDX10]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[R3HDM2]] | +0.57 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MAP3K14]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NAA15]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM185B]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[TAF1B]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SERBP1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[REXO1]] | +0.53 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPDL3A]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CIAO2A]] | -0.57 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[FHIP2A]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MICA]] | -0.56 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TMEM94]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[APTR]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ORMDL1]] | -0.54 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[SNX3]] | -0.53 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ABCD4]] | -0.53 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[SLC18B1]] | -0.53 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[GNAS]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DNASE2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC57's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.367). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.4, -38.8); signed map (8.8, -48.4). **Vector** length 107, 32.9% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Omeprazole (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.5 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,101,460-82,212,878 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00130, FLJ23754 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAC2](https://www.uniprot.org/uniprotkb/Q2TAC2) (Coiled-coil domain-containing protein 57):

> Pleiotropic regulator of centriole duplication, mitosis, and ciliogenesis. Critical interface between centrosome and microtubule-mediated cellular processes. Centriole duplication protein required for recruitment of CEP63, CEP152, and PLK4 to the centrosome. Independent of its centrosomal targeting, localizes to and interacts with microtubules and regulates microtubule nucleation, stability, and mitotic progression.

**Summary**, from NCBI Gene [284001](https://www.ncbi.nlm.nih.gov/gene/284001):

> Involved in several processes, including G2/M transition of mitotic cell cycle; cilium assembly; and microtubule cytoskeleton organization. Located in centriolar satellite; centriole; and spindle microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27564) · Entrez [284001](https://www.ncbi.nlm.nih.gov/gene/284001) · UniProt [Q2TAC2](https://www.uniprot.org/uniprotkb/Q2TAC2) · Ensembl [ENSG00000176155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176155)

## Data

Gene col 10689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10689); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10689]; `tensor/DDL_lfc|DDL_z.npy` [10689]; `embed/gene_vectors.npy` [10689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10689 or target_col == 10689). Every well: [[CCDC57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
