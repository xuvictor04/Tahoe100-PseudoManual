---
symbol: "THRA"
type: "gene"
col: 4730
ensembl_id: "ENSG00000126351"
name: "thyroid hormone receptor alpha"
location: "17q21.1"
module: 45
arm: "+"
pooled_cpm: 22.56
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# THRA

*thyroid hormone receptor alpha* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 1.46× (z +6.5, q 6e-08, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.409× (z -15.1, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHMT2]] (+0.71, fdr 7e-06), [[PNKD]] (+0.71, fdr 7e-06), [[ALAD]] (+0.68, fdr 1e-05); moves opposite to [[LINC01829]] (-0.71, fdr 9e-06), [[ENOX2]] (-0.63, fdr 2e-05), [[AVEN]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **1.46×** | +6.5 | 6e-08 | 36/48 (SK-MEL-2, AsPC-1, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +5.0 | 2e-04 | 31/48 (KATO III, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.9 | 2e-04 | 16/33 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.8 | 2e-04 | 20/39 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.019 | 20/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.55×** | +3.7 | 0.023 | 19/48 (KATO III, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.034 | 22/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.34×** | +3.5 | 0.036 | 18/45 (AsPC-1, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.065 | 18/47 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.073 | 15/48 (KATO III, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.14 | 18/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.409×** | -15.1 | 0e+00 | 40/47 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.371×** | -11.9 | 6e-30 | 35/45 (LS 180, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -10.6 | 4e-24 | 36/46 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -9.5 | 3e-19 | 36/45 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.511×** | -8.0 | 1e-13 | 41/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.533×** | -7.5 | 5e-12 | 39/48 (CHP-212, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -6.7 | 1e-09 | 32/46 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.701×** | -6.0 | 1e-07 | 31/48 (COLO 205, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -5.9 | 3e-07 | 30/48 (HT-29, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -5.4 | 4e-06 | 25/48 (HT-29, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.644×** | -5.1 | 2e-05 | 29/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.561×** | -4.8 | 6e-05 | 27/48 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.472×** | -4.7 | 1e-04 | 23/46 (A498, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.691×** | -4.4 | 4e-04 | 25/46 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.697×** | -4.3 | 6e-04 | 26/47 (HT-29, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.001 | 24/47 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.522×** | -4.1 | 0.002 | 23/45 (KATO III, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 47.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -19.0) |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 1 (1 ⚠) | 4 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.0) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -11.6) |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -14.9) |
| [[KATO III (line)]] | alt | 42.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -19.4) |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.6) |
| [[A-172 (line)]] | wt | 40.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -17.8) |
| [[A498 (line)]] | wt | 41.0 | 0 | 2 | — | [[TAK-733 (drug)]] 5 µM 0.0894× (z -9.8) |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.1) |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -13.6) |
| [[LoVo (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.8) |
| [[RKO (line)]] | wt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0637× (z -14.5) |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.9) |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.0) |
| [[SW480 (line)]] | alt | 19.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -12.2) |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.7) |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0948× (z -9.8) |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -8.6) |
| [[SW48 (line)]] | wt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.2) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PNKD]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ALAD]] | +0.68 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SNX30]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[CFD]] | +0.66 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[USP2]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HAUS4]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RHOXF1]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[GALM]] | +0.63 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[HMGN3]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01829]] | -0.71 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[ENOX2]] | -0.63 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[AVEN]] | -0.62 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[DESI1]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.62 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[TMEM217]] | -0.59 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FAM120B]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[ALG13]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PDK1-AS1]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HCG18]] | -0.57 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PBLD]] | -0.56 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises THRA's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without BCAM | 0.032 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises THRA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CXXC5]] | B | CXXC5 activity raises THRA's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without CXXC5 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ACSS1]] | B | ACSS1 activity raises THRA's level | lines that do not express ACSS1 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without ACSS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRXL2A, STAT5A, MGST2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.1, -5.3); signed map (-28.1, -5.8). **Vector** length 116, 32.1% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.7 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.4 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.5 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +3.4 | +3.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -15.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,058,290-40,093,867 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EAR-7.1/EAR-7.2, THRA3, AR7, ERBA, NR1A1, TRalpha, TRalpha1, TRalpha2; previously THRA1, THRA2, ERBA1 |
| Gene groups (HGNC) | Thyroid hormone receptors |
| Reactome | 4 pathways, smallest: SUMOylation of intracellular receptors; Nuclear Receptor transcription pathway; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P10827](https://www.uniprot.org/uniprotkb/P10827) (Thyroid hormone receptor alpha):

> [Isoform Alpha-1]: Nuclear hormone receptor that can act as a repressor or activator of transcription. High affinity receptor for thyroid hormones, including triiodothyronine and thyroxine.; [Isoform Alpha-2]: Does not bind thyroid hormone and functions as a weak dominant negative inhibitor of thyroid hormone action.

**Summary**, from NCBI Gene [7067](https://www.ncbi.nlm.nih.gov/gene/7067):

> The protein encoded by this gene is a nuclear hormone receptor for triiodothyronine. It is one of the several receptors for thyroid hormone, and has been shown to mediate the biological activities of thyroid hormone. Knockout studies in mice suggest that the different receptors, while having certain extent of redundancy, may mediate different functions of thyroid hormone. Alternatively spliced transcript variants encoding distinct isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11796) · Entrez [7067](https://www.ncbi.nlm.nih.gov/gene/7067) · UniProt [P10827](https://www.uniprot.org/uniprotkb/P10827) · Ensembl [ENSG00000126351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126351)

## Data

Gene col 4730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4730); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4730]; `tensor/DDL_lfc|DDL_z.npy` [4730]; `embed/gene_vectors.npy` [4730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4730 or target_col == 4730). Every well: [[THRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
