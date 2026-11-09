---
symbol: "TMEM132B"
type: "gene"
col: 6299
ensembl_id: "ENSG00000139364"
name: "transmembrane protein 132B"
location: "12q24.31"
module: 165
arm: "+"
pooled_cpm: 10.69
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# TMEM132B

*transmembrane protein 132B* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.22× (z +22.9, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.614× (z -5.5, q 2e-05, down in 21 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.467× (z -4.5, q 0.001, down in 17 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL23A1]] (+0.71, fdr 7e-06), [[RELN]] (+0.64, fdr 7e-06), [[DISP3]] (+0.64, fdr 7e-06); moves opposite to [[FIGN]] (-0.55, fdr 2e-05), [[VPS50]] (-0.51, fdr 2e-05), [[LCLAT1]] (-0.50, fdr 3e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.22×** | +22.9 | 0e+00 | 37/40 (SW480, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.02×** | +22.1 | 0e+00 | 29/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +15.8 | 0e+00 | 38/41 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.62×** | +14.5 | 3e-45 | 33/39 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.57×** | +14.3 | 2e-44 | 38/40 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +13.8 | 2e-41 | 30/34 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ position correction uncertain | **3.20×** | +12.6 | 3e-34 | 25/36 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.69×** | +11.1 | 8e-27 | 34/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +10.9 | 8e-26 | 27/40 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +10.1 | 4e-22 | 20/36 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +9.2 | 2e-18 | 29/39 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.98×** | +7.7 | 8e-13 | 25/40 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.0 | 2e-10 | 7/19 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.54×** | +6.9 | 2e-10 | 22/40 (A498, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.50×** | +6.4 | 5e-09 | 12/41 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.2 | 2e-08 | 20/41 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +6.0 | 7e-08 | 19/38 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.58×** | +5.6 | 7e-07 | 16/38 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 4e-06 | 19/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.614×** | -5.5 | 2e-05 | 21/34 (H4, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.617×** | -5.4 | 2e-05 | 22/42 (H4, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.459×** | -4.6 | 9e-04 | 18/33 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -4.5 | 0.001 | 17/37 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.491×** | -4.2 | 0.003 | 14/37 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -4.1 | 0.004 | 16/41 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.500×** | -4.1 | 0.004 | 14/31 (hTERT-HPNE, H4, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.700×** | -4.0 | 0.004 | 10/40 (H4, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.722×** | -3.7 | 0.015 | 15/39 (H4, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.723×** | -3.6 | 0.015 | 15/38 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.021 | 16/39 (A-427, SW 900, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.821×** | -3.1 | 0.073 | 14/40 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.822×** | -3.1 | 0.073 | 3/42 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.073 | 15/39 (LOX-IMVI, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.087 | 9/42 (NCI-H1573, AN3 CA, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.764×** | -3.0 | 0.087 | 14/39 (A-427, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.3 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +17.8) | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 7 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.55× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.77 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +15.5) | — |
| [[H4 (line)]] | wt | 66.4 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0231× (z -17.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.113× (z -14.1) |
| [[PANC-1 (line)]] | alt | 7.42 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 5.06× (z +11.3) | — |
| [[SW480 (line)]] | alt | 5.41 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 6.65× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 15.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.12× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 12.6 | 3 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +10.4) ⚠ position correction uncertain · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.8) | — |
| [[A-427 (line)]] | wt | 24.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.91× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -12.1) |
| [[BT-474 (line)]] | alt | 10.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.16× (z +10.8) | [[Nimesulide (drug)]] 5 µM 0.0629× (z -10.7) ⚠ toxic; unreliable plate only |
| [[C32 (line)]] | wt | 3.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 3.11 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 9.04× (z +11.4) | [[Mozavaptan (drug)]] 5 µM 0.0804× (z -8.9) |
| [[KATO III (line)]] | alt | 3.93 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.9× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 2.83 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 23.5× (z +9.0) | — |
| [[A-172 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.235× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 7.35 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0659× (z -8.6) |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HT-29 (line)]] | alt | 2.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0959× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 4.32 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 3.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.8× (z +12.5) | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL23A1]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RELN]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[DISP3]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[GBX1]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RYR1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GPR84-AS1]] | +0.58 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[MTUS2]] | +0.58 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[RYR3]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PLD5]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DLGAP2]] | +0.56 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[VPS50]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[LCLAT1]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CEP162]] | -0.49 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[TUBGCP3]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[AIFM1]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[IRAK1BP1]] | -0.46 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[C22orf39]] | -0.46 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[DTWD2]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM132B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[COL6A2]] | B | COL6A2 activity weakens TMEM132B's drug response | lines that do not express COL6A2 (24) vs lines expressing it (17) | the lines without COL6A2 respond 1.74× as strongly (z diff -2.07); strongest at Homoharringtonine 5 µM: 2.02x vs 0.70x (z diff -5.9) | 0.020 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 32.3); signed map (28.9, 19.0). **Vector** length 82.6, 16.8% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +22.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +22.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +1.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.9 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 132B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:125,186,386-125,662,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1906, KIAA1786 |
| Matched by | ensembl_id |

UniProt [Q14DG7](https://www.uniprot.org/uniprotkb/Q14DG7) carries no function annotation.

**Summary**, from NCBI Gene [114795](https://www.ncbi.nlm.nih.gov/gene/114795):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29397) · Entrez [114795](https://www.ncbi.nlm.nih.gov/gene/114795) · UniProt [Q14DG7](https://www.uniprot.org/uniprotkb/Q14DG7) · Ensembl [ENSG00000139364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139364)

## Data

Gene col 6299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6299); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6299]; `tensor/DDL_lfc|DDL_z.npy` [6299]; `embed/gene_vectors.npy` [6299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6299 or target_col == 6299). Every well: [[TMEM132B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM132B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
