---
symbol: "PELO"
type: "gene"
col: 7650
ensembl_id: "ENSG00000152684"
name: "pelota mRNA surveillance and ribosome rescue factor"
location: "5q11.2"
module: 194
arm: "-"
pooled_cpm: 40.82
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# PELO

*pelota mRNA surveillance and ribosome rescue factor* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.18× (z +10.5, q 4e-23, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.526× (z -8.7, q 2e-15, down in 25 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.755× (z -5.6, q 6e-06, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL4D]] (+0.59, fdr 1e-04), [[FAM104A]] (+0.58, fdr 1e-05), [[RGL1]] (+0.54, fdr 3e-05); moves opposite to [[PCNT]] (-0.60, fdr 1e-05), [[ZMYND11]] (-0.59, fdr 1e-05), [[PAK2]] (-0.57, fdr 6e-05).
> It sits in the **-** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.18×** | +10.5 | 4e-23 | 42/49 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +9.1 | 3e-17 | 34/48 (HT-29, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +8.3 | 2e-14 | 35/48 (PANC-1, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.5 | 9e-09 | 31/47 (LoVo, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 1e-06 | 30/48 (A498, HS-578T, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.48×** | +5.5 | 4e-06 | 24/47 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.1 | 3e-05 | 20/48 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.42×** | +4.7 | 1e-04 | 25/48 (J82, A498, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.002 | 18/46 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 21/47 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.004 | 25/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.060 | 11/47 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +3.1 | 0.092 | 14/48 (NCI-H460, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -8.7 | 2e-15 | 25/33 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -5.6 | 6e-06 | 28/48 (SW 900, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.698×** | -4.9 | 1e-04 | 23/45 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.732×** | -4.4 | 0.001 | 22/48 (SW 900, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -4.4 | 0.001 | 23/48 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -4.2 | 0.003 | 16/48 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.727×** | -4.1 | 0.003 | 19/37 (LS 180, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.018 | 20/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.763×** | -3.2 | 0.075 | 14/49 (SW 900, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.647×** | -3.2 | 0.075 | 10/49 (SW 900, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.798×** | -3.2 | 0.075 | 15/48 (SW 1088, A-172, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.075 | 14/47 (SW 900, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 334 | 1 (1 ⚠) | 20 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.76× (z +8.5) ⚠ cell-cycle shift, explains ~88% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -21.3) |
| [[NCI-H2347 (line)]] | alt | 108 | 3 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.27× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.3) |
| [[A498 (line)]] | wt | 64.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.24× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 77.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -16.8) |
| [[CHP-212 (line)]] | wt | 145 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0822× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.6) |
| [[HS-578T (line)]] | alt | 39.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 45.4 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -17.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.9 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.67× (z +13.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.83× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.47× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 71.1 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 5.73× (z +10.6) ⚠ cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.4) |
| [[SNU-423 (line)]] | alt | 34.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 50.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.46× (z +10.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0894× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4D]] | +0.59 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[FAM104A]] | +0.58 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RGL1]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[UBTD2]] | +0.53 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[MCTP2]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[IFI27L2]] | +0.51 | +0.25 / +0.53 | both halves | 4e-04 |  |
| [[RIMKLA]] | +0.51 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[TRAPPC5]] | +0.51 | +0.27 / +0.51 | both halves | 3e-04 |  |
| [[CDK18]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[GRAMD1A]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[LSM10]] | +0.50 | +0.21 / +0.53 | both halves | 7e-04 |  |
| [[RNF181]] | +0.50 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNT]] | -0.60 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PAK2]] | -0.57 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[UBTF]] | -0.56 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[ZNF236]] | -0.55 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PSMD6-AS1]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PHF2]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[FAM120A]] | -0.52 | -0.18 / -0.63 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CERS2]] | -0.50 | -0.19 / -0.52 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PARVA]] | -0.50 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[OXCT1]] | -0.49 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ERLIN2]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[SCRN1]] | -0.49 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[FGD5-AS1]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA1]] | B | ITGA1 activity raises PELO's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without ITGA1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[PDLIM4]] | B | PDLIM4 activity raises PELO's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without PDLIM4 | 0.052 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3 |
| [[TOP2A]] | B | TOP2A activity raises PELO's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **-** arm (projection on the module's main direction -0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.0, 4.0); signed map (-12.8, 47.2). **Vector** length 97.9, 23.4% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.7 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | pelota mRNA surveillance and ribosome rescue factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:52,787,916-52,804,044 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRX2](https://www.uniprot.org/uniprotkb/Q9BRX2) (Protein pelota homolog):

> Component of the Pelota-HBS1L complex, a complex that recognizes stalled ribosomes and triggers the No-Go Decay (NGD) pathway. In the Pelota-HBS1L complex, PELO recognizes ribosomes stalled at the 3' end of an mRNA and engages stalled ribosomes by destabilizing mRNA in the mRNA channel. Following mRNA extraction from stalled ribosomes by the SKI complex, the Pelota-HBS1L complex promotes recruitment of ABCE1, which drives the disassembly of stalled ribosomes, followed by degradation of damaged …

**Summary**, from NCBI Gene [53918](https://www.ncbi.nlm.nih.gov/gene/53918):

> This gene encodes a protein which contains a conserved nuclear localization signal. The encoded protein may have a role in spermatogenesis, cell cycle control, and in meiotic cell division. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8829) · Entrez [53918](https://www.ncbi.nlm.nih.gov/gene/53918) · UniProt [Q9BRX2](https://www.uniprot.org/uniprotkb/Q9BRX2) · Ensembl [ENSG00000152684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152684)

## Data

Gene col 7650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7650); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7650]; `tensor/DDL_lfc|DDL_z.npy` [7650]; `embed/gene_vectors.npy` [7650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7650 or target_col == 7650). Every well: [[PELO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PELO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
