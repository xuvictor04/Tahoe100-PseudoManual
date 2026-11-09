---
symbol: "CCDC92"
type: "gene"
col: 4047
ensembl_id: "ENSG00000119242"
name: "coiled-coil domain containing 92"
location: "12q24.31"
module: 15
arm: "+"
pooled_cpm: 38.78
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CCDC92

*coiled-coil domain containing 92* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 1.30× (z +6.2, q 3e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.447× (z -13.1, q 2e-36, down in 40 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.537× (z -10.1, q 1e-21, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM228B]] (+0.56, fdr 1e-05), [[APLF]] (+0.53, fdr 3e-05), [[ZNNT1]] (+0.53, fdr 1e-05); moves opposite to [[CDKAL1]] (-0.53, fdr 1e-05), [[RAD54B]] (-0.52, fdr 2e-05), [[MIR924HG]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +6.2 | 3e-07 | 32/48 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.1 | 3e-07 | 28/48 (SW1417, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +5.4 | 1e-05 | 31/47 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +4.8 | 2e-04 | 25/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 3e-04 | 23/47 (SW480, H4, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.003 | 18/48 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +4.0 | 0.005 | 22/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.005 | 19/47 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.8 | 0.008 | 12/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.013 | 15/48 (SW480, NCI-H2030, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.018 | 17/48 (A498, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.018 | 15/48 (A498, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.041 | 14/48 (C-33 A, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.068 | 11/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.447×** | -13.1 | 2e-36 | 40/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -10.1 | 1e-21 | 35/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -8.5 | 4e-15 | 37/49 (NCI-H23, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.594×** | -8.5 | 4e-15 | 35/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -7.9 | 2e-13 | 33/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.640×** | -7.3 | 4e-11 | 32/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.652×** | -7.0 | 3e-10 | 30/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.639×** | -6.9 | 4e-10 | 32/48 (A549, A-172, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.473×** | -6.4 | 1e-08 | 29/43 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.671×** | -6.2 | 4e-08 | 27/46 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -5.9 | 2e-07 | 31/47 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.717×** | -5.1 | 2e-05 | 25/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.760×** | -4.5 | 4e-04 | 20/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -4.3 | 6e-04 | 26/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.766×** | -4.3 | 6e-04 | 23/48 (BT-474, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.737×** | -3.5 | 0.013 | 15/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.028 | 21/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.039 | 18/48 (SW480, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.706×** | -3.0 | 0.082 | 15/48 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 82.3 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -10.5) |
| [[PANC-1 (line)]] | alt | 59.5 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.334× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 71.6 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 85.2 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.325× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 40.6 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.276× (z -12.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.405× (z -8.5) |
| [[SW480 (line)]] | alt | 28.1 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -9.8) |
| [[A-172 (line)]] | wt | 60.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 53.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.429× (z -9.4) |
| [[LoVo (line)]] | wt | 34.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.328× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 37.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 66.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 45.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -10.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[C-33 A (line)]] | alt | 66.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HS-578T (line)]] | alt | 57.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.356× (z -8.5) |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -8.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0945× (z -8.8) |
| [[RKO (line)]] | wt | 12.9 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.138× (z -8.8) |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM228B]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[APLF]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ZNNT1]] | +0.53 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TMCO3]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SLC30A4]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KCTD13]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[HGSNAT]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[C14orf28]] | +0.50 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[TCP11L1]] | +0.50 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[UPP2]] | +0.49 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF706]] | +0.49 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[UGDH-AS1]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKAL1]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RAD54B]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[MIR924HG]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SHMT1]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TTLL5]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[RTTN]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[USP54]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[FSBP]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[CSTF2]] | -0.48 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SLC19A3]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[PRIM2]] | -0.47 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[HAUS1]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.315). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.8, 21.9); signed map (11.6, 1.6). **Vector** length 87.7, 21.1% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.6 | +4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +4.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -7.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -5.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.9 | -6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 92 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,918,660-123,972,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22471 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HC0](https://www.uniprot.org/uniprotkb/Q53HC0) (Coiled-coil domain-containing protein 92):

> Interferon-stimulated protein that plays a role in innate immunity. Strongly inhibits ebolavirus transcription and replication. Forms a complex with viral RNA-bound nucleocapsid NP and thereby prevents the transport of NP to the cell surface.

**Summary**, from NCBI Gene [80212](https://www.ncbi.nlm.nih.gov/gene/80212):

> Enables identical protein binding activity. Predicted to be involved in innate immune response and regulation of defense response to virus. Predicted to act upstream of or within several processes, including NLRP3 inflammasome complex assembly; connective tissue replacement involved in inflammatory response wound healing; and macrophage migration. Located in centriole and centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29563) · Entrez [80212](https://www.ncbi.nlm.nih.gov/gene/80212) · UniProt [Q53HC0](https://www.uniprot.org/uniprotkb/Q53HC0) · Ensembl [ENSG00000119242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119242)

## Data

Gene col 4047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4047); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4047]; `tensor/DDL_lfc|DDL_z.npy` [4047]; `embed/gene_vectors.npy` [4047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4047 or target_col == 4047). Every well: [[CCDC92 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC92.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
