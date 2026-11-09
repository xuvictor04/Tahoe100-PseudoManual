---
symbol: "THOC5"
type: "gene"
col: 1916
ensembl_id: "ENSG00000100296"
name: "THO complex subunit 5"
location: "22q12.2"
module: 36
arm: "+"
pooled_cpm: 31.59
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# THOC5

*THO complex subunit 5* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.72× (z +12.5, q 6e-33, up in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.50× (z +9.6, q 1e-19, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.771× (z -8.8, q 9e-16, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.363×, PANC-1 0.587×; ⚠ cell-cycle shift, explains ~56% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.123×; ⚠ toxic; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Pimitespib (drug)]] 5 µM in 1 line (RPMI-7951 0.0864×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSF1]] (+0.75, fdr 7e-06), [[BCAP31]] (+0.67, fdr 7e-06), [[RNPS1]] (+0.66, fdr 7e-06); moves opposite to [[LMNA]] (-0.65, fdr 7e-06), [[PIM3]] (-0.62, fdr 1e-05), [[ARL4A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GATA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +12.5 | 6e-33 | 28/39 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +12.2 | 6e-32 | 33/45 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +9.6 | 1e-19 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.6 | 1e-15 | 34/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +8.0 | 9e-14 | 22/48 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.38×** | +7.3 | 3e-11 | 31/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +7.1 | 1e-10 | 28/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +6.7 | 2e-09 | 27/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.5 | 2e-06 | 19/43 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +5.4 | 3e-06 | 22/48 (NCI-H2030, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 2e-05 | 18/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.4 | 5e-04 | 20/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +4.4 | 5e-04 | 16/47 (LS 180, SW48, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 5e-04 | 17/48 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.20×** | +4.4 | 5e-04 | 12/47 (A498, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 11/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.8 | 0.005 | 13/48 (SW1417, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.013 | 5/48 (HOP62, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.026 | 9/47 (NCI-H460, AN3 CA, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +2.9 | 0.086 | 6/48 (LS 180, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +2.9 | 0.086 | 5/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.098 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1916.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.363×, PANC-1 0.587×; ⚠ cell-cycle shift, explains ~56% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.123×; ⚠ toxic; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Pimitespib (drug)]] 5 µM in 1 line (RPMI-7951 0.0864×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.771×** | -8.8 | 9e-16 | 30/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.792×** | -5.4 | 2e-05 | 22/48 (A-172, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.1 | 6e-05 | 3/48 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.824×** | -4.6 | 5e-04 | 19/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.848× | -3.9 | 0.009 | 10/48 (A-427, RKO, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.875× | -3.1 | 0.20 | 17/47 (LOX-IMVI, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[A-427 (line)]] | wt | 37.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H1792 (line)]] | alt | 25.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 49.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.93× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -19.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +17.5) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0864× (z -9.0) |
| [[SW1417 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSF1]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 609 |
| [[CHID1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RPSA]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[POMT2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LY6G5B]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[AGO1]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TPD52L2]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.60 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RPUSD4]] | +0.60 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMNA]] | -0.65 | -0.74 / -0.61 | both halves | 7e-06 |  |
| [[PIM3]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[ARL4A]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TMEM205]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[H3-3B]] | -0.60 | -0.57 / -0.63 | both halves | 8e-06 |  |
| [[TXNIP]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LGALS3]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[REL]] | -0.58 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[BCL3]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[SLC2A6]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA6]] | B | GATA6 activity lowers THOC5's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without GATA6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[LGALS3]] | B | LGALS3 activity lowers THOC5's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.55× higher at baseline in the lines without LGALS3 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[KLF5]] | B | KLF5 activity lowers THOC5's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.27× higher at baseline in the lines without KLF5 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[GATA6]] | B | GATA6 activity strengthens THOC5's drug response | lines that do not express GATA6 (18) vs lines expressing it (30) | the lines without GATA6 respond 0.78× as strongly (z diff +0.32); strongest at Panobinostat 5 µM: 1.21x vs 1.56x (z diff +1.7) | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3; target measured in part of the lines; artifact flags |
| [[LGALS3]] | B | LGALS3 activity strengthens THOC5's drug response | lines that do not express LGALS3 (11) vs lines expressing it (37) | the lines without LGALS3 respond 0.51× as strongly (z diff +0.97); strongest at Topotecan (hydrochloride) 5 µM: 0.76x vs 1.44x (z diff +3.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; target measured in part of the lines; artifact flags |
| [[H2AJ]] | B | H2AJ activity lowers THOC5's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without H2AJ | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[TRIM15]] | B | TRIM15 activity lowers THOC5's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.26× higher at baseline in the lines without TRIM15 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ID3]] | B | ID3 activity raises THOC5's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without ID3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-20.4, -28.4); signed map (-23.7, -45.9). **Vector** length 83.0, 15.3% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | +4.2 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -6.2 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.8 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.9 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,505,879-29,555,216 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PK1.3, KIAA0983, Fmip, fSAP79; previously C22orf19 |
| Gene groups (HGNC) | THO complex |
| Reactome | 7 pathways, smallest: Signaling by CSF1 (M-CSF) in myeloid cells; Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13769](https://www.uniprot.org/uniprotkb/Q13769) (THO complex subunit 5):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Plays a key structural role in the oligomerization of the THO-DDX39B complex. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream of the exon-junction complex (EJC) and is recruited in a splicing- and cap-dependent manner to a region …

**Summary**, from NCBI Gene [8563](https://www.ncbi.nlm.nih.gov/gene/8563):

> Predicted to enable mRNA binding activity. Involved in mRNA export from nucleus and monocyte differentiation. Located in chromosome, telomeric region and nucleoplasm. Part of THO complex part of transcription export complex. Implicated in breast carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19074) · Entrez [8563](https://www.ncbi.nlm.nih.gov/gene/8563) · UniProt [Q13769](https://www.uniprot.org/uniprotkb/Q13769) · Ensembl [ENSG00000100296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100296)

## Data

Gene col 1916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1916); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1916]; `tensor/DDL_lfc|DDL_z.npy` [1916]; `embed/gene_vectors.npy` [1916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1916 or target_col == 1916). Every well: [[THOC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
