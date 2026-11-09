---
symbol: "TRIM9"
type: "gene"
col: 1976
ensembl_id: "ENSG00000100505"
name: "tripartite motif containing 9"
location: "14q22.1"
module: 152
arm: "+"
pooled_cpm: 34.1
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 39
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 17
direction_downstream: 25
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# TRIM9

*tripartite motif containing 9* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.99× (z +14.4, q 2e-44, up in 25 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.362× (z -15.1, q 0e+00, down in 29 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL4]] (+0.64, fdr 7e-06), [[KCNK3]] (+0.63, fdr 1e-05), [[SFRP1]] (+0.62, fdr 5e-05); moves opposite to [[RNF146]] (-0.53, fdr 5e-05), [[NEXN]] (-0.53, fdr 5e-05), [[ENTPD3-AS1]] (-0.53, fdr 6e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[SGIP1]] → it (grade B ⚠); 25 go from it, the strongest it → [[FZD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +14.4 | 2e-44 | 25/32 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.46×** | +13.3 | 4e-38 | 24/32 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.15×** | +11.4 | 1e-27 | 24/32 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.97×** | +10.1 | 7e-22 | 21/32 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +9.5 | 3e-19 | 21/32 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +8.1 | 5e-14 | 19/32 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +5.4 | 7e-06 | 14/32 (J82, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +4.2 | 0.002 | 13/31 (SW 900, PANC-1, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.039 | 11/32 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.051 | 4/33 (A549, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.082 | 6/32 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.082 | 10/31 (A549, PANC-1, …) | top dose only |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.099 | 4/32 (C32, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.362×** | -15.1 | 0e+00 | 29/32 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -15.1 | 0e+00 | 24/32 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -14.8 | 0e+00 | 27/31 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.472×** | -11.1 | 1e-26 | 25/32 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -10.9 | 1e-25 | 26/32 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -10.4 | 3e-23 | 23/29 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.550×** | -8.9 | 6e-17 | 23/32 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.661×** | -8.7 | 3e-16 | 28/32 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.548×** | -8.6 | 6e-16 | 23/32 (NCI-H2030, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.558×** | -8.5 | 7e-16 | 21/30 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -8.4 | 2e-15 | 22/27 (AN3 CA, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.579×** | -8.1 | 3e-14 | 26/31 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -7.8 | 3e-13 | 21/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.620×** | -7.0 | 1e-10 | 24/31 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.623×** | -6.5 | 4e-09 | 20/28 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -6.2 | 2e-08 | 20/32 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.669×** | -6.0 | 9e-08 | 21/32 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -5.7 | 4e-07 | 20/32 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.683×** | -5.4 | 2e-06 | 19/31 (H4, C32, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.693×** | -5.1 | 8e-06 | 18/32 (Hs 766T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.5 | 1 | 11 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.12× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 79.6 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.160× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 49.1 | 3 (3 ⚠) | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.31× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Harringtonine (drug)]] 5 µM 0.102× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0732× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 37.7 | 2 (2 ⚠) | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 5 µM 0.133× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 95.1 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -11.8) |
| [[J82 (line)]] | alt | 29.2 | 4 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.23× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.54× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -10.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 98.0 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.81× (z +11.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.331× (z -9.6) |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 14.8 | 4 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 4.59× (z +12.7) | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -8.7) |
| [[SW480 (line)]] | alt | 23.7 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.48× (z +14.5) | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -10.6) |
| [[C32 (line)]] | wt | 298 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.61× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.44× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.169× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -10.0) |
| [[A549 (line)]] | wt | 77.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.5) |
| [[HOP62 (line)]] | alt | 39.1 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.576× (z -12.0) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -8.8) |
| [[A498 (line)]] | wt | 22.8 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.303× (z -9.7) |
| [[AN3 CA (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0648× (z -13.7) |
| [[SW 900 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.72× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 22.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.69× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 12.6 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0761× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.8) |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0472× (z -10.7) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL4]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KCNK3]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SFRP1]] | +0.62 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[CHD1L]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[GLDC]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SGIP1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CACNG7]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[EBF2]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SEMA4B]] | +0.58 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[GRAMD1B]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 | same gene group |
| [[NEXN]] | -0.53 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ENTPD3-AS1]] | -0.53 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[N4BP2L2]] | -0.50 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[FBXW4]] | -0.48 | -0.36 / -0.41 | both halves | 1e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[COMT]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGIP1]] | B | SGIP1 activity raises TRIM9's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without SGIP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[SORBS2]] | B | SORBS2 activity weakens TRIM9's drug response | lines that do not express SORBS2 (14) vs lines expressing it (18) | the lines without SORBS2 respond 1.26× as strongly (z diff -1.63); strongest at Digitoxin 5 µM: 0.26x vs 0.41x (z diff -3.6) | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR; target measured in part of the lines; artifact flags |
| [[FZD1]] | B | FZD1 activity raises TRIM9's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.66× lower at baseline in the lines without FZD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[MEG3]] | B | MEG3 activity raises TRIM9's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.69× lower at baseline in the lines without MEG3 | 0.067 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[PDE10A]] | B | PDE10A activity raises TRIM9's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without PDE10A | 0.068 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[TMEM145]] | B | TMEM145 activity raises TRIM9's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 3.71× lower at baseline in the lines without TMEM145 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[GALNT18]] | B | GALNT18 activity raises TRIM9's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without GALNT18 | 0.082 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ZMAT4]] | B | ZMAT4 activity raises TRIM9's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without ZMAT4 | 0.082 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11 |
| [[MIR493HG]] | B | MIR493HG activity raises TRIM9's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without MIR493HG | 0.084 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[TSPAN5]] | B | TSPAN5 activity raises TRIM9's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without TSPAN5 | 0.088 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[VAT1L]] | C | VAT1L activity raises TRIM9's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 4.49× lower at baseline in the lines without VAT1L | 0.028 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[NRG2]] | C | NRG2 activity raises TRIM9's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 4.81× lower at baseline in the lines without NRG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 8, C 17. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD1]] | B | TRIM9 activity raises FZD1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without TRIM9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[SLIT3]] | B | TRIM9 activity raises SLIT3's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.94× lower at baseline in the lines without TRIM9 | 0.040 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[GNAO1]] | B | TRIM9 activity raises GNAO1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without TRIM9 | 0.056 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[LPCAT2]] | B | TRIM9 activity raises LPCAT2's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.91× lower at baseline in the lines without TRIM9 | 0.068 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[PCDHGA2]] | B | TRIM9 activity raises PCDHGA2's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without TRIM9 | 0.083 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[DPYSL4]] | B | TRIM9 activity raises DPYSL4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without TRIM9 | 0.091 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[CYTH4]] | B | TRIM9 activity raises CYTH4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without TRIM9 | 0.093 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| cells under [[Bortezomib (drug)]] 0.05 µM | B | TRIM9 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express TRIM9 (16) vs lines expressing it (32) | the lines without TRIM9: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[STK32B]] | C | TRIM9 activity raises STK32B's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 4.47× lower at baseline in the lines without TRIM9 | 0.002 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[SETBP1]] | C | TRIM9 activity raises SETBP1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 5.21× lower at baseline in the lines without TRIM9 | 0.003 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[TMEM255B]] | C | TRIM9 activity raises TMEM255B's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 3.84× lower at baseline in the lines without TRIM9 | 0.003 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[CAMK4]] | C | TRIM9 activity raises CAMK4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 5.66× lower at baseline in the lines without TRIM9 | 0.005 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.6, 14.5); signed map (22.3, 43.4). **Vector** length 105, 28.3% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +14.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.6 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.9 | +10.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.9 | +11.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -4.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.9 | +1.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.1 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.6 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -8.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -8.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,975,262-51,096,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPRING, RNF91 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Fibronectin type III domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C026](https://www.uniprot.org/uniprotkb/Q9C026) (E3 ubiquitin-protein ligase TRIM9):

> E3 ubiquitin-protein ligase which ubiquitinates itself in cooperation with an E2 enzyme UBE2D2/UBC4 and serves as a targeting signal for proteasomal degradation. Regulates filopodial dynamics in brain by promoting the ubiqutination and degradation of actin polymerase VASP; this activity is antagonized by TRIM67 (By similarity). May play a role in regulation of neuronal functions and may also participate in the formation or breakdown of abnormal inclusions in neurodegenerative disorders. May act …

**Summary**, from NCBI Gene [114088](https://www.ncbi.nlm.nih.gov/gene/114088):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies. Its function has not been identified. Alternate splicing of this gene generates two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16288) · Entrez [114088](https://www.ncbi.nlm.nih.gov/gene/114088) · UniProt [Q9C026](https://www.uniprot.org/uniprotkb/Q9C026) · Ensembl [ENSG00000100505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100505)

## Data

Gene col 1976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1976); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1976]; `tensor/DDL_lfc|DDL_z.npy` [1976]; `embed/gene_vectors.npy` [1976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1976 or target_col == 1976). Every well: [[TRIM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
