---
symbol: "UBAC2"
type: "gene"
col: 5619
ensembl_id: "ENSG00000134882"
name: "UBA domain containing 2"
location: "13q32.3"
module: 36
arm: "+"
pooled_cpm: 150.07
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# UBAC2

*UBA domain containing 2* — 13q32.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 2.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 1.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -32.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERI3]] (+0.67, fdr 7e-06), [[UTP18]] (+0.64, fdr 7e-06), [[PTGES2]] (+0.63, fdr 1e-05); moves opposite to [[GPR137C]] (-0.65, fdr 1e-05), [[FBXO48]] (-0.58, fdr 1e-05), [[NBPF10]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM132D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5619.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 2.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 1.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.15× | +4.7 | 0.002 | 5/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.382×** | -32.9 | 0e+00 | 46/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -16.6 | 0e+00 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -15.5 | 0e+00 | 46/49 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -15.0 | 0e+00 | 44/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.615×** | -11.7 | 9e-30 | 34/48 (BT-474, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.642×** | -10.7 | 1e-24 | 35/48 (BT-474, SW480, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -10.2 | 1e-22 | 39/48 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.668×** | -9.7 | 2e-20 | 44/48 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -9.4 | 4e-19 | 38/50 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -9.2 | 2e-18 | 36/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -8.3 | 4e-15 | 40/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.516×** | -8.3 | 4e-15 | 38/49 (LOX-IMVI, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.732×** | -7.5 | 2e-12 | 41/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.747×** | -7.0 | 8e-11 | 36/48 (NCI-H1573, SK-MEL-2, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -6.9 | 2e-10 | 29/47 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -5.6 | 6e-07 | 20/48 (NCI-H2347, SW 1271, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.002 | 20/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.879× | -3.0 | 0.066 | 15/48 (CFPAC-1, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 122 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -30.5) |
| [[SW480 (line)]] | alt | 317 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -18.2) |
| [[KATO III (line)]] | alt | 187 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 307 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -34.1) |
| [[SW 900 (line)]] | alt | 131 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -18.6) |
| [[SW48 (line)]] | wt | 176 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.9) |
| [[BT-474 (line)]] | alt | 138 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -19.0) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.464× (z -13.7) |
| [[HT-29 (line)]] | alt | 270 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -17.8) |
| [[LS 180 (line)]] | wt | 212 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -15.0) |
| [[A498 (line)]] | wt | 154 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -31.5) |
| [[C32 (line)]] | wt | 152 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -31.6) |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -28.1) |
| [[SK-MEL-2 (line)]] | alt | 91.8 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -20.0) |
| [[A549 (line)]] | wt | 99.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -22.2) |
| [[HCT15 (line)]] | alt | 214 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -20.3) |
| [[HOP62 (line)]] | alt | 87.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.94× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -24.3) |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -25.0) |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -21.8) |
| [[Panc 03.27 (line)]] | alt | 205 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -17.5) |
| [[PANC-1 (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -28.4) |
| [[SW1417 (line)]] | alt | 149 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -18.5) |
| [[A-172 (line)]] | wt | 94.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -14.1) |
| [[H4 (line)]] | wt | 94.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.3) |
| [[HS-578T (line)]] | alt | 76.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -24.7) |
| [[J82 (line)]] | alt | 171 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -20.9) |
| [[LoVo (line)]] | wt | 168 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -33.0) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -15.6) |
| [[SNU-423 (line)]] | alt | 96.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -21.8) |
| [[A-427 (line)]] | wt | 98.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 89.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.6) |
| [[COLO 205 (line)]] | alt | 470 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 79.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -20.2) |
| [[SHP-77 (line)]] | alt | 225 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.3) |
| [[SNU-1 (line)]] | wt | 135 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 91.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -18.0) |
| [[RKO (line)]] | wt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.9) |
| [[C-33 A (line)]] | alt | 93.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[CFPAC-1 (line)]] | alt | 82.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -19.9) |
| [[HepG2_C3A (line)]] | wt | 97.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.412× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.5) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 286 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERI3]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[UTP18]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PTGES2]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[XPO7]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[IPO11]] | +0.61 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[EBPL]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ARMH3]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ANAPC10]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[IQCB1]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[HERC2]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR137C]] | -0.65 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.58 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[KCTD11]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[THAP1]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ERF]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[LETM2]] | -0.52 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R15A]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MARCKS]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MAD2L1BP]] | -0.51 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZFHX2]] | -0.51 | -0.63 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM132D]] | B | TMEM132D activity raises UBAC2's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without TMEM132D | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.9, -31.6); signed map (-11.9, -51.8). **Vector** length 91.4, 26.7% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | -0.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | -1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -32.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -5.6 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | UBA domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:99,200,774-99,386,504 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30548, RP11-178C10.1; previously PHGDHL1 |
| Gene groups (HGNC) | Rhomboid family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBM4](https://www.uniprot.org/uniprotkb/Q8NBM4) (Ubiquitin-associated domain-containing protein 2):

> Acts as an ER-phagy receptor required for the selective autophagic degradation of endoplasmic reticulum (ER) fragments to maintain ER homeostasis and restrain ER stress-induced inflammatory responses. Its function depends on phosphorylation-induced dimerization, which enhances interaction with GABARAP and facilitates recruitment of ER fragments to autophagosomes. Restricts trafficking of FAF2 from the endoplasmic reticulum to lipid droplets. In association with LMBR1L and E3 ubiquitin-protein …

**Summary**, from NCBI Gene [337867](https://www.ncbi.nlm.nih.gov/gene/337867):

> Predicted to enable serine-type endopeptidase activity. Involved in negative regulation of canonical Wnt signaling pathway and negative regulation of retrograde protein transport, ER to cytosol. Acts upstream of or within protein localization to endoplasmic reticulum. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20486) · Entrez [337867](https://www.ncbi.nlm.nih.gov/gene/337867) · UniProt [Q8NBM4](https://www.uniprot.org/uniprotkb/Q8NBM4) · Ensembl [ENSG00000134882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134882)

## Data

Gene col 5619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5619); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5619]; `tensor/DDL_lfc|DDL_z.npy` [5619]; `embed/gene_vectors.npy` [5619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5619 or target_col == 5619). Every well: [[UBAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
