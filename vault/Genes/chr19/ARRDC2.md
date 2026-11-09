---
symbol: "ARRDC2"
type: "gene"
col: 2634
ensembl_id: "ENSG00000105643"
name: "arrestin domain containing 2"
location: "19p13.11"
module: 29
arm: "-"
pooled_cpm: 18.44
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ARRDC2

*arrestin domain containing 2* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +9.8, q 4e-20, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.532× (z -9.2, q 3e-17, down in 17 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.500× (z -4.5, q 4e-04, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM265]] (+0.69, fdr 7e-06), [[IRX3]] (+0.67, fdr 1e-05), [[SNHG11]] (+0.66, fdr 9e-06); moves opposite to [[UGGT1]] (-0.62, fdr 1e-05), [[BANF1]] (-0.61, fdr 1e-05), [[TMEM30A]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +9.8 | 4e-20 | 29/47 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +8.2 | 8e-14 | 27/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 9e-08 | 23/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 23/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.63×** | +5.3 | 2e-05 | 20/47 (PANC-1, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.2 | 2e-05 | 19/41 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.9 | 8e-05 | 17/42 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 2e-04 | 21/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 8e-04 | 15/43 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.016 | 10/45 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.021 | 8/44 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.022 | 11/43 (HS-578T, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.4 | 0.033 | 10/48 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.034 | 13/43 (A498, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.057 | 8/47 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.057 | 6/47 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.058 | 5/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.066 | 5/46 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.532×** | -9.2 | 3e-17 | 17/27 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.590×** | -8.0 | 4e-13 | 23/37 (CFPAC-1, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.569×** | -7.9 | 7e-13 | 19/29 (NCI-H2347, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.668×** | -6.1 | 1e-07 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.683×** | -5.8 | 8e-07 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.731×** | -4.7 | 2e-04 | 19/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.722×** | -4.7 | 2e-04 | 22/48 (A-172, Panc 03.27, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.500×** | -4.5 | 4e-04 | 17/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.752×** | -4.3 | 0.001 | 17/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.717×** | -3.6 | 0.018 | 7/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.793×** | -3.5 | 0.023 | 13/47 (SW 900, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.811×** | -3.2 | 0.070 | 14/45 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.626×** | -3.1 | 0.089 | 10/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.089 | 11/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.805×** | -3.0 | 0.089 | 8/47 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.5 | 2 | 5 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 5.44× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.1) ⚠ cell-cycle shift, explains ~92% of this change |
| [[CFPAC-1 (line)]] | alt | 52.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 69.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0805× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 29.2 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 3 | — | [[Neratinib (drug)]] 0.05 µM 0.0916× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 10.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +10.5) | [[Pemetrexed (drug)]] 0.05 µM 0.0531× (z -10.8) |
| [[A-427 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -9.1) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A498 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0852× (z -8.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 6.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +8.8) | — |
| [[LoVo (line)]] | wt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -9.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM265]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[IRX3]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.66 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PIM3]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SEMA4C]] | +0.61 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[NFKBIL1]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[RCE1]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PNRC1]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CBX4]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[POLR1H]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGGT1]] | -0.62 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[BANF1]] | -0.61 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[OPA1]] | -0.59 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[PRDX3]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TMX1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PIGK]] | -0.57 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[PSMD2]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-32.4, 19.4); signed map (-2.0, 14.2). **Vector** length 93.6, 19.0% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.3 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.7 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.7 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.7 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | arrestin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,001,132-18,014,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLONE24945, PP2703 |
| Gene groups (HGNC) | Alpha arrestins |
| Matched by | ensembl_id |

UniProt [Q8TBH0](https://www.uniprot.org/uniprotkb/Q8TBH0) carries no function annotation.

**Summary**, from NCBI Gene [27106](https://www.ncbi.nlm.nih.gov/gene/27106):

> Predicted to enable molecular adaptor activity. Predicted to act upstream of or within myotube differentiation; response to mechanical stimulus; and skeletal muscle tissue development. Located in cytoplasmic vesicle and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25225) · Entrez [27106](https://www.ncbi.nlm.nih.gov/gene/27106) · UniProt [Q8TBH0](https://www.uniprot.org/uniprotkb/Q8TBH0) · Ensembl [ENSG00000105643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105643)

## Data

Gene col 2634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2634); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2634]; `tensor/DDL_lfc|DDL_z.npy` [2634]; `embed/gene_vectors.npy` [2634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2634 or target_col == 2634). Every well: [[ARRDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
