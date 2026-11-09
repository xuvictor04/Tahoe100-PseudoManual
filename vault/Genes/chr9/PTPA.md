---
symbol: "PTPA"
type: "gene"
col: 4057
ensembl_id: "ENSG00000119383"
name: "protein phosphatase 2 phosphatase activator"
location: "9q34.11"
module: 43
arm: "-"
pooled_cpm: 36.0
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# PTPA

*protein phosphatase 2 phosphatase activator* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +15.3, q 0e+00, up in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.22× (z +3.3, q 0.092, up in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-427 5.58×, A498 2.80×, A-172 3.23×, LoVo 3.65×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 3.81×, Hs 766T 4.16×, SW480 2.64×, NCI-H1792 5.13×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.471× (z -13.6, q 4e-39, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPL]] (+0.62, fdr 1e-05), [[ZMYM3]] (+0.60, fdr 1e-05), [[RAB1B]] (+0.59, fdr 4e-05); moves opposite to [[RPL23]] (-0.60, fdr 2e-05), [[RPL18]] (-0.60, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[ATP5MK]] (-0.59, fdr 3e-05), [[SF3B6]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-427 5.58×, A498 2.80×, A-172 3.23×, LoVo 3.65×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 3.81×, Hs 766T 4.16×, SW480 2.64×, NCI-H1792 5.13×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +15.3 | 0e+00 | 38/47 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +14.5 | 1e-45 | 36/37 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +7.2 | 1e-10 | 24/43 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.31×** | +4.9 | 1e-04 | 24/46 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.092 | 17/47 (A-172, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.1 | 0.17 | 0/48 | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.20 | 11/48 (AsPC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.471×** | -13.6 | 4e-39 | 45/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.481×** | -13.2 | 2e-37 | 47/48 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -12.4 | 5e-33 | 45/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -7.3 | 6e-11 | 26/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.674×** | -6.9 | 6e-10 | 30/48 (A-427, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -6.4 | 1e-08 | 33/48 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -5.4 | 6e-06 | 26/48 (C32, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.595×** | -4.9 | 7e-05 | 24/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -4.7 | 1e-04 | 25/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.7 | 1e-04 | 20/48 (C-33 A, SW48, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -4.7 | 2e-04 | 22/47 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.785×** | -4.4 | 6e-04 | 21/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.665×** | -3.8 | 0.005 | 19/43 (KATO III, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.011 | 20/48 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.867× | -3.6 | 0.011 | 13/48 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.012 | 20/47 (LOX-IMVI, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.821×** | -3.6 | 0.013 | 20/48 (KATO III, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -19.6) |
| [[SW480 (line)]] | alt | 39.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.391× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 52.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -12.9) |
| [[C32 (line)]] | wt | 108 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -12.6) |
| [[HOP62 (line)]] | alt | 35.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -9.5) |
| [[SW48 (line)]] | wt | 47.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.200× (z -11.2) |
| [[A-427 (line)]] | wt | 21.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -12.0) |
| [[A498 (line)]] | wt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 68.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -9.4) |
| [[Hs 766T (line)]] | wt | 43.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.16× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.2) |
| [[HS-578T (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.5) |
| [[KATO III (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 37.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +11.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 33.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -8.8) |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -10.8) |
| [[H4 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.429× (z -8.9) |
| [[RKO (line)]] | wt | 71.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -9.5) |
| [[SHP-77 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | +0.62 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ZMYM3]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.59 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[POMK]] | +0.58 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[USP22]] | +0.58 | +0.49 / +0.54 | both halves | 2e-05 |  |
| [[PNPO]] | +0.57 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MAN2A2]] | +0.57 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CILK1]] | +0.56 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[CAPRIN1]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[HFE]] | +0.55 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ZNF532]] | +0.54 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[TMPO]] | +0.54 | +0.55 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL23]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[RPL18]] ⚠ | -0.60 | -0.52 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SF3B6]] | -0.59 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RPL26]] | -0.59 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[RPL35]] ⚠ | -0.58 | -0.45 / -0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | -0.58 | -0.53 / -0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | -0.58 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[RPL9]] ⚠ | -0.58 | -0.47 / -0.55 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.57 | -0.47 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | -0.57 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[COMMD6]] | -0.56 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[RPS8]] | -0.56 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[RPS14]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RPL31]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RPL34]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCRN1]] | B | SCRN1 activity lowers PTPA's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without SCRN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **-** arm (projection on the module's main direction -0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.0, -25.9); signed map (-11.1, -36.4). **Vector** length 65.2, 11.8% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -2.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | +2.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +0.1 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 phosphatase activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,110,950-129,148,946 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PR53; previously PPP2R4 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; Protein phosphatase 2 modulatory subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15257](https://www.uniprot.org/uniprotkb/Q15257) (Serine/threonine-protein phosphatase 2A activator):

> PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (By similarity). Acts as a regulatory subunit for serine/threonine-protein phosphatase 2A (PP2A). Modulates PP2A activity or substrate specificity, probably by inducing a conformational change in the catalytic subunit, a proposed direct target of the PPIase. Can reactivate inactive phosphatase PP2A-phosphatase methylesterase complexes (PP2A(i)) in presence of ATP …

**Summary**, from NCBI Gene [5524](https://www.ncbi.nlm.nih.gov/gene/5524):

> Protein phosphatase 2A (PP2A) is one of the four major Ser/Thr phosphatases and is implicated in the negative control of cell growth and division. The core PP2A holoenzyme is a heterotrimer of a structural A subunit, a catalytic C subunit, and one of several regulatory B subunits, which are grouped into distinct families (B/PR55, B'/PR61, B''/PR72) that confer different substrate specificities and localizations. This gene, PTPA, does not encode one of these conventional B-type regulatory …

**Accessions** — [HGNC:9308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9308) · Entrez [5524](https://www.ncbi.nlm.nih.gov/gene/5524) · UniProt [Q15257](https://www.uniprot.org/uniprotkb/Q15257) · Ensembl [ENSG00000119383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119383)

## Data

Gene col 4057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4057); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4057]; `tensor/DDL_lfc|DDL_z.npy` [4057]; `embed/gene_vectors.npy` [4057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4057 or target_col == 4057). Every well: [[PTPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
