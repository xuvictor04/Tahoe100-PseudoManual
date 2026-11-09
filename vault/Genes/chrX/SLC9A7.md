---
symbol: "SLC9A7"
type: "gene"
col: 810
ensembl_id: "ENSG00000065923"
name: "solute carrier family 9 member A7"
location: "Xp11.3"
module: 84
arm: "+"
pooled_cpm: 91.48
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 38
n_dd_up_clean: 10
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SLC9A7

*solute carrier family 9 member A7* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.41× (z +6.7, q 1e-08, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.425× (z -23.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST3GAL5]] (+0.70, fdr 8e-06), [[RAC2]] (+0.68, fdr 9e-06), [[CD82]] (+0.66, fdr 7e-06); moves opposite to [[MGST1]] (-0.55, fdr 6e-05), [[DDX59]] (-0.54, fdr 1e-04), [[STXBP5]] (-0.54, fdr 2e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GALNT18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.7 | 1e-08 | 29/47 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.5 | 1e-08 | 28/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +6.5 | 1e-08 | 29/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.8 | 1e-06 | 21/47 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 26/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 2e-04 | 28/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.001 | 21/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 21/47 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.015 | 20/48 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.033 | 11/47 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.425×** | -23.5 | 0e+00 | 44/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -10.0 | 4e-21 | 35/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -9.4 | 9e-19 | 36/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -8.3 | 1e-14 | 36/49 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -7.9 | 3e-13 | 32/43 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -7.5 | 4e-12 | 26/41 (SK-MEL-2, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.728×** | -6.1 | 6e-08 | 27/47 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.732×** | -6.0 | 1e-07 | 26/48 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.750×** | -5.6 | 2e-06 | 26/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -5.2 | 1e-05 | 25/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.773×** | -5.0 | 3e-05 | 24/47 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.779×** | -5.0 | 3e-05 | 26/48 (SK-MEL-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.780×** | -5.0 | 3e-05 | 23/49 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.806×** | -4.9 | 5e-05 | 24/47 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 6e-05 | 23/47 (BT-474, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -4.7 | 1e-04 | 24/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 2e-04 | 28/47 (Hs 766T, A498, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.791×** | -4.5 | 2e-04 | 25/47 (SNU-423, J82, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.793×** | -4.5 | 2e-04 | 25/47 (SNU-423, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 59.9 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.8) |
| [[RKO (line)]] | wt | 176 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -21.2) |
| [[NCI-H460 (line)]] | wt | 25.3 | 6 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.1) | [[Trametinib (drug)]] 5 µM 0.395× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 224 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.1) |
| [[SNU-423 (line)]] | alt | 131 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.5) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.290× (z -13.4) |
| [[SW480 (line)]] | alt | 78.1 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -16.9) |
| [[BT-474 (line)]] | alt | 179 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.5) |
| [[Hs 766T (line)]] | wt | 118 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 237 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -18.1) |
| [[J82 (line)]] | alt | 97.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 160 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -20.5) |
| [[A-427 (line)]] | wt | 75.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -11.9) |
| [[SW 900 (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -18.9) |
| [[SW48 (line)]] | wt | 87.4 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 10.3× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 88.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 66.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.7) |
| [[HS-578T (line)]] | alt | 94.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -14.0) |
| [[HT-29 (line)]] | alt | 48.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.3) |
| [[LoVo (line)]] | wt | 59.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 69.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 105 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.02× (z +9.1) | [[Budesonide (drug)]] 0.5 µM 0.456× (z -8.5) |
| [[SW1417 (line)]] | alt | 77.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -14.9) |
| [[A-172 (line)]] | wt | 87.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.9) |
| [[A498 (line)]] | wt | 52.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.1) |
| [[A549 (line)]] | wt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -15.7) |
| [[AN3 CA (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.9) |
| [[COLO 205 (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.2) |
| [[KATO III (line)]] | alt | 61.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.9) |
| [[LS 180 (line)]] | wt | 42.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.8) |
| [[PANC-1 (line)]] | alt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -18.0) |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 94.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0750× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL5]] | +0.70 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[RAC2]] | +0.68 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[CD82]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PKIA]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SHB]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[KCNN4]] | +0.62 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[TNFRSF11A]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.61 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[GDPGP1]] | +0.60 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[BCL2A1]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[DDX59]] | -0.54 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[STXBP5]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[EFCAB2]] | -0.53 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[KANSL1L]] | -0.52 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT18]] | B | GALNT18 activity raises SLC9A7's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without GALNT18 | 0.020 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[PDGFB]] | B | PDGFB activity strengthens SLC9A7's drug response | lines that do not express PDGFB (16) vs lines expressing it (33) | the lines without PDGFB respond 0.71× as strongly (z diff +1.38); strongest at Topotecan (hydrochloride) 5 µM: 0.72x vs 0.54x (z diff +2.5) | 0.028 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises SLC9A7's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.3% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCP1]] | B | CDCP1 activity raises SLC9A7's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without CDCP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[TSPAN5]] | B | TSPAN5 activity raises SLC9A7's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without TSPAN5 | 0.064 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[ICAM1]] | B | ICAM1 activity raises SLC9A7's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without ICAM1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[MYO10]] | B | MYO10 activity raises SLC9A7's level | lines that do not express MYO10 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without MYO10 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM111A, RARG, DPH6-DT; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SLC9A7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SLC9A7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers SLC9A7's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.3% of all compounds | 0.099 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.9, -0.1); signed map (1.3, 47.3). **Vector** length 136, 43.6% of its response variance represented; |z| ≥ 3 in 1,754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +8.5 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -23.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.4 | -4.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -5.9 | -4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.9 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.7 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:46,599,251-46,759,118 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NHE7, NHE-7 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 4 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T83](https://www.uniprot.org/uniprotkb/Q96T83) (Sodium/hydrogen exchanger 7):

> Golgi Na(+), K(+)/(H+) antiporter. Mediates the electoneutral influx of Na(+) or K(+) in exchange for H(+). May contribute to the regulation of Golgi apparatus volume and pH.

**Summary**, from NCBI Gene [84679](https://www.ncbi.nlm.nih.gov/gene/84679):

> This gene encodes a sodium and potassium/ proton antiporter that is a member of the solute carrier family 9 protein family. The encoded protein is primarily localized to the trans-Golgi network and is involved in maintaining pH homeostasis in organelles along the secretory and endocytic pathways. This protein may enhance cell growth of certain breast tumors. This gene is part of a gene cluster on chromosome Xp11.23. A pseudogene of this gene is found on chromosome 12. Alternate splicing results …

**Accessions** — [HGNC:17123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17123) · Entrez [84679](https://www.ncbi.nlm.nih.gov/gene/84679) · UniProt [Q96T83](https://www.uniprot.org/uniprotkb/Q96T83) · Ensembl [ENSG00000065923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065923)

## Data

Gene col 810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 810); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 810]; `tensor/DDL_lfc|DDL_z.npy` [810]; `embed/gene_vectors.npy` [810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 810 or target_col == 810). Every well: [[SLC9A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
