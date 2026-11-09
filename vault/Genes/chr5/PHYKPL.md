---
symbol: "PHYKPL"
type: "gene"
col: 10592
ensembl_id: "ENSG00000175309"
name: "5-phosphohydroxy-L-lysine phospho-lyase"
location: "5q35.3"
module: 172
arm: "+"
pooled_cpm: 56.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# PHYKPL

*5-phosphohydroxy-L-lysine phospho-lyase* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 1.26× (z +4.6, q 0.002, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.274× (z -25.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.72, fdr 1e-05), [[KEAP1]] (+0.64, fdr 1e-05), [[CCZ1P1]] (+0.63, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.61, fdr 1e-05), [[MYH10]] (-0.56, fdr 2e-05), [[TFRC]] (-0.53, fdr 3e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.26×** | +4.6 | 0.002 | 27/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.006 | 26/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.013 | 23/49 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +3.8 | 0.021 | 25/49 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.6 | 0.036 | 13/48 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.038 | 24/48 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.55× | +3.2 | 0.10 | 20/50 (SW480, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.12 | 20/48 (KATO III, LOX-IMVI, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.25× | +3.1 | 0.13 | 21/47 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.13 | 11/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.13 | 14/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10592.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.274×** | -25.7 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -16.6 | 0e+00 | 47/49 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.329×** | -15.0 | 0e+00 | 44/48 (RPMI-7951, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.346×** | -14.9 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.389×** | -13.2 | 7e-38 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.395×** | -13.0 | 9e-37 | 47/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.414×** | -12.4 | 4e-33 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.444×** | -11.4 | 4e-28 | 44/47 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.446×** | -11.3 | 6e-28 | 42/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.577×** | -7.4 | 7e-12 | 40/47 (PANC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.599×** | -7.2 | 4e-11 | 36/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -6.8 | 6e-10 | 42/48 (HCT15, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.397×** | -6.8 | 6e-10 | 42/49 (SNU-1, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.624×** | -6.6 | 2e-09 | 31/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -6.6 | 2e-09 | 38/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -3.9 | 0.003 | 25/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.018 | 21/48 (SW 900, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.036 | 23/48 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.037 | 23/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.667×** | -3.0 | 0.057 | 17/49 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 56.8 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -29.0) |
| [[PANC-1 (line)]] | alt | 61.8 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -30.2) |
| [[LoVo (line)]] | wt | 102 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -21.9) |
| [[SW480 (line)]] | alt | 53.9 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -20.0) |
| [[KATO III (line)]] | alt | 64.8 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.1) |
| [[LS 180 (line)]] | wt | 71.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -28.1) |
| [[SW48 (line)]] | wt | 65.2 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 78.7 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 50.0 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -23.6) |
| [[NCI-H1573 (line)]] | alt | 58.8 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -27.3) |
| [[RKO (line)]] | wt | 59.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.2) |
| [[A549 (line)]] | wt | 42.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -19.8) |
| [[AsPC-1 (line)]] | alt | 50.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -16.8) |
| [[COLO 205 (line)]] | alt | 110 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -26.8) |
| [[H4 (line)]] | wt | 72.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 96.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.8) |
| [[NCI-H1792 (line)]] | alt | 43.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -15.2) |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -19.3) |
| [[SNU-1 (line)]] | wt | 82.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -16.4) |
| [[SW 900 (line)]] | alt | 74.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.6) |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.0) |
| [[HCT15 (line)]] | alt | 91.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.6) |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.2) |
| [[HT-29 (line)]] | alt | 54.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 51.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 79.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0160× (z -26.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.5) |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.4) |
| [[A-172 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.6) |
| [[A498 (line)]] | wt | 36.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 56.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.1) |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.4) |
| [[A-427 (line)]] | wt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.6) |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.8) |
| [[C-33 A (line)]] | alt | 62.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.6) |
| [[C32 (line)]] | wt | 25.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.210× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.7) |
| [[Hs 766T (line)]] | wt | 57.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.3) |
| [[J82 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0801× (z -10.9) |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0784× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.72 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[KEAP1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CCZ1P1]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[WDR81]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TEFM]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[HEXD]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHM2]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[N4BP2L2]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[C19orf12]] | +0.58 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[NUTM2A-AS1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.61 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[MYH10]] | -0.56 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TFRC]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[IDH2]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ECT2]] | -0.49 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MDH1]] | -0.49 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[EXTL2]] | -0.49 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[DPYSL2]] | -0.48 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TMEM106C]] | -0.48 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[PTGS1]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ETV1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[COL13A1]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 | pathway: Collagen degradation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity lowers PHYKPL's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.9, 12.0); signed map (-7.8, -19.3). **Vector** length 74.3, 21.4% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.7 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.6 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.4 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -16.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | 5-phosphohydroxy-L-lysine phospho-lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,208,471-178,232,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15875; previously AGXT2L2 |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Reactome | 5 pathways, smallest: Lysine catabolism; Collagen degradation; Degradation of the extracellular matrix |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUZ5](https://www.uniprot.org/uniprotkb/Q8IUZ5) (5-phosphohydroxy-L-lysine phospho-lyase):

> Catalyzes the pyridoxal-phosphate-dependent breakdown of 5-phosphohydroxy-L-lysine, converting it to ammonia, inorganic phosphate and 2-aminoadipate semialdehyde.

**Summary**, from NCBI Gene [85007](https://www.ncbi.nlm.nih.gov/gene/85007):

> This is a nuclear gene encoding a mitochondrial enzyme that catalyzes the conversion of 5-phosphonooxy-L-lysine to ammonia, inorganic phosphate, and 2-aminoadipate semialdehyde. Mutations in this gene may cause phosphohydroxylysinuria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:28249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28249) · Entrez [85007](https://www.ncbi.nlm.nih.gov/gene/85007) · UniProt [Q8IUZ5](https://www.uniprot.org/uniprotkb/Q8IUZ5) · Ensembl [ENSG00000175309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175309)

## Data

Gene col 10592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10592); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10592]; `tensor/DDL_lfc|DDL_z.npy` [10592]; `embed/gene_vectors.npy` [10592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10592 or target_col == 10592). Every well: [[PHYKPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHYKPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
