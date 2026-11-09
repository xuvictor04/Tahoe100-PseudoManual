---
symbol: "SLC12A6"
type: "gene"
col: 6377
ensembl_id: "ENSG00000140199"
name: "solute carrier family 12 member 6"
location: "15q14"
module: 34
arm: "+"
pooled_cpm: 57.25
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SLC12A6

*solute carrier family 12 member 6* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +10.0, q 1e-20, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.594× (z -10.1, q 4e-21, down in 34 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.660× (z -4.2, q 0.002, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG9B]] (+0.54, fdr 5e-05), [[MOSPD1]] (+0.54, fdr 4e-05), [[ATP6V1D]] (+0.52, fdr 1e-05); moves opposite to [[PMS1]] (-0.46, fdr 2e-04), [[ATL2]] (-0.46, fdr 4e-05), [[TTF2]] (-0.45, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAST4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +10.0 | 1e-20 | 33/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +9.5 | 6e-19 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.0 | 6e-17 | 33/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.6 | 4e-12 | 28/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.28×** | +6.7 | 3e-09 | 26/48 (LoVo, A-427, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.5 | 7e-04 | 18/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 23/47 (NCI-H460, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.1 | 0.003 | 23/49 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.004 | 21/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.011 | 16/49 (A-427, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.011 | 15/49 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.022 | 14/48 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.594×** | -10.1 | 4e-21 | 34/47 (SNU-423, SNU-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.629×** | -8.6 | 2e-15 | 36/47 (SK-MEL-2, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.650×** | -8.3 | 2e-14 | 33/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -8.2 | 4e-14 | 36/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.707×** | -6.7 | 2e-09 | 33/47 (SNU-423, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.718×** | -6.4 | 2e-08 | 28/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.741×** | -5.8 | 5e-07 | 26/48 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.749×** | -5.6 | 2e-06 | 27/48 (H4, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.756×** | -5.4 | 4e-06 | 25/47 (SW 1271, SW480, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.660×** | -4.2 | 0.002 | 22/47 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.672×** | -4.0 | 0.003 | 19/48 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.676×** | -4.0 | 0.004 | 17/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.821×** | -3.8 | 0.006 | 21/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.830×** | -3.5 | 0.021 | 22/48 (NCI-H1792, H4, …) | two highest doses | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.028 | 17/47 (Hs 766T, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.028 | 16/49 (SK-MEL-2, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.2 | 0.041 | 19/48 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.851× | -2.9 | 0.083 | 9/47 (HOP62, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.811×** | -2.9 | 0.092 | 6/49 (Hs 766T, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -2.9 | 0.095 | 9/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.863× | -2.9 | 0.095 | 15/47 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | 0.863× | -2.8 | 0.095 | 15/48 (SW 1088, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 91.7 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[PANC-1 (line)]] | alt | 61.0 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.55× (z +10.6) | — |
| [[SW480 (line)]] | alt | 56.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.391× (z -11.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 66.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.68× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 5 µM 0.0412× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 23.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 69.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0909× (z -10.1) |
| [[Hs 766T (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -13.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.286× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.329× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 51.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 54.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 77.8 | 1 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.69× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 83.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.24× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H2030 (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.370× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.193× (z -8.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW 1271 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0717× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW1417 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[A-172 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG9B]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[MOSPD1]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ATP6V1D]] | +0.52 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RNF11]] | +0.51 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[ZNF611]] | +0.48 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[GDI1]] | +0.48 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[CREBL2]] | +0.46 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[JMJD1C]] | +0.46 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNF165]] | +0.46 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[TMCC3]] | +0.46 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[F11R]] | +0.46 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[UBL3]] | +0.45 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS1]] | -0.46 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[ATL2]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[TTF2]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.45 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[HNRNPF]] | -0.44 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[CDCA7]] | -0.44 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC1]] | -0.44 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[MCM6]] | -0.43 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PRMT1]] | -0.43 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[FANCC]] | -0.43 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[EXOSC7]] | -0.42 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[TDRD3]] | -0.42 | -0.29 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST4]] | B | MAST4 activity raises SLC12A6's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without MAST4 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -54.0); signed map (-13.6, 15.5). **Vector** length 97.4, 24.6% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.4 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.0 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.1 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.9 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -3.7 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,229,784-34,338,060 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCC3A, KCC3B; previously KCC3, ACCPN |
| Gene groups (HGNC) | Solute carrier family 12 |
| Reactome | 6 pathways, smallest: Cation-coupled Chloride cotransporters; SLC-mediated transport of inorganic anions; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHW9](https://www.uniprot.org/uniprotkb/Q9UHW9) (Solute carrier family 12 member 6):

> [Isoform 1]: Mediates electroneutral potassium-chloride cotransport when activated by cell swelling. May contribute to cell volume homeostasis in single cells.; [Isoform 2]: Mediates electroneutral potassium-chloride cotransport when activated by cell swelling. May contribute to cell volume homeostasis in single cells (Probable).; [Isoform 3]: Mediates electroneutral potassium-chloride cotransport when activated by cell swelling. May contribute to cell volume homeostasis in single cells …

**Summary**, from NCBI Gene [9990](https://www.ncbi.nlm.nih.gov/gene/9990):

> This gene is a member of the K-Cl cotransporter (KCC) family. K-Cl cotransporters are integral membrane proteins that lower intracellular chloride concentrations below the electrochemical equilibrium potential. The proteins encoded by this gene are activated by cell swelling induced by hypotonic conditions. Alternate splicing results in multiple transcript variants encoding different isoforms. Mutations in this gene are associated with agenesis of the corpus callosum with peripheral neuropathy. …

**Accessions** — [HGNC:10914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10914) · Entrez [9990](https://www.ncbi.nlm.nih.gov/gene/9990) · UniProt [Q9UHW9](https://www.uniprot.org/uniprotkb/Q9UHW9) · Ensembl [ENSG00000140199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140199)

## Data

Gene col 6377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6377); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6377]; `tensor/DDL_lfc|DDL_z.npy` [6377]; `embed/gene_vectors.npy` [6377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6377 or target_col == 6377). Every well: [[SLC12A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
