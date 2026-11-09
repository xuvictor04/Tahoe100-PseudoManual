---
symbol: "TYW3"
type: "gene"
col: 8547
ensembl_id: "ENSG00000162623"
name: "tRNA-yW synthesizing protein 3 homolog"
location: "1p31.1"
module: 64
arm: "+"
pooled_cpm: 34.62
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TYW3

*tRNA-yW synthesizing protein 3 homolog* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.58× (z +14.3, q 2e-43, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.467× (z -11.5, q 8e-28, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPID]] (+0.74, fdr 7e-06), [[MTX3]] (+0.72, fdr 7e-06), [[NUDT9]] (+0.71, fdr 7e-06); moves opposite to [[FAM234A]] (-0.60, fdr 4e-05), [[C1QL1]] (-0.60, fdr 4e-05), [[CYB5R3]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GCNT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.58×** | +14.3 | 2e-43 | 45/47 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +13.8 | 1e-40 | 46/47 (C32, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +12.6 | 7e-34 | 40/45 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.31×** | +11.8 | 4e-30 | 45/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.13×** | +11.4 | 4e-28 | 45/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +9.9 | 5e-21 | 35/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.08×** | +8.9 | 5e-17 | 40/43 (A498, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +8.9 | 5e-17 | 41/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.38×** | +6.8 | 5e-10 | 40/46 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.6 | 2e-09 | 34/44 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.54×** | +6.3 | 2e-08 | 33/48 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +6.2 | 3e-08 | 28/47 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.9 | 2e-07 | 34/46 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 3e-06 | 31/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 4e-06 | 29/48 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-05 | 32/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +4.3 | 7e-04 | 25/47 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.001 | 21/48 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.002 | 20/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.002 | 22/47 (KATO III, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.010 | 19/48 (LOX-IMVI, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.013 | 20/47 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -11.5 | 8e-28 | 46/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.483×** | -11.0 | 1e-25 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -8.3 | 2e-14 | 38/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -5.0 | 7e-05 | 28/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.762×** | -4.1 | 0.004 | 22/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.607×** | -3.9 | 0.007 | 21/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.621×** | -3.8 | 0.013 | 15/47 (Hs 766T, J82, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.813× | -3.1 | 0.12 | 13/47 (SW 1271, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | 0.682× | -3.0 | 0.16 | 15/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.6 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.67× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 21.6 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.67× (z +11.2) | — |
| [[SW480 (line)]] | alt | 47.2 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.40× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.232× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 45.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.18× (z +11.8) | [[TAK-901 (drug)]] 5 µM 0.0638× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 30.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.4) |
| [[A-172 (line)]] | wt | 12.5 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.75× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.39× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 34.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 38.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +10.3) | — |
| [[RKO (line)]] | wt | 68.3 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.22× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.46× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -8.7) |
| [[C32 (line)]] | wt | 39.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +18.6) | — |
| [[HT-29 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.40× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -8.8) |
| [[SHP-77 (line)]] | alt | 28.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.44× (z +9.4) | — |
| [[A-427 (line)]] | wt | 54.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -9.0) |
| [[BT-474 (line)]] | alt | 25.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.72× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 49.5 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.69× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 32.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.77× (z +9.1) | — |
| [[KATO III (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 21.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 21.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.30× (z +8.7) | — |
| [[A549 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPID]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[MTX3]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[DNAJC7]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[BAG2]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[SLC38A6]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MTA3]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[EPDR1]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RHBDD3]] | +0.66 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[PSMA1]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.66 | +0.67 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM234A]] | -0.60 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[C1QL1]] | -0.60 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[CYB5R3]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SUN1]] | -0.58 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[KDM4B]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DNAAF3]] | -0.56 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[PRKACA]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ECE1]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PDXP]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT2]] | B | GCNT2 activity lowers TYW3's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 1.34× higher at baseline in the lines without GCNT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |
| [[HDAC6]] | B | HDAC6 activity raises TYW3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CYP46A1]] | B | CYP46A1 activity raises TYW3's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without CYP46A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[CTXN1]] | B | CTXN1 activity raises TYW3's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without CTXN1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[RNASEL]] | B | RNASEL activity lowers TYW3's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 1.37× higher at baseline in the lines without RNASEL | 0.084 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-18.8, 10.2); signed map (7.9, -31.6). **Vector** length 110, 32.3% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *proteasome* (control, mean cos +0.51 to 9); *Vif-mediated degradation of APOBEC3G* (reactome, mean cos +0.53 to 9); *Hedgehog 'on' state* (reactome, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.3 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +14.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +13.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA-yW synthesizing protein 3 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:74,733,152-74,766,678 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40918; previously C1orf171 |
| Gene groups (HGNC) | tRNA wybutosine-synthesizing protein domain containing; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: Synthesis of wybutosine at G37 of tRNA(Phe); tRNA modification in the nucleus and cytosol; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IPR3](https://www.uniprot.org/uniprotkb/Q6IPR3) (tRNA wybutosine-synthesizing protein 3 homolog):

> S-adenosyl-L-methionine-dependent methyltransferase involved in the biosynthesis of wybutosine, a hyper modified guanosine with a tricyclic base located at position 37 of eukaryotic phenylalanine tRNA (tRNA(Phe)) that contributes to maintenance of the translational reading frame. Catalyzes the methylation of 4-demethylwyosine, generating intermediates required for the formation of mature wybutosine.

**Summary**, from NCBI Gene [127253](https://www.ncbi.nlm.nih.gov/gene/127253):

> Wybutosine (yW) is a hypermodified guanosine at the 3-prime position adjacent to the anticodon of phenylalanine tRNA that stabilizes codon-anticodon interactions during decoding on the ribosome. TYW3 is the human homolog of a yeast gene essential for yW synthesis (Noma and Suzuki, 2006).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24757) · Entrez [127253](https://www.ncbi.nlm.nih.gov/gene/127253) · UniProt [Q6IPR3](https://www.uniprot.org/uniprotkb/Q6IPR3) · Ensembl [ENSG00000162623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162623)

## Data

Gene col 8547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8547); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8547]; `tensor/DDL_lfc|DDL_z.npy` [8547]; `embed/gene_vectors.npy` [8547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8547 or target_col == 8547). Every well: [[TYW3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYW3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
