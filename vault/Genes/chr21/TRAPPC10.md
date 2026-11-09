---
symbol: "TRAPPC10"
type: "gene"
col: 8324
ensembl_id: "ENSG00000160218"
name: "trafficking protein particle complex subunit 10"
location: "21q22.3"
module: 36
arm: "+"
pooled_cpm: 88.67
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TRAPPC10

*trafficking protein particle complex subunit 10* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.64× (z +9.2, q 2e-17, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.484× (z -13.6, q 2e-39, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.766× (z -7.1, q 3e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AREL1]] (+0.77, fdr 7e-06), [[HIRA]] (+0.73, fdr 7e-06), [[NPLOC4]] (+0.72, fdr 7e-06); moves opposite to [[KPNA5]] (-0.63, fdr 8e-06), [[LGALS3]] (-0.62, fdr 1e-05), [[NDUFA5]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LGALS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +9.2 | 2e-17 | 44/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +9.1 | 2e-17 | 47/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +7.0 | 4e-10 | 33/49 (NCI-H460, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.9 | 7e-10 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +6.4 | 1e-08 | 39/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +6.3 | 2e-08 | 37/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.39×** | +6.2 | 6e-08 | 32/48 (CFPAC-1, SNU-423, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.9 | 2e-07 | 33/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 3e-07 | 35/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.4 | 4e-06 | 25/47 (COLO 205, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 6e-06 | 35/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.1 | 1e-05 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +5.0 | 3e-05 | 28/48 (NCI-H1792, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.25×** | +4.1 | 0.001 | 26/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.1 | 0.002 | 26/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.012 | 19/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.013 | 19/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.484×** | -13.6 | 2e-39 | 43/49 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -12.8 | 6e-35 | 39/44 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.766×** | -7.1 | 3e-10 | 34/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -6.4 | 2e-08 | 27/45 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.755×** | -5.3 | 2e-05 | 33/49 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.8 | 1e-04 | 21/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.808×** | -4.0 | 0.005 | 24/48 (H4, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.13 | 19/48 (NCI-H661, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.852× | -3.0 | 0.15 | 20/48 (A549, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 91.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 86.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -15.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 121 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.477× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 111 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 98.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -22.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 65.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 67.1 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 2 (1 ⚠) | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0550× (z -14.1) |
| [[A-427 (line)]] | wt | 99.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -12.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AN3 CA (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0988× (z -14.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -14.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 93.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 77.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.540× (z -10.4) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AREL1]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[HIRA]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[NPLOC4]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ZNF767P-1]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.71 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ARPC5L]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CHUK]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.66 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[EHMT1]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[FBXW11]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SENP5]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | -0.63 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[LGALS3]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RPS6KA6]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[CLK4]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.59 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[OCIAD1]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[MATCAP2]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[NOTCH2NLC]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MAK]] | -0.57 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ARRDC3]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers TRAPPC10's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.26× higher at baseline in the lines without LGALS3 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[NOTCH2NLR]] | B | NOTCH2NLR activity raises TRAPPC10's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without NOTCH2NLR | 0.094 | ⚠ within organs, on part of the lines |
| [[NBPF26]] | C | NBPF26 activity raises TRAPPC10's level | lines that do not express NBPF26 (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without NBPF26 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.0, -17.2); signed map (-46.2, -21.3). **Vector** length 114, 36.1% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.8 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -7.7 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.8 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,012,309-44,106,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EHOC-1, TRS130; previously TMEM1 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P48553](https://www.uniprot.org/uniprotkb/P48553) (Trafficking protein particle complex subunit 10):

> Specific subunit of the TRAPP (transport protein particle) II complex, a highly conserved vesicle tethering complex that functions in late Golgi trafficking as a membrane tether.

**Summary**, from NCBI Gene [7109](https://www.ncbi.nlm.nih.gov/gene/7109):

> The protein encoded by this gene is a transmembrane protein found in the cis-Golgi complex. The encoded protein is part of the multisubunit transport protein particle (TRAPP) complex and may be involved in vesicular transport from the endoplasmic reticulum to the Golgi. Mutations in this gene could be responsible for the Unverricht-Lundborg type of progressive myoclonus epilepsy, or for autoimmune polyglandular disease type 1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11868) · Entrez [7109](https://www.ncbi.nlm.nih.gov/gene/7109) · UniProt [P48553](https://www.uniprot.org/uniprotkb/P48553) · Ensembl [ENSG00000160218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160218)

## Data

Gene col 8324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8324); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8324]; `tensor/DDL_lfc|DDL_z.npy` [8324]; `embed/gene_vectors.npy` [8324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8324 or target_col == 8324). Every well: [[TRAPPC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
