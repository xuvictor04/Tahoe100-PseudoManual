---
symbol: "IKZF5"
type: "gene"
col: 1749
ensembl_id: "ENSG00000095574"
name: "IKAROS family zinc finger 5"
location: "10q26.13"
module: 187
arm: "+"
pooled_cpm: 36.96
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 24
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# IKZF5

*IKAROS family zinc finger 5* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +14.5, q 6e-45, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.448× (z -12.2, q 3e-31, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.421× (z -6.9, q 1e-09, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR48]] (+0.73, fdr 7e-06), [[HBP1]] (+0.67, fdr 1e-05), [[UBXN6]] (+0.66, fdr 8e-06); moves opposite to [[BRI3BP]] (-0.54, fdr 1e-05), [[RNGTT]] (-0.52, fdr 2e-05), [[LYAR]] (-0.52, fdr 1e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +14.5 | 6e-45 | 43/48 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +14.3 | 1e-43 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.2 | 7e-18 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +8.6 | 9e-16 | 39/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +8.3 | 1e-14 | 43/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +8.3 | 1e-14 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.9 | 2e-13 | 42/48 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 3e-11 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +6.9 | 4e-10 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 30/48 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 25/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.3 | 8e-04 | 20/49 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.004 | 20/48 (PANC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.015 | 20/47 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.031 | 12/47 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.054 | 14/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.448×** | -12.2 | 3e-31 | 48/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.545×** | -9.2 | 1e-17 | 34/48 (A-427, C-33 A, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.558×** | -8.5 | 3e-15 | 30/38 (A549, H4, …) | two highest doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.421×** | -6.9 | 1e-09 | 37/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.459×** | -6.2 | 8e-08 | 34/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.467×** | -6.0 | 2e-07 | 35/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.470×** | -6.0 | 2e-07 | 32/48 (HEC-1-A, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.534×** | -5.0 | 5e-05 | 29/48 (HCT15, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.746×** | -4.4 | 6e-04 | 24/48 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -4.2 | 0.002 | 23/48 (SNU-423, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.707×** | -3.7 | 0.010 | 20/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.836× | -3.6 | 0.012 | 18/48 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.632×** | -3.6 | 0.012 | 17/46 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.797×** | -3.5 | 0.023 | 17/48 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.024 | 11/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.030 | 17/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.040 | 13/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.743×** | -3.2 | 0.044 | 16/48 (HepG2/C3A, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.814×** | -3.1 | 0.052 | 15/49 (A498, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 37.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -8.9) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 39.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -8.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 41.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 51.3 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 33.8 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.44× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 38.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 31.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 26.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0474× (z -11.6) |
| [[LoVo (line)]] | wt | 36.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 36.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 2 (1 ⚠) | — | [[Pralsetinib (drug)]] 5 µM 0.0710× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 43.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 35.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 44.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -11.4) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 54.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0710× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 29.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0877× (z -13.8) |
| [[SNU-423 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR48]] | +0.73 | +0.62 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[HBP1]] | +0.67 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.66 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[RXRB]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EAPP]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[KLHDC2]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[CREBRF]] | +0.63 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[CCDC28A]] | +0.62 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[CCDC186]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[AKAP9]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3BP]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RNGTT]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[LYAR]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PA2G4]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[EIF4G1]] | -0.49 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EBNA1BP2]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.5, -46.3); signed map (-15.9, 8.8). **Vector** length 84.0, 21.2% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +8.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.0 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | -0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.6 | -12.2 |
|  | [[EX229 (drug)]] 5 µM |  | -6.5 | -6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.1 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.9 | -6.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | IKAROS family zinc finger 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,990,807-123,008,812 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Pegasus, FLJ22973; previously ZNFN1A5 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5V7](https://www.uniprot.org/uniprotkb/Q9H5V7) (Zinc finger protein Pegasus):

> Transcriptional repressor that binds the core 5'GNNTGTNG-3' DNA consensus sequence. Involved in megakaryocyte differentiation.

**Summary**, from NCBI Gene [64376](https://www.ncbi.nlm.nih.gov/gene/64376):

> Members of the Ikaros (ZNFN1A1; MIM 603023) family of transcription factors, which includes Pegasus, are expressed in lymphocytes and are implicated in the control of lymphoid development.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:14283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14283) · Entrez [64376](https://www.ncbi.nlm.nih.gov/gene/64376) · UniProt [Q9H5V7](https://www.uniprot.org/uniprotkb/Q9H5V7) · Ensembl [ENSG00000095574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095574)

## Data

Gene col 1749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1749); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1749]; `tensor/DDL_lfc|DDL_z.npy` [1749]; `embed/gene_vectors.npy` [1749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1749 or target_col == 1749). Every well: [[IKZF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKZF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
