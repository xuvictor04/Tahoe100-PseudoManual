---
symbol: "STBD1"
type: "gene"
col: 4019
ensembl_id: "ENSG00000118804"
name: "starch binding domain 1"
location: "4q21.1"
module: 107
arm: "+"
pooled_cpm: 14.47
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# STBD1

*starch binding domain 1* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +6.7, q 8e-09, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.233× (z -26.5, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R8]] (+0.68, fdr 5e-05), [[DIPK2A]] (+0.64, fdr 3e-05), [[AK4]] (+0.63, fdr 1e-05); moves opposite to [[PMEPA1]] (-0.53, fdr 3e-05), [[CPSF6]] (-0.49, fdr 8e-04, ⚠ one half only (not replicated)), [[THOC2]] (-0.48, fdr 1e-04), [[AIG1]] (-0.47, fdr 2e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[VLDLR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.7 | 8e-09 | 25/44 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.7 | 8e-09 | 10/46 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.29× | +3.3 | 0.18 | 15/40 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.24 | 9/41 (SK-MEL-2, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.28 | 11/44 (NCI-H2030, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.233×** | -26.5 | 0e+00 | 43/45 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.167×** | -23.0 | 0e+00 | 45/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.190×** | -21.3 | 0e+00 | 43/45 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.207×** | -20.3 | 0e+00 | 43/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.274×** | -16.0 | 0e+00 | 38/45 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -12.3 | 8e-33 | 39/42 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -12.0 | 3e-31 | 40/46 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.441×** | -10.5 | 4e-24 | 38/46 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -8.6 | 6e-16 | 34/45 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.526×** | -8.3 | 8e-15 | 31/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.523×** | -8.0 | 5e-14 | 29/40 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.519×** | -7.8 | 3e-13 | 21/30 (NCI-H1792, LoVo, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -7.5 | 2e-12 | 36/45 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.671×** | -7.3 | 1e-11 | 32/45 (SW1417, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.600×** | -6.3 | 9e-09 | 21/26 (CFPAC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -5.8 | 2e-07 | 25/43 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -5.7 | 3e-07 | 25/42 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -5.6 | 6e-07 | 26/46 (A498, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -5.3 | 3e-06 | 24/45 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.1) |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.7) |
| [[A-172 (line)]] | wt | 19.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0360× (z -30.7) |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.4) |
| [[HepG2_C3A (line)]] | wt | 36.7 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0737× (z -15.3) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -19.6) |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -20.9) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -21.0) |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0677× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0973× (z -13.7) |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0775× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -15.6) |
| [[LoVo (line)]] | wt | 16.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0851× (z -17.3) |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.105× (z -12.6) |
| [[A549 (line)]] | wt | 9.92 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.4) |
| [[C32 (line)]] | wt | 16.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 32.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.2) |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -23.0) |
| [[RKO (line)]] | wt | 12.9 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0766× (z -12.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.9) |
| [[A498 (line)]] | wt | 11.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.3) |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.3) |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0853× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 7.55 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0714× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0626× (z -19.8) |
| [[SW480 (line)]] | alt | 6.78 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.181× (z -10.1) |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0945× (z -24.1) |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.5) |
| [[C-33 A (line)]] | alt | 8.29 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0389× (z -11.7) |
| [[J82 (line)]] | alt | 11.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -9.4) |
| [[KATO III (line)]] | alt | 9.15 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 9.08 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 8.78 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.1000× (z -9.5) |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0737× (z -13.5) |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0579× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 7.62 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -8.8) |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.160× (z -9.1) |
| [[A-427 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R8]] | +0.68 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[DIPK2A]] | +0.64 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[AK4]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[ACBD5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[DBR1]] | +0.61 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[MSL1]] | +0.59 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[ZNF419]] | +0.57 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[TPI1]] | +0.55 | +0.44 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |
| [[PGAP4]] | +0.54 | +0.16 / +0.64 | ⚠ one half (not replicated) | 0.001 |  |
| [[GRPEL1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SMG8]] | +0.52 | +0.21 / +0.53 | both halves | 7e-04 |  |
| [[EEF1AKMT3]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TMED8]] | +0.52 | +0.31 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMEPA1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.49 | -0.19 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |
| [[THOC2]] | -0.48 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[AIG1]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[RPRD1A]] | -0.47 | -0.13 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[SMARCC1]] | -0.46 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[SLC23A2]] | -0.46 | -0.18 / -0.50 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ARMH4]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GGA1]] | -0.45 | -0.34 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[LINC02934]] | -0.44 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[DDX46]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[ARMC9]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SFPQ]] | -0.43 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VLDLR]] | B | VLDLR activity raises STBD1's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without VLDLR | 0.032 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 17.2); signed map (-41.3, 28.1). **Vector** length 87.9, 20.8% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -8.1 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -7.3 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -12.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | starch binding domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,306,733-76,311,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41801, GENX-3414 |
| Hallmark sets | HYPOXIA |
| Reactome | 10 pathways, smallest: RHOD GTPase cycle; RHOG GTPase cycle; RAC2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O95210](https://www.uniprot.org/uniprotkb/O95210) (Starch-binding domain-containing protein 1):

> Acts as a cargo receptor for glycogen. Delivers its cargo to an autophagic pathway called glycophagy, resulting in the transport of glycogen to lysosomes.

**Summary**, from NCBI Gene [8987](https://www.ncbi.nlm.nih.gov/gene/8987):

> Enables enzyme binding activity and glycogen binding activity. Involved in glycophagy and lysosomal transport. Located in T-tubule; endoplasmic reticulum; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24854) · Entrez [8987](https://www.ncbi.nlm.nih.gov/gene/8987) · UniProt [O95210](https://www.uniprot.org/uniprotkb/O95210) · Ensembl [ENSG00000118804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118804)

## Data

Gene col 4019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4019); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4019]; `tensor/DDL_lfc|DDL_z.npy` [4019]; `embed/gene_vectors.npy` [4019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4019 or target_col == 4019). Every well: [[STBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
