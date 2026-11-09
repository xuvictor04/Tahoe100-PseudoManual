---
symbol: "RASA1"
type: "gene"
col: 7015
ensembl_id: "ENSG00000145715"
name: "RAS p21 protein activator 1"
location: "5q14.3"
module: 34
arm: "+"
pooled_cpm: 225.5
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# RASA1

*RAS p21 protein activator 1* — 5q14.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 1.99×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.512× (z -12.7, q 3e-34, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.564× (z -10.9, q 4e-25, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM10]] (+0.54, fdr 1e-05), [[PIGN]] (+0.54, fdr 3e-05), [[MYCBP]] (+0.54, fdr 2e-05); moves opposite to [[SLC3A2]] (-0.53, fdr 2e-05), [[SRP14-DT]] (-0.51, fdr 1e-05), [[HSBP1L1]] (-0.51, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITGA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 1.99×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.512×** | -12.7 | 3e-34 | 42/48 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -11.0 | 9e-26 | 38/44 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -10.9 | 4e-25 | 42/47 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.611×** | -9.0 | 3e-17 | 37/43 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -8.5 | 2e-15 | 43/46 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -7.6 | 2e-12 | 30/47 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.702×** | -6.7 | 2e-09 | 39/47 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.699×** | -6.5 | 5e-09 | 35/47 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -5.7 | 7e-07 | 35/47 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.747×** | -5.5 | 2e-06 | 33/47 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.750×** | -5.4 | 3e-06 | 31/47 (KATO III, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.752×** | -5.4 | 3e-06 | 32/47 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.824×** | -4.9 | 4e-05 | 24/48 (Panc 03.27, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.786×** | -4.5 | 2e-04 | 26/47 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -4.5 | 3e-04 | 28/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.003 | 23/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.680×** | -3.5 | 0.014 | 29/47 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.018 | 21/47 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.024 | 25/46 (RPMI-7951, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.726×** | -2.9 | 0.086 | 16/47 (HEC-1-A, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 352 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 232 | 2 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.9) |
| [[HOP62 (line)]] | alt | 374 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.5) |
| [[KATO III (line)]] | alt | 201 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.5) |
| [[LoVo (line)]] | wt | 177 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.523× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 231 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 714 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -15.1) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -9.3) |
| [[A-172 (line)]] | wt | 148 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.7) |
| [[SNU-423 (line)]] | alt | 220 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.424× (z -11.1) |
| [[SW 900 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.421× (z -11.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -10.8) |
| [[SW480 (line)]] | alt | 206 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -9.0) |
| [[A498 (line)]] | wt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -13.5) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 180 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -9.0) |
| [[PANC-1 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -13.1) |
| [[A-427 (line)]] | wt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -17.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 256 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -14.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 196 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 346 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -10.2) ⚠ toxic |
| [[J82 (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 417 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[MIA PaCa-2 (line)]] | alt | 183 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 536 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -9.9) |
| [[C-33 A (line)]] | alt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -8.5) |
| [[CHP-212 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 161 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.576× (z -8.7) |
| [[Hs 766T (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -13.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -14.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 149 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.421× (z -10.3) |
| [[SNU-1 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 1088 (line)]] | alt | 276 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 258 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM10]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 | pathway: EPH-Ephrin signaling |
| [[PIGN]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[MYCBP]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ITGA6]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SNX25]] | +0.52 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PIGF]] | +0.52 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[S100A16]] | +0.52 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ADAM19]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[TIMP1]] | +0.51 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[ITGB5]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.51 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[CD9]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC3A2]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SRP14-DT]] | -0.51 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[HSBP1L1]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TBKBP1]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ZBED3]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[GPRASP3]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TRMO]] | -0.50 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CCDC102A]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[DUSP3]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[DXO]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[KCNMB3]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ARMCX1]] | -0.49 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | ITGA2 activity raises RASA1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without ITGA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[JAKMIP3]] | B | JAKMIP3 activity lowers RASA1's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without JAKMIP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |
| [[SLC26A11]] | B | SLC26A11 activity lowers RASA1's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 1.93× higher at baseline in the lines without SLC26A11 | 0.048 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |
| [[ANTXR2]] | B | ANTXR2 activity raises RASA1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without ANTXR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, 37.7); signed map (-4.1, 51.9). **Vector** length 86.7, 25.1% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.2 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.1 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.6 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.5 | -0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -11.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RAS p21 protein activator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:87,267,883-87,391,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAP, CM-AVM, p120GAP, p120RASGAP, p120; previously RASA |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; C2 and RasGAP domain containing; SH3 domain containing |
| Hallmark sets | HEDGEHOG_SIGNALING, APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; VEGFR2 mediated cell proliferation; Downstream signal transduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P20936](https://www.uniprot.org/uniprotkb/P20936) (Ras GTPase-activating protein 1):

> GTPase-activating protein (GAP) that stimulates the intrinsic GTPase activity of Ras proteins, such as NRAS, facilitating their transition from the active GTP-bound state to the inactive GDP-bound state, thereby terminating Ras signaling.

**Summary**, from NCBI Gene [5921](https://www.ncbi.nlm.nih.gov/gene/5921):

> The protein encoded by this gene is located in the cytoplasm and is part of the GAP1 family of GTPase-activating proteins. The gene product stimulates the GTPase activity of normal RAS p21 but not its oncogenic counterpart. Acting as a suppressor of RAS function, the protein enhances the weak intrinsic GTPase activity of RAS proteins resulting in the inactive GDP-bound form of RAS, thereby allowing control of cellular proliferation and differentiation. Mutations leading to changes in the …

**Accessions** — [HGNC:9871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9871) · Entrez [5921](https://www.ncbi.nlm.nih.gov/gene/5921) · UniProt [P20936](https://www.uniprot.org/uniprotkb/P20936) · Ensembl [ENSG00000145715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145715)

## Data

Gene col 7015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7015); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7015]; `tensor/DDL_lfc|DDL_z.npy` [7015]; `embed/gene_vectors.npy` [7015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7015 or target_col == 7015). Every well: [[RASA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
