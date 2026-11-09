---
symbol: "ZBED1"
type: "gene"
col: 13216
ensembl_id: "ENSG00000214717"
name: "zinc finger BED-type containing 1"
location: "Xp22.33 and Yp11"
module: 7
arm: "+"
pooled_cpm: 23.32
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBED1

*zinc finger BED-type containing 1* — Xp22.33 and Yp11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +5.7, q 8e-06, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.156× (z -21.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAGN1]] (+0.64, fdr 7e-06), [[PBDC1]] (+0.64, fdr 7e-06), [[NKAPD1]] (+0.64, fdr 7e-06); moves opposite to [[NOMO2]] (-0.62, fdr 1e-05), [[SETD3]] (-0.59, fdr 2e-05), [[BPNT2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZFY]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.7 | 8e-06 | 32/48 (SW480, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.8 | 0.024 | 21/45 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.8 | 0.024 | 19/43 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.048 | 17/48 (SW480, H4, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.098 | 11/48 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.156×** | -21.4 | 0e+00 | 48/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.170×** | -20.4 | 0e+00 | 47/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.230×** | -16.9 | 0e+00 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.477×** | -12.0 | 6e-31 | 41/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.432×** | -9.6 | 7e-20 | 41/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.367×** | -6.0 | 2e-07 | 31/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.593×** | -6.0 | 2e-07 | 30/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -5.9 | 2e-07 | 28/47 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -5.7 | 6e-07 | 31/48 (H4, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -5.5 | 2e-06 | 25/46 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -5.5 | 2e-06 | 31/48 (RKO, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -5.2 | 1e-05 | 27/46 (A-427, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.646×** | -5.0 | 3e-05 | 27/46 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.646×** | -4.8 | 7e-05 | 28/46 (A-427, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -4.3 | 7e-04 | 24/48 (NCI-H23, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.004 | 21/48 (AN3 CA, COLO 205, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.007 | 20/47 (AN3 CA, A549, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.547×** | -3.6 | 0.010 | 18/45 (RKO, SNU-423, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 46.6 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 59.9 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.81× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.132× (z -17.4) |
| [[SW48 (line)]] | wt | 30.3 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0680× (z -12.6) |
| [[SW480 (line)]] | alt | 33.0 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0541× (z -26.1) |
| [[H4 (line)]] | wt | 47.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0887× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -11.7) |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0610× (z -13.9) |
| [[RKO (line)]] | wt | 30.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0829× (z -16.1) |
| [[SNU-423 (line)]] | alt | 34.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0678× (z -19.9) |
| [[HepG2_C3A (line)]] | wt | 49.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0739× (z -16.4) |
| [[J82 (line)]] | alt | 43.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0594× (z -16.2) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -10.1) |
| [[A549 (line)]] | wt | 22.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 7.77 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0753× (z -11.3) |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.00907× (z -22.4) |
| [[HEC-1-A (line)]] | alt | 27.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -12.3) |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -12.7) |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.114× (z -11.9) |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0978× (z -12.8) |
| [[KATO III (line)]] | alt | 19.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0564× (z -16.8) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0959× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 23.4 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.187× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0592× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.1) |
| [[SNU-1 (line)]] | wt | 29.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.101× (z -11.6) |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.184× (z -10.2) |
| [[A-427 (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0806× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0549× (z -8.9) |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0743× (z -9.3) |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0988× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.8) |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -9.5) |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0829× (z -12.8) |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -8.6) |
| [[C32 (line)]] | wt | 15.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 7.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0708× (z -10.4) |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.112× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.75 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0517× (z -10.6) |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAGN1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PBDC1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[INTS14]] | +0.62 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[DHRSX]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 | same gene group; STRING 879; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TOE1]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CCDC102A]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZNF24]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[RPP25L]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | -0.62 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SETD3]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[BPNT2]] | -0.56 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PIGF]] | -0.56 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[ATP6AP2]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PDIA4]] | -0.54 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TMEM8B]] | -0.54 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CDS2]] | -0.54 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[NOMO1]] | -0.54 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TM9SF2]] | -0.54 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[GET1]] | -0.54 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[FAM13A-AS1]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFY]] | B | ZFY activity raises ZBED1's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.62× lower at baseline in the lines without ZFY | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.7, 7.6); signed map (3.4, -18.3). **Vector** length 94.9, 24.1% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +11.1 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -3.0 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -20.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -21.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11 — chrX:2,486,414-2,500,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAMP, KIAA0785, DREF, hDREF; previously ALTE |
| Gene groups (HGNC) | Zinc fingers BED-type; Pseudoautosomal region 1 |
| Reactome | 3 pathways, smallest: SUMOylation of chromatin organization proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O96006](https://www.uniprot.org/uniprotkb/O96006) (E3 SUMO-protein ligase ZBED1):

> Functions as an E3-type small ubiquitin-like modifier (SUMO) ligase which sumoylates CHD3/Mi2-alpha, causing its release from DNA. This results in suppression of CHD3/Mi2-alpha transcription repression, increased recruitment of RNA polymerase II to gene promoters and positive regulation of transcription including H1-5 and ribosomal proteins such as: RPS6, RPL10A, and RPL12. The resulting increased transcriptional activity drives cell proliferation. Binds to 5'-TGTCG[CT]GA[CT]A-3' consensus …

**Summary**, from NCBI Gene [9189](https://www.ncbi.nlm.nih.gov/gene/9189):

> This gene is located in the pseudoautosomal region 1 (PAR1) of X and Y chromosomes. It was earlier identified as a gene with similarity to Ac transposable elements, however, was found not to have transposase activity. Later studies show that this gene product is localized in the nucleus and functions as a transcription factor. It binds to DNA elements found in the promoter regions of several genes related to cell proliferation, such as histone H1, hence may have a role in regulating genes …

**Accessions** — [HGNC:447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:447) · Entrez [9189](https://www.ncbi.nlm.nih.gov/gene/9189) · UniProt [O96006](https://www.uniprot.org/uniprotkb/O96006) · Ensembl [ENSG00000214717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214717)

## Data

Gene col 13216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13216); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13216]; `tensor/DDL_lfc|DDL_z.npy` [13216]; `embed/gene_vectors.npy` [13216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13216 or target_col == 13216). Every well: [[ZBED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
