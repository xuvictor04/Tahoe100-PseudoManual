---
symbol: "DDR1"
type: "gene"
col: 12894
ensembl_id: "ENSG00000204580"
name: "discoidin domain receptor tyrosine kinase 1"
location: "6p21.33"
module: 14
arm: "+"
pooled_cpm: 27.14
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 18
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# DDR1

*discoidin domain receptor tyrosine kinase 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +7.2, q 3e-10, up in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.34× (z +6.2, q 1e-07, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.569× (z -8.5, q 1e-14, down in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.640× (z -6.7, q 2e-09, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF14]] (+0.67, fdr 7e-06), [[HCN3]] (+0.66, fdr 7e-06), [[ANO9]] (+0.65, fdr 7e-06); moves opposite to [[CUTC]] (-0.54, fdr 3e-05), [[ZNF544]] (-0.51, fdr 2e-05), [[DAP3]] (-0.51, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); 18 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.2 | 3e-10 | 30/39 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.2 | 1e-07 | 23/45 (LS 180, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.8 | 1e-06 | 17/32 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.7 | 2e-06 | 17/36 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 3e-04 | 19/43 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.7 | 3e-04 | 20/39 (NCI-H2030, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.006 | 16/42 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.008 | 13/44 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.8 | 0.008 | 8/24 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.008 | 15/42 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.8 | 0.008 | 2/45 (MIA PaCa-2, HOP62) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.034 | 16/45 (MIA PaCa-2, Hs 766T, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.037 | 7/42 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.24×** | +3.2 | 0.048 | 14/44 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.1 | 0.063 | 6/34 (A498, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.569×** | -8.5 | 1e-14 | 32/45 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.591×** | -7.9 | 6e-13 | 33/44 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.595×** | -7.8 | 9e-13 | 33/45 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -6.7 | 2e-09 | 26/44 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -5.8 | 8e-07 | 27/43 (SW48, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -5.8 | 8e-07 | 25/44 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -5.0 | 6e-05 | 23/43 (HepG2/C3A, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -4.6 | 2e-04 | 23/45 (SW480, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.741×** | -4.5 | 4e-04 | 18/43 (SW48, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.748×** | -4.4 | 6e-04 | 20/44 (SW48, LoVo, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.749×** | -4.2 | 0.001 | 21/43 (SHP-77, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.761×** | -4.1 | 0.002 | 17/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.775×** | -3.9 | 0.005 | 18/45 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.770×** | -3.8 | 0.006 | 20/40 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.788×** | -3.6 | 0.012 | 14/43 (SW480, J82, …) | all doses, flat | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.047 | 9/43 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.069 | 12/45 (LoVo, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.0 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -13.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 75.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -10.7) |
| [[LoVo (line)]] | wt | 47.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -11.8) |
| [[PANC-1 (line)]] | alt | 20.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 59.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.6) ⚠ cell-cycle shift, explains ~15% of this change | [[Auranofin (drug)]] 5 µM 0.269× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.61 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +9.9) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[J82 (line)]] | alt | 7.70 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +14.9) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[LS 180 (line)]] | wt | 50.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.0) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.95× (z +11.3) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 46.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.5) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[SW1417 (line)]] | alt | 70.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -10.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.6) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[CFPAC-1 (line)]] | alt | 64.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -9.4) |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |
| [[HCN3]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ANO9]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[EFNA1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MVP-DT]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[BMF]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[BCL3]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | same gene group |
| [[TNFAIP2]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PLXNB2]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CGNL1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[COL16A1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[TMPRSS3]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTC]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF544]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[DAP3]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TRIM27]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[RUSC2]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ST3GAL3]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 | same gene group |
| [[GPR89A]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[MPP3]] | -0.48 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PRKAG1]] | -0.48 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[SMYD2]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MAP2K1]] | -0.47 | -0.35 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises DDR1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without ANO9 | 0.003 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises DDR1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without TMPRSS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ELF3]] | B | ELF3 activity raises DDR1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without ELF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises DDR1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without ELF3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity raises DDR1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without EFNA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises DDR1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without TNFRSF14-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[USP43]] | B | USP43 activity raises DDR1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without USP43 | 0.096 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | C | DDR1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.38× the cells of the other lines | 0.009 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | DDR1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.54× the cells of the other lines | 0.012 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[BCL3]] | C | DDR1 activity raises BCL3's level | lines that do not express DDR1 (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without DDR1 | 0.016 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | DDR1 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 1.36× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Pimozide (drug)]] 0.5 µM | C | DDR1 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.70× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.5 µM | C | DDR1 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.18× the cells of the other lines | 0.032 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | C | DDR1 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.27× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | DDR1 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.71× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | C | DDR1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.20× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[LGALS3]] | C | DDR1 activity raises LGALS3's level | lines that do not express DDR1 (3) vs lines expressing it (47) | 6.31× lower at baseline in the lines without DDR1 | 0.047 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | DDR1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 1.37× the cells of the other lines | 0.049 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | C | DDR1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.33× the cells of the other lines | 0.074 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 3.4); signed map (46.3, 7.5). **Vector** length 107, 26.4% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.3 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.5 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.2 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | discoidin domain receptor tyrosine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,876,421-30,900,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RTK6, CD167; previously NTRK4, PTK3A, NEP, CAK, EDDR1 |
| Gene groups (HGNC) | CD molecules; MicroRNA protein coding host genes; Discoidin domain receptor tyrosine kinase family |
| Reactome | 2 pathways, smallest: Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08345](https://www.uniprot.org/uniprotkb/Q08345) (Epithelial discoidin domain-containing receptor 1):

> Tyrosine kinase that functions as a cell surface receptor for fibrillar collagen and regulates cell attachment to the extracellular matrix, remodeling of the extracellular matrix, cell migration, differentiation, survival and cell proliferation. Collagen binding triggers a signaling pathway that involves SRC and leads to the activation of MAP kinases. Regulates remodeling of the extracellular matrix by up-regulation of the matrix metalloproteinases MMP2, MMP7 and MMP9, and thereby facilitates …

**Summary**, from NCBI Gene [780](https://www.ncbi.nlm.nih.gov/gene/780):

> Receptor tyrosine kinases play a key role in the communication of cells with their microenvironment. These kinases are involved in the regulation of cell growth, differentiation and metabolism. The protein encoded by this gene belongs to a subfamily of tyrosine kinase receptors with homology to Dictyostelium discoideum protein discoidin I in their extracellular domain, and that are activated by various types of collagen. Expression of this protein is restricted to epithelial cells, particularly …

**Accessions** — [HGNC:2730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2730) · Entrez [780](https://www.ncbi.nlm.nih.gov/gene/780) · UniProt [Q08345](https://www.uniprot.org/uniprotkb/Q08345) · Ensembl [ENSG00000204580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204580)

## Data

Gene col 12894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12894); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12894]; `tensor/DDL_lfc|DDL_z.npy` [12894]; `embed/gene_vectors.npy` [12894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12894 or target_col == 12894). Every well: [[DDR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
