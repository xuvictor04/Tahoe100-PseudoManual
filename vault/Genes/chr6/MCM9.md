---
symbol: "MCM9"
type: "gene"
col: 3298
ensembl_id: "ENSG00000111877"
name: "minichromosome maintenance 9 homologous recombination repair factor"
location: "6q22.31"
module: 36
arm: "+"
pooled_cpm: 41.48
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# MCM9

*minichromosome maintenance 9 homologous recombination repair factor* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.40× (z +4.6, q 0.002, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.468× (z -14.8, q 0e+00, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.548× (z -8.3, q 2e-14, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11-DT]] (+0.66, fdr 1e-05), [[ZNF718]] (+0.65, fdr 1e-05), [[PRDM15]] (+0.63, fdr 1e-05); moves opposite to [[RYBP]] (-0.61, fdr 7e-06), [[GADD45B]] (-0.58, fdr 1e-05), [[DHRS2]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SRRM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 0.002 | 28/47 (HEC-1-A, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.19× | +3.5 | 0.14 | 15/48 (SW480, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.468×** | -14.8 | 0e+00 | 45/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.475×** | -10.2 | 3e-22 | 37/46 (NCI-H23, AN3 CA, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.446×** | -9.4 | 7e-19 | 43/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -8.3 | 2e-14 | 41/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.581×** | -7.5 | 9e-12 | 36/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.593×** | -7.2 | 6e-11 | 33/48 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.569×** | -6.6 | 4e-09 | 25/40 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.632×** | -6.3 | 2e-08 | 32/47 (HOP62, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.627×** | -5.9 | 2e-07 | 29/43 (NCI-H1573, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -5.7 | 5e-07 | 31/48 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.668×** | -5.5 | 1e-06 | 28/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.625×** | -5.5 | 2e-06 | 27/47 (SNU-1, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.678×** | -5.3 | 4e-06 | 27/48 (NCI-H460, RKO, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.728×** | -4.4 | 5e-04 | 29/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -4.3 | 7e-04 | 25/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.015 | 20/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 70.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.381× (z -10.0) |
| [[A-427 (line)]] | wt | 66.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 50.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0638× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.373× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.374× (z -9.4) |
| [[HOP62 (line)]] | alt | 28.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.318× (z -9.8) |
| [[SW480 (line)]] | alt | 74.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.424× (z -9.0) |
| [[A549 (line)]] | wt | 35.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.306× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 35.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.270× (z -9.5) |
| [[C-33 A (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 51.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 26.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0665× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C32 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0824× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.208× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.236× (z -10.1) |
| [[SNU-1 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW48 (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ZNF718]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PRDM15]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NAF1]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PRDM10]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TOR3A]] | +0.59 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[NSMAF]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[GADD45B]] | -0.58 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[DHRS2]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RING1]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.56 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[CGN]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ILK]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SNAPIN]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[LMNA]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[EHD2]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TPPP]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SKAP2]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SRRM3 activity raises MCM9's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without SRRM3 | 0.016 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[DEPP1]] | B | DEPP1 activity lowers MCM9's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.42× higher at baseline in the lines without DEPP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[CHGB]] | B | CHGB activity raises MCM9's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.34× lower at baseline in the lines without CHGB | 0.048 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[EHD2]] | B | EHD2 activity lowers MCM9's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 1.52× higher at baseline in the lines without EHD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.5, -17.0); signed map (-46.7, -21.6). **Vector** length 93.4, 23.7% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.4 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.5 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | -0.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | -0.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +1.6 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.4 | -14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.6 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.3 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance 9 homologous recombination repair factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:118,813,442-118,935,162 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35304, dJ329L24.3, FLJ20170; previously MCMDC1, C6orf61 |
| Gene groups (HGNC) | MCM family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXL9](https://www.uniprot.org/uniprotkb/Q9NXL9) (DNA helicase MCM9):

> Component of the MCM8-MCM9 complex, which is involved in the repair of double-stranded DNA breaks (DBSs) and DNA interstrand cross-links (ICLs) by homologous recombination (HR). The MCM8-MCM9 complex is a 3'-5' DNA helicase and single-stranded (ss)DNA-stimulated ATPase which binds ssDNA in the presence of nucleoside triphosphates. Required for DNA resection by the MRE11-RAD50-NBN/NBS1 (MRN) complex by recruiting the MRN complex to the repair site and by promoting the complex nuclease activity. …

**Summary**, from NCBI Gene [254394](https://www.ncbi.nlm.nih.gov/gene/254394):

> The protein encoded by this gene is a member of the mini-chromosome maintenance (MCM) protein family that are essential for the initiation of eukaryotic genome replication. Binding of this protein to chromatin has been shown to be a pre-requisite for recruiting the MCM2-7 helicase to DNA replication origins. This protein also binds, and is a positive regulator of, the chromatin licensing and DNA replication factor 1, CDT1. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:21484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21484) · Entrez [254394](https://www.ncbi.nlm.nih.gov/gene/254394) · UniProt [Q9NXL9](https://www.uniprot.org/uniprotkb/Q9NXL9) · Ensembl [ENSG00000111877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111877)

## Data

Gene col 3298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3298); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3298]; `tensor/DDL_lfc|DDL_z.npy` [3298]; `embed/gene_vectors.npy` [3298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3298 or target_col == 3298). Every well: [[MCM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
