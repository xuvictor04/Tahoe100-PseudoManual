---
symbol: "DNMBP"
type: "gene"
col: 2858
ensembl_id: "ENSG00000107554"
name: "dynamin binding protein"
location: "10q24.2"
module: 84
arm: "+"
pooled_cpm: 118.81
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# DNMBP

*dynamin binding protein* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +7.4, q 9e-11, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.432× (z -20.7, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WWTR1]] (+0.66, fdr 7e-06), [[PHC2]] (+0.66, fdr 1e-05), [[MIR100HG]] (+0.65, fdr 7e-06); moves opposite to [[GARS1-DT]] (-0.53, fdr 1e-04), [[ZCCHC8]] (-0.52, fdr 3e-05), [[NRSN2-AS1]] (-0.50, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TMEM156]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +7.4 | 9e-11 | 34/49 (A-427, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.8 | 2e-06 | 32/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.1 | 5e-05 | 30/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.0 | 9e-05 | 23/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.002 | 24/48 (C-33 A, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.2 | 0.003 | 23/48 (HEC-1-A, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +3.4 | 0.061 | 20/48 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[Bentamapimod (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.087 | 19/48 (MIA PaCa-2, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -20.7 | 0e+00 | 45/49 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -14.5 | 4e-45 | 44/49 (COLO 205, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -11.6 | 9e-29 | 37/44 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -9.2 | 5e-18 | 34/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -7.8 | 5e-13 | 33/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -7.0 | 3e-10 | 31/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -6.5 | 7e-09 | 31/47 (SW1417, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.746×** | -5.8 | 4e-07 | 28/48 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -5.5 | 2e-06 | 31/50 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.807×** | -5.1 | 2e-05 | 27/49 (HCT15, NCI-H2030, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.772×** | -5.1 | 2e-05 | 28/48 (NCI-H23, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -5.0 | 2e-05 | 26/49 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.749×** | -5.0 | 2e-05 | 28/49 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.611×** | -4.5 | 3e-04 | 29/48 (SW1417, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.705×** | -4.3 | 6e-04 | 24/48 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.766×** | -4.2 | 7e-04 | 28/48 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.802×** | -3.6 | 0.008 | 22/48 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.014 | 18/47 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.015 | 16/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 340 | 0 | 16 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -23.2) |
| [[NCI-H1573 (line)]] | alt | 89.0 | 9 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.93× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.4× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 118 | 5 (4 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.01× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.364× (z -9.6) |
| [[A-427 (line)]] | wt | 91.3 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.4× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 233 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -19.5) |
| [[A-172 (line)]] | wt | 160 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 64.5 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.61× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.8) |
| [[J82 (line)]] | alt | 63.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 129 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.8) |
| [[COLO 205 (line)]] | alt | 181 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.2) |
| [[H4 (line)]] | wt | 140 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.3) |
| [[HCT15 (line)]] | alt | 148 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -10.9) |
| [[LoVo (line)]] | wt | 95.0 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.24× (z +13.2) | [[Auranofin (drug)]] 5 µM 0.339× (z -13.1) |
| [[LS 180 (line)]] | wt | 142 | 2 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.78× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 87.9 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.56× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -15.3) |
| [[CHP-212 (line)]] | wt | 260 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.3) |
| [[PANC-1 (line)]] | alt | 204 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.7) |
| [[RKO (line)]] | wt | 65.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -13.0) |
| [[SW1417 (line)]] | alt | 158 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -13.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.8) |
| [[A498 (line)]] | wt | 60.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.4) |
| [[KATO III (line)]] | alt | 83.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.26× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -14.6) |
| [[SW 900 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.8) |
| [[A549 (line)]] | wt | 94.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.5) |
| [[C-33 A (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[Hs 766T (line)]] | wt | 78.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.5) |
| [[HS-578T (line)]] | alt | 89.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +9.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SNU-423 (line)]] | alt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.4) |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -9.5) |
| [[SW480 (line)]] | alt | 59.4 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.76× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WWTR1]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PHC2]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[MIR100HG]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[AMOTL1]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[STX1A]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CCN2]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[F2R]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PHLDA1]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RAC2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NDFIP2]] | +0.58 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1-DT]] | -0.53 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ZCCHC8]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NRSN2-AS1]] | -0.50 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[SOS1]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 | same gene group |
| [[ZNF460-AS1]] | -0.49 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[NBR2]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM156]] | B | TMEM156 activity raises DNMBP's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without TMEM156 | 0.050 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[TMEM156]] | B | TMEM156 activity strengthens DNMBP's drug response | lines that do not express TMEM156 (26) vs lines expressing it (23) | the lines without TMEM156 respond 0.72× as strongly (z diff +1.73); strongest at Dinaciclib 0.05 µM: 0.67x vs 0.40x (z diff +3.0) | 0.065 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4; target measured in part of the lines; artifact flags |
| [[CCN2]] | B | CCN2 activity raises DNMBP's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without CCN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[HDAC6]] | B | HDAC6 activity lowers DNMBP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.4, 7.7); signed map (6.0, 49.0). **Vector** length 127, 39.4% of its response variance represented; |z| ≥ 3 in 1,671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.1 | -20.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -7.3 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.8 | -5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.0 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | dynamin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,875,577-100,009,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1010, Tuba, ARHGEF36 |
| Gene groups (HGNC) | Dbl family Rho GEFs; BAR and Dbl domain containing; SH3 domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XZF7](https://www.uniprot.org/uniprotkb/Q6XZF7) (Dynamin-binding protein):

> Plays a critical role as a guanine nucleotide exchange factor (GEF) for CDC42 in several intracellular processes associated with the actin and microtubule cytoskeleton. Regulates the structure of apical junctions through F-actin organization in epithelial cells. Participates in the normal lumenogenesis of epithelial cell cysts by regulating spindle orientation. Plays a role in ciliogenesis (By similarity). May play a role in membrane trafficking between the cell surface and the Golgi (By …

**Summary**, from NCBI Gene [23268](https://www.ncbi.nlm.nih.gov/gene/23268):

> This gene encodes a protein belonging to the guanine nucleotide exchange factor family, and which regulates the configuration of cell junctions. It contains multiple binding sites for dynamin and thus links dynamin to actin regulatory proteins. Polymorphisms in this gene have been linked to Alzheimer's disease in some populations, though there are conflicting reports of such linkages in other populations. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec …

**Accessions** — [HGNC:30373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30373) · Entrez [23268](https://www.ncbi.nlm.nih.gov/gene/23268) · UniProt [Q6XZF7](https://www.uniprot.org/uniprotkb/Q6XZF7) · Ensembl [ENSG00000107554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107554)

## Data

Gene col 2858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2858); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2858]; `tensor/DDL_lfc|DDL_z.npy` [2858]; `embed/gene_vectors.npy` [2858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2858 or target_col == 2858). Every well: [[DNMBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNMBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
