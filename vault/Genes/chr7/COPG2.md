---
symbol: "COPG2"
type: "gene"
col: 8177
ensembl_id: "ENSG00000158623"
name: "coat protein complex I subunit gamma 2"
location: "7q32.2"
module: 26
arm: "-"
pooled_cpm: 40.98
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# COPG2

*coat protein complex I subunit gamma 2* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.81× (z +11.9, q 7e-30, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -28.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP93]] (+0.70, fdr 7e-06), [[PCCB]] (+0.67, fdr 7e-06), [[RALGPS1]] (+0.65, fdr 7e-06); moves opposite to [[MMADHC-DT]] (-0.66, fdr 1e-05), [[ST8SIA5]] (-0.66, fdr 3e-05), [[LINC00571]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +11.9 | 7e-30 | 38/48 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +10.3 | 1e-22 | 36/48 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.6 | 2e-15 | 34/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.6 | 3e-06 | 27/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.7 | 3e-04 | 22/48 (HT-29, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.25×** | +4.4 | 9e-04 | 17/48 (C32, SW48, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +4.2 | 0.002 | 23/48 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 13/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.7 | 0.011 | 13/48 (HEC-1-A, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.362×** | -28.6 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.408×** | -17.3 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.431×** | -16.9 | 0e+00 | 43/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.432×** | -16.8 | 0e+00 | 40/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.471×** | -15.1 | 0e+00 | 43/47 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.487×** | -14.4 | 3e-45 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -10.6 | 4e-24 | 32/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -10.4 | 1e-23 | 35/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -8.3 | 8e-15 | 32/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -8.0 | 6e-14 | 31/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -6.1 | 6e-08 | 22/48 (A-427, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.8 | 4e-07 | 22/48 (HS-578T, NCI-H661, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -5.0 | 2e-05 | 21/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -4.9 | 4e-05 | 23/48 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -4.9 | 4e-05 | 23/49 (SW1417, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -4.8 | 7e-05 | 25/48 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -4.2 | 9e-04 | 19/48 (HEC-1-A, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -26.8) |
| [[LoVo (line)]] | wt | 40.2 | 2 | 7 | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -20.9) |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -19.2) |
| [[SW48 (line)]] | wt | 45.4 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -11.8) |
| [[PANC-1 (line)]] | alt | 64.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -31.5) |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 6 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -12.5) |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.3) |
| [[HS-578T (line)]] | alt | 50.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.2) |
| [[J82 (line)]] | alt | 30.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.3) |
| [[SW480 (line)]] | alt | 49.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -19.5) |
| [[HT-29 (line)]] | alt | 39.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.4) |
| [[A-427 (line)]] | wt | 56.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.462× (z -11.5) |
| [[A549 (line)]] | wt | 39.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.5) |
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.2) |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0807× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 87.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.257× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 65.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.6) |
| [[C-33 A (line)]] | alt | 98.3 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.314× (z -11.1) |
| [[C32 (line)]] | wt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -25.1) |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 33.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.5) |
| [[RKO (line)]] | wt | 39.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.262× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 3 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0759× (z -12.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.8) |
| [[A498 (line)]] | wt | 34.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.7) |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.6) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.8) |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.1) |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.243× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -8.8) |
| [[SNU-1 (line)]] | wt | 48.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -9.4) |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.7) |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -9.0) |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PCCB]] | +0.67 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[RALGPS1]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[STIMATE]] | +0.65 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[BORCS5]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ALG6]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[FAM20B]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NTAQ1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PIGU]] | +0.62 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[LRRC20]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.66 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ST8SIA5]] | -0.66 | -0.59 / -0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[LINC00571]] | -0.65 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SLC6A13]] | -0.65 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.64 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[NEB]] | -0.63 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[EIF4EBP3]] | -0.63 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[AEBP2]] | -0.62 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[N4BP2L1]] | -0.62 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ANGPT2]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DNAH12]] | -0.61 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[SLC22A1]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers COPG2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.4, -27.9); signed map (-39.6, -16.2). **Vector** length 98.3, 26.3% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +11.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +10.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.1 | +1.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.4 | -16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -28.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -16.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,506,238-130,668,748 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 2-COP |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Coat protein complex I |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBF2](https://www.uniprot.org/uniprotkb/Q9UBF2) (Coatomer subunit gamma-2):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to ADP-ribosylation …

**Summary**, from NCBI Gene [26958](https://www.ncbi.nlm.nih.gov/gene/26958):

> Predicted to enable structural molecule activity. Involved in intra-Golgi vesicle-mediated transport. Part of COPI vesicle coat. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2237) · Entrez [26958](https://www.ncbi.nlm.nih.gov/gene/26958) · UniProt [Q9UBF2](https://www.uniprot.org/uniprotkb/Q9UBF2) · Ensembl [ENSG00000158623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158623)

## Data

Gene col 8177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8177); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8177]; `tensor/DDL_lfc|DDL_z.npy` [8177]; `embed/gene_vectors.npy` [8177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8177 or target_col == 8177). Every well: [[COPG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
