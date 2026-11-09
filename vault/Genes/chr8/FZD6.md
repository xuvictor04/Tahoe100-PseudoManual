---
symbol: "FZD6"
type: "gene"
col: 9033
ensembl_id: "ENSG00000164930"
name: "frizzled class receptor 6"
location: "8q22.3"
module: 137
arm: "+"
pooled_cpm: 58.04
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# FZD6

*frizzled class receptor 6* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 1.55× (z +4.9, q 5e-04, up in 26 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.93×, NCI-H2347 1.78×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H1573 2.78×, HT-29 2.28×; ⚠ cell-cycle shift, explains ~70% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.83×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.444× (z -17.6, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAIM]] (+0.66, fdr 1e-05), [[MCCC2]] (+0.63, fdr 1e-05), [[GTF3C6]] (+0.62, fdr 1e-04); moves opposite to [[PLA2G15]] (-0.60, fdr 4e-05), [[DNAAF3]] (-0.60, fdr 4e-05), [[LINC02935]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → cells under [[olaparib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9033.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 1.93×, NCI-H2347 1.78×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H1573 2.78×, HT-29 2.28×; ⚠ cell-cycle shift, explains ~70% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 2.83×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +4.9 | 5e-04 | 26/43 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.5 | 0.11 | 14/43 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.14 | 6/43 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.2 | 0.14 | 16/43 (RKO, NCI-H2347, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.2 | 0.14 | 15/43 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 17/42 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.14 | 15/40 (A-172, HOP62, …) | all doses, flat | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.14 | 7/43 (HS-578T, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.0 | 0.15 | 8/43 (NCI-H2030, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -17.6 | 0e+00 | 41/43 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.465×** | -16.6 | 0e+00 | 38/43 (SW480, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -15.2 | 0e+00 | 41/43 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -14.9 | 0e+00 | 40/43 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -8.5 | 2e-15 | 29/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -8.1 | 4e-14 | 33/43 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.689×** | -8.1 | 6e-14 | 31/43 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.750×** | -6.2 | 4e-08 | 26/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -5.1 | 2e-05 | 19/43 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.803×** | -4.7 | 1e-04 | 24/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.696×** | -4.1 | 0.002 | 21/43 (HOP62, C32, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.881× | -3.9 | 0.005 | 19/43 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.006 | 16/43 (A-427, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.833×** | -3.8 | 0.006 | 19/43 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.867× | -3.1 | 0.076 | 14/43 (SW480, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.7 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.200× (z -21.0) |
| [[RKO (line)]] | wt | 135 | 3 (3 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -18.0) |
| [[C32 (line)]] | wt | 103 | 0 | 7 | — | [[Auranofin (drug)]] 5 µM 0.212× (z -16.2) |
| [[HS-578T (line)]] | alt | 147 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 58.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -13.2) |
| [[SNU-1 (line)]] | wt | 92.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -12.4) |
| [[HOP62 (line)]] | alt | 66.0 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.281× (z -13.3) |
| [[LoVo (line)]] | wt | 55.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 79.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.335× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 83.9 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.243× (z -14.9) |
| [[SW1417 (line)]] | alt | 80.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -11.3) |
| [[SW48 (line)]] | wt | 52.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -9.3) |
| [[A-172 (line)]] | wt | 55.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -11.0) |
| [[KATO III (line)]] | alt | 58.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -10.8) |
| [[LS 180 (line)]] | wt | 65.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 86.7 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 33.9 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -12.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-427 (line)]] | wt | 42.2 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.334× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 86.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -16.5) |
| [[HT-29 (line)]] | alt | 47.4 | 1 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +8.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Auranofin (drug)]] 5 µM 0.292× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 56.6 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.83× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 41.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -11.2) |
| [[SW 900 (line)]] | alt | 66.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.371× (z -9.5) |
| [[A498 (line)]] | wt | 52.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -9.2) |
| [[COLO 205 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 53.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 72.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[Hs 766T (line)]] | wt | 68.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.390× (z -9.4) |
| [[J82 (line)]] | alt | 69.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.480× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.254× (z -12.6) |
| [[PANC-1 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -14.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 95.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -11.3) |
| [[A549 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | +0.66 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.62 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[POGLUT1]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[DCLRE1A]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RCBTB2]] | +0.62 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[YTHDC2]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SETMAR]] | +0.61 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MRPL9]] | +0.60 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[MTMR2]] | +0.60 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[EWSR1]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FUNDC1]] | +0.59 | +0.65 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G15]] | -0.60 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DNAAF3]] | -0.60 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LINC02935]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RASA4B]] | -0.60 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SH3GL1]] | -0.58 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[STK32C]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[RRAS]] | -0.58 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[RAB40C]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DNASE1L1]] | -0.57 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MYO9B]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RFX2]] | -0.56 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[SLC17A7]] | -0.56 | -0.57 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[olaparib (drug)]] 5 µM | C | FZD6 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.61× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[APTO-253 (drug)]] 5 µM | C | FZD6 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.34× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[IQ 1 (drug)]] 5 µM | C | FZD6 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 0.73× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[Dabrafenib (drug)]] 5 µM | C | FZD6 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.50× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[PH-797804 (drug)]] 0.05 µM | C | FZD6 activity lowers the cells' numbers under PH-797804 0.05 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.31× the cells of the other lines | 0.046 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | FZD6 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.31× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | FZD6 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 0.81× the cells of the other lines | 0.070 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| cells under [[Pralsetinib (drug)]] 5 µM | C | FZD6 activity lowers the cells' numbers under Pralsetinib 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.54× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.7, 7.0); signed map (20.6, -31.8). **Vector** length 109, 27.4% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.4 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.9 | -16.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -15.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -17.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,298,433-103,332,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hfz6 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Reactome | 12 pathways, smallest: Signaling by RNF43 mutants; Regulation of FZD by ubiquitination; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [O60353](https://www.uniprot.org/uniprotkb/O60353) (Frizzled-6):

> Receptor for Wnt proteins. Most of frizzled receptors are coupled to the beta-catenin canonical signaling pathway, which leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt target genes. A second signaling pathway involving PKC and calcium fluxes has been seen for some family members, but it is not yet clear if it represents a distinct pathway or if it can be integrated in the canonical pathway, as PKC seems to …

**Summary**, from NCBI Gene [8323](https://www.ncbi.nlm.nih.gov/gene/8323):

> This gene represents a member of the 'frizzled' gene family, which encode 7-transmembrane domain proteins that are receptors for Wnt signaling proteins. The protein encoded by this family member contains a signal peptide, a cysteine-rich domain in the N-terminal extracellular region, and seven transmembrane domains, but unlike other family members, this protein does not contain a C-terminal PDZ domain-binding motif. This protein functions as a negative regulator of the canonical …

**Accessions** — [HGNC:4044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4044) · Entrez [8323](https://www.ncbi.nlm.nih.gov/gene/8323) · UniProt [O60353](https://www.uniprot.org/uniprotkb/O60353) · Ensembl [ENSG00000164930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164930)

## Data

Gene col 9033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9033); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9033]; `tensor/DDL_lfc|DDL_z.npy` [9033]; `embed/gene_vectors.npy` [9033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9033 or target_col == 9033). Every well: [[FZD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
