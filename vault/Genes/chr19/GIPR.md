---
symbol: "GIPR"
type: "gene"
col: 206
ensembl_id: "ENSG00000010310"
name: "gastric inhibitory polypeptide receptor"
location: "19q13.32"
module: 208
arm: "+"
pooled_cpm: 12.59
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 36
n_dd_up_clean: 21
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# GIPR

*gastric inhibitory polypeptide receptor* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.98× (z +11.5, q 7e-28, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.385× (z -11.3, q 4e-27, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3B]] (+0.73, fdr 7e-06), [[LYPD3]] (+0.69, fdr 7e-06), [[MYO9B]] (+0.68, fdr 1e-05); moves opposite to [[ZMYND11]] (-0.68, fdr 1e-05), [[ARID1B]] (-0.64, fdr 1e-05), [[FBXL17]] (-0.63, fdr 3e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +11.5 | 7e-28 | 26/41 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +10.4 | 1e-22 | 33/40 (KATO III, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +10.2 | 3e-22 | 27/41 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +9.8 | 1e-20 | 26/40 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +9.6 | 9e-20 | 26/41 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +8.8 | 2e-16 | 26/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +7.9 | 2e-13 | 26/40 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +6.8 | 7e-10 | 17/40 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +6.4 | 8e-09 | 24/36 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +6.1 | 5e-08 | 15/39 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 1e-04 | 18/39 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +4.6 | 2e-04 | 13/39 (SW1417, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.89×** | +4.0 | 0.003 | 6/28 (NCI-H1573, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.006 | 15/39 (A-172, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.027 | 7/40 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.027 | 8/35 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.027 | 14/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -11.3 | 4e-27 | 32/41 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.386×** | -11.3 | 4e-27 | 30/37 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -10.3 | 1e-22 | 27/40 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -9.9 | 7e-21 | 31/40 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.573×** | -9.3 | 1e-18 | 26/38 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.265×** | -8.2 | 2e-14 | 30/39 (CFPAC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -8.0 | 1e-13 | 26/40 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.532×** | -7.5 | 5e-12 | 23/37 (SW 900, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.546×** | -7.2 | 4e-11 | 23/30 (HOP62, NCI-H1792, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -7.1 | 5e-11 | 22/32 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -6.2 | 4e-08 | 21/40 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.607×** | -5.9 | 2e-07 | 21/41 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -5.7 | 4e-07 | 21/34 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.621×** | -5.6 | 7e-07 | 23/40 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -5.3 | 5e-06 | 20/35 (HT-29, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.455×** | -4.9 | 4e-05 | 17/39 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.657×** | -4.7 | 9e-05 | 21/40 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -4.5 | 2e-04 | 19/34 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -4.4 | 3e-04 | 19/37 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 29.5 | 1 | 12 (5 ⚠) | [[Auranofin (drug)]] 5 µM 3.45× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0738× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -17.4) |
| [[CFPAC-1 (line)]] | alt | 31.1 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0267× (z -17.6) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0286× (z -16.4) |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0696× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.105× (z -10.4) |
| [[SW1417 (line)]] | alt | 13.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.16× (z +11.2) | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0923× (z -12.7) |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0482× (z -13.7) |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -12.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.181× (z -9.1) |
| [[Hs 766T (line)]] | wt | 35.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -9.2) |
| [[KATO III (line)]] | alt | 10.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.42× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 8.03 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0608× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 6.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 6.19 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0518× (z -11.5) |
| [[LS 180 (line)]] | wt | 7.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H460 (line)]] | wt | 6.33 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.99× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.111× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 8.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.259× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LYPD3]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TNNT1]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RTN2]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[KLC3]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.65 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[GDPD5]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[F11R]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[DNASE1L1]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.68 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ARID1B]] | -0.64 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[FBXL17]] | -0.63 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | -0.62 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[SNX5]] | -0.62 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[NFIB]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[C5orf15]] | -0.61 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[USP13]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FUBP1]] | -0.61 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[USP24]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[ZFP91]] | -0.60 | -0.53 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity raises GIPR's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without ADAM8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PEAR1]] | B | PEAR1 activity raises GIPR's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without PEAR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[PDGFB]] | B | PDGFB activity raises GIPR's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without PDGFB | 0.007 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[CDA]] | B | CDA activity raises GIPR's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without CDA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[ATG9B]] | B | ATG9B activity raises GIPR's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without ATG9B | 0.057 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[THEMIS2]] | B | THEMIS2 activity raises GIPR's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without THEMIS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[GCKR]] | B | GCKR activity raises GIPR's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without GCKR | 0.090 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[CARD11]] | B | CARD11 activity raises GIPR's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.55× lower at baseline in the lines without CARD11 | 0.095 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.5, 1.9); signed map (-24.3, 22.8). **Vector** length 120, 32.6% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | gastric inhibitory polypeptide receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,668,221-45,683,722 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glucagon receptor family; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Glucagon-type ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P48546](https://www.uniprot.org/uniprotkb/P48546) (Gastric inhibitory polypeptide receptor):

> This is a receptor for GIP. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.

**Summary**, from NCBI Gene [2696](https://www.ncbi.nlm.nih.gov/gene/2696):

> This gene encodes a G-protein coupled receptor for gastric inhibitory polypeptide (GIP), which was originally identified as an activity in gut extracts that inhibited gastric acid secretion and gastrin release, but subsequently was demonstrated to stimulate insulin release in the presence of elevated glucose. Mice lacking this gene exhibit higher blood glucose levels with impaired initial insulin response after oral glucose load. Defect in this gene thus may contribute to the pathogenesis of …

**Accessions** — [HGNC:4271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4271) · Entrez [2696](https://www.ncbi.nlm.nih.gov/gene/2696) · UniProt [P48546](https://www.uniprot.org/uniprotkb/P48546) · Ensembl [ENSG00000010310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010310)

## Data

Gene col 206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 206); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 206]; `tensor/DDL_lfc|DDL_z.npy` [206]; `embed/gene_vectors.npy` [206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 206 or target_col == 206). Every well: [[GIPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
