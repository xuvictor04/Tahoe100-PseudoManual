---
symbol: "ERCC1"
type: "gene"
col: 251
ensembl_id: "ENSG00000012061"
name: "ERCC excision repair 1, endonuclease non-catalytic subunit"
location: "19q13.32"
module: 109
arm: "+"
pooled_cpm: 54.35
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# ERCC1

*ERCC excision repair 1, endonuclease non-catalytic subunit* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.82× (z +9.6, q 5e-19, up in 31 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 1.66× (z +3.4, q 0.048, up in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 3.19×, SNU-423 2.92×, Hs 766T 2.51×, A-172 2.37×, …; ⚠ cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 4.23×, KATO III 4.13×, SHP-77 3.71×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW 900 3.40×, NCI-H460 2.58×, A549 2.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.637× (z -6.9, q 3e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR1]] (+0.83, fdr 7e-06), [[MCL1]] (+0.80, fdr 7e-06), [[EGR3]] (+0.75, fdr 7e-06); moves opposite to [[HSF2]] (-0.64, fdr 7e-06), [[FHIP2A]] (-0.60, fdr 1e-05), [[FBXO7]] (-0.60, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ROBO4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 3.19×, SNU-423 2.92×, Hs 766T 2.51×, A-172 2.37×, …; ⚠ cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 4.23×, KATO III 4.13×, SHP-77 3.71×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW 900 3.40×, NCI-H460 2.58×, A549 2.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.6 | 5e-19 | 31/40 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.66×** | +8.4 | 1e-14 | 35/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +7.8 | 9e-13 | 33/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +5.1 | 5e-05 | 23/47 (AsPC-1, SNU-423, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +4.9 | 1e-04 | 22/48 (HOP62, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +4.6 | 4e-04 | 25/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.048 | 17/48 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.4 | 0.048 | 20/47 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.070 | 21/48 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Regorafenib (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.15 | 10/48 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.637×** | -6.9 | 3e-09 | 35/48 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -6.5 | 1e-08 | 33/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.664×** | -6.5 | 1e-08 | 32/47 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.640×** | -6.2 | 9e-08 | 29/49 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -5.7 | 1e-06 | 29/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.730×** | -5.2 | 2e-05 | 28/49 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.734×** | -5.1 | 3e-05 | 25/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.809×** | -4.9 | 8e-05 | 28/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.734×** | -4.8 | 9e-05 | 25/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.819×** | -4.6 | 2e-04 | 26/48 (NCI-H23, RKO, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.751×** | -4.6 | 3e-04 | 24/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.756×** | -4.4 | 4e-04 | 25/47 (hTERT-HPNE, AN3 CA, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.829×** | -4.4 | 6e-04 | 22/48 (RKO, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.770×** | -4.3 | 7e-04 | 21/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.780×** | -4.2 | 0.001 | 23/48 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.832×** | -4.1 | 0.001 | 20/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 17 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.263× (z -37.1) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.192× (z -13.4) |
| [[RKO (line)]] | wt | 173 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.230× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 46.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +9.3) ⚠ cell-cycle shift, explains ~19% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.341× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 61.6 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.646× (z -13.0) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.5) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[PANC-1 (line)]] | alt | 56.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.6) |
| [[A-172 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A549 (line)]] | wt | 74.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 37.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0928× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[C32 (line)]] | wt | 73.6 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.319× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[Hs 766T (line)]] | wt | 47.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.204× (z -11.9) |
| [[KATO III (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.2) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[SW 900 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | +0.83 | +0.85 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MCL1]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[EGR3]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[IER2]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[EGR2]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ASTL]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NABP1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[BTBD19]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.63 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSF2]] | -0.64 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[FHIP2A]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[FBXO7]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FBXO9]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[NPEPPS]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 | STRING 907 |
| [[PAIP1]] | -0.57 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[SNX4]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ZNF148]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ASB7]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MBIP]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO4]] | B | ROBO4 activity raises ERCC1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without ROBO4 | 0.015 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[LINC02934]] | B | LINC02934 activity weakens ERCC1's drug response | lines that do not express LINC02934 (8) vs lines expressing it (41) | the lines without LINC02934 respond 1.47× as strongly (z diff -1.03); strongest at Trametinib 5 µM: 0.45x vs 0.64x (z diff -2.3) | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LAMA1]] | B | LAMA1 activity raises ERCC1's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.28× lower at baseline in the lines without LAMA1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ASTL]] | B | ASTL activity raises ERCC1's level | lines that do not express ASTL (26) vs lines expressing it (24) | 1.21× lower at baseline in the lines without ASTL | 0.078 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent |
| [[LINC02934]] | B | LINC02934 activity lowers ERCC1's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.39× higher at baseline in the lines without LINC02934 | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ERCC1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -0.2); signed map (5.7, 30.1). **Vector** length 124, 35.4% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.61 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.61 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.60 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Proglumide (drug)]] 0.05 µM |  | +2.0 | +0.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.2 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.1 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.1 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.7 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.2 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | ERCC excision repair 1, endonuclease non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,407,334-45,478,828 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAD10 |
| Gene groups (HGNC) | ERCC excision repair associated |
| Hallmark sets | PEROXISOME, DNA_REPAIR |
| Reactome | 12 pathways, smallest: Fanconi Anemia Pathway; HDR through Single Strand Annealing (SSA); Dual Incision in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P07992](https://www.uniprot.org/uniprotkb/P07992) (DNA excision repair protein ERCC-1):

> [Isoform 1]: Non-catalytic component of a structure-specific DNA repair endonuclease responsible for the 5'-incision during DNA repair. Responsible, in conjunction with SLX4, for the first step in the repair of interstrand cross-links (ICL). Participates in the processing of anaphase bridge-generating DNA structures, which consist in incompletely processed DNA lesions arising during S or G2 phase, and can result in cytokinesis failure. Also required for homology-directed repair (HDR) of DNA …

**Summary**, from NCBI Gene [2067](https://www.ncbi.nlm.nih.gov/gene/2067):

> The product of this gene functions in the nucleotide excision repair pathway, and is required for the repair of DNA lesions such as those induced by UV light or formed by electrophilic compounds including cisplatin. The encoded protein forms a heterodimer with the XPF endonuclease (also known as ERCC4), and the heterodimeric endonuclease catalyzes the 5' incision in the process of excising the DNA lesion. The heterodimeric endonuclease is also involved in recombinational DNA repair and in the …

**Accessions** — [HGNC:3433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3433) · Entrez [2067](https://www.ncbi.nlm.nih.gov/gene/2067) · UniProt [P07992](https://www.uniprot.org/uniprotkb/P07992) · Ensembl [ENSG00000012061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012061)

## Data

Gene col 251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 251); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 251]; `tensor/DDL_lfc|DDL_z.npy` [251]; `embed/gene_vectors.npy` [251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 251 or target_col == 251). Every well: [[ERCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
