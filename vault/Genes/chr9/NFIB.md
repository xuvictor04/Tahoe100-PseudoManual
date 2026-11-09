---
symbol: "NFIB"
type: "gene"
col: 7227
ensembl_id: "ENSG00000147862"
name: "nuclear factor I B"
location: "9p23-p22.3"
module: 143
arm: "+"
pooled_cpm: 156.61
n_lines_expressing: 43
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# NFIB

*nuclear factor I B* — 9p23-p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 1.24× (z +5.1, q 2e-04, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.304× (z -20.6, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIGN]] (+0.66, fdr 7e-06), [[USP13]] (+0.66, fdr 1e-05), [[CABLES1]] (+0.65, fdr 1e-05); moves opposite to [[MYO9B]] (-0.65, fdr 1e-05), [[GIPR]] (-0.62, fdr 1e-05), [[KRBOX4]] (-0.61, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[HOPX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +5.1 | 2e-04 | 24/41 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +4.9 | 2e-04 | 22/41 (A-172, SNU-423, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.9 | 2e-04 | 26/41 (NCI-H460, RKO, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 2e-04 | 28/41 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.7 | 4e-04 | 27/41 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.6 | 4e-04 | 24/41 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 5e-04 | 24/41 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 5e-04 | 23/41 (SW 900, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.5 | 5e-04 | 23/41 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 8e-04 | 19/41 (CFPAC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.3 | 8e-04 | 21/41 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 1e-03 | 23/42 (CFPAC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.2 | 0.001 | 16/42 (CFPAC-1, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 20/43 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.007 | 22/41 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.020 | 19/41 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.033 | 17/41 (A498, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -20.6 | 0e+00 | 39/41 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.332×** | -19.0 | 0e+00 | 40/41 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.473×** | -12.9 | 7e-36 | 38/41 (HT-29, A-427, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.624×** | -8.2 | 5e-14 | 28/41 (HT-29, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -7.0 | 4e-10 | 25/41 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.661×** | -6.7 | 2e-09 | 28/41 (Panc 03.27, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -6.2 | 5e-08 | 28/41 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -6.0 | 2e-07 | 26/41 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -5.5 | 2e-06 | 29/41 (AN3 CA, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.008 | 23/41 (NCI-H1792, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.030 | 19/41 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.759×** | -3.4 | 0.033 | 20/41 (NCI-H460, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.041 | 16/42 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.817×** | -3.3 | 0.046 | 18/41 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.658×** | -3.2 | 0.050 | 14/41 (Panc 03.27, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.079 | 19/41 (KATO III, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 1,255 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.202× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 247 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -25.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -20.9) |
| [[Panc 03.27 (line)]] | alt | 332 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -19.3) |
| [[A498 (line)]] | wt | 451 | 2 (1 ⚠) | 7 (4 ⚠) | [[Penfluridol (drug)]] 5 µM 2.05× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -14.6) |
| [[HT-29 (line)]] | alt | 259 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -28.6) |
| [[KATO III (line)]] | alt | 323 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -27.1) |
| [[NCI-H2030 (line)]] | alt | 159 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.6) |
| [[RKO (line)]] | wt | 135 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.217× (z -14.3) |
| [[SHP-77 (line)]] | alt | 306 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -21.7) |
| [[LoVo (line)]] | wt | 240 | 1 | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.85× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.186× (z -24.8) |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.9) |
| [[A-172 (line)]] | wt | 47.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.17× (z +11.9) | [[Selinexor (drug)]] 5 µM 0.421× (z -10.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 238 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -21.2) |
| [[C-33 A (line)]] | alt | 287 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -20.8) |
| [[LS 180 (line)]] | wt | 190 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.33× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.163× (z -25.4) |
| [[PANC-1 (line)]] | alt | 98.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -16.3) |
| [[A549 (line)]] | wt | 206 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 322 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -23.4) |
| [[Hs 766T (line)]] | wt | 213 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -14.1) |
| [[SW48 (line)]] | wt | 285 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -17.9) |
| [[CHP-212 (line)]] | wt | 267 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -11.8) |
| [[HOP62 (line)]] | alt | 110 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.0) |
| [[HS-578T (line)]] | alt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -17.5) |
| [[SNU-423 (line)]] | alt | 103 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.333× (z -11.4) |
| [[BT-474 (line)]] | alt | 115 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -11.1) |
| [[C32 (line)]] | wt | 40.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 67.2 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.15× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 176 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.299× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.304× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 92.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 49.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 69.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +16.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 24.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[USP13]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CABLES1]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TGFB2]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[MBNL1]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TCF12]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NFIA]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 | same gene group; pathway: RNA Polymerase III Abortive And Retractive Initiation; STRING 812 |
| [[JADE1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF12]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_UV_RESPONSE_DN |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[GIPR]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.61 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZNF841]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MPG]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[DHDDS]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[PLEKHM1P1]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.58 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[VRK3]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GNAI3]] | -0.57 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[ARPC1A]] | -0.57 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[CIB1]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NFIB's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[NFIA]] | B | NFIA activity raises NFIB's level | lines that do not express NFIA (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without NFIA | 0.085 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOPX]] | B | NFIB activity lowers HOPX's level | lines that do not express NFIB (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without NFIB | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA3C]] | B | NFIB activity raises SEMA3C's level | lines that do not express NFIB (7) vs lines expressing it (43) | 3.67× lower at baseline in the lines without NFIB | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADGRG6]] | B | NFIB activity raises ADGRG6's level | lines that do not express NFIB (7) vs lines expressing it (43) | 3.45× lower at baseline in the lines without NFIB | 0.071 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STAU2]] | B | NFIB activity raises STAU2's level | lines that do not express NFIB (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without NFIB | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 15.5); signed map (47.3, 18.6). **Vector** length 143, 46.8% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.3 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.8 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.5 | +4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -20.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -19.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -5.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor I B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p23-p22.3 — chr9:14,081,843-14,398,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NFI-RED, NFIB2, NFIB3 |
| Gene groups (HGNC) | Nuclear factor I family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: RNA Polymerase III Transcription Termination; RNA Polymerase III Abortive And Retractive Initiation; RNA Polymerase III Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [O00712](https://www.uniprot.org/uniprotkb/O00712) (Nuclear factor 1 B-type):

> Transcriptional activator of GFAP, essential for proper brain development. Recognizes and binds the palindromic sequence 5'-TTGGCNNNNNGCCAA-3' present in viral and cellular promoters and in the origin of replication of adenovirus type 2. These proteins are individually capable of activating transcription and replication.

**Summary**, from NCBI Gene [4781](https://www.ncbi.nlm.nih.gov/gene/4781):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and transcription regulator inhibitor activity. Involved in brain development and regulation of DNA-templated transcription. Located in fibrillar center and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7785) · Entrez [4781](https://www.ncbi.nlm.nih.gov/gene/4781) · UniProt [O00712](https://www.uniprot.org/uniprotkb/O00712) · Ensembl [ENSG00000147862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147862)

## Data

Gene col 7227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7227); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7227]; `tensor/DDL_lfc|DDL_z.npy` [7227]; `embed/gene_vectors.npy` [7227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7227 or target_col == 7227). Every well: [[NFIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
